# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BeneficiaryCertificationType1FormatChoice
from . import ConversionType1FormatChoice
from . import CorporateActionCalculationMethod1FormatChoice
from . import CorporateActionChangeType1FormatChoice
from . import CorporateActionDate2
from . import CorporateActionEventStage1FormatChoice
from . import CorporateActionFrequencyType1FormatChoice
from . import CorporateActionNarrative1
from . import CorporateActionOption1FormatChoice
from . import CorporateActionPeriod1
from . import CorporateActionPrice2
from . import CorporateActionRate1
from . import DistributionType1FormatChoice
from . import EUCapitalGain2Code
from . import ElectionMovementType1FormatChoice
from . import Exact3NumericText
from . import GenericIdentification13
from . import IntermediateSecurityDistributionType1FormatChoice
from . import LotteryType1FormatChoice
from . import Max3NumericText
from . import Max70Text
from . import Number
from . import OfferType1FormatChoice
from . import RenounceableStatus1FormatChoice
from . import TaxableIncomePerShareCalculated2Code
from . import UnitOrFaceAmount1Choice
from . import UnitOrFaceAmountOrCode1Choice
from . import YesNoIndicator

class CorporateAction2(base_types._BaseFieldType):

	__slots__ = ["_BaseDnmtn", "_BckEndOddLotSctiesQty", "_CertfctnReqrdInd", "_CertfctnTp", "_ChngTp", "_ClctnMtd", "_ConvsTp", "_CorpActnAddtlInf", "_CpnNb", "_CptlGn", "_DfltOptnNb", "_DfltOptnTp", "_DstrbtnTp", "_DtDtls", "_DvddTp", "_ElctnTp", "_EvtStag", "_FrntEndOddLotSctiesQty", "_IncmTp", "_IncrmtlDnmtn", "_IntrmdtSctiesDstrbtnTp", "_IntrstAcrdNbOfDays", "_LtryTp", "_MinExrcblMltplSctiesQty", "_MinExrcblSctiesQty", "_NewBrdLotSctiesQty", "_NewDnmtnCcy", "_NewDnmtnSctiesQty", "_NewPlcOfIncorprtn", "_OfferTp", "_PrdDtls", "_PricDtls", "_PrtlElctnInd", "_RateAndAmtDtls", "_RedChrgsApldInd", "_RnncblEntitlmntStsTp", "_RstrctnInd", "_SctiesQtySght", "_TaxblIncmPerShrClctd"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if value is not None else base_types.UninitialisedField(self, 'BaseDnmtn', UnitOrFaceAmount1Choice, False)

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = base_types.UninitialisedField(self, 'BaseDnmtn', UnitOrFaceAmount1Choice, False)

	@property
	def BckEndOddLotSctiesQty(self):
		return self._BckEndOddLotSctiesQty

	@BckEndOddLotSctiesQty.setter
	def BckEndOddLotSctiesQty(self, value):
		self._BckEndOddLotSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'BckEndOddLotSctiesQty', UnitOrFaceAmountOrCode1Choice, False)

	@BckEndOddLotSctiesQty.deleter
	def BckEndOddLotSctiesQty(self):
		del self._BckEndOddLotSctiesQty
		self._BckEndOddLotSctiesQty = base_types.UninitialisedField(self, 'BckEndOddLotSctiesQty', UnitOrFaceAmountOrCode1Choice, False)

	@property
	def CertfctnReqrdInd(self):
		return self._CertfctnReqrdInd

	@CertfctnReqrdInd.setter
	def CertfctnReqrdInd(self, value):
		self._CertfctnReqrdInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnReqrdInd', YesNoIndicator, False)

	@CertfctnReqrdInd.deleter
	def CertfctnReqrdInd(self):
		del self._CertfctnReqrdInd
		self._CertfctnReqrdInd = base_types.UninitialisedField(self, 'CertfctnReqrdInd', YesNoIndicator, False)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if value is not None else base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeType1FormatChoice, True)

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeType1FormatChoice, True)

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'ClctnMtd', CorporateActionCalculationMethod1FormatChoice, False)

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = base_types.UninitialisedField(self, 'ClctnMtd', CorporateActionCalculationMethod1FormatChoice, False)

	@property
	def ConvsTp(self):
		return self._ConvsTp

	@ConvsTp.setter
	def ConvsTp(self, value):
		self._ConvsTp = value if value is not None else base_types.UninitialisedField(self, 'ConvsTp', ConversionType1FormatChoice, False)

	@ConvsTp.deleter
	def ConvsTp(self):
		del self._ConvsTp
		self._ConvsTp = base_types.UninitialisedField(self, 'ConvsTp', ConversionType1FormatChoice, False)

	@property
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionNarrative1, False)

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionNarrative1, False)

	@property
	def CpnNb(self):
		return self._CpnNb

	@CpnNb.setter
	def CpnNb(self, value):
		self._CpnNb = value if value is not None else base_types.UninitialisedField(self, 'CpnNb', Max3NumericText, True)

	@CpnNb.deleter
	def CpnNb(self):
		del self._CpnNb
		self._CpnNb = base_types.UninitialisedField(self, 'CpnNb', Max3NumericText, True)

	@property
	def CptlGn(self):
		return self._CptlGn

	@CptlGn.setter
	def CptlGn(self, value):
		self._CptlGn = value if value is not None else base_types.UninitialisedField(self, 'CptlGn', EUCapitalGain2Code, False)

	@CptlGn.deleter
	def CptlGn(self):
		del self._CptlGn
		self._CptlGn = base_types.UninitialisedField(self, 'CptlGn', EUCapitalGain2Code, False)

	@property
	def DfltOptnNb(self):
		return self._DfltOptnNb

	@DfltOptnNb.setter
	def DfltOptnNb(self, value):
		self._DfltOptnNb = value if value is not None else base_types.UninitialisedField(self, 'DfltOptnNb', Exact3NumericText, False)

	@DfltOptnNb.deleter
	def DfltOptnNb(self):
		del self._DfltOptnNb
		self._DfltOptnNb = base_types.UninitialisedField(self, 'DfltOptnNb', Exact3NumericText, False)

	@property
	def DfltOptnTp(self):
		return self._DfltOptnTp

	@DfltOptnTp.setter
	def DfltOptnTp(self, value):
		self._DfltOptnTp = value if value is not None else base_types.UninitialisedField(self, 'DfltOptnTp', CorporateActionOption1FormatChoice, False)

	@DfltOptnTp.deleter
	def DfltOptnTp(self):
		del self._DfltOptnTp
		self._DfltOptnTp = base_types.UninitialisedField(self, 'DfltOptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def DstrbtnTp(self):
		return self._DstrbtnTp

	@DstrbtnTp.setter
	def DstrbtnTp(self, value):
		self._DstrbtnTp = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnTp', DistributionType1FormatChoice, False)

	@DstrbtnTp.deleter
	def DstrbtnTp(self):
		del self._DstrbtnTp
		self._DstrbtnTp = base_types.UninitialisedField(self, 'DstrbtnTp', DistributionType1FormatChoice, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate2, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate2, False)

	@property
	def DvddTp(self):
		return self._DvddTp

	@DvddTp.setter
	def DvddTp(self, value):
		self._DvddTp = value if value is not None else base_types.UninitialisedField(self, 'DvddTp', CorporateActionFrequencyType1FormatChoice, False)

	@DvddTp.deleter
	def DvddTp(self):
		del self._DvddTp
		self._DvddTp = base_types.UninitialisedField(self, 'DvddTp', CorporateActionFrequencyType1FormatChoice, False)

	@property
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if value is not None else base_types.UninitialisedField(self, 'ElctnTp', ElectionMovementType1FormatChoice, False)

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = base_types.UninitialisedField(self, 'ElctnTp', ElectionMovementType1FormatChoice, False)

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if value is not None else base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStage1FormatChoice, True)

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStage1FormatChoice, True)

	@property
	def FrntEndOddLotSctiesQty(self):
		return self._FrntEndOddLotSctiesQty

	@FrntEndOddLotSctiesQty.setter
	def FrntEndOddLotSctiesQty(self, value):
		self._FrntEndOddLotSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'FrntEndOddLotSctiesQty', UnitOrFaceAmountOrCode1Choice, False)

	@FrntEndOddLotSctiesQty.deleter
	def FrntEndOddLotSctiesQty(self):
		del self._FrntEndOddLotSctiesQty
		self._FrntEndOddLotSctiesQty = base_types.UninitialisedField(self, 'FrntEndOddLotSctiesQty', UnitOrFaceAmountOrCode1Choice, False)

	@property
	def IncmTp(self):
		return self._IncmTp

	@IncmTp.setter
	def IncmTp(self, value):
		self._IncmTp = value if value is not None else base_types.UninitialisedField(self, 'IncmTp', GenericIdentification13, False)

	@IncmTp.deleter
	def IncmTp(self):
		del self._IncmTp
		self._IncmTp = base_types.UninitialisedField(self, 'IncmTp', GenericIdentification13, False)

	@property
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if value is not None else base_types.UninitialisedField(self, 'IncrmtlDnmtn', UnitOrFaceAmount1Choice, False)

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = base_types.UninitialisedField(self, 'IncrmtlDnmtn', UnitOrFaceAmount1Choice, False)

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if value is not None else base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecurityDistributionType1FormatChoice, False)

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecurityDistributionType1FormatChoice, False)

	@property
	def IntrstAcrdNbOfDays(self):
		return self._IntrstAcrdNbOfDays

	@IntrstAcrdNbOfDays.setter
	def IntrstAcrdNbOfDays(self, value):
		self._IntrstAcrdNbOfDays = value if value is not None else base_types.UninitialisedField(self, 'IntrstAcrdNbOfDays', Number, False)

	@IntrstAcrdNbOfDays.deleter
	def IntrstAcrdNbOfDays(self):
		del self._IntrstAcrdNbOfDays
		self._IntrstAcrdNbOfDays = base_types.UninitialisedField(self, 'IntrstAcrdNbOfDays', Number, False)

	@property
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if value is not None else base_types.UninitialisedField(self, 'LtryTp', LotteryType1FormatChoice, False)

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = base_types.UninitialisedField(self, 'LtryTp', LotteryType1FormatChoice, False)

	@property
	def MinExrcblMltplSctiesQty(self):
		return self._MinExrcblMltplSctiesQty

	@MinExrcblMltplSctiesQty.setter
	def MinExrcblMltplSctiesQty(self, value):
		self._MinExrcblMltplSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblMltplSctiesQty', UnitOrFaceAmount1Choice, False)

	@MinExrcblMltplSctiesQty.deleter
	def MinExrcblMltplSctiesQty(self):
		del self._MinExrcblMltplSctiesQty
		self._MinExrcblMltplSctiesQty = base_types.UninitialisedField(self, 'MinExrcblMltplSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def MinExrcblSctiesQty(self):
		return self._MinExrcblSctiesQty

	@MinExrcblSctiesQty.setter
	def MinExrcblSctiesQty(self, value):
		self._MinExrcblSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblSctiesQty', UnitOrFaceAmount1Choice, False)

	@MinExrcblSctiesQty.deleter
	def MinExrcblSctiesQty(self):
		del self._MinExrcblSctiesQty
		self._MinExrcblSctiesQty = base_types.UninitialisedField(self, 'MinExrcblSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NewBrdLotSctiesQty(self):
		return self._NewBrdLotSctiesQty

	@NewBrdLotSctiesQty.setter
	def NewBrdLotSctiesQty(self, value):
		self._NewBrdLotSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'NewBrdLotSctiesQty', UnitOrFaceAmount1Choice, False)

	@NewBrdLotSctiesQty.deleter
	def NewBrdLotSctiesQty(self):
		del self._NewBrdLotSctiesQty
		self._NewBrdLotSctiesQty = base_types.UninitialisedField(self, 'NewBrdLotSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NewDnmtnCcy(self):
		return self._NewDnmtnCcy

	@NewDnmtnCcy.setter
	def NewDnmtnCcy(self, value):
		self._NewDnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'NewDnmtnCcy', ActiveCurrencyCode, False)

	@NewDnmtnCcy.deleter
	def NewDnmtnCcy(self):
		del self._NewDnmtnCcy
		self._NewDnmtnCcy = base_types.UninitialisedField(self, 'NewDnmtnCcy', ActiveCurrencyCode, False)

	@property
	def NewDnmtnSctiesQty(self):
		return self._NewDnmtnSctiesQty

	@NewDnmtnSctiesQty.setter
	def NewDnmtnSctiesQty(self, value):
		self._NewDnmtnSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'NewDnmtnSctiesQty', UnitOrFaceAmount1Choice, False)

	@NewDnmtnSctiesQty.deleter
	def NewDnmtnSctiesQty(self):
		del self._NewDnmtnSctiesQty
		self._NewDnmtnSctiesQty = base_types.UninitialisedField(self, 'NewDnmtnSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NewPlcOfIncorprtn(self):
		return self._NewPlcOfIncorprtn

	@NewPlcOfIncorprtn.setter
	def NewPlcOfIncorprtn(self, value):
		self._NewPlcOfIncorprtn = value if value is not None else base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max70Text, False)

	@NewPlcOfIncorprtn.deleter
	def NewPlcOfIncorprtn(self):
		del self._NewPlcOfIncorprtn
		self._NewPlcOfIncorprtn = base_types.UninitialisedField(self, 'NewPlcOfIncorprtn', Max70Text, False)

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if value is not None else base_types.UninitialisedField(self, 'OfferTp', OfferType1FormatChoice, True)

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = base_types.UninitialisedField(self, 'OfferTp', OfferType1FormatChoice, True)

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod1, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod1, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice2, True)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice2, True)

	@property
	def PrtlElctnInd(self):
		return self._PrtlElctnInd

	@PrtlElctnInd.setter
	def PrtlElctnInd(self, value):
		self._PrtlElctnInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlElctnInd', YesNoIndicator, False)

	@PrtlElctnInd.deleter
	def PrtlElctnInd(self):
		del self._PrtlElctnInd
		self._PrtlElctnInd = base_types.UninitialisedField(self, 'PrtlElctnInd', YesNoIndicator, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate1, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate1, False)

	@property
	def RedChrgsApldInd(self):
		return self._RedChrgsApldInd

	@RedChrgsApldInd.setter
	def RedChrgsApldInd(self, value):
		self._RedChrgsApldInd = value if value is not None else base_types.UninitialisedField(self, 'RedChrgsApldInd', YesNoIndicator, False)

	@RedChrgsApldInd.deleter
	def RedChrgsApldInd(self):
		del self._RedChrgsApldInd
		self._RedChrgsApldInd = base_types.UninitialisedField(self, 'RedChrgsApldInd', YesNoIndicator, False)

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if value is not None else base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableStatus1FormatChoice, False)

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableStatus1FormatChoice, False)

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
	def SctiesQtySght(self):
		return self._SctiesQtySght

	@SctiesQtySght.setter
	def SctiesQtySght(self, value):
		self._SctiesQtySght = value if value is not None else base_types.UninitialisedField(self, 'SctiesQtySght', UnitOrFaceAmountOrCode1Choice, False)

	@SctiesQtySght.deleter
	def SctiesQtySght(self):
		del self._SctiesQtySght
		self._SctiesQtySght = base_types.UninitialisedField(self, 'SctiesQtySght', UnitOrFaceAmountOrCode1Choice, False)

	@property
	def TaxblIncmPerShrClctd(self):
		return self._TaxblIncmPerShrClctd

	@TaxblIncmPerShrClctd.setter
	def TaxblIncmPerShrClctd(self, value):
		self._TaxblIncmPerShrClctd = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Code, False)

	@TaxblIncmPerShrClctd.deleter
	def TaxblIncmPerShrClctd(self):
		del self._TaxblIncmPerShrClctd
		self._TaxblIncmPerShrClctd = base_types.UninitialisedField(self, 'TaxblIncmPerShrClctd', TaxableIncomePerShareCalculated2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseDnmtn', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckEndOddLotSctiesQty', type=UnitOrFaceAmountOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnReqrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeType1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnMtd', type=CorporateActionCalculationMethod1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsTp', type=ConversionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnAddtlInf', type=CorporateActionNarrative1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnNb', type=Max3NumericText, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CptlGn', type=EUCapitalGain2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltOptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltOptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnTp', type=DistributionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddTp', type=CorporateActionFrequencyType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnTp', type=ElectionMovementType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStage1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrntEndOddLotSctiesQty', type=UnitOrFaceAmountOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrmtlDnmtn', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecurityDistributionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrdNbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblMltplSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPlcOfIncorprtn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferType1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlElctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableStatus1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtySght', type=UnitOrFaceAmountOrCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShrClctd', type=TaxableIncomePerShareCalculated2Code, min=0, max=1, mutex_group=None, array=False),
	))