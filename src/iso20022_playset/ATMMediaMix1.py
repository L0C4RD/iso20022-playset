from . import base_types
from .Number import Number
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class ATMMediaMix1(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_CshUnitNb", "_UnitVal"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def CshUnitNb(self):
		return self._CshUnitNb

	@CshUnitNb.setter
	def CshUnitNb(self, value):
		self._CshUnitNb = value if type(value) != base_types.auto else self.make_default("CshUnitNb")

	@CshUnitNb.deleter
	def CshUnitNb(self):
		del self._CshUnitNb
		self._CshUnitNb = None

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if type(value) != base_types.auto else self.make_default("UnitVal")

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshUnitNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

