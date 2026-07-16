# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountIdentification9Choice
from . import CorporateActionAmounts72
from . import CorporateActionDate84
from . import CountryCode
from . import CreditDebitCode
from . import ForeignExchangeTerms39
from . import GenericIdentification30
from . import IssuerOfferorTaxabilityIndicator2Choice
from . import NonEligibleProceedsIndicator3Choice
from . import Payment1Code
from . import PriceDetails38
from . import Rate42

class CashOption104(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_CdtDbtInd", "_CshAcctId", "_CtrctlPmtInd", "_CtryOfIncmSrc", "_DtDtls", "_FXDtls", "_IncmTp", "_IssrOfferrTaxbltyInd", "_NonElgblPrcdsInd", "_OthrIncmTp", "_PricDtls", "_RateAndAmtDtls", "_XmptnTp"]
	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts72, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts72, False)

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
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification9Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification9Choice, False)

	@property
	def CtrctlPmtInd(self):
		return self._CtrctlPmtInd

	@CtrctlPmtInd.setter
	def CtrctlPmtInd(self, value):
		self._CtrctlPmtInd = value if value is not None else base_types.UninitialisedField(self, 'CtrctlPmtInd', Payment1Code, False)

	@CtrctlPmtInd.deleter
	def CtrctlPmtInd(self):
		del self._CtrctlPmtInd
		self._CtrctlPmtInd = base_types.UninitialisedField(self, 'CtrctlPmtInd', Payment1Code, False)

	@property
	def CtryOfIncmSrc(self):
		return self._CtryOfIncmSrc

	@CtryOfIncmSrc.setter
	def CtryOfIncmSrc(self, value):
		self._CtryOfIncmSrc = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIncmSrc', CountryCode, False)

	@CtryOfIncmSrc.deleter
	def CtryOfIncmSrc(self):
		del self._CtryOfIncmSrc
		self._CtryOfIncmSrc = base_types.UninitialisedField(self, 'CtryOfIncmSrc', CountryCode, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate84, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate84, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms39, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms39, False)

	@property
	def IncmTp(self):
		return self._IncmTp

	@IncmTp.setter
	def IncmTp(self, value):
		self._IncmTp = value if value is not None else base_types.UninitialisedField(self, 'IncmTp', GenericIdentification30, False)

	@IncmTp.deleter
	def IncmTp(self):
		del self._IncmTp
		self._IncmTp = base_types.UninitialisedField(self, 'IncmTp', GenericIdentification30, False)

	@property
	def IssrOfferrTaxbltyInd(self):
		return self._IssrOfferrTaxbltyInd

	@IssrOfferrTaxbltyInd.setter
	def IssrOfferrTaxbltyInd(self, value):
		self._IssrOfferrTaxbltyInd = value if value is not None else base_types.UninitialisedField(self, 'IssrOfferrTaxbltyInd', IssuerOfferorTaxabilityIndicator2Choice, False)

	@IssrOfferrTaxbltyInd.deleter
	def IssrOfferrTaxbltyInd(self):
		del self._IssrOfferrTaxbltyInd
		self._IssrOfferrTaxbltyInd = base_types.UninitialisedField(self, 'IssrOfferrTaxbltyInd', IssuerOfferorTaxabilityIndicator2Choice, False)

	@property
	def NonElgblPrcdsInd(self):
		return self._NonElgblPrcdsInd

	@NonElgblPrcdsInd.setter
	def NonElgblPrcdsInd(self, value):
		self._NonElgblPrcdsInd = value if value is not None else base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator3Choice, False)

	@NonElgblPrcdsInd.deleter
	def NonElgblPrcdsInd(self):
		del self._NonElgblPrcdsInd
		self._NonElgblPrcdsInd = base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator3Choice, False)

	@property
	def OthrIncmTp(self):
		return self._OthrIncmTp

	@OthrIncmTp.setter
	def OthrIncmTp(self, value):
		self._OthrIncmTp = value if value is not None else base_types.UninitialisedField(self, 'OthrIncmTp', GenericIdentification30, True)

	@OthrIncmTp.deleter
	def OthrIncmTp(self):
		del self._OthrIncmTp
		self._OthrIncmTp = base_types.UninitialisedField(self, 'OthrIncmTp', GenericIdentification30, True)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceDetails38, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceDetails38, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate42, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate42, False)

	@property
	def XmptnTp(self):
		return self._XmptnTp

	@XmptnTp.setter
	def XmptnTp(self, value):
		self._XmptnTp = value if value is not None else base_types.UninitialisedField(self, 'XmptnTp', GenericIdentification30, True)

	@XmptnTp.deleter
	def XmptnTp(self):
		del self._XmptnTp
		self._XmptnTp = base_types.UninitialisedField(self, 'XmptnTp', GenericIdentification30, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctlPmtInd', type=Payment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate84, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricDtls', type=PriceDetails38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))