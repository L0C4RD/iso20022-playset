import base_types
import GenericIdentification36
import Exact3UpperCaseAlphaNumericText
import Max30Text

class IdentificationFormat3Choice(base_types._BaseFieldType):

	__slots__ = ["_ShrtId", "_PrtryId", "_LngId"]
	@property
	def ShrtId(self):
		return self._ShrtId

	@ShrtId.setter
	def ShrtId(self, value):
		self._ShrtId = value if type(value) != auto else self.make_default("ShrtId")

	@ShrtId.deleter
	def ShrtId(self):
		del self._ShrtId
		self._ShrtId = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def LngId(self):
		return self._LngId

	@LngId.setter
	def LngId(self, value):
		self._LngId = value if type(value) != auto else self.make_default("LngId")

	@LngId.deleter
	def LngId(self):
		del self._LngId
		self._LngId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtId', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LngId', type=Max30Text, min=0, max=1, mutex_group=1, array=False),
	))

