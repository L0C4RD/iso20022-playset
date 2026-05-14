from . import base_types
from ._AdditionalBusinessProcessFormat17Choice import AdditionalBusinessProcessFormat17Choice
from ._CapitalGainFormat3Choice import CapitalGainFormat3Choice
from ._CertificationTypeFormat3Choice import CertificationTypeFormat3Choice
from ._ConsentTypeFormat4Choice import ConsentTypeFormat4Choice
from ._CorporateActionChangeTypeFormat5Choice import CorporateActionChangeTypeFormat5Choice
from ._CorporateActionDate83 import CorporateActionDate83
from ._CorporateActionEventStageFormat13Choice import CorporateActionEventStageFormat13Choice
from ._CorporateActionNarrative58 import CorporateActionNarrative58
from ._CorporateActionPeriod17 import CorporateActionPeriod17
from ._CorporateActionPrice85 import CorporateActionPrice85
from ._CorporateActionQuantity15 import CorporateActionQuantity15
from ._CorporateActionRate122 import CorporateActionRate122
from ._DistributionTypeFormat7Choice import DistributionTypeFormat7Choice
from ._DividendTypeFormat9Choice import DividendTypeFormat9Choice
from ._DutchAuctionTypeFormat1Choice import DutchAuctionTypeFormat1Choice
from ._ElectionTypeFormat3Choice import ElectionTypeFormat3Choice
from ._EventSequenceTypeFormat1Choice import EventSequenceTypeFormat1Choice
from ._Exact3UpperCaseAlphaNumericText import Exact3UpperCaseAlphaNumericText
from ._GenericIdentification30 import GenericIdentification30
from ._IdentificationFormat3Choice import IdentificationFormat3Choice
from ._InformationTypeFormat4Choice import InformationTypeFormat4Choice
from ._IntermediateSecuritiesDistributionTypeFormat19Choice import IntermediateSecuritiesDistributionTypeFormat19Choice
from ._LotteryTypeFormat4Choice import LotteryTypeFormat4Choice
from ._Max350Text import Max350Text
from ._Max3Number import Max3Number
from ._OfferTypeFormat18Choice import OfferTypeFormat18Choice
from ._RenounceableEntitlementStatusTypeFormat3Choice import RenounceableEntitlementStatusTypeFormat3Choice
from ._TaxableIncomePerShareCalculatedFormat3Choice import TaxableIncomePerShareCalculatedFormat3Choice
from ._YesNoIndicator import YesNoIndicator

class CorporateAction94(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AcrdIntrstInd", "_AddtlBizPrcInd", "_AddtlInf", "_CertfctnBrkdwnInd", "_CertfctnTp", "_ChngTp", "_ChrgsApldInd", "_CnsntTp", "_CpnNb", "_CptlGnInOutInd", "_DtDtls", "_DtchAuctnTp", "_DvddTp", "_ElctnTp", "_EvtSeqTp", "_EvtStag", "_FllwngEvtTpInd", "_FrftrOfIntrstInd", "_InfTp", "_IntrstAcrdNbOfDays", "_LtryTp", "_LttrOfGrntedDlvryInd", "_NewPlcOfIncorprtn", "_OcrncTp", "_OfferTp", "_PrdDtls", "_PricDtls", "_RateAndAmtDtls", "_RnncblEntitlmntStsTp", "_RstrctnInd", "_RvsDtchAuctnInd", "_SctiesQty", "_ShrhldrRghtsDrctvInd", "_TaxOnNonDstrbtdPrcdsInd", "_TaxblIncmPerShrClctd"]
	@property
	def AccptncPrtyLvl(self):
		return self._AccptncPrtyLvl

	@AccptncPrtyLvl.setter
	def AccptncPrtyLvl(self, value):
		self._AccptncPrtyLvl = value if type(value) != base_types.auto else self.make_default("AccptncPrtyLvl")

	@AccptncPrtyLvl.deleter
	def AccptncPrtyLvl(self):
		del self._AccptncPrtyLvl
		self._AccptncPrtyLvl = None

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
	def AddtlBizPrcInd(self):
		return self._AddtlBizPrcInd

	@AddtlBizPrcInd.setter
	def AddtlBizPrcInd(self, value):
		self._AddtlBizPrcInd = value if type(value) != base_types.auto else self.make_default("AddtlBizPrcInd")

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CertfctnBrkdwnInd(self):
		return self._CertfctnBrkdwnInd

	@CertfctnBrkdwnInd.setter
	def CertfctnBrkdwnInd(self, value):
		self._CertfctnBrkdwnInd = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwnInd")

	@CertfctnBrkdwnInd.deleter
	def CertfctnBrkdwnInd(self):
		del self._CertfctnBrkdwnInd
		self._CertfctnBrkdwnInd = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != base_types.auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if type(value) != base_types.auto else self.make_default("ChngTp")

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = None

	@property
	def ChrgsApldInd(self):
		return self._ChrgsApldInd

	@ChrgsApldInd.setter
	def ChrgsApldInd(self, value):
		self._ChrgsApldInd = value if type(value) != base_types.auto else self.make_default("ChrgsApldInd")

	@ChrgsApldInd.deleter
	def ChrgsApldInd(self):
		del self._ChrgsApldInd
		self._ChrgsApldInd = None

	@property
	def CnsntTp(self):
		return self._CnsntTp

	@CnsntTp.setter
	def CnsntTp(self, value):
		self._CnsntTp = value if type(value) != base_types.auto else self.make_default("CnsntTp")

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = None

	@property
	def CpnNb(self):
		return self._CpnNb

	@CpnNb.setter
	def CpnNb(self, value):
		self._CpnNb = value if type(value) != base_types.auto else self.make_default("CpnNb")

	@CpnNb.deleter
	def CpnNb(self):
		del self._CpnNb
		self._CpnNb = None

	@property
	def CptlGnInOutInd(self):
		return self._CptlGnInOutInd

	@CptlGnInOutInd.setter
	def CptlGnInOutInd(self, value):
		self._CptlGnInOutInd = value if type(value) != base_types.auto else self.make_default("CptlGnInOutInd")

	@CptlGnInOutInd.deleter
	def CptlGnInOutInd(self):
		del self._CptlGnInOutInd
		self._CptlGnInOutInd = None

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
	def DtchAuctnTp(self):
		return self._DtchAuctnTp

	@DtchAuctnTp.setter
	def DtchAuctnTp(self, value):
		self._DtchAuctnTp = value if type(value) != base_types.auto else self.make_default("DtchAuctnTp")

	@DtchAuctnTp.deleter
	def DtchAuctnTp(self):
		del self._DtchAuctnTp
		self._DtchAuctnTp = None

	@property
	def DvddTp(self):
		return self._DvddTp

	@DvddTp.setter
	def DvddTp(self, value):
		self._DvddTp = value if type(value) != base_types.auto else self.make_default("DvddTp")

	@DvddTp.deleter
	def DvddTp(self):
		del self._DvddTp
		self._DvddTp = None

	@property
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if type(value) != base_types.auto else self.make_default("ElctnTp")

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = None

	@property
	def EvtSeqTp(self):
		return self._EvtSeqTp

	@EvtSeqTp.setter
	def EvtSeqTp(self, value):
		self._EvtSeqTp = value if type(value) != base_types.auto else self.make_default("EvtSeqTp")

	@EvtSeqTp.deleter
	def EvtSeqTp(self):
		del self._EvtSeqTp
		self._EvtSeqTp = None

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if type(value) != base_types.auto else self.make_default("EvtStag")

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = None

	@property
	def FllwngEvtTpInd(self):
		return self._FllwngEvtTpInd

	@FllwngEvtTpInd.setter
	def FllwngEvtTpInd(self, value):
		self._FllwngEvtTpInd = value if type(value) != base_types.auto else self.make_default("FllwngEvtTpInd")

	@FllwngEvtTpInd.deleter
	def FllwngEvtTpInd(self):
		del self._FllwngEvtTpInd
		self._FllwngEvtTpInd = None

	@property
	def FrftrOfIntrstInd(self):
		return self._FrftrOfIntrstInd

	@FrftrOfIntrstInd.setter
	def FrftrOfIntrstInd(self, value):
		self._FrftrOfIntrstInd = value if type(value) != base_types.auto else self.make_default("FrftrOfIntrstInd")

	@FrftrOfIntrstInd.deleter
	def FrftrOfIntrstInd(self):
		del self._FrftrOfIntrstInd
		self._FrftrOfIntrstInd = None

	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if type(value) != base_types.auto else self.make_default("InfTp")

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = None

	@property
	def IntrstAcrdNbOfDays(self):
		return self._IntrstAcrdNbOfDays

	@IntrstAcrdNbOfDays.setter
	def IntrstAcrdNbOfDays(self, value):
		self._IntrstAcrdNbOfDays = value if type(value) != base_types.auto else self.make_default("IntrstAcrdNbOfDays")

	@IntrstAcrdNbOfDays.deleter
	def IntrstAcrdNbOfDays(self):
		del self._IntrstAcrdNbOfDays
		self._IntrstAcrdNbOfDays = None

	@property
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if type(value) != base_types.auto else self.make_default("LtryTp")

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = None

	@property
	def LttrOfGrntedDlvryInd(self):
		return self._LttrOfGrntedDlvryInd

	@LttrOfGrntedDlvryInd.setter
	def LttrOfGrntedDlvryInd(self, value):
		self._LttrOfGrntedDlvryInd = value if type(value) != base_types.auto else self.make_default("LttrOfGrntedDlvryInd")

	@LttrOfGrntedDlvryInd.deleter
	def LttrOfGrntedDlvryInd(self):
		del self._LttrOfGrntedDlvryInd
		self._LttrOfGrntedDlvryInd = None

	@property
	def NewPlcOfIncorprtn(self):
		return self._NewPlcOfIncorprtn

	@NewPlcOfIncorprtn.setter
	def NewPlcOfIncorprtn(self, value):
		self._NewPlcOfIncorprtn = value if type(value) != base_types.auto else self.make_default("NewPlcOfIncorprtn")

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = None

	@property
	def OcrncTp(self):
		return self._OcrncTp

	@OcrncTp.setter
	def OcrncTp(self, value):
		self._OcrncTp = value if type(value) != base_types.auto else self.make_default("OcrncTp")

	@OcrncTp.deleter
	def OcrncTp(self):
		del self._OcrncTp
		self._OcrncTp = None

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if type(value) != base_types.auto else self.make_default("OfferTp")

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = None

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if type(value) != base_types.auto else self.make_default("PrdDtls")

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = None

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
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if type(value) != base_types.auto else self.make_default("RnncblEntitlmntStsTp")

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = None

	@property
	def RstrctnInd(self):
		return self._RstrctnInd

	@RstrctnInd.setter
	def RstrctnInd(self, value):
		self._RstrctnInd = value if type(value) != base_types.auto else self.make_default("RstrctnInd")

	@RstrctnInd.deleter
	def RstrctnInd(self):
		del self._RstrctnInd
		self._RstrctnInd = None

	@property
	def RvsDtchAuctnInd(self):
		return self._RvsDtchAuctnInd

	@RvsDtchAuctnInd.setter
	def RvsDtchAuctnInd(self, value):
		self._RvsDtchAuctnInd = value if type(value) != base_types.auto else self.make_default("RvsDtchAuctnInd")

	@RvsDtchAuctnInd.deleter
	def RvsDtchAuctnInd(self):
		del self._RvsDtchAuctnInd
		self._RvsDtchAuctnInd = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != base_types.auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if type(value) != base_types.auto else self.make_default("ShrhldrRghtsDrctvInd")

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = None

	@property
	def TaxOnNonDstrbtdPrcdsInd(self):
		return self._TaxOnNonDstrbtdPrcdsInd

	@TaxOnNonDstrbtdPrcdsInd.setter
	def TaxOnNonDstrbtdPrcdsInd(self, value):
		self._TaxOnNonDstrbtdPrcdsInd = value if type(value) != base_types.auto else self.make_default("TaxOnNonDstrbtdPrcdsInd")

	@TaxOnNonDstrbtdPrcdsInd.deleter
	def TaxOnNonDstrbtdPrcdsInd(self):
		del self._TaxOnNonDstrbtdPrcdsInd
		self._TaxOnNonDstrbtdPrcdsInd = None

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShrClctd")

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat17Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=CertificationTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=ConsentTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnNb', type=IdentificationFormat3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CptlGnInOutInd', type=CapitalGainFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchAuctnTp', type=DutchAuctionTypeFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddTp', type=DividendTypeFormat9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnTp', type=ElectionTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtSeqTp', type=EventSequenceTypeFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat13Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FllwngEvtTpInd', type=IntermediateSecuritiesDistributionTypeFormat19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftrOfIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfTp', type=InformationTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfGrntedDlvryInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OcrncTp', type=DistributionTypeFormat7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice85, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsDtchAuctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnNonDstrbtdPrcdsInd', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculatedFormat3Choice, min=0, max=1, mutex_group=None, array=False),
	))

