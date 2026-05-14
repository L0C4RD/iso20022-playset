# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._CreditDebitCode import CreditDebitCode
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._ForeignExchangeTerms23 import ForeignExchangeTerms23
from ._YesNoIndicator import YesNoIndicator

class AmountAndDirection94(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstInd", "_Amt", "_BrkrgAmtInd", "_CdtDbtInd", "_FXDtls", "_OrgnlCcyAndOrdrdAmt", "_RsrchFeeInd", "_StmpDtyInd", "_ValDt"]
	@property
	def AcrdIntrstInd(self):
		return self._AcrdIntrstInd

	@AcrdIntrstInd.setter
	def AcrdIntrstInd(self, value):
		self._AcrdIntrstInd = value if type(value) != base_types.auto else self.make_default("AcrdIntrstInd")

	@AcrdIntrstInd.deleter
	def AcrdIntrstInd(self):
		del self._AcrdIntrstInd
		self._AcrdIntrstInd = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def BrkrgAmtInd(self):
		return self._BrkrgAmtInd

	@BrkrgAmtInd.setter
	def BrkrgAmtInd(self, value):
		self._BrkrgAmtInd = value if type(value) != base_types.auto else self.make_default("BrkrgAmtInd")

	@BrkrgAmtInd.deleter
	def BrkrgAmtInd(self):
		del self._BrkrgAmtInd
		self._BrkrgAmtInd = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def OrgnlCcyAndOrdrdAmt(self):
		return self._OrgnlCcyAndOrdrdAmt

	@OrgnlCcyAndOrdrdAmt.setter
	def OrgnlCcyAndOrdrdAmt(self, value):
		self._OrgnlCcyAndOrdrdAmt = value if type(value) != base_types.auto else self.make_default("OrgnlCcyAndOrdrdAmt")

	@OrgnlCcyAndOrdrdAmt.deleter
	def OrgnlCcyAndOrdrdAmt(self):
		del self._OrgnlCcyAndOrdrdAmt
		self._OrgnlCcyAndOrdrdAmt = None

	@property
	def RsrchFeeInd(self):
		return self._RsrchFeeInd

	@RsrchFeeInd.setter
	def RsrchFeeInd(self, value):
		self._RsrchFeeInd = value if type(value) != base_types.auto else self.make_default("RsrchFeeInd")

	@RsrchFeeInd.deleter
	def RsrchFeeInd(self):
		del self._RsrchFeeInd
		self._RsrchFeeInd = None

	@property
	def StmpDtyInd(self):
		return self._StmpDtyInd

	@StmpDtyInd.setter
	def StmpDtyInd(self, value):
		self._StmpDtyInd = value if type(value) != base_types.auto else self.make_default("StmpDtyInd")

	@StmpDtyInd.deleter
	def StmpDtyInd(self):
		del self._StmpDtyInd
		self._StmpDtyInd = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrgAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAndOrdrdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))