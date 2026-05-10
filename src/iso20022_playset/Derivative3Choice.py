from . import base_types
from .EquityDerivative2 import EquityDerivative2
from .ContractForDifference2 import ContractForDifference2
from .CreditDefaultSwapsDerivative4Choice import CreditDefaultSwapsDerivative4Choice
from .CommodityDerivative4 import CommodityDerivative4
from .InterestRateDerivative5 import InterestRateDerivative5
from .EmissionAllowanceProductType1Code import EmissionAllowanceProductType1Code
from .ForeignExchangeDerivative2 import ForeignExchangeDerivative2

class Derivative3Choice(base_types._BaseFieldType):

	__slots__ = ["_CtrctForDiff", "_Cmmdty", "_IntrstRate", "_EmssnAllwnc", "_FX", "_Eqty", "_Cdt"]
	@property
	def CtrctForDiff(self):
		return self._CtrctForDiff

	@CtrctForDiff.setter
	def CtrctForDiff(self, value):
		self._CtrctForDiff = value if type(value) != base_types.auto else self.make_default("CtrctForDiff")

	@CtrctForDiff.deleter
	def CtrctForDiff(self):
		del self._CtrctForDiff
		self._CtrctForDiff = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def EmssnAllwnc(self):
		return self._EmssnAllwnc

	@EmssnAllwnc.setter
	def EmssnAllwnc(self, value):
		self._EmssnAllwnc = value if type(value) != base_types.auto else self.make_default("EmssnAllwnc")

	@EmssnAllwnc.deleter
	def EmssnAllwnc(self):
		del self._EmssnAllwnc
		self._EmssnAllwnc = None

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if type(value) != base_types.auto else self.make_default("FX")

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = None

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if type(value) != base_types.auto else self.make_default("Eqty")

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = None

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if type(value) != base_types.auto else self.make_default("Cdt")

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctForDiff', type=ContractForDifference2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmmdty', type=CommodityDerivative4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateDerivative5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=EmissionAllowanceProductType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchangeDerivative2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Eqty', type=EquityDerivative2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cdt', type=CreditDefaultSwapsDerivative4Choice, min=0, max=1, mutex_group=1, array=False),
	))

