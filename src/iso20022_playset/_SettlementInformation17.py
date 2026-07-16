# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1Choice
from . import ISOYearMonth
from . import SettlementUnitType3Choice

class SettlementInformation17(base_types._BaseFieldType):

	__slots__ = ["_CtrctSttlmMnth", "_DevtgSttlmUnit", "_MinDnmtn", "_MinMltplQty", "_SctiesQtyTp"]
	@property
	def CtrctSttlmMnth(self):
		return self._CtrctSttlmMnth

	@CtrctSttlmMnth.setter
	def CtrctSttlmMnth(self, value):
		self._CtrctSttlmMnth = value if value is not None else base_types.UninitialisedField(self, 'CtrctSttlmMnth', ISOYearMonth, False)

	@CtrctSttlmMnth.deleter
	def CtrctSttlmMnth(self):
		del self._CtrctSttlmMnth
		self._CtrctSttlmMnth = base_types.UninitialisedField(self, 'CtrctSttlmMnth', ISOYearMonth, False)

	@property
	def DevtgSttlmUnit(self):
		return self._DevtgSttlmUnit

	@DevtgSttlmUnit.setter
	def DevtgSttlmUnit(self, value):
		self._DevtgSttlmUnit = value if value is not None else base_types.UninitialisedField(self, 'DevtgSttlmUnit', FinancialInstrumentQuantity1Choice, True)

	@DevtgSttlmUnit.deleter
	def DevtgSttlmUnit(self):
		del self._DevtgSttlmUnit
		self._DevtgSttlmUnit = base_types.UninitialisedField(self, 'DevtgSttlmUnit', FinancialInstrumentQuantity1Choice, True)

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if value is not None else base_types.UninitialisedField(self, 'MinDnmtn', FinancialInstrumentQuantity1Choice, False)

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = base_types.UninitialisedField(self, 'MinDnmtn', FinancialInstrumentQuantity1Choice, False)

	@property
	def MinMltplQty(self):
		return self._MinMltplQty

	@MinMltplQty.setter
	def MinMltplQty(self, value):
		self._MinMltplQty = value if value is not None else base_types.UninitialisedField(self, 'MinMltplQty', FinancialInstrumentQuantity1Choice, False)

	@MinMltplQty.deleter
	def MinMltplQty(self):
		del self._MinMltplQty
		self._MinMltplQty = base_types.UninitialisedField(self, 'MinMltplQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def SctiesQtyTp(self):
		return self._SctiesQtyTp

	@SctiesQtyTp.setter
	def SctiesQtyTp(self, value):
		self._SctiesQtyTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesQtyTp', SettlementUnitType3Choice, False)

	@SctiesQtyTp.deleter
	def SctiesQtyTp(self):
		del self._SctiesQtyTp
		self._SctiesQtyTp = base_types.UninitialisedField(self, 'SctiesQtyTp', SettlementUnitType3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSttlmMnth', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DevtgSttlmUnit', type=FinancialInstrumentQuantity1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MinDnmtn', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyTp', type=SettlementUnitType3Choice, min=0, max=1, mutex_group=None, array=False),
	))