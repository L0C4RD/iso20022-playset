# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBusinessProcessFormat22Choice
from . import CapitalGainFormat4Choice
from . import CertificationTypeFormat4Choice
from . import ConsentTypeFormat5Choice
from . import CorporateActionChangeTypeFormat8Choice
from . import CorporateActionDate96
from . import CorporateActionEventStageFormat20Choice
from . import CorporateActionNarrative63
from . import CorporateActionPeriod16
from . import CorporateActionPrice96
from . import CorporateActionQuantity14
from . import CorporateActionRate135
from . import DistributionTypeFormat8Choice
from . import DividendTypeFormat10Choice
from . import DutchAuctionTypeFormat2Choice
from . import ElectionTypeFormat4Choice
from . import EventSequenceTypeFormat2Choice
from . import Exact3UpperCaseAlphaNumericText
from . import GenericIdentification47
from . import IdentificationFormat4Choice
from . import InformationTypeFormat5Choice
from . import IntermediateSecuritiesDistributionTypeFormat18Choice
from . import LotteryTypeFormat5Choice
from . import Max3Number
from . import OfferTypeFormat16Choice
from . import RenounceableEntitlementStatusTypeFormat4Choice
from . import RestrictedFINXMax350Text
from . import TaxableIncomePerShareCalculatedFormat4Choice
from . import YesNoIndicator

