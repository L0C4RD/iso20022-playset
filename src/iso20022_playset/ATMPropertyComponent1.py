from . import base_types
from .ATMPropertyType1Code import ATMPropertyType1Code
from .Max70Text import Max70Text
from .Max2000Text import Max2000Text

class ATMPropertyComponent1(base_types._BaseFieldType):

	__slots__ = ["_PrprtyNm", "_PrprtyTp", "_PrprtyVal"]
	@property
	def PrprtyNm(self):
		return self._PrprtyNm

	@PrprtyNm.setter
	def PrprtyNm(self, value):
		self._PrprtyNm = value if type(value) != auto else self.make_default("PrprtyNm")

	@PrprtyNm.deleter
	def PrprtyNm(self):
		del self._PrprtyNm
		self._PrprtyNm = None

	@property
	def PrprtyTp(self):
		return self._PrprtyTp

	@PrprtyTp.setter
	def PrprtyTp(self, value):
		self._PrprtyTp = value if type(value) != auto else self.make_default("PrprtyTp")

	@PrprtyTp.deleter
	def PrprtyTp(self):
		del self._PrprtyTp
		self._PrprtyTp = None

	@property
	def PrprtyVal(self):
		return self._PrprtyVal

	@PrprtyVal.setter
	def PrprtyVal(self, value):
		self._PrprtyVal = value if type(value) != auto else self.make_default("PrprtyVal")

	@PrprtyVal.deleter
	def PrprtyVal(self):
		del self._PrprtyVal
		self._PrprtyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrprtyNm', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyTp', type=ATMPropertyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyVal', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
	))

