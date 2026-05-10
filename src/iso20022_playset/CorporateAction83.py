from . import base_types
from .CorporateActionEventStageFormat13Choice import CorporateActionEventStageFormat13Choice
from .DistributionTypeFormat7Choice import DistributionTypeFormat7Choice
from .OfferTypeFormat14Choice import OfferTypeFormat14Choice
from .RenounceableEntitlementStatusTypeFormat3Choice import RenounceableEntitlementStatusTypeFormat3Choice
from .RedemptionAnnouncementNoticeType1Code import RedemptionAnnouncementNoticeType1Code
from .CorporateActionPrice85 import CorporateActionPrice85
from .GenericIdentification30 import GenericIdentification30
from .ConsentTypeFormat4Choice import ConsentTypeFormat4Choice
from .Max3Number import Max3Number
from .DividendTypeFormat9Choice import DividendTypeFormat9Choice
from .TaxableIncomePerShareCalculatedFormat3Choice import TaxableIncomePerShareCalculatedFormat3Choice
from .CorporateActionChangeTypeFormat5Choice import CorporateActionChangeTypeFormat5Choice
from .LotteryTypeFormat4Choice import LotteryTypeFormat4Choice
from .Exact3UpperCaseAlphaNumericText import Exact3UpperCaseAlphaNumericText
from .YesNoIndicator import YesNoIndicator
from .CorporateActionNarrative58 import CorporateActionNarrative58
from .CorporateActionPeriod16 import CorporateActionPeriod16
from .CertificationTypeFormat3Choice import CertificationTypeFormat3Choice
from .Max350Text import Max350Text
from .IntermediateSecuritiesDistributionTypeFormat15Choice import IntermediateSecuritiesDistributionTypeFormat15Choice
from .CorporateActionBalanceDetails47 import CorporateActionBalanceDetails47
from .CorporateActionSD26 import CorporateActionSD26
from .ProrationReturnQuantityTreatment1Code import ProrationReturnQuantityTreatment1Code
from .CorporateActionDate83 import CorporateActionDate83
from .CorporateActionQuantity11 import CorporateActionQuantity11
from .AdditionalBusinessProcessFormat17Choice import AdditionalBusinessProcessFormat17Choice
from .InformationTypeFormat4Choice import InformationTypeFormat4Choice
from .CapitalGainFormat3Choice import CapitalGainFormat3Choice
from .DutchAuctionTypeFormat1Choice import DutchAuctionTypeFormat1Choice
from .CorporateActionAmounts70 import CorporateActionAmounts70
from .CorporateActionSupplementaryIndicators1 import CorporateActionSupplementaryIndicators1
from .CorporateActionRate122 import CorporateActionRate122

class CorporateAction83(base_types._BaseFieldType):

	__slots__ = ["_NtceTp", "_SplmtryIndctrs", "_AmtDtls", "_FrftrOfIntrstInd", "_NewPlcOfIncorprtn", "_AccptncPrtyLvl", "_EvtBalDtls", "_LtryTp", "_ChngTp", "_OcrncTp", "_SctiesQty", "_PricDtls", "_IntrstAcrdNbOfDays", "_CertfctnTp", "_DtDtls", "_PrratnRtrMinQtyTrtmnt", "_CertDtls", "_CptlGnInOutInd", "_TaxOnNonDstrbtdPrcdsInd", "_AddtlBizPrcInd", "_RnncblEntitlmntStsTp", "_RateAndAmtDtls", "_DvddTp", "_TaxblIncmPerShrClctd", "_CnsntTp", "_AddtlInf", "_InfTp", "_RstrctnInd", "_EvtStag", "_OfferTp", "_IntrmdtSctiesDstrbtnTp", "_DtchAuctnTp", "_AcrdIntrstInd", "_PrdDtls", "_ChrgsApldInd"]
	@property
	def NtceTp(self):
		return self._NtceTp

	@NtceTp.setter
	def NtceTp(self, value):
		self._NtceTp = value if type(value) != auto else self.make_default("NtceTp")

	@NtceTp.deleter
	def NtceTp(self):
		del self._NtceTp
		self._NtceTp = None

	@property
	def SplmtryIndctrs(self):
		return self._SplmtryIndctrs

	@SplmtryIndctrs.setter
	def SplmtryIndctrs(self, value):
		self._SplmtryIndctrs = value if type(value) != auto else self.make_default("SplmtryIndctrs")

	@SplmtryIndctrs.deleter
	def SplmtryIndctrs(self):
		del self._SplmtryIndctrs
		self._SplmtryIndctrs = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def FrftrOfIntrstInd(self):
		return self._FrftrOfIntrstInd

	@FrftrOfIntrstInd.setter
	def FrftrOfIntrstInd(self, value):
		self._FrftrOfIntrstInd = value if type(value) != auto else self.make_default("FrftrOfIntrstInd")

	@FrftrOfIntrstInd.deleter
	def FrftrOfIntrstInd(self):
		del self._FrftrOfIntrstInd
		self._FrftrOfIntrstInd = None

	@property
	def NewPlcOfIncorprtn(self):
		return self._NewPlcOfIncorprtn

	@NewPlcOfIncorprtn.setter
	def NewPlcOfIncorprtn(self, value):
		self._NewPlcOfIncorprtn = value if type(value) != auto else self.make_default("NewPlcOfIncorprtn")

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = None

	@property
	def AccptncPrtyLvl(self):
		return self._AccptncPrtyLvl

	@AccptncPrtyLvl.setter
	def AccptncPrtyLvl(self, value):
		self._AccptncPrtyLvl = value if type(value) != auto else self.make_default("AccptncPrtyLvl")

	@AccptncPrtyLvl.deleter
	def AccptncPrtyLvl(self):
		del self._AccptncPrtyLvl
		self._AccptncPrtyLvl = None

	@property
	def EvtBalDtls(self):
		return self._EvtBalDtls

	@EvtBalDtls.setter
	def EvtBalDtls(self, value):
		self._EvtBalDtls = value if type(value) != auto else self.make_default("EvtBalDtls")

	@EvtBalDtls.deleter
	def EvtBalDtls(self):
		del self._EvtBalDtls
		self._EvtBalDtls = None

	@property
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if type(value) != auto else self.make_default("LtryTp")

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = None

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if type(value) != auto else self.make_default("ChngTp")

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = None

	@property
	def OcrncTp(self):
		return self._OcrncTp

	@OcrncTp.setter
	def OcrncTp(self, value):
		self._OcrncTp = value if type(value) != auto else self.make_default("OcrncTp")

	@OcrncTp.deleter
	def OcrncTp(self):
		del self._OcrncTp
		self._OcrncTp = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def IntrstAcrdNbOfDays(self):
		return self._IntrstAcrdNbOfDays

	@IntrstAcrdNbOfDays.setter
	def IntrstAcrdNbOfDays(self, value):
		self._IntrstAcrdNbOfDays = value if type(value) != auto else self.make_default("IntrstAcrdNbOfDays")

	@IntrstAcrdNbOfDays.deleter
	def IntrstAcrdNbOfDays(self):
		del self._IntrstAcrdNbOfDays
		self._IntrstAcrdNbOfDays = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

	@property
	def PrratnRtrMinQtyTrtmnt(self):
		return self._PrratnRtrMinQtyTrtmnt

	@PrratnRtrMinQtyTrtmnt.setter
	def PrratnRtrMinQtyTrtmnt(self, value):
		self._PrratnRtrMinQtyTrtmnt = value if type(value) != auto else self.make_default("PrratnRtrMinQtyTrtmnt")

	@PrratnRtrMinQtyTrtmnt.deleter
	def PrratnRtrMinQtyTrtmnt(self):
		del self._PrratnRtrMinQtyTrtmnt
		self._PrratnRtrMinQtyTrtmnt = None

	@property
	def CertDtls(self):
		return self._CertDtls

	@CertDtls.setter
	def CertDtls(self, value):
		self._CertDtls = value if type(value) != auto else self.make_default("CertDtls")

	@CertDtls.deleter
	def CertDtls(self):
		del self._CertDtls
		self._CertDtls = None

	@property
	def CptlGnInOutInd(self):
		return self._CptlGnInOutInd

	@CptlGnInOutInd.setter
	def CptlGnInOutInd(self, value):
		self._CptlGnInOutInd = value if type(value) != auto else self.make_default("CptlGnInOutInd")

	@CptlGnInOutInd.deleter
	def CptlGnInOutInd(self):
		del self._CptlGnInOutInd
		self._CptlGnInOutInd = None

	@property
	def TaxOnNonDstrbtdPrcdsInd(self):
		return self._TaxOnNonDstrbtdPrcdsInd

	@TaxOnNonDstrbtdPrcdsInd.setter
	def TaxOnNonDstrbtdPrcdsInd(self, value):
		self._TaxOnNonDstrbtdPrcdsInd = value if type(value) != auto else self.make_default("TaxOnNonDstrbtdPrcdsInd")

	@TaxOnNonDstrbtdPrcdsInd.deleter
	def TaxOnNonDstrbtdPrcdsInd(self):
		del self._TaxOnNonDstrbtdPrcdsInd
		self._TaxOnNonDstrbtdPrcdsInd = None

	@property
	def AddtlBizPrcInd(self):
		return self._AddtlBizPrcInd

	@AddtlBizPrcInd.setter
	def AddtlBizPrcInd(self, value):
		self._AddtlBizPrcInd = value if type(value) != auto else self.make_default("AddtlBizPrcInd")

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = None

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if type(value) != auto else self.make_default("RnncblEntitlmntStsTp")

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = None

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def DvddTp(self):
		return self._DvddTp

	@DvddTp.setter
	def DvddTp(self, value):
		self._DvddTp = value if type(value) != auto else self.make_default("DvddTp")

	@DvddTp.deleter
	def DvddTp(self):
		del self._DvddTp
		self._DvddTp = None

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if type(value) != auto else self.make_default("TaxblIncmPerShrClctd")

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = None

	@property
	def CnsntTp(self):
		return self._CnsntTp

	@CnsntTp.setter
	def CnsntTp(self, value):
		self._CnsntTp = value if type(value) != auto else self.make_default("CnsntTp")

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if type(value) != auto else self.make_default("InfTp")

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = None

	@property
	def RstrctnInd(self):
		return self._RstrctnInd

	@RstrctnInd.setter
	def RstrctnInd(self, value):
		self._RstrctnInd = value if type(value) != auto else self.make_default("RstrctnInd")

	@RstrctnInd.deleter
	def RstrctnInd(self):
		del self._RstrctnInd
		self._RstrctnInd = None

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if type(value) != auto else self.make_default("EvtStag")

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = None

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if type(value) != auto else self.make_default("OfferTp")

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = None

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if type(value) != auto else self.make_default("IntrmdtSctiesDstrbtnTp")

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = None

	@property
	def DtchAuctnTp(self):
		return self._DtchAuctnTp

	@DtchAuctnTp.setter
	def DtchAuctnTp(self, value):
		self._DtchAuctnTp = value if type(value) != auto else self.make_default("DtchAuctnTp")

	@DtchAuctnTp.deleter
	def DtchAuctnTp(self):
		del self._DtchAuctnTp
		self._DtchAuctnTp = None

	@property
	def AcrdIntrstInd(self):
		return self._AcrdIntrstInd

	@AcrdIntrstInd.setter
	def AcrdIntrstInd(self, value):
		self._AcrdIntrstInd = value if type(value) != auto else self.make_default("AcrdIntrstInd")

	@AcrdIntrstInd.deleter
	def AcrdIntrstInd(self):
		del self._AcrdIntrstInd
		self._AcrdIntrstInd = None

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if type(value) != auto else self.make_default("PrdDtls")

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = None

	@property
	def ChrgsApldInd(self):
		return self._ChrgsApldInd

	@ChrgsApldInd.setter
	def ChrgsApldInd(self, value):
		self._ChrgsApldInd = value if type(value) != auto else self.make_default("ChrgsApldInd")

	@ChrgsApldInd.deleter
	def ChrgsApldInd(self):
		del self._ChrgsApldInd
		self._ChrgsApldInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtceTp', type=RedemptionAnnouncementNoticeType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryIndctrs', type=CorporateActionSupplementaryIndicators1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts70, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftrOfIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtBalDtls', type=CorporateActionBalanceDetails47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OcrncTp', type=DistributionTypeFormat7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice85, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=CertificationTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnRtrMinQtyTrtmnt', type=ProrationReturnQuantityTreatment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertDtls', type=CorporateActionSD26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CptlGnInOutInd', type=CapitalGainFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnNonDstrbtdPrcdsInd', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat17Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddTp', type=DividendTypeFormat9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculatedFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=ConsentTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfTp', type=InformationTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat13Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat14Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecuritiesDistributionTypeFormat15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchAuctnTp', type=DutchAuctionTypeFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