class CorporateAction87(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AcrdIntrstInd", "_AddtlBizPrcInd", "_AddtlInf", "_CertfctnBrkdwnInd", "_CertfctnTp", "_ChngTp", "_ChrgsApldInd", "_CnsntTp", "_CpnNb", "_CptlGnInOutInd", "_DtDtls", "_DtchAuctnTp", "_DvddTp", "_ElctnTp", "_EvtSeqTp", "_EvtStag", "_FrftrOfIntrstInd", "_InfTp", "_IntrmdtSctiesDstrbtnTp", "_IntrstAcrdNbOfDays", "_LtryTp", "_LttrOfGrntedDlvryInd", "_NewPlcOfIncorprtn", "_OcrncTp", "_OfferTp", "_PrdDtls", "_PricDtls", "_RateAndAmtDtls", "_RnncblEntitlmntStsTp", "_RstrctnInd", "_SctiesQty", "_ShrhldrRghtsDrctvInd", "_TaxOnNonDstrbtdPrcdsInd", "_TaxblIncmPerShrClctd"]
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
		self._AddtlBizPrcInd = value if value is not None else base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat22Choice, True)

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat22Choice, True)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative63, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative63, False)

	@property
	def CertfctnBrkdwnInd(self):
		return self._CertfctnBrkdwnInd

	@CertfctnBrkdwnInd.setter
	def CertfctnBrkdwnInd(self, value):
		self._CertfctnBrkdwnInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwnInd', YesNoIndicator, False)

	@CertfctnBrkdwnInd.deleter
	def CertfctnBrkdwnInd(self):
		del self._CertfctnBrkdwnInd
		self._CertfctnBrkdwnInd = base_types.UninitialisedField(self, 'CertfctnBrkdwnInd', YesNoIndicator, False)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', CertificationTypeFormat4Choice, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', CertificationTypeFormat4Choice, False)

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if value is not None else base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat8Choice, True)

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat8Choice, True)

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
		self._CnsntTp = value if value is not None else base_types.UninitialisedField(self, 'CnsntTp', ConsentTypeFormat5Choice, False)

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = base_types.UninitialisedField(self, 'CnsntTp', ConsentTypeFormat5Choice, False)

	@property
	def CpnNb(self):
		return self._CpnNb

	@CpnNb.setter
	def CpnNb(self, value):
		self._CpnNb = value if value is not None else base_types.UninitialisedField(self, 'CpnNb', IdentificationFormat4Choice, True)

	@CpnNb.deleter
	def CpnNb(self):
		del self._CpnNb
		self._CpnNb = base_types.UninitialisedField(self, 'CpnNb', IdentificationFormat4Choice, True)

	@property
	def CptlGnInOutInd(self):
		return self._CptlGnInOutInd

	@CptlGnInOutInd.setter
	def CptlGnInOutInd(self, value):
		self._CptlGnInOutInd = value if value is not None else base_types.UninitialisedField(self, 'CptlGnInOutInd', CapitalGainFormat4Choice, False)

	@CptlGnInOutInd.deleter
	def CptlGnInOutInd(self):
		del self._CptlGnInOutInd
		self._CptlGnInOutInd = base_types.UninitialisedField(self, 'CptlGnInOutInd', CapitalGainFormat4Choice, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate96, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate96, False)

	@property
	def DtchAuctnTp(self):
		return self._DtchAuctnTp

	@DtchAuctnTp.setter
	def DtchAuctnTp(self, value):
		self._DtchAuctnTp = value if value is not None else base_types.UninitialisedField(self, 'DtchAuctnTp', DutchAuctionTypeFormat2Choice, False)

	@DtchAuctnTp.deleter
	def DtchAuctnTp(self):
		del self._DtchAuctnTp
		self._DtchAuctnTp = base_types.UninitialisedField(self, 'DtchAuctnTp', DutchAuctionTypeFormat2Choice, False)

	@property
	def DvddTp(self):
		return self._DvddTp

	@DvddTp.setter
	def DvddTp(self, value):
		self._DvddTp = value if value is not None else base_types.UninitialisedField(self, 'DvddTp', DividendTypeFormat10Choice, False)

	@DvddTp.deleter
	def DvddTp(self):
		del self._DvddTp
		self._DvddTp = base_types.UninitialisedField(self, 'DvddTp', DividendTypeFormat10Choice, False)

	@property
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if value is not None else base_types.UninitialisedField(self, 'ElctnTp', ElectionTypeFormat4Choice, False)

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = base_types.UninitialisedField(self, 'ElctnTp', ElectionTypeFormat4Choice, False)

	@property
	def EvtSeqTp(self):
		return self._EvtSeqTp

	@EvtSeqTp.setter
	def EvtSeqTp(self, value):
		self._EvtSeqTp = value if value is not None else base_types.UninitialisedField(self, 'EvtSeqTp', EventSequenceTypeFormat2Choice, False)

	@EvtSeqTp.deleter
	def EvtSeqTp(self):
		del self._EvtSeqTp
		self._EvtSeqTp = base_types.UninitialisedField(self, 'EvtSeqTp', EventSequenceTypeFormat2Choice, False)

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if value is not None else base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat20Choice, True)

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat20Choice, True)

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
		self._InfTp = value if value is not None else base_types.UninitialisedField(self, 'InfTp', InformationTypeFormat5Choice, False)

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = base_types.UninitialisedField(self, 'InfTp', InformationTypeFormat5Choice, False)

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if value is not None else base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecuritiesDistributionTypeFormat18Choice, False)

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecuritiesDistributionTypeFormat18Choice, False)

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
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if value is not None else base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat5Choice, False)

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat5Choice, False)

	@property
	def LttrOfGrntedDlvryInd(self):
		return self._LttrOfGrntedDlvryInd

	@LttrOfGrntedDlvryInd.setter
	def LttrOfGrntedDlvryInd(self, value):
		self._LttrOfGrntedDlvryInd = value if value is not None else base_types.UninitialisedField(self, 'LttrOfGrntedDlvryInd', YesNoIndicator, False)

	@LttrOfGrntedDlvryInd.deleter
	def LttrOfGrntedDlvryInd(self):
		del self._LttrOfGrntedDlvryInd
		self._LttrOfGrntedDlvryInd = base_types.UninitialisedField(self, 'LttrOfGrntedDlvryInd', YesNoIndicator, False)

	@property
	def NewPlcOfIncorprtn(self):
		return self._NewPlcOfIncorprtn

	@NewPlcOfIncorprtn.setter
	def NewPlcOfIncorprtn(self, value):
		self._NewPlcOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', RestrictedFINXMax350Text, False)

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', RestrictedFINXMax350Text, False)

	@property
	def OcrncTp(self):
		return self._OcrncTp

	@OcrncTp.setter
	def OcrncTp(self, value):
		self._OcrncTp = value if value is not None else base_types.UninitialisedField(self, 'OcrncTp', DistributionTypeFormat8Choice, False)

	@OcrncTp.deleter
	def OcrncTp(self):
		del self._OcrncTp
		self._OcrncTp = base_types.UninitialisedField(self, 'OcrncTp', DistributionTypeFormat8Choice, False)

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if value is not None else base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat16Choice, True)

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat16Choice, True)

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod16, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod16, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice96, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice96, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate135, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate135, False)

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if value is not None else base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat4Choice, False)

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat4Choice, False)

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
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity14, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity14, False)

	@property
	def ShrhldrRghtsDrctvInd(self):
		return self._ShrhldrRghtsDrctvInd

	@ShrhldrRghtsDrctvInd.setter
	def ShrhldrRghtsDrctvInd(self, value):
		self._ShrhldrRghtsDrctvInd = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	@ShrhldrRghtsDrctvInd.deleter
	def ShrhldrRghtsDrctvInd(self):
		del self._ShrhldrRghtsDrctvInd
		self._ShrhldrRghtsDrctvInd = base_types.UninitialisedField(self, 'ShrhldrRghtsDrctvInd', YesNoIndicator, False)

	@property
	def TaxOnNonDstrbtdPrcdsInd(self):
		return self._TaxOnNonDstrbtdPrcdsInd

	@TaxOnNonDstrbtdPrcdsInd.setter
	def TaxOnNonDstrbtdPrcdsInd(self, value):
		self._TaxOnNonDstrbtdPrcdsInd = value if value is not None else base_types.UninitialisedField(self, 'TaxOnNonDstrbtdPrcdsInd', GenericIdentification47, True)

	@TaxOnNonDstrbtdPrcdsInd.deleter
	def TaxOnNonDstrbtdPrcdsInd(self):
		del self._TaxOnNonDstrbtdPrcdsInd
		self._TaxOnNonDstrbtdPrcdsInd = base_types.UninitialisedField(self, 'TaxOnNonDstrbtdPrcdsInd', GenericIdentification47, True)

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculatedFormat4Choice, False)

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculatedFormat4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat22Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative63, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=CertificationTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat8Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=ConsentTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnNb', type=IdentificationFormat4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CptlGnInOutInd', type=CapitalGainFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchAuctnTp', type=DutchAuctionTypeFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddTp', type=DividendTypeFormat10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnTp', type=ElectionTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtSeqTp', type=EventSequenceTypeFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat20Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrftrOfIntrstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfTp', type=InformationTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecuritiesDistributionTypeFormat18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfGrntedDlvryInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OcrncTp', type=DistributionTypeFormat8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate135, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrRghtsDrctvInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnNonDstrbtdPrcdsInd', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculatedFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))