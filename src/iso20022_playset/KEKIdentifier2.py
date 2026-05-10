import base_types
import Min5Max16Binary
import Number
import Max140Text

class KEKIdentifier2(base_types._BaseFieldType):

	__slots__ = ["_KeyId", "_DerivtnId", "_SeqNb", "_KeyVrsn"]
	@property
	def KeyId(self):
		return self._KeyId

	@KeyId.setter
	def KeyId(self, value):
		self._KeyId = value if type(value) != auto else self.make_default("KeyId")

	@KeyId.deleter
	def KeyId(self):
		del self._KeyId
		self._KeyId = None

	@property
	def DerivtnId(self):
		return self._DerivtnId

	@DerivtnId.setter
	def DerivtnId(self, value):
		self._DerivtnId = value if type(value) != auto else self.make_default("DerivtnId")

	@DerivtnId.deleter
	def DerivtnId(self):
		del self._DerivtnId
		self._DerivtnId = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def KeyVrsn(self):
		return self._KeyVrsn

	@KeyVrsn.setter
	def KeyVrsn(self, value):
		self._KeyVrsn = value if type(value) != auto else self.make_default("KeyVrsn")

	@KeyVrsn.deleter
	def KeyVrsn(self):
		del self._KeyVrsn
		self._KeyVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KeyId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivtnId', type=Min5Max16Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyVrsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

