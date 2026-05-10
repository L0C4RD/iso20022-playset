from . import base_types
from ._GenericIdentification47 import GenericIdentification47
from ._PriceDetails43 import PriceDetails43
from ._IssuerOfferorTaxabilityIndicator1Choice import IssuerOfferorTaxabilityIndicator1Choice
from ._CreditDebitCode import CreditDebitCode
from ._ForeignExchangeTerms43 import ForeignExchangeTerms43
from ._Rate47 import Rate47
from ._CountryCode import CountryCode
from ._CorporateActionAmounts76 import CorporateActionAmounts76
from ._Payment2Code import Payment2Code
from ._NonEligibleProceedsIndicator6Choice import NonEligibleProceedsIndicator6Choice
from ._PriceCalculationMethod1Choice import PriceCalculationMethod1Choice
from ._CorporateActionDate97 import CorporateActionDate97
from ._CashAccountIdentification15Choice import CashAccountIdentification15Choice

class CashOption113(base_types._BaseFieldType):

	__slots__ = ["_PricDtls", "_CtrctlPmtInd", "_DtDtls", "_IncmTp", "_AmtDtls", "_CtryOfIncmSrc", "_FXDtls", "_PricClctnMtd", "_IssrOfferrTaxbltyInd", "_CshAcctId", "_XmptnTp", "_OthrIncmTp", "_NonElgblPrcdsInd", "_CdtDbtInd", "_RateAndAmtDtls"]
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
	def PricClctnMtd(self):
		return self._PricClctnMtd

	@PricClctnMtd.setter
	def PricClctnMtd(self, value):
		self._PricClctnMtd = value if type(value) != base_types.auto else self.make_default("PricClctnMtd")

	@PricClctnMtd.deleter
	def PricClctnMtd(self):
		del self._PricClctnMtd
		self._PricClctnMtd = None

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

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if type(value) != base_types.auto else self.make_default("CshAcctId")

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = None

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
	def NonElgblPrcdsInd(self):
		return self._NonElgblPrcdsInd

	@NonElgblPrcdsInd.setter
	def NonElgblPrcdsInd(self, value):
		self._NonElgblPrcdsInd = value if type(value) != base_types.auto else self.make_default("NonElgblPrcdsInd")

	@NonElgblPrcdsInd.deleter
	def NonElgblPrcdsInd(self):
		del self._NonElgblPrcdsInd
		self._NonElgblPrcdsInd = None

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
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != base_types.auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricDtls', type=PriceDetails43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctlPmtInd', type=Payment2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate97, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts76, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnMtd', type=PriceCalculationMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=CashAccountIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate47, min=0, max=1, mutex_group=None, array=False),
	))

