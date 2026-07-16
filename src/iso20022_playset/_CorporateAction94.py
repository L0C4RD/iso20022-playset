# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBusinessProcessFormat17Choice
from . import CapitalGainFormat3Choice
from . import CertificationTypeFormat3Choice
from . import ConsentTypeFormat4Choice
from . import CorporateActionChangeTypeFormat5Choice
from . import CorporateActionDate83
from . import CorporateActionEventStageFormat13Choice
from . import CorporateActionNarrative58
from . import CorporateActionPeriod17
from . import CorporateActionPrice85
from . import CorporateActionQuantity15
from . import CorporateActionRate122
from . import DistributionTypeFormat7Choice
from . import DividendTypeFormat9Choice
from . import DutchAuctionTypeFormat1Choice
from . import ElectionTypeFormat3Choice
from . import EventSequenceTypeFormat1Choice
from . import Exact3UpperCaseAlphaNumericText
from . import GenericIdentification30
from . import IdentificationFormat3Choice
from . import InformationTypeFormat4Choice
from . import IntermediateSecuritiesDistributionTypeFormat19Choice
from . import LotteryTypeFormat4Choice
from . import Max350Text
from . import Max3Number
from . import OfferTypeFormat18Choice
from . import RenounceableEntitlementStatusTypeFormat3Choice
from . import TaxableIncomePerShareCalculatedFormat3Choice
from . import YesNoIndicator

class CorporateAction94(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AcrdIntrstInd", "_AddtlBizPrcInd", "_AddtlInf", "_CertfctnBrkdwnInd", "_CertfctnTp", "_ChngTp", "_ChrgsApldInd", "_CnsntTp", "_CpnNb", "_CptlGnInOutInd", "_DtDtls", "_DtchAuctnTp", "_DvddTp", "_ElctnTp", "_EvtSeqTp", "_EvtStag", "_FllwngEvtTpInd", "_FrftrOfIntrstInd", "_InfTp", "_IntrstAcrdNbOfDays", "_LtryTp", "_LttrOfGrntedDlvryInd", "_NewPlcOfIncorprtn", "_OcrncTp", "_OfferTp", "_PrdDtls", "_PricDtls", "_RateAndAmtDtls", "_RnncblEntitlmntStsTp", "_RstrctnInd", "_RvsDtchAuctnInd", "_SctiesQty", "_ShrhldrRghtsDrctvInd", "_TaxOnNonDstrbtdPrcdsInd", "_TaxblIncmPerShrClctd"]
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
		self._AddtlBizPrcInd = value if value is not None else base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat17Choice, True)

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat17Choice, True)

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
	def CpnNb(self):
		return self._CpnNb

	@CpnNb.setter
	def CpnNb(self, value):
		self._CpnNb = value if value is not None else base_types.UninitialisedField(self, 'CpnNb', IdentificationFormat3Choice, True)

	@CpnNb.deleter
	def CpnNb(self):
		del self._CpnNb
		self._CpnNb = base_types.UninitialisedField(self, 'CpnNb', IdentificationFormat3Choice, True)

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
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if value is not None else base_types.UninitialisedField(self, 'ElctnTp', ElectionTypeFormat3Choice, False)

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = base_types.UninitialisedField(self, 'ElctnTp', ElectionTypeFormat3Choice, False)

	@property
	def EvtSeqTp(self):
		return self._EvtSeqTp

	@EvtSeqTp.setter
	def EvtSeqTp(self, value):
		self._EvtSeqTp = value if value is not None else base_types.UninitialisedField(self, 'EvtSeqTp', EventSequenceTypeFormat1Choice, False)

	@EvtSeqTp.deleter
	def EvtSeqTp(self):
		del self._EvtSeqTp
		self._EvtSeqTp = base_types.UninitialisedField(self, 'EvtSeqTp', EventSequenceTypeFormat1Choice, False)

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
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if value is not None else base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat4Choice, False)

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat4Choice, False)

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
		self._NewPlcOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max350Text, False)

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max350Text, False)

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