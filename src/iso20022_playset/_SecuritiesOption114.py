from . import base_types
from .ReinvestmentIncomeClassification2Code import ReinvestmentIncomeClassification2Code
from .NonEligibleProceedsIndicator5Choice import NonEligibleProceedsIndicator5Choice
from .CountryCode import CountryCode
from .FinancialInstrumentAttributes130 import FinancialInstrumentAttributes130
from .Period6Choice import Period6Choice
from .ActiveCurrencyCode import ActiveCurrencyCode
from .CorporateActionPrice82 import CorporateActionPrice82
from .DecimalNumber import DecimalNumber
from .CorporateActionRate129 import CorporateActionRate129
from .YesNoIndicator import YesNoIndicator
from .CreditDebitCode import CreditDebitCode
from .TemporaryFinancialInstrumentIndicator3Choice import TemporaryFinancialInstrumentIndicator3Choice
from .GenericIdentification30 import GenericIdentification30
from .Quantity51Choice import Quantity51Choice
from .DTCBaseDisbursed1Code import DTCBaseDisbursed1Code
from .NewSecuritiesIssuanceType5Code import NewSecuritiesIssuanceType5Code
from .SecurityDate20 import SecurityDate20
from .SafekeepingPlaceFormat41Choice import SafekeepingPlaceFormat41Choice
from .FractionDispositionType26Choice import FractionDispositionType26Choice

class SecuritiesOption114(base_types._BaseFieldType):

	__slots__ = ["_ChrgInd", "_PricDtls", "_CtryOfIncmSrc", "_SctyDtls", "_SfkpgPlc", "_RinvstmtIncmClssfctn", "_NonElgblPrcdsInd", "_IncmTp", "_EntitldQty", "_XmptnTp", "_RndgFctr", "_TempFinInstrmInd", "_EstmtdPricInd", "_RateDtls", "_OthrIncmTp", "_TradgPrd", "_PricBsis", "_NewSctiesIssncInd", "_CdtDbtInd", "_FrctnDspstn", "_DtDtls", "_CcyOptn"]
	@property
	def ChrgInd(self):
		return self._ChrgInd

	@ChrgInd.setter
	def ChrgInd(self, value):
		self._ChrgInd = value if type(value) != base_types.auto else self.make_default("ChrgInd")

	@ChrgInd.deleter
	def ChrgInd(self):
		del self._ChrgInd
		self._ChrgInd = None

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
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if type(value) != base_types.auto else self.make_default("SctyDtls")

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def RinvstmtIncmClssfctn(self):
		return self._RinvstmtIncmClssfctn

	@RinvstmtIncmClssfctn.setter
	def RinvstmtIncmClssfctn(self, value):
		self._RinvstmtIncmClssfctn = value if type(value) != base_types.auto else self.make_default("RinvstmtIncmClssfctn")

	@RinvstmtIncmClssfctn.deleter
	def RinvstmtIncmClssfctn(self):
		del self._RinvstmtIncmClssfctn
		self._RinvstmtIncmClssfctn = None

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
	def EntitldQty(self):
		return self._EntitldQty

	@EntitldQty.setter
	def EntitldQty(self, value):
		self._EntitldQty = value if type(value) != base_types.auto else self.make_default("EntitldQty")

	@EntitldQty.deleter
	def EntitldQty(self):
		del self._EntitldQty
		self._EntitldQty = None

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
	def RndgFctr(self):
		return self._RndgFctr

	@RndgFctr.setter
	def RndgFctr(self, value):
		self._RndgFctr = value if type(value) != base_types.auto else self.make_default("RndgFctr")

	@RndgFctr.deleter
	def RndgFctr(self):
		del self._RndgFctr
		self._RndgFctr = None

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if type(value) != base_types.auto else self.make_default("TempFinInstrmInd")

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = None

	@property
	def EstmtdPricInd(self):
		return self._EstmtdPricInd

	@EstmtdPricInd.setter
	def EstmtdPricInd(self, value):
		self._EstmtdPricInd = value if type(value) != base_types.auto else self.make_default("EstmtdPricInd")

	@EstmtdPricInd.deleter
	def EstmtdPricInd(self):
		del self._EstmtdPricInd
		self._EstmtdPricInd = None

	@property
	def RateDtls(self):
		return self._RateDtls

	@RateDtls.setter
	def RateDtls(self, value):
		self._RateDtls = value if type(value) != base_types.auto else self.make_default("RateDtls")

	@RateDtls.deleter
	def RateDtls(self):
		del self._RateDtls
		self._RateDtls = None

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
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if type(value) != base_types.auto else self.make_default("TradgPrd")

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = None

	@property
	def PricBsis(self):
		return self._PricBsis

	@PricBsis.setter
	def PricBsis(self, value):
		self._PricBsis = value if type(value) != base_types.auto else self.make_default("PricBsis")

	@PricBsis.deleter
	def PricBsis(self):
		del self._PricBsis
		self._PricBsis = None

	@property
	def NewSctiesIssncInd(self):
		return self._NewSctiesIssncInd

	@NewSctiesIssncInd.setter
	def NewSctiesIssncInd(self, value):
		self._NewSctiesIssncInd = value if type(value) != base_types.auto else self.make_default("NewSctiesIssncInd")

	@NewSctiesIssncInd.deleter
	def NewSctiesIssncInd(self):
		del self._NewSctiesIssncInd
		self._NewSctiesIssncInd = None

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
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != base_types.auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

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
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if type(value) != base_types.auto else self.make_default("CcyOptn")

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice82, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=FinancialInstrumentAttributes130, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtIncmClssfctn', type=ReinvestmentIncomeClassification2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RndgFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=TemporaryFinancialInstrumentIndicator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdPricInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateDtls', type=CorporateActionRate129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricBsis', type=DTCBaseDisbursed1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesIssncInd', type=NewSecuritiesIssuanceType5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=SecurityDate20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

