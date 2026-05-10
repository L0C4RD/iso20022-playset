from . import base_types
from ._ISOYearMonth import ISOYearMonth
from ._SettlementUnitType3Choice import SettlementUnitType3Choice
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice

class SettlementInformation17(base_types._BaseFieldType):

	__slots__ = ["_CtrctSttlmMnth", "_MinDnmtn", "_MinMltplQty", "_DevtgSttlmUnit", "_SctiesQtyTp"]
	@property
	def CtrctSttlmMnth(self):
		return self._CtrctSttlmMnth

	@CtrctSttlmMnth.setter
	def CtrctSttlmMnth(self, value):
		self._CtrctSttlmMnth = value if type(value) != base_types.auto else self.make_default("CtrctSttlmMnth")

	@CtrctSttlmMnth.deleter
	def CtrctSttlmMnth(self):
		del self._CtrctSttlmMnth
		self._CtrctSttlmMnth = None

	@property
	def DevtgSttlmUnit(self):
		return self._DevtgSttlmUnit

	@DevtgSttlmUnit.setter
	def DevtgSttlmUnit(self, value):
		self._DevtgSttlmUnit = value if type(value) != base_types.auto else self.make_default("DevtgSttlmUnit")

	@DevtgSttlmUnit.deleter
	def DevtgSttlmUnit(self):
		del self._DevtgSttlmUnit
		self._DevtgSttlmUnit = None

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if type(value) != base_types.auto else self.make_default("MinDnmtn")

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = None

	@property
	def MinMltplQty(self):
		return self._MinMltplQty

	@MinMltplQty.setter
	def MinMltplQty(self, value):
		self._MinMltplQty = value if type(value) != base_types.auto else self.make_default("MinMltplQty")

	@MinMltplQty.deleter
	def MinMltplQty(self):
		del self._MinMltplQty
		self._MinMltplQty = None

	@property
	def SctiesQtyTp(self):
		return self._SctiesQtyTp

	@SctiesQtyTp.setter
	def SctiesQtyTp(self, value):
		self._SctiesQtyTp = value if type(value) != base_types.auto else self.make_default("SctiesQtyTp")

	@SctiesQtyTp.deleter
	def SctiesQtyTp(self):
		del self._SctiesQtyTp
		self._SctiesQtyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSttlmMnth', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DevtgSttlmUnit', type=FinancialInstrumentQuantity1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MinDnmtn', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyTp', type=SettlementUnitType3Choice, min=0, max=1, mutex_group=None, array=False),
	))

