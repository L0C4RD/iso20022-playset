from . import base_types
from .AdditionalBusinessProcessFormat22Choice import AdditionalBusinessProcessFormat22Choice
from .EventSequenceTypeFormat2Choice import EventSequenceTypeFormat2Choice
from .CorporateActionQuantity14 import CorporateActionQuantity14
from .LotteryTypeFormat5Choice import LotteryTypeFormat5Choice
from .DutchAuctionTypeFormat2Choice import DutchAuctionTypeFormat2Choice
from .CorporateActionPrice96 import CorporateActionPrice96
from .CorporateActionEventStageFormat20Choice import CorporateActionEventStageFormat20Choice
from .CorporateActionDate96 import CorporateActionDate96
from .CorporateActionNarrative63 import CorporateActionNarrative63
from .OfferTypeFormat16Choice import OfferTypeFormat16Choice
from .Max3Number import Max3Number
from .Exact3UpperCaseAlphaNumericText import Exact3UpperCaseAlphaNumericText
from .YesNoIndicator import YesNoIndicator
from .ElectionTypeFormat4Choice import ElectionTypeFormat4Choice
from .CertificationTypeFormat4Choice import CertificationTypeFormat4Choice
from .ConsentTypeFormat5Choice import ConsentTypeFormat5Choice
from .RenounceableEntitlementStatusTypeFormat4Choice import RenounceableEntitlementStatusTypeFormat4Choice
from .IdentificationFormat4Choice import IdentificationFormat4Choice
from .CorporateActionRate135 import CorporateActionRate135
from .CorporateActionPeriod16 import CorporateActionPeriod16
from .DividendTypeFormat10Choice import DividendTypeFormat10Choice
from .CorporateActionChangeTypeFormat8Choice import CorporateActionChangeTypeFormat8Choice
from .CapitalGainFormat4Choice import CapitalGainFormat4Choice
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text
from .TaxableIncomePerShareCalculatedFormat4Choice import TaxableIncomePerShareCalculatedFormat4Choice
from .InformationTypeFormat5Choice import InformationTypeFormat5Choice
from .DistributionTypeFormat8Choice import DistributionTypeFormat8Choice
from .GenericIdentification47 import GenericIdentification47
from .IntermediateSecuritiesDistributionTypeFormat18Choice import IntermediateSecuritiesDistributionTypeFormat18Choice

class CorporateAction87(base_types._BaseFieldType):

	__slots__ = ["_DtchAuctnTp", "_AddtlBizPrcInd", "_NewPlcOfIncorprtn", "_AccptncPrtyLvl", "_ChngTp", "_CpnNb", "_ElctnTp", "_AddtlInf", "_LtryTp", "_EvtStag", "_ChrgsApldInd", "_PrdDtls", "_CnsntTp", "_DtDtls", "_OcrncTp", "_CertfctnTp", "_OfferTp", "_DvddTp", "_TaxblIncmPerShrClctd", "_IntrmdtSctiesDstrbtnTp", "_InfTp", "_FrftrOfIntrstInd", "_CertfctnBrkdwnInd", "_ShrhldrRghtsDrctvInd", "_CptlGnInOutInd", "_RateAndAmtDtls", "_EvtSeqTp", "_LttrOfGrntedDlvryInd", "_PricDtls", "_RstrctnInd", "_TaxOnNonDstrbtdPrcdsInd", "_RnncblEntitlmntStsTp", "_SctiesQty", "_AcrdIntrstInd", "_IntrstAcrdNbOfDays"]
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
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShrClctd")

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = None

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if type(value) != base_types.auto else self.make_default("IntrmdtSctiesDstrbtnTp")

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = None

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
	def IntrstAcrdNbOfDays(self):
		return self._IntrstAcrdNbOfDays

	@IntrstAcrdNbOfDays.setter
	def IntrstAcrdNbOfDays(self, value):
		self._IntrstAcrdNbOfDays = value if type(value) != base_types.auto else self.make_default("IntrstAcrdNbOfDays")

	@IntrstAcrdNbOfDays.deleter
	def IntrstAcrdNbOfDays(self):
		del self._IntrstAcrdNbOfDays
		self._IntrstAcrdNbOfDays = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtchAuctnTp', type=DutchAuctionTypeFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat22Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat8Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnNb', type=IdentificationFormat4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ElctnTp', type=ElectionTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative63, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat20Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=ConsentTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OcrncTp', type=DistributionTypeFormat8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=CertificationTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvddTp', type=DividendTypeFormat10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculatedFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecuritiesDistributionTypeFormat18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfTp', type=InformationTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrftrOfIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGnInOutInd', type=CapitalGainFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtSeqTp', type=EventSequenceTypeFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfGrntedDlvryInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnNonDstrbtdPrcdsInd', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
	))

