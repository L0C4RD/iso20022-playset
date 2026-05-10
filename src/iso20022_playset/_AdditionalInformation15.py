from . import base_types
from ._GenericIdentification36 import GenericIdentification36
from ._Max350Text import Max350Text

class AdditionalInformation15(base_types._BaseFieldType):

	__slots__ = ["_InfTp", "_InfVal"]
	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if type(value) != base_types.auto else self.make_default("InfTp")

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = None

	@property
	def InfVal(self):
		return self._InfVal

	@InfVal.setter
	def InfVal(self, value):
		self._InfVal = value if type(value) != base_types.auto else self.make_default("InfVal")

	@InfVal.deleter
	def InfVal(self):
		del self._InfVal
		self._InfVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfTp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

