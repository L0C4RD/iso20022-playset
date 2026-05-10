from . import base_types
from ._EarlyPaymentsVAT1 import EarlyPaymentsVAT1
from ._ISODate import ISODate
from ._PercentageRate import PercentageRate
from ._CurrencyAndAmount import CurrencyAndAmount

class EarlyPayment1(base_types._BaseFieldType):

	__slots__ = ["_DuePyblAmtWthEarlyPmt", "_DscntPct", "_DscntAmt", "_EarlyPmtDt", "_EarlyPmtTaxTtl", "_EarlyPmtTaxSpcfctn"]
	@property
	def DuePyblAmtWthEarlyPmt(self):
		return self._DuePyblAmtWthEarlyPmt

	@DuePyblAmtWthEarlyPmt.setter
	def DuePyblAmtWthEarlyPmt(self, value):
		self._DuePyblAmtWthEarlyPmt = value if type(value) != base_types.auto else self.make_default("DuePyblAmtWthEarlyPmt")

	@DuePyblAmtWthEarlyPmt.deleter
	def DuePyblAmtWthEarlyPmt(self):
		del self._DuePyblAmtWthEarlyPmt
		self._DuePyblAmtWthEarlyPmt = None

	@property
	def DscntPct(self):
		return self._DscntPct

	@DscntPct.setter
	def DscntPct(self, value):
		self._DscntPct = value if type(value) != base_types.auto else self.make_default("DscntPct")

	@DscntPct.deleter
	def DscntPct(self):
		del self._DscntPct
		self._DscntPct = None

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if type(value) != base_types.auto else self.make_default("DscntAmt")

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = None

	@property
	def EarlyPmtDt(self):
		return self._EarlyPmtDt

	@EarlyPmtDt.setter
	def EarlyPmtDt(self, value):
		self._EarlyPmtDt = value if type(value) != base_types.auto else self.make_default("EarlyPmtDt")

	@EarlyPmtDt.deleter
	def EarlyPmtDt(self):
		del self._EarlyPmtDt
		self._EarlyPmtDt = None

	@property
	def EarlyPmtTaxTtl(self):
		return self._EarlyPmtTaxTtl

	@EarlyPmtTaxTtl.setter
	def EarlyPmtTaxTtl(self, value):
		self._EarlyPmtTaxTtl = value if type(value) != base_types.auto else self.make_default("EarlyPmtTaxTtl")

	@EarlyPmtTaxTtl.deleter
	def EarlyPmtTaxTtl(self):
		del self._EarlyPmtTaxTtl
		self._EarlyPmtTaxTtl = None

	@property
	def EarlyPmtTaxSpcfctn(self):
		return self._EarlyPmtTaxSpcfctn

	@EarlyPmtTaxSpcfctn.setter
	def EarlyPmtTaxSpcfctn(self, value):
		self._EarlyPmtTaxSpcfctn = value if type(value) != base_types.auto else self.make_default("EarlyPmtTaxSpcfctn")

	@EarlyPmtTaxSpcfctn.deleter
	def EarlyPmtTaxSpcfctn(self):
		del self._EarlyPmtTaxSpcfctn
		self._EarlyPmtTaxSpcfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DuePyblAmtWthEarlyPmt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtTaxTtl', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtTaxSpcfctn', type=EarlyPaymentsVAT1, min=0, max=None, mutex_group=None, array=True),
	))

