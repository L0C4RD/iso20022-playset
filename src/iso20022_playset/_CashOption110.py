from . import base_types
from .CreditDebitCode import CreditDebitCode
from .ForeignExchangeTerms41 import ForeignExchangeTerms41
from .TaxVoucher5 import TaxVoucher5
from .CountryCode import CountryCode
from .IssuerOfferorTaxabilityIndicator1Choice import IssuerOfferorTaxabilityIndicator1Choice
from .Rate45 import Rate45
from .CorporateActionAmounts74 import CorporateActionAmounts74
from .Account11Choice import Account11Choice
from .CorporateActionDate99 import CorporateActionDate99
from .CashParties44 import CashParties44
from .GenericIdentification47 import GenericIdentification47
from .Payment1Code import Payment1Code
from .PriceDetails41 import PriceDetails41

class CashOption110(base_types._BaseFieldType):

	__slots__ = ["_IncmTp", "_CtryOfIncmSrc", "_FXDtls", "_RateAndAmtDtls", "_TaxVchrDtls", "_CdtDbtInd", "_OthrIncmTp", "_DtDtls", "_CtrctlPmtInd", "_AmtDtls", "_Acct", "_XmptnTp", "_CshPties", "_PricDtls", "_IssrOfferrTaxbltyInd"]
	@property
	def IncmTp(self):
		return self._IncmTp

	@IncmTp.setter
	def IncmTp(self, value):
		self._IncmTp = value if type(value) != base_types.auto else self.make_default("IncmTp")

	@IncmTp.deleter
	def IncmTp(self):
		del self._IncmTp
		self._IncmTp = None

	@property
	def CtryOfIncmSrc(self):
		return self._CtryOfIncmSrc

	@CtryOfIncmSrc.setter
	def CtryOfIncmSrc(self, value):
		self._CtryOfIncmSrc = value if type(value) != base_types.auto else self.make_default("CtryOfIncmSrc")

	@CtryOfIncmSrc.deleter
	def CtryOfIncmSrc(self):
		del self._CtryOfIncmSrc
		self._CtryOfIncmSrc = None

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
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != base_types.auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def TaxVchrDtls(self):
		return self._TaxVchrDtls

	@TaxVchrDtls.setter
	def TaxVchrDtls(self, value):
		self._TaxVchrDtls = value if type(value) != base_types.auto else self.make_default("TaxVchrDtls")

	@TaxVchrDtls.deleter
	def TaxVchrDtls(self):
		del self._TaxVchrDtls
		self._TaxVchrDtls = None

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
	def OthrIncmTp(self):
		return self._OthrIncmTp

	@OthrIncmTp.setter
	def OthrIncmTp(self, value):
		self._OthrIncmTp = value if type(value) != base_types.auto else self.make_default("OthrIncmTp")

	@OthrIncmTp.deleter
	def OthrIncmTp(self):
		del self._OthrIncmTp
		self._OthrIncmTp = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != base_types.auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

	@property
	def CtrctlPmtInd(self):
		return self._CtrctlPmtInd

	@CtrctlPmtInd.setter
	def CtrctlPmtInd(self, value):
		self._CtrctlPmtInd = value if type(value) != base_types.auto else self.make_default("CtrctlPmtInd")

	@CtrctlPmtInd.deleter
	def CtrctlPmtInd(self):
		del self._CtrctlPmtInd
		self._CtrctlPmtInd = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != base_types.auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def XmptnTp(self):
		return self._XmptnTp

	@XmptnTp.setter
	def XmptnTp(self, value):
		self._XmptnTp = value if type(value) != base_types.auto else self.make_default("XmptnTp")

	@XmptnTp.deleter
	def XmptnTp(self):
		del self._XmptnTp
		self._XmptnTp = None

	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if type(value) != base_types.auto else self.make_default("CshPties")

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def IssrOfferrTaxbltyInd(self):
		return self._IssrOfferrTaxbltyInd

	@IssrOfferrTaxbltyInd.setter
	def IssrOfferrTaxbltyInd(self, value):
		self._IssrOfferrTaxbltyInd = value if type(value) != base_types.auto else self.make_default("IssrOfferrTaxbltyInd")

	@IssrOfferrTaxbltyInd.deleter
	def IssrOfferrTaxbltyInd(self):
		del self._IssrOfferrTaxbltyInd
		self._IssrOfferrTaxbltyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxVchrDtls', type=TaxVoucher5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate99, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctlPmtInd', type=Payment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts74, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshPties', type=CashParties44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceDetails41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator1Choice, min=0, max=1, mutex_group=None, array=False),
	))

