from . import base_types
from .FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class FundBalance1(base_types._BaseFieldType):

	__slots__ = ["_TtlUnitsFrCshOrdrs", "_TtlCshFrCshOrdrs", "_TtlUnitsFrUnitOrdrs", "_TtlCshFrUnitOrdrs"]
	@property
	def TtlUnitsFrCshOrdrs(self):
		return self._TtlUnitsFrCshOrdrs

	@TtlUnitsFrCshOrdrs.setter
	def TtlUnitsFrCshOrdrs(self, value):
		self._TtlUnitsFrCshOrdrs = value if type(value) != base_types.auto else self.make_default("TtlUnitsFrCshOrdrs")

	@TtlUnitsFrCshOrdrs.deleter
	def TtlUnitsFrCshOrdrs(self):
		del self._TtlUnitsFrCshOrdrs
		self._TtlUnitsFrCshOrdrs = None

	@property
	def TtlCshFrCshOrdrs(self):
		return self._TtlCshFrCshOrdrs

	@TtlCshFrCshOrdrs.setter
	def TtlCshFrCshOrdrs(self, value):
		self._TtlCshFrCshOrdrs = value if type(value) != base_types.auto else self.make_default("TtlCshFrCshOrdrs")

	@TtlCshFrCshOrdrs.deleter
	def TtlCshFrCshOrdrs(self):
		del self._TtlCshFrCshOrdrs
		self._TtlCshFrCshOrdrs = None

	@property
	def TtlUnitsFrUnitOrdrs(self):
		return self._TtlUnitsFrUnitOrdrs

	@TtlUnitsFrUnitOrdrs.setter
	def TtlUnitsFrUnitOrdrs(self, value):
		self._TtlUnitsFrUnitOrdrs = value if type(value) != base_types.auto else self.make_default("TtlUnitsFrUnitOrdrs")

	@TtlUnitsFrUnitOrdrs.deleter
	def TtlUnitsFrUnitOrdrs(self):
		del self._TtlUnitsFrUnitOrdrs
		self._TtlUnitsFrUnitOrdrs = None

	@property
	def TtlCshFrUnitOrdrs(self):
		return self._TtlCshFrUnitOrdrs

	@TtlCshFrUnitOrdrs.setter
	def TtlCshFrUnitOrdrs(self, value):
		self._TtlCshFrUnitOrdrs = value if type(value) != base_types.auto else self.make_default("TtlCshFrUnitOrdrs")

	@TtlCshFrUnitOrdrs.deleter
	def TtlCshFrUnitOrdrs(self):
		del self._TtlCshFrUnitOrdrs
		self._TtlCshFrUnitOrdrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlUnitsFrCshOrdrs', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshFrCshOrdrs', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsFrUnitOrdrs', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshFrUnitOrdrs', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

