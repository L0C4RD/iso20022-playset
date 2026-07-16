# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import CorporateActionPrice82
from . import CorporateActionRate129
from . import CountryCode
from . import CreditDebitCode
from . import DTCBaseDisbursed1Code
from . import DecimalNumber
from . import FinancialInstrumentAttributes130
from . import FractionDispositionType26Choice
from . import GenericIdentification30
from . import NewSecuritiesIssuanceType5Code
from . import NonEligibleProceedsIndicator5Choice
from . import Period6Choice
from . import Quantity51Choice
from . import ReinvestmentIncomeClassification2Code
from . import SafekeepingPlaceFormat41Choice
from . import SecurityDate20
from . import TemporaryFinancialInstrumentIndicator3Choice
from . import YesNoIndicator

class SecuritiesOption114(base_types._BaseFieldType):

	__slots__ = ["_CcyOptn", "_CdtDbtInd", "_ChrgInd", "_CtryOfIncmSrc", "_DtDtls", "_EntitldQty", "_EstmtdPricInd", "_FrctnDspstn", "_IncmTp", "_NewSctiesIssncInd", "_NonElgblPrcdsInd", "_OthrIncmTp", "_PricBsis", "_PricDtls", "_RateDtls", "_RinvstmtIncmClssfctn", "_RndgFctr", "_SctyDtls", "_SfkpgPlc", "_TempFinInstrmInd", "_TradgPrd", "_XmptnTp"]
	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if value is not None else base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

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
	def ChrgInd(self):
		return self._ChrgInd

	@ChrgInd.setter
	def ChrgInd(self, value):
		self._ChrgInd = value if value is not None else base_types.UninitialisedField(self, 'ChrgInd', YesNoIndicator, False)

	@ChrgInd.deleter
	def ChrgInd(self):
		del self._ChrgInd
		self._ChrgInd = base_types.UninitialisedField(self, 'ChrgInd', YesNoIndicator, False)

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
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', SecurityDate20, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', SecurityDate20, False)

	@property
	def EntitldQty(self):
		return self._EntitldQty

	@EntitldQty.setter
	def EntitldQty(self, value):
		self._EntitldQty = value if value is not None else base_types.UninitialisedField(self, 'EntitldQty', Quantity51Choice, False)

	@EntitldQty.deleter
	def EntitldQty(self):
		del self._EntitldQty
		self._EntitldQty = base_types.UninitialisedField(self, 'EntitldQty', Quantity51Choice, False)

	@property
	def EstmtdPricInd(self):
		return self._EstmtdPricInd

	@EstmtdPricInd.setter
	def EstmtdPricInd(self, value):
		self._EstmtdPricInd = value if value is not None else base_types.UninitialisedField(self, 'EstmtdPricInd', YesNoIndicator, False)

	@EstmtdPricInd.deleter
	def EstmtdPricInd(self):
		del self._EstmtdPricInd
		self._EstmtdPricInd = base_types.UninitialisedField(self, 'EstmtdPricInd', YesNoIndicator, False)

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType26Choice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType26Choice, False)

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
	def NewSctiesIssncInd(self):
		return self._NewSctiesIssncInd

	@NewSctiesIssncInd.setter
	def NewSctiesIssncInd(self, value):
		self._NewSctiesIssncInd = value if value is not None else base_types.UninitialisedField(self, 'NewSctiesIssncInd', NewSecuritiesIssuanceType5Code, False)

	@NewSctiesIssncInd.deleter
	def NewSctiesIssncInd(self):
		del self._NewSctiesIssncInd
		self._NewSctiesIssncInd = base_types.UninitialisedField(self, 'NewSctiesIssncInd', NewSecuritiesIssuanceType5Code, False)

	@property
	def NonElgblPrcdsInd(self):
		return self._NonElgblPrcdsInd

	@NonElgblPrcdsInd.setter
	def NonElgblPrcdsInd(self, value):
		self._NonElgblPrcdsInd = value if value is not None else base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator5Choice, False)

	@NonElgblPrcdsInd.deleter
	def NonElgblPrcdsInd(self):
		del self._NonElgblPrcdsInd
		self._NonElgblPrcdsInd = base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator5Choice, False)

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
	def PricBsis(self):
		return self._PricBsis

	@PricBsis.setter
	def PricBsis(self, value):
		self._PricBsis = value if value is not None else base_types.UninitialisedField(self, 'PricBsis', DTCBaseDisbursed1Code, False)

	@PricBsis.deleter
	def PricBsis(self):
		del self._PricBsis
		self._PricBsis = base_types.UninitialisedField(self, 'PricBsis', DTCBaseDisbursed1Code, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice82, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice82, False)

	@property
	def RateDtls(self):
		return self._RateDtls

	@RateDtls.setter
	def RateDtls(self, value):
		self._RateDtls = value if value is not None else base_types.UninitialisedField(self, 'RateDtls', CorporateActionRate129, False)

	@RateDtls.deleter
	def RateDtls(self):
		del self._RateDtls
		self._RateDtls = base_types.UninitialisedField(self, 'RateDtls', CorporateActionRate129, False)

	@property
	def RinvstmtIncmClssfctn(self):
		return self._RinvstmtIncmClssfctn

	@RinvstmtIncmClssfctn.setter
	def RinvstmtIncmClssfctn(self, value):
		self._RinvstmtIncmClssfctn = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtIncmClssfctn', ReinvestmentIncomeClassification2Code, False)

	@RinvstmtIncmClssfctn.deleter
	def RinvstmtIncmClssfctn(self):
		del self._RinvstmtIncmClssfctn
		self._RinvstmtIncmClssfctn = base_types.UninitialisedField(self, 'RinvstmtIncmClssfctn', ReinvestmentIncomeClassification2Code, False)

	@property
	def RndgFctr(self):
		return self._RndgFctr

	@RndgFctr.setter
	def RndgFctr(self, value):
		self._RndgFctr = value if value is not None else base_types.UninitialisedField(self, 'RndgFctr', DecimalNumber, False)

	@RndgFctr.deleter
	def RndgFctr(self):
		del self._RndgFctr
		self._RndgFctr = base_types.UninitialisedField(self, 'RndgFctr', DecimalNumber, False)

	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if value is not None else base_types.UninitialisedField(self, 'SctyDtls', FinancialInstrumentAttributes130, False)

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = base_types.UninitialisedField(self, 'SctyDtls', FinancialInstrumentAttributes130, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat41Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat41Choice, False)

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if value is not None else base_types.UninitialisedField(self, 'TempFinInstrmInd', TemporaryFinancialInstrumentIndicator3Choice, False)

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = base_types.UninitialisedField(self, 'TempFinInstrmInd', TemporaryFinancialInstrumentIndicator3Choice, False)

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if value is not None else base_types.UninitialisedField(self, 'TradgPrd', Period6Choice, False)

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = base_types.UninitialisedField(self, 'TradgPrd', Period6Choice, False)

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
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=SecurityDate20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdPricInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesIssncInd', type=NewSecuritiesIssuanceType5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricBsis', type=DTCBaseDisbursed1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice82, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateDtls', type=CorporateActionRate129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtIncmClssfctn', type=ReinvestmentIncomeClassification2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgFctr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=FinancialInstrumentAttributes130, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=TemporaryFinancialInstrumentIndicator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))