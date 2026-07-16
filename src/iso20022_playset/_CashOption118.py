# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account10Choice
from . import CashParties43
from . import CorporateActionAmounts79
from . import CorporateActionDate99
from . import CountryCode
from . import CreditDebitCode
from . import ForeignExchangeTerms40
from . import GenericIdentification30
from . import IssuerOfferorTaxabilityIndicator2Choice
from . import Payment1Code
from . import PriceDetails37
from . import Rate51
from . import TaxVoucher6

class CashOption118(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AmtDtls", "_CdtDbtInd", "_CshPties", "_CtrctlPmtInd", "_CtryOfIncmSrc", "_DtDtls", "_FXDtls", "_IncmTp", "_IssrOfferrTaxbltyInd", "_OthrIncmTp", "_PricDtls", "_RateAndAmtDtls", "_TaxDcmnttnDtls", "_XmptnTp"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', Account10Choice, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', Account10Choice, False)

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts79, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts79, False)

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
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if value is not None else base_types.UninitialisedField(self, 'CshPties', CashParties43, False)

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = base_types.UninitialisedField(self, 'CshPties', CashParties43, False)

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
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate99, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate99, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms40, True)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms40, True)

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
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceDetails37, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceDetails37, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate51, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate51, False)

	@property
	def TaxDcmnttnDtls(self):
		return self._TaxDcmnttnDtls

	@TaxDcmnttnDtls.setter
	def TaxDcmnttnDtls(self, value):
		self._TaxDcmnttnDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxDcmnttnDtls', TaxVoucher6, False)

	@TaxDcmnttnDtls.deleter
	def TaxDcmnttnDtls(self):
		del self._TaxDcmnttnDtls
		self._TaxDcmnttnDtls = base_types.UninitialisedField(self, 'TaxDcmnttnDtls', TaxVoucher6, False)

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
		base_types.FieldEntry(name='Acct', type=Account10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts79, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctlPmtInd', type=Payment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate99, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricDtls', type=PriceDetails37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDcmnttnDtls', type=TaxVoucher6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))