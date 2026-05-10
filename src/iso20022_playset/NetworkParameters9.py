from . import base_types
from .NetworkType1Code import NetworkType1Code
from .Max500Text import Max500Text

class NetworkParameters9(base_types._BaseFieldType):

	__slots__ = ["_AdrVal", "_NtwkTp"]
	@property
	def AdrVal(self):
		return self._AdrVal

	@AdrVal.setter
	def AdrVal(self, value):
		self._AdrVal = value if type(value) != base_types.auto else self.make_default("AdrVal")

	@AdrVal.deleter
	def AdrVal(self):
		del self._AdrVal
		self._AdrVal = None

	@property
	def NtwkTp(self):
		return self._NtwkTp

	@NtwkTp.setter
	def NtwkTp(self, value):
		self._NtwkTp = value if type(value) != base_types.auto else self.make_default("NtwkTp")

	@NtwkTp.deleter
	def NtwkTp(self):
		del self._NtwkTp
		self._NtwkTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrVal', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkTp', type=NetworkType1Code, min=1, max=1, mutex_group=None, array=False),
	))

