# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import EarlyPaymentsVAT1
from . import ISODate
from . import PercentageRate

class EarlyPayment1(base_types._BaseFieldType):

	__slots__ = ["_DscntAmt", "_DscntPct", "_DuePyblAmtWthEarlyPmt", "_EarlyPmtDt", "_EarlyPmtTaxSpcfctn", "_EarlyPmtTaxTtl"]
	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntAmt', CurrencyAndAmount, False)

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = base_types.UninitialisedField(self, 'DscntAmt', CurrencyAndAmount, False)

	@property
	def DscntPct(self):
		return self._DscntPct

	@DscntPct.setter
	def DscntPct(self, value):
		self._DscntPct = value if value is not None else base_types.UninitialisedField(self, 'DscntPct', PercentageRate, False)

	@DscntPct.deleter
	def DscntPct(self):
		del self._DscntPct
		self._DscntPct = base_types.UninitialisedField(self, 'DscntPct', PercentageRate, False)

	@property
	def DuePyblAmtWthEarlyPmt(self):
		return self._DuePyblAmtWthEarlyPmt

	@DuePyblAmtWthEarlyPmt.setter
	def DuePyblAmtWthEarlyPmt(self, value):
		self._DuePyblAmtWthEarlyPmt = value if value is not None else base_types.UninitialisedField(self, 'DuePyblAmtWthEarlyPmt', CurrencyAndAmount, False)

	@DuePyblAmtWthEarlyPmt.deleter
	def DuePyblAmtWthEarlyPmt(self):
		del self._DuePyblAmtWthEarlyPmt
		self._DuePyblAmtWthEarlyPmt = base_types.UninitialisedField(self, 'DuePyblAmtWthEarlyPmt', CurrencyAndAmount, False)

	@property
	def EarlyPmtDt(self):
		return self._EarlyPmtDt

	@EarlyPmtDt.setter
	def EarlyPmtDt(self, value):
		self._EarlyPmtDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmtDt', ISODate, False)

	@EarlyPmtDt.deleter
	def EarlyPmtDt(self):
		del self._EarlyPmtDt
		self._EarlyPmtDt = base_types.UninitialisedField(self, 'EarlyPmtDt', ISODate, False)

	@property
	def EarlyPmtTaxSpcfctn(self):
		return self._EarlyPmtTaxSpcfctn

	@EarlyPmtTaxSpcfctn.setter
	def EarlyPmtTaxSpcfctn(self, value):
		self._EarlyPmtTaxSpcfctn = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmtTaxSpcfctn', EarlyPaymentsVAT1, True)

	@EarlyPmtTaxSpcfctn.deleter
	def EarlyPmtTaxSpcfctn(self):
		del self._EarlyPmtTaxSpcfctn
		self._EarlyPmtTaxSpcfctn = base_types.UninitialisedField(self, 'EarlyPmtTaxSpcfctn', EarlyPaymentsVAT1, True)

	@property
	def EarlyPmtTaxTtl(self):
		return self._EarlyPmtTaxTtl

	@EarlyPmtTaxTtl.setter
	def EarlyPmtTaxTtl(self, value):
		self._EarlyPmtTaxTtl = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmtTaxTtl', CurrencyAndAmount, False)

	@EarlyPmtTaxTtl.deleter
	def EarlyPmtTaxTtl(self):
		del self._EarlyPmtTaxTtl
		self._EarlyPmtTaxTtl = base_types.UninitialisedField(self, 'EarlyPmtTaxTtl', CurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPct', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DuePyblAmtWthEarlyPmt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmtTaxSpcfctn', type=EarlyPaymentsVAT1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlyPmtTaxTtl', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))