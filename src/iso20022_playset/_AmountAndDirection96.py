# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import ForeignExchangeTerms27
from . import RestrictedFINActiveCurrencyAndAmount
from . import RestrictedFINActiveOrHistoricCurrencyAndAmount
from . import YesNoIndicator

class AmountAndDirection96(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstInd", "_Amt", "_BrkrgAmtInd", "_CdtDbtInd", "_FXDtls", "_OrgnlCcyAndOrdrdAmt", "_RsrchFeeInd", "_StmpDtyInd", "_ValDt"]
	@property
	def AcrdIntrstInd(self):
		return self._AcrdIntrstInd

	@AcrdIntrstInd.setter
	def AcrdIntrstInd(self, value):
		self._AcrdIntrstInd = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstInd', YesNoIndicator, False)

	@AcrdIntrstInd.deleter
	def AcrdIntrstInd(self):
		del self._AcrdIntrstInd
		self._AcrdIntrstInd = base_types.UninitialisedField(self, 'AcrdIntrstInd', YesNoIndicator, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def BrkrgAmtInd(self):
		return self._BrkrgAmtInd

	@BrkrgAmtInd.setter
	def BrkrgAmtInd(self, value):
		self._BrkrgAmtInd = value if value is not None else base_types.UninitialisedField(self, 'BrkrgAmtInd', YesNoIndicator, False)

	@BrkrgAmtInd.deleter
	def BrkrgAmtInd(self):
		del self._BrkrgAmtInd
		self._BrkrgAmtInd = base_types.UninitialisedField(self, 'BrkrgAmtInd', YesNoIndicator, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms27, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms27, False)

	@property
	def OrgnlCcyAndOrdrdAmt(self):
		return self._OrgnlCcyAndOrdrdAmt

	@OrgnlCcyAndOrdrdAmt.setter
	def OrgnlCcyAndOrdrdAmt(self, value):
		self._OrgnlCcyAndOrdrdAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCcyAndOrdrdAmt', RestrictedFINActiveOrHistoricCurrencyAndAmount, False)

	@OrgnlCcyAndOrdrdAmt.deleter
	def OrgnlCcyAndOrdrdAmt(self):
		del self._OrgnlCcyAndOrdrdAmt
		self._OrgnlCcyAndOrdrdAmt = base_types.UninitialisedField(self, 'OrgnlCcyAndOrdrdAmt', RestrictedFINActiveOrHistoricCurrencyAndAmount, False)

	@property
	def RsrchFeeInd(self):
		return self._RsrchFeeInd

	@RsrchFeeInd.setter
	def RsrchFeeInd(self, value):
		self._RsrchFeeInd = value if value is not None else base_types.UninitialisedField(self, 'RsrchFeeInd', YesNoIndicator, False)

	@RsrchFeeInd.deleter
	def RsrchFeeInd(self):
		del self._RsrchFeeInd
		self._RsrchFeeInd = base_types.UninitialisedField(self, 'RsrchFeeInd', YesNoIndicator, False)

	@property
	def StmpDtyInd(self):
		return self._StmpDtyInd

	@StmpDtyInd.setter
	def StmpDtyInd(self, value):
		self._StmpDtyInd = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyInd', YesNoIndicator, False)

	@StmpDtyInd.deleter
	def StmpDtyInd(self):
		del self._StmpDtyInd
		self._StmpDtyInd = base_types.UninitialisedField(self, 'StmpDtyInd', YesNoIndicator, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrgAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAndOrdrdAmt', type=RestrictedFINActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))