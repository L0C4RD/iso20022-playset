# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBusinessProcessFormat25Choice
from . import CapitalGainFormat3Choice
from . import CertificationTypeFormat3Choice
from . import ConsentTypeFormat4Choice
from . import CorporateActionAmounts80
from . import CorporateActionBalanceDetails48
from . import CorporateActionChangeTypeFormat5Choice
from . import CorporateActionDate83
from . import CorporateActionEventStageFormat13Choice
from . import CorporateActionLotteryEvent1
from . import CorporateActionNarrative58
from . import CorporateActionPeriod17
from . import CorporateActionPrice85
from . import CorporateActionQuantity15
from . import CorporateActionRate122
from . import CorporateActionSD26
from . import CorporateActionSupplementaryIndicators2
from . import DistributionTypeFormat7Choice
from . import DividendTypeFormat9Choice
from . import DutchAuctionTypeFormat1Choice
from . import Exact3UpperCaseAlphaNumericText
from . import GenericIdentification30
from . import InformationTypeFormat4Choice
from . import IntermediateSecuritiesDistributionTypeFormat19Choice
from . import Max350Text
from . import Max3Number
from . import OfferTypeFormat18Choice
from . import ProrationReturnQuantityTreatment1Code
from . import RedemptionAnnouncementNoticeType1Code
from . import RenounceableEntitlementStatusTypeFormat3Choice
from . import TaxableIncomePerShareCalculatedFormat3Choice
from . import YesNoIndicator

class CorporateAction88(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AcrdIntrstInd", "_AddtlBizPrcInd", "_AddtlInf", "_AmtDtls", "_CertDtls", "_CertfctnTp", "_ChngTp", "_ChrgsApldInd", "_CnsntTp", "_CptlGnInOutInd", "_DtDtls", "_DtchAuctnTp", "_DvddTp", "_EvtBalDtls", "_EvtStag", "_FllwngEvtTpInd", "_FrftrOfIntrstInd", "_InfTp", "_IntrstAcrdNbOfDays", "_LtryEvtInf", "_NewPlcOfIncorprtn", "_NtceTp", "_OcrncTp", "_OfferTp", "_PrdDtls", "_PricDtls", "_PrratnRtrMinQtyTrtmnt", "_RateAndAmtDtls", "_RnncblEntitlmntStsTp", "_RstrctnInd", "_RvsDtchAuctnInd", "_SctiesQty", "_SplmtryIndctrs", "_TaxOnNonDstrbtdPrcdsInd", "_TaxblIncmPerShrClctd"]
	@property
	def AccptncPrtyLvl(self):
		return self._AccptncPrtyLvl

	@AccptncPrtyLvl.setter
	def AccptncPrtyLvl(self, value):
		self._AccptncPrtyLvl = value if value is not None else base_types.UninitialisedField(self, 'AccptncPrtyLvl', Exact3UpperCaseAlphaNumericText, False)

	@AccptncPrtyLvl.deleter
	def AccptncPrtyLvl(self):
		del self._AccptncPrtyLvl
		self._AccptncPrtyLvl = base_types.UninitialisedField(self, 'AccptncPrtyLvl', Exact3UpperCaseAlphaNumericText, False)

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
	def AddtlBizPrcInd(self):
		return self._AddtlBizPrcInd

	@AddtlBizPrcInd.setter
	def AddtlBizPrcInd(self, value):
		self._AddtlBizPrcInd = value if value is not None else base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat25Choice, True)

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat25Choice, True)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative58, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative58, False)

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts80, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts80, False)

	@property
	def CertDtls(self):
		return self._CertDtls

	@CertDtls.setter
	def CertDtls(self, value):
		self._CertDtls = value if value is not None else base_types.UninitialisedField(self, 'CertDtls', CorporateActionSD26, True)

	@CertDtls.deleter
	def CertDtls(self):
		del self._CertDtls
		self._CertDtls = base_types.UninitialisedField(self, 'CertDtls', CorporateActionSD26, True)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', CertificationTypeFormat3Choice, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', CertificationTypeFormat3Choice, False)

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if value is not None else base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat5Choice, True)

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat5Choice, True)

	@property
	def ChrgsApldInd(self):
		return self._ChrgsApldInd

	@ChrgsApldInd.setter
	def ChrgsApldInd(self, value):
		self._ChrgsApldInd = value if value is not None else base_types.UninitialisedField(self, 'ChrgsApldInd', YesNoIndicator, False)

	@ChrgsApldInd.deleter
	def ChrgsApldInd(self):
		del self._ChrgsApldInd
		self._ChrgsApldInd = base_types.UninitialisedField(self, 'ChrgsApldInd', YesNoIndicator, False)

	@property
	def CnsntTp(self):
		return self._CnsntTp

	@CnsntTp.setter
	def CnsntTp(self, value):
		self._CnsntTp = value if value is not None else base_types.UninitialisedField(self, 'CnsntTp', ConsentTypeFormat4Choice, False)

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = base_types.UninitialisedField(self, 'CnsntTp', ConsentTypeFormat4Choice, False)

	@property
	def CptlGnInOutInd(self):
		return self._CptlGnInOutInd

	@CptlGnInOutInd.setter
	def CptlGnInOutInd(self, value):
		self._CptlGnInOutInd = value if value is not None else base_types.UninitialisedField(self, 'CptlGnInOutInd', CapitalGainFormat3Choice, False)

	@CptlGnInOutInd.deleter
	def CptlGnInOutInd(self):
		del self._CptlGnInOutInd
		self._CptlGnInOutInd = base_types.UninitialisedField(self, 'CptlGnInOutInd', CapitalGainFormat3Choice, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate83, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate83, False)

	@property
	def DtchAuctnTp(self):
		return self._DtchAuctnTp

	@DtchAuctnTp.setter
	def DtchAuctnTp(self, value):
		self._DtchAuctnTp = value if value is not None else base_types.UninitialisedField(self, 'DtchAuctnTp', DutchAuctionTypeFormat1Choice, False)

	@DtchAuctnTp.deleter
	def DtchAuctnTp(self):
		del self._DtchAuctnTp
		self._DtchAuctnTp = base_types.UninitialisedField(self, 'DtchAuctnTp', DutchAuctionTypeFormat1Choice, False)

	@property
	def DvddTp(self):
		return self._DvddTp

	@DvddTp.setter
	def DvddTp(self, value):
		self._DvddTp = value if value is not None else base_types.UninitialisedField(self, 'DvddTp', DividendTypeFormat9Choice, False)

	@DvddTp.deleter
	def DvddTp(self):
		del self._DvddTp
		self._DvddTp = base_types.UninitialisedField(self, 'DvddTp', DividendTypeFormat9Choice, False)

	@property
	def EvtBalDtls(self):
		return self._EvtBalDtls

	@EvtBalDtls.setter
	def EvtBalDtls(self, value):
		self._EvtBalDtls = value if value is not None else base_types.UninitialisedField(self, 'EvtBalDtls', CorporateActionBalanceDetails48, False)

	@EvtBalDtls.deleter
	def EvtBalDtls(self):
		del self._EvtBalDtls
		self._EvtBalDtls = base_types.UninitialisedField(self, 'EvtBalDtls', CorporateActionBalanceDetails48, False)

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if value is not None else base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat13Choice, True)

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat13Choice, True)

	@property
	def FllwngEvtTpInd(self):
		return self._FllwngEvtTpInd

	@FllwngEvtTpInd.setter
	def FllwngEvtTpInd(self, value):
		self._FllwngEvtTpInd = value if value is not None else base_types.UninitialisedField(self, 'FllwngEvtTpInd', IntermediateSecuritiesDistributionTypeFormat19Choice, False)

	@FllwngEvtTpInd.deleter
	def FllwngEvtTpInd(self):
		del self._FllwngEvtTpInd
		self._FllwngEvtTpInd = base_types.UninitialisedField(self, 'FllwngEvtTpInd', IntermediateSecuritiesDistributionTypeFormat19Choice, False)

	@property
	def FrftrOfIntrstInd(self):
		return self._FrftrOfIntrstInd

	@FrftrOfIntrstInd.setter
	def FrftrOfIntrstInd(self, value):
		self._FrftrOfIntrstInd = value if value is not None else base_types.UninitialisedField(self, 'FrftrOfIntrstInd', YesNoIndicator, False)

	@FrftrOfIntrstInd.deleter
	def FrftrOfIntrstInd(self):
		del self._FrftrOfIntrstInd
		self._FrftrOfIntrstInd = base_types.UninitialisedField(self, 'FrftrOfIntrstInd', YesNoIndicator, False)

	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if value is not None else base_types.UninitialisedField(self, 'InfTp', InformationTypeFormat4Choice, False)

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = base_types.UninitialisedField(self, 'InfTp', InformationTypeFormat4Choice, False)

	@property
	def IntrstAcrdNbOfDays(self):
		return self._IntrstAcrdNbOfDays

	@IntrstAcrdNbOfDays.setter
	def IntrstAcrdNbOfDays(self, value):
		self._IntrstAcrdNbOfDays = value if value is not None else base_types.UninitialisedField(self, 'IntrstAcrdNbOfDays', Max3Number, False)

	@IntrstAcrdNbOfDays.deleter
	def IntrstAcrdNbOfDays(self):
		del self._IntrstAcrdNbOfDays
		self._IntrstAcrdNbOfDays = base_types.UninitialisedField(self, 'IntrstAcrdNbOfDays', Max3Number, False)

	@property
	def LtryEvtInf(self):
		return self._LtryEvtInf

	@LtryEvtInf.setter
	def LtryEvtInf(self, value):
		self._LtryEvtInf = value if value is not None else base_types.UninitialisedField(self, 'LtryEvtInf', CorporateActionLotteryEvent1, False)

	@LtryEvtInf.deleter
	def LtryEvtInf(self):
		del self._LtryEvtInf
		self._LtryEvtInf = base_types.UninitialisedField(self, 'LtryEvtInf', CorporateActionLotteryEvent1, False)

	@property
	def NewPlcOfIncorprtn(self):
		return self._NewPlcOfIncorprtn

	@NewPlcOfIncorprtn.setter
	def NewPlcOfIncorprtn(self, value):
		self._NewPlcOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max350Text, False)

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max350Text, False)

	@property
	def NtceTp(self):
		return self._NtceTp

	@NtceTp.setter
	def NtceTp(self, value):
		self._NtceTp = value if value is not None else base_types.UninitialisedField(self, 'NtceTp', RedemptionAnnouncementNoticeType1Code, False)

	@NtceTp.deleter
	def NtceTp(self):
		del self._NtceTp
		self._NtceTp = base_types.UninitialisedField(self, 'NtceTp', RedemptionAnnouncementNoticeType1Code, False)

	@property
	def OcrncTp(self):
		return self._OcrncTp

	@OcrncTp.setter
	def OcrncTp(self, value):
		self._OcrncTp = value if value is not None else base_types.UninitialisedField(self, 'OcrncTp', DistributionTypeFormat7Choice, False)

	@OcrncTp.deleter
	def OcrncTp(self):
		del self._OcrncTp
		self._OcrncTp = base_types.UninitialisedField(self, 'OcrncTp', DistributionTypeFormat7Choice, False)

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if value is not None else base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat18Choice, True)

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat18Choice, True)

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod17, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod17, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice85, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice85, False)

	@property
	def PrratnRtrMinQtyTrtmnt(self):
		return self._PrratnRtrMinQtyTrtmnt

	@PrratnRtrMinQtyTrtmnt.setter
	def PrratnRtrMinQtyTrtmnt(self, value):
		self._PrratnRtrMinQtyTrtmnt = value if value is not None else base_types.UninitialisedField(self, 'PrratnRtrMinQtyTrtmnt', ProrationReturnQuantityTreatment1Code, False)

	@PrratnRtrMinQtyTrtmnt.deleter
	def PrratnRtrMinQtyTrtmnt(self):
		del self._PrratnRtrMinQtyTrtmnt
		self._PrratnRtrMinQtyTrtmnt = base_types.UninitialisedField(self, 'PrratnRtrMinQtyTrtmnt', ProrationReturnQuantityTreatment1Code, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate122, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate122, False)

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if value is not None else base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat3Choice, False)

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat3Choice, False)

	@property
	def RstrctnInd(self):
		return self._RstrctnInd

	@RstrctnInd.setter
	def RstrctnInd(self, value):
		self._RstrctnInd = value if value is not None else base_types.UninitialisedField(self, 'RstrctnInd', YesNoIndicator, False)

	@RstrctnInd.deleter
	def RstrctnInd(self):
		del self._RstrctnInd
		self._RstrctnInd = base_types.UninitialisedField(self, 'RstrctnInd', YesNoIndicator, False)

	@property
	def RvsDtchAuctnInd(self):
		return self._RvsDtchAuctnInd

	@RvsDtchAuctnInd.setter
	def RvsDtchAuctnInd(self, value):
		self._RvsDtchAuctnInd = value if value is not None else base_types.UninitialisedField(self, 'RvsDtchAuctnInd', YesNoIndicator, False)

	@RvsDtchAuctnInd.deleter
	def RvsDtchAuctnInd(self):
		del self._RvsDtchAuctnInd
		self._RvsDtchAuctnInd = base_types.UninitialisedField(self, 'RvsDtchAuctnInd', YesNoIndicator, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity15, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity15, False)

	@property
	def SplmtryIndctrs(self):
		return self._SplmtryIndctrs

	@SplmtryIndctrs.setter
	def SplmtryIndctrs(self, value):
		self._SplmtryIndctrs = value if value is not None else base_types.UninitialisedField(self, 'SplmtryIndctrs', CorporateActionSupplementaryIndicators2, False)

	@SplmtryIndctrs.deleter
	def SplmtryIndctrs(self):
		del self._SplmtryIndctrs
		self._SplmtryIndctrs = base_types.UninitialisedField(self, 'SplmtryIndctrs', CorporateActionSupplementaryIndicators2, False)

	@property
	def TaxOnNonDstrbtdPrcdsInd(self):
		return self._TaxOnNonDstrbtdPrcdsInd

	@TaxOnNonDstrbtdPrcdsInd.setter
	def TaxOnNonDstrbtdPrcdsInd(self, value):
		self._TaxOnNonDstrbtdPrcdsInd = value if value is not None else base_types.UninitialisedField(self, 'TaxOnNonDstrbtdPrcdsInd', GenericIdentification30, True)

	@TaxOnNonDstrbtdPrcdsInd.deleter
	def TaxOnNonDstrbtdPrcdsInd(self):
		del self._TaxOnNonDstrbtdPrcdsInd
		self._TaxOnNonDstrbtdPrcdsInd = base_types.UninitialisedField(self, 'TaxOnNonDstrbtdPrcdsInd', GenericIdentification30, True)

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculatedFormat3Choice, False)

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculatedFormat3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat25Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts80, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertDtls', type=CorporateActionSD26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnTp', type=CertificationTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=ConsentTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGnInOutInd', type=CapitalGainFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchAuctnTp', type=DutchAuctionTypeFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddTp', type=DividendTypeFormat9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtBalDtls', type=CorporateActionBalanceDetails48, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat13Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FllwngEvtTpInd', type=IntermediateSecuritiesDistributionTypeFormat19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftrOfIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfTp', type=InformationTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryEvtInf', type=CorporateActionLotteryEvent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtceTp', type=RedemptionAnnouncementNoticeType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OcrncTp', type=DistributionTypeFormat7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice85, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnRtrMinQtyTrtmnt', type=ProrationReturnQuantityTreatment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsDtchAuctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryIndctrs', type=CorporateActionSupplementaryIndicators2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnNonDstrbtdPrcdsInd', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculatedFormat3Choice, min=0, max=1, mutex_group=None, array=False),
	))