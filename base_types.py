# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

import re
import base64
from collections import namedtuple

from exceptions import ParseError, ValidateError, XMLError, GenerateError
import gen_utils

FieldEntry = namedtuple("FieldEntry", ["name", "type", "min", "max", "mutex_group", "array"])

AttributeEntry = namedtuple("AttributeEntry", ["name", "type", "required"])

class _BaseElemType(object):

	_tag = None
	_ns = None

	_attrib_defs = None

	def __init__(self, tag, data=None, ns=None):

		self._tag=tag
		self._ns=ns

	def _whoami(self, path_in=None):

		my_name = self.__class__.__name__ if self._tag is None else self._tag
		return my_name if path_in is None else ".".join((path_in, my_name))

	def tag(self):
		return self._tag

	def tag_with_ns(self):
		return self.tag() if self._ns is None else f"{{{self._ns}}}{self._tag}"

	def parse(self, node_in, path_in=None, force=False):

		# Parse attribs
		if self._attrib_defs is not None:
			for attrib_def in self._attrib_defs:

				try:
					this_attrib_data = node_in.attrib.get(attrib_def.name)
				except:
					raise ParseError(f"{self._whoami()} : Missing required attribute {attrib_def.name}")

				try:
					self.attrib[attrib_def.name] = attrib_def.type(data = this_attrib_data)
				except:
					raise ParseError(f"{self._whoami()} : Could not parse attribute {attrib_def.name}")

		# Parse the rest of the data.
		self._do_parse(node_in, path_in, force)

	def validate(self, path_in=None):

		# Build the path for reporting errors
		this_path = self._whoami(path_in)

		# Validate attribs
		if self._attrib_defs is not None:
			for attrib_def in self._attrib_defs:
				try:
					assert(attrib_def.name in self.attrib)
					this_attrib = self.attrib[attrib_def.name]
					assert(type(this_attrib) == attrib_def.type)

					try:
						this_attrib.validate(this_path)
					except ValidateError as e:
						raise AssertionError(str(e))

				except AssertionError as e:
					raise ValidateError(f"{this_path}[{attrib_def.name}] : Invalid value")

			# Check for undefined attribs
			undefined_attribs = { k for k in self.attrib } - {attrib_def.name for attrib_def in self._attrib_defs}

			if len(undefined_attribs) > 0:
				raise ValidateError(f"{this_path} : Invalid attributes {', '.join(undefined_attribs)}")

		try:
			self._do_validation(this_path)
		except AssertionError as e:
			raise ValidateError(f"{this_path} : Invalid value")
		else:
			return True

	def to_xml(self, indentlevel=0, indent="\t"):

		try:
			contents = self._do_xml(indentlevel=indentlevel+1, indent=indent)
		except Exception as e:
			raise XMLError(f"{self._whoami()} : Could not create XML")

		if self._attrib_defs is not None:
			attr_pairs = [ f'{ad.name}="{self.attrib.get(ad.name)}"' for ad in self._attrib_defs if self.attrib.get(ad.name, None) is not None ]
		else:
			attr_pairs = []

		xml_toks = [self.tag()] + attr_pairs

		xml = (indent * indentlevel) + "<" + " ".join(xml_toks)

		if contents is not None:
			xml += ">\n" + contents + f"{'\n' if contents else ''}{(indent * indentlevel)}</{self.tag()}>"
		else:
			xml += "/>"

		return xml

	def generate(self):
		
		# Do attributes

		self.attrib = dict()

		if self._attrib_defs is not None:
			for attrib_def in self._attrib_defs:

				# Decide if we'll include it or not.
				will_generate = True if attrib_def.required else gen_utils.coin_flip()

				if will_generate:
					this_attrib = attrib_def.type(attrib_def.name)
					this_attrib.generate()
					self.attrib[attrib_def.name] = this_attrib

		# Do the rest.
		self._do_generate()

	def _do_validation(self, path_in=None):

		raise NotImplementedError("Base class cannot do validation.")

	def _do_parse(self, node_in, path_in=None, force=False):

		raise NotImplementedError("Base class cannot do parsing.")

	def _do_xml(self, indentlevel=0, indent="\t"):

		raise NotImplementedError("Base class cannot create XML.")

	def _do_generate(self):

		raise NotImplementedError("Base class cannot self-populate.")

class _BaseDataType(_BaseElemType):

	data = None

	def __init__(self, tag, data=None, ns=None):

		super().__init__(tag, data=data, ns=ns)

		self.set(data)
		#if validate:
		#    self.validate()

	def __str__(self):
		return self.data

	def set(self, data):
		self.data = data

	def get(self):
		return self.data

	def _do_xml(self, indentlevel=0, indent="\t"):

		if not self.data:
			return None

		return (indentlevel * indent) + str(self)

class _BaseFieldType(_BaseElemType):

	_field_defs = {}

	def __init__(self, tag, data=None, ns=None):

		super().__init__(tag, data=data, ns=ns)

		"""
		if data is not None:
			raise ValueError(f"{self._whoami()} : Cannot contain data (Contains data {data})")
		"""

	def _do_validation(self, path_in=None):

		seen_mutex_groups = set()

		for field_def in self._field_defs:

			field_class = type(field_def)

			# Check field is defined.
			try:
				field = getattr(self, field_def.name)
			except AttributeError as e:
				raise ValidateError(f"{self._whoami()} : Missing field {field_def.name} (check class definition)")

			# Check limits are valid
			if field_def.array:
				if field_def.min is not None and field_def.min < 0:
					raise ValidateError(f"{self._whoami()} : Invalid lower bound for {field_def.name}")
				if field_def.max is not None and field_def.max < field_def.min:
					raise ValidateError(f"{self._whoami()} : Invalid upper bound for {field_def.name}")
			else:
				if field_def.min not in (0,1) or field_def.max != 1:
					raise ValidateError(f"{self._whoami()} : Invalid bounds for {field_def.name}")

			# Check field is within size limits
			if field_def.array:
				field_length = 0 if field is None else len(field)
				if field_def.min is not None and field_length < field_def.min:
					raise ValidateError(f"{self._whoami()} : length of {field_def.name} has lower size bound {field_def.min}, but is defined as length {field_length}.")
				if field_def.max is not None and field_length > field_def.max:
					raise ValidateError(f"{self._whoami()} : length of {field_def.name} has upper size bound {field_def.max}, but is defined as length {field_length}.")
			else:
				# (This is basically checking that mandatory fields  are defined)
				if field_def.min > 0 and field is None:
					raise ValidateError(f"{self._whoami()} : Missing required field {field_def.name}")

			# Check mutex groups
			if field is not None and field_def.mutex_group is not None:
				if field_def.mutex_group in seen_mutex_groups:
					fields_in_mutex_group = {fd for fd in self._field_defs if fd.mutex_group == field_def.mutex_group}
					raise ValidateError(f"{self._whoami()} : Can only contain one from this list: " + ", ".join(fd.name for fd in fields_in_mutex_group))
				else:
					seen_mutex_groups.add(field_def.mutex_group)

			# Check type
			if field_def.array:
				if field is not None:
					if (type(field) != list):
						raise ValidateError(f"{self._whoami()} : {field_def.name} expected value of type list, got {type(field).__name__}") 
					elif any(type(f) != field_def.type for f in field):
						raise ValidateError(f"{self._whoami()} : {field_def.name} expected list of entries of type {field_def.type}, got [{', '.join(type(f).__name__ for f in field)}]")
			else:
				if field is not None:
					if type(field) != field_def.type:
						raise ValidateError(f"{self._whoami()} : {field_def.name} expected value of type {field_def.type}, got {type(field).__name__}")


		# validate each field
		for field_def in self._field_defs:
			field = getattr(self, field_def.name)
			if field is None:
				pass
			elif field_def.array:
				for x in field:
					x.validate(path_in)
			else:
				field.validate(path_in)

		# If all fields validate, return True.
		return True

	def _do_parse(self, node_in, path_in=None, force=False):
		
		"""
		This isn't the most memory-efficient way of parsing, 
		but probably fine for now.
		TODO: come back and optimise this.
		"""

		# Make sure we're looking at the right node for this class.
		if node_in.tag != self.tag_with_ns():
			raise ParseError(f"{self._whoami()} : Expected {self.tag_with_ns()}, got {node_in.tag}")

		# Go through tags.
		for n in node_in:

			# Forget the namespace if it's there.
			tagname = n.tag.rsplit("}", 1)[-1]

			# Check if we've got one of these in our field defs
			try:
				field_def = next(x for x in self._field_defs if x.name == tagname)
			except StopIteration:
				raise ParseError(f"{self._whoami()} : Unknown field {tagname}")
			
			# Ugh. (We're parsing depth first.)
			# (Shouldn't be an issue for iso20022 as messages are relatively
			# shallow. But still not ideal.)
			new_item = field_def.type(tagname, data=n.text, ns=self._ns)
			new_item.parse(n, f"{path_in}.{tagname}")

			if field_def.array:
				if getattr(self, field_def.name) is None:
					setattr(self, field_def.name, [])
				getattr(self, field_def.name).append(new_item)
			else:
				setattr(self, field_def.name, new_item)


	def _do_xml(self, indentlevel=0, indent="\t"):

		if not self._field_defs:
			return None

		content = []

		for field_def in self._field_defs:
			field = getattr(self, field_def.name)

			if field is not None:
				if field_def.array:
					for f in field:
						content.append(f.to_xml(indentlevel=indentlevel, indent=indent))
				else:
					content.append(field.to_xml(indentlevel=indentlevel, indent=indent))
		
		return "\n".join(content)

	def _do_generate(self):

		# Mutex groups first.
		mutex_groups = set(f.mutex_group for f in self._field_defs if f.mutex_group is not None)

		for mutex_group in mutex_groups:

			# Pick one item and generate it
			field_defs = set(f for f in self._field_defs if f.mutex_group == mutex_group)
			selected_field_def = gen_utils.choose_one(field_defs)
			self._generate_single_field(selected_field_def)

			# Set the other items to None
			field_defs.remove(selected_field_def)
			for field_def in field_defs:
				setattr(self, field_def.name, None)

		# Now do all the other items
		for field_def in self._field_defs:

			# Skip the mutex groups (done those above.)
			if field_def.mutex_group is not None:
				continue

			# Decide if we're going to generate it or not.
			will_include = True if field_def.min > 0 else gen_utils.coin_flip()

			# If we are: generate it.
			if will_include:
				self._generate_single_field(field_def)

	def _generate_single_field(self, field_def:FieldEntry):

		# Arrays
		if field_def.array:
	
			list_size = gen_utils.list_length(field_def)

			this_field = [
				field_def.type(field_def.name) for _ in range(list_size)
			]

			for f in this_field:
				f.generate()

		# Non-arrays
		else:
			this_field = field_def.type(field_def.name)
			this_field.generate()

		# Set the attribute
		setattr(self, field_def.name, this_field)



class _BaseDataType_String(_BaseDataType):

	_pattern = None
	_values = None
	_max = None
	_min = None
	_length = None
	
	def parse(self, node_in, path_in=None, force=False):

		self.data = node_in.text
		
		if force:
			try:
				self.validate()
			except:
				raise ParseError(f"{self._whoami()} : Invalid value")

	def _do_validation(self, path_in=None):

		# Check type
		assert(type(self.data)==str)

		# If pattern is defined, check it
		if self._pattern is not None:
			assert(re.fullmatch(self._pattern, self.data))

		# If enum values are defined, check them
		if self._values is not None:
			assert(len(self._values) > 0)
			assert(self.data in self._values)

		# If bounds are defined, check them
		if self._max is not None:
			assert(len(self.data)<=self._max)
		if self._min is not None:
			assert(self._min<=len(self.data))
		if self._length is not None:
			assert(len(self.data)==self._length)

	def _do_generate(self):

		new_data = None

		# Enum first.
		if self._values is not None:
			new_data = gen_utils.choose_one(self._values)

		# Pattern second.
		if self._pattern is not None:

			if new_data is None:
				new_data = gen_utils.string_from_pattern(self._pattern)
			else:
				if not re.fullmatch(self._pattern, new_data):
					raise GenerateError(f"{self._whoami()} : Incompatible pattern + enum definitions")

		# Finally, min/max values
		if new_data is not None:
			if self._min is not None and len(new_data) < self._min:
				raise GenerateError(f"{self._whoami()} : Incompatible pattern/enum + min_length definitions")
			if self._max is not None and len(new_data) > self._max:
				raise GenerateError(f"{self._whoami()} : Incompatible pattern/enum + max_length definitions")
			if self._length is not None and len(new_data) != self._length:
				raise GenerateError(f"{self._whoami()} : Incompatible pattern/enum + length definitions")

		else:
			new_data = gen_utils.random_string_xmlescape(self._min, self._max)

		self.set(new_data)

class _BaseDataType_B64Binary(_BaseDataType):

	_max = None
	_min = None

	def set_bin(self, data:bin):
		self.data = base64.b64encode(data)

	def get_bin(self):
		return base64.b64decode(self.data)

	def parse(self, node_in, path_in=None, force=False):

		self.data = node_in.text
		
		if force:
			try:
				self.validate()
			except:
				raise ParseError(f"{self._whoami()} : Invalid value")

	def _do_validation(self, path_in=None):

		# Check type
		assert(type(self.data)==str)

		# Ensure valid base64.
		try:
			base64.b64decode(self.data)
		except Exception as e:
			raise AssertionError(str(e))

		# If bounds are defined, check them
		if self._max is not None:
			assert(len(self.data)<=self._max)
		if self._min is not None:
			assert(self._min<=len(self.data))

	def _do_generate(self):
		
		new_data = gen_utils.random_string_b64(self._min, self._max)
		self.set(new_data)

class _BaseDataType_Boolean(_BaseDataType_String):

	_values = {"true", "false", "1", "0"}

class _BaseDataType_Decimal(_BaseDataType):

	_max_totaldigits = None
	_max_fractiondigits = None
	_min_inclusive = None
	_max_inclusive = None
	_pattern = None

	def __float__(self):
		return float(self.data)

	def parse(self, node_in, path_in=None, force=False):

		self.data = node_in.text

		if force:
			try:
				self.validate()
			except:
				raise ParseError(f"{self._whoami()} : Invalid value")

	def _do_validation(self, path_in=None):

		# Check type
		assert(type(self.data)==str)

		if "-" in self.data:
			assert(self.data[0] == "-")
			assert(self.data.count("-") == 1)
			unsigned_data = self.data[1:]
		else:
			unsigned_data = self.data[:]

		if "." in unsigned_data:
			assert(self.data.count(".") == 1)
			left_digits, right_digits = unsigned_data.split(".", 1)
		else:
			left_digits = unsigned_data
			right_digits = ""
		
		for d in (left_digits, right_digits):
			if len(d) > 0:
				assert(d.isdigit())

		# if totaldigits is defined, check it
		if self._max_totaldigits is not None:
			assert(len(left_digits) + len(right_digits) <= self._max_totaldigits)

		# if fractiondigits is defined, check it
		if self._max_fractiondigits is not None:
			assert(len(left_digits) + len(right_digits) <= self._max_totaldigits)

		# if min_inclusive is defined, check it
		if self._min_inclusive is not None:
			assert(self._min_inclusive <= float(self.data))

		# if max_inclusive is defined, check it
		if self._max_inclusive is not None:
			assert(float(self.data) <= self._max_inclusive)
		
		# if pattern is defined, check it
		if self._pattern is not None:
			assert(re.fullmatch(self._pattern, self.data))
			

	def _do_generate(self):

		# God this is awful
		if self._pattern:
			found = False
			for i in range(100):
				new_data = gen_utils.string_from_pattern(self._pattern)
				
				if self._min_inclusive is not None and float(new_data) < self._min_inclusive:
					continue
				if self._max_inclusive is not None and float(new_data) > self._max_inclusive:
					continue
				found = True
			if not found:
				raise GenerateError(f"{self._whoami()} : Incompatible pattern + bounds definitions")

		else:
			new_data = gen_utils.random_decimal(
				self._min_inclusive, 
				self._max_inclusive, 
				self._max_fractiondigits, 
				self._max_totaldigits
			)

		self.set(new_data)

class _BaseDataType_Date(_BaseDataType):

	_pattern = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
	
	def parse(self, node_in, path_in=None, force=False):

		self.data = node_in.text
		
		if force:
			try:
				self.validate()
			except:
				raise ParseError(f"{self._whoami()} : Invalid value")

	def _do_validation(self, path_in=None):

		# Check type
		assert(type(self.data)==str)

		# Pattern is defined by default; check it
		assert(re.fullmatch(self._pattern, self.data))

	def _do_generate(self):
		
		new_data = gen_utils.string_from_pattern(self._pattern)
		self.set(new_data)

class _BaseDataType_Time(_BaseDataType_Date):

	_pattern = r"([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?(Z|[+-](0[0-9]|1[0-4]):[0-5][0-9])?"

class _BaseDataType_gYear(_BaseDataType_Date):

	# From ISO 8601
	# Gregorian year with optional timezone info
	# e.g.:
	# > 1970
	# > 2000+06:45
	# Note that the maximum time offset is +14:00 and the minimum is -12:00,
	# Hence this slightly unhinged regex.

	#_pattern = r"^\d{4}([+-]\d{2}:\d{2})?$"
	#_pattern = r"^\d{4}(\+(0[0-9]|1[0-4]):[0-5]\d|-(0[0-9]|1[0-2]):[0-5]\d)?$"
	#_pattern = r"^\d{4}(\+(0[0-9]|1[0-3]):[0-5]\d|-(0[0-9]|1[0-1]):[0-5]\d|\+14:00|-12:00|Z)?$"
	_pattern = r"^[0-9]{4}(\+(0[0-9]|1[0-3]):[0-5][0-9]|-(0[0-9]|1[0-1]):[0-5][0-9]|\+14:00|-12:00|Z)?$"

class _BaseDataType_gYearMonth(_BaseDataType_Date):

	# From ISO 8601
	# Gregorian year and month with optional timezone info

	# Note that the maximum time offset is +14:00 and the minimum is -12:00,
	# Hence this slightly unhinged regex.

	#_pattern = r"^\d{4}-(0[1-9]|1[0-2])(\+(0[0-9]|1[0-3]):[0-5]\d|-(0[0-9]|1[0-1]):[0-5]\d|\+14:00|-12:00|Z)?$"
	_pattern = r"^[0-9]{4}-(0[1-9]|1[0-2])(\+(0[0-9]|1[0-3]):[0-5][0-9]|-(0[0-9]|1[0-1]):[0-5][0-9]|\+14:00|-12:00|Z)?$"

class _BaseDataType_gMonth(_BaseDataType_Date):

	# From ISO 8601
	# Gregorian year and month with optional timezone info

	# Note that the maximum time offset is +14:00 and the minimum is -12:00,
	# Hence this slightly unhinged regex.

	_pattern = r"^(0[1-9]|1[0-2])(\+(0[0-9]|1[0-3]):[0-5][0-9]|-(0[0-9]|1[0-1]):[0-5][0-9]|\+14:00|-12:00|Z)?$"

class _BaseDataType_DateTime(_BaseDataType):

	_pattern_UTC_time = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{3})?Z"
	_pattern_UTC_localtime = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{3})?([+-](0[0-9]|1[0-4]):[0-5][0-9])"
	_pattern_UTC_localtime_offset = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]{3})?"
	_pattern = None
	
	def parse(self, node_in, path_in=None, force=False):

		self.data = node_in.text
		
		if force:
			try:
				self.validate()
			except:
				raise ParseError(f"{self._whoami()} : Invalid value")

	def _do_validation(self, path_in=None):

		# Check type
		assert(type(self.data)==str)

		# If pattern is defined, ignore defaults.
		if self._pattern is None:
			assert(any([
				re.fullmatch(self._pattern_UTC_time, self.data),
				re.fullmatch(self._pattern_UTC_localtime, self.data),
				re.fullmatch(self._pattern_UTC_localtime_offset, self.data),
			]))
		else:
			assert(re.fullmatch(self._pattern, self.data))

	def _do_generate(self):
		
		if self._pattern is not None:
			this_pattern = self._pattern
		else:
			this_pattern = gen_utils.choose_one((
				self._pattern_UTC_time,
				self._pattern_UTC_localtime,
				self._pattern_UTC_localtime_offset,
			))

		new_data = gen_utils.string_from_pattern(this_pattern)
		self.set(new_data)

class XS_ID(_BaseDataType_String):

	_pattern = r"[\i-[:]][\c-[:]]*"

class XS_IDREF(_BaseDataType_String):

	_pattern = r"[\i-[:]][\c-[:]]*"

class XS_positiveInteger(_BaseDataType_String):

	_pattern = r"[0-9]+"

	def __int__(self):
		return int(self.data)