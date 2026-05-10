from . import base_types
from .PercentageRate import PercentageRate
from .DecimalNumber import DecimalNumber
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class FinancialInstrumentQuantity29Choice(base_types._BaseFieldType):

	__slots__ = ["_GrssAmt", "_UnitsNb", "_NetAmt", "_PctgOfTtlSbcptAmt", "_HldgsRedRate"]
	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def PctgOfTtlSbcptAmt(self):
		return self._PctgOfTtlSbcptAmt

	@PctgOfTtlSbcptAmt.setter
	def PctgOfTtlSbcptAmt(self, value):
		self._PctgOfTtlSbcptAmt = value if type(value) != auto else self.make_default("PctgOfTtlSbcptAmt")

	@PctgOfTtlSbcptAmt.deleter
	def PctgOfTtlSbcptAmt(self):
		del self._PctgOfTtlSbcptAmt
		self._PctgOfTtlSbcptAmt = None

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if type(value) != auto else self.make_default("HldgsRedRate")

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgOfTtlSbcptAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

