from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._PercentageRate import PercentageRate
from ._DecimalNumber import DecimalNumber

class FinancialInstrumentQuantity26Choice(base_types._BaseFieldType):

	__slots__ = ["_GrssAmt", "_UnitsNb", "_PctgOfTtlRedAmt", "_NetAmt"]
	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	@property
	def PctgOfTtlRedAmt(self):
		return self._PctgOfTtlRedAmt

	@PctgOfTtlRedAmt.setter
	def PctgOfTtlRedAmt(self, value):
		self._PctgOfTtlRedAmt = value if type(value) != base_types.auto else self.make_default("PctgOfTtlRedAmt")

	@PctgOfTtlRedAmt.deleter
	def PctgOfTtlRedAmt(self):
		del self._PctgOfTtlRedAmt
		self._PctgOfTtlRedAmt = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgOfTtlRedAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

