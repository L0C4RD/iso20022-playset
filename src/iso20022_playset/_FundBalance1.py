# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import FinancialInstrumentQuantity1

class FundBalance1(base_types._BaseFieldType):

	__slots__ = ["_TtlCshFrCshOrdrs", "_TtlCshFrUnitOrdrs", "_TtlUnitsFrCshOrdrs", "_TtlUnitsFrUnitOrdrs"]
	@property
	def TtlCshFrCshOrdrs(self):
		return self._TtlCshFrCshOrdrs

	@TtlCshFrCshOrdrs.setter
	def TtlCshFrCshOrdrs(self, value):
		self._TtlCshFrCshOrdrs = value if value is not None else base_types.UninitialisedField(self, 'TtlCshFrCshOrdrs', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlCshFrCshOrdrs.deleter
	def TtlCshFrCshOrdrs(self):
		del self._TtlCshFrCshOrdrs
		self._TtlCshFrCshOrdrs = base_types.UninitialisedField(self, 'TtlCshFrCshOrdrs', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlCshFrUnitOrdrs(self):
		return self._TtlCshFrUnitOrdrs

	@TtlCshFrUnitOrdrs.setter
	def TtlCshFrUnitOrdrs(self, value):
		self._TtlCshFrUnitOrdrs = value if value is not None else base_types.UninitialisedField(self, 'TtlCshFrUnitOrdrs', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlCshFrUnitOrdrs.deleter
	def TtlCshFrUnitOrdrs(self):
		del self._TtlCshFrUnitOrdrs
		self._TtlCshFrUnitOrdrs = base_types.UninitialisedField(self, 'TtlCshFrUnitOrdrs', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlUnitsFrCshOrdrs(self):
		return self._TtlUnitsFrCshOrdrs

	@TtlUnitsFrCshOrdrs.setter
	def TtlUnitsFrCshOrdrs(self, value):
		self._TtlUnitsFrCshOrdrs = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsFrCshOrdrs', FinancialInstrumentQuantity1, False)

	@TtlUnitsFrCshOrdrs.deleter
	def TtlUnitsFrCshOrdrs(self):
		del self._TtlUnitsFrCshOrdrs
		self._TtlUnitsFrCshOrdrs = base_types.UninitialisedField(self, 'TtlUnitsFrCshOrdrs', FinancialInstrumentQuantity1, False)

	@property
	def TtlUnitsFrUnitOrdrs(self):
		return self._TtlUnitsFrUnitOrdrs

	@TtlUnitsFrUnitOrdrs.setter
	def TtlUnitsFrUnitOrdrs(self, value):
		self._TtlUnitsFrUnitOrdrs = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsFrUnitOrdrs', FinancialInstrumentQuantity1, False)

	@TtlUnitsFrUnitOrdrs.deleter
	def TtlUnitsFrUnitOrdrs(self):
		del self._TtlUnitsFrUnitOrdrs
		self._TtlUnitsFrUnitOrdrs = base_types.UninitialisedField(self, 'TtlUnitsFrUnitOrdrs', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCshFrCshOrdrs', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshFrUnitOrdrs', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsFrCshOrdrs', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsFrUnitOrdrs', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))