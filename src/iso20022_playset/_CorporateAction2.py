from . import base_types
from ._CorporateActionFrequencyType1FormatChoice import CorporateActionFrequencyType1FormatChoice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._CorporateActionOption1FormatChoice import CorporateActionOption1FormatChoice
from ._LotteryType1FormatChoice import LotteryType1FormatChoice
from ._OfferType1FormatChoice import OfferType1FormatChoice
from ._ConversionType1FormatChoice import ConversionType1FormatChoice
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice
from ._GenericIdentification13 import GenericIdentification13
from ._IntermediateSecurityDistributionType1FormatChoice import IntermediateSecurityDistributionType1FormatChoice
from ._RenounceableStatus1FormatChoice import RenounceableStatus1FormatChoice
from ._Number import Number
from ._UnitOrFaceAmountOrCode1Choice import UnitOrFaceAmountOrCode1Choice
from ._CorporateActionDate2 import CorporateActionDate2
from ._CorporateActionChangeType1FormatChoice import CorporateActionChangeType1FormatChoice
from ._Max3NumericText import Max3NumericText
from ._CorporateActionCalculationMethod1FormatChoice import CorporateActionCalculationMethod1FormatChoice
from ._CorporateActionPrice2 import CorporateActionPrice2
from ._ElectionMovementType1FormatChoice import ElectionMovementType1FormatChoice
from ._BeneficiaryCertificationType1FormatChoice import BeneficiaryCertificationType1FormatChoice
from ._CorporateActionNarrative1 import CorporateActionNarrative1
from ._TaxableIncomePerShareCalculated2Code import TaxableIncomePerShareCalculated2Code
from ._YesNoIndicator import YesNoIndicator
from ._CorporateActionRate1 import CorporateActionRate1
from ._CorporateActionEventStage1FormatChoice import CorporateActionEventStage1FormatChoice
from ._DistributionType1FormatChoice import DistributionType1FormatChoice
from ._CorporateActionPeriod1 import CorporateActionPeriod1
from ._Exact3NumericText import Exact3NumericText
from ._Max70Text import Max70Text
from ._EUCapitalGain2Code import EUCapitalGain2Code

class CorporateAction2(base_types._BaseFieldType):

	__slots__ = ["_PrdDtls", "_RstrctnInd", "_DstrbtnTp", "_ConvsTp", "_DtDtls", "_NewPlcOfIncorprtn", "_TaxblIncmPerShrClctd", "_MinExrcblMltplSctiesQty", "_ChngTp", "_PrtlElctnInd", "_RnncblEntitlmntStsTp", "_EvtStag", "_OfferTp", "_CpnNb", "_IncmTp", "_DfltOptnNb", "_RedChrgsApldInd", "_CertfctnTp", "_LtryTp", "_MinExrcblSctiesQty", "_NewBrdLotSctiesQty", "_FrntEndOddLotSctiesQty", "_NewDnmtnSctiesQty", "_IntrmdtSctiesDstrbtnTp", "_ClctnMtd", "_DvddTp", "_NewDnmtnCcy", "_RateAndAmtDtls", "_BckEndOddLotSctiesQty", "_IncrmtlDnmtn", "_CorpActnAddtlInf", "_BaseDnmtn", "_SctiesQtySght", "_PricDtls", "_ElctnTp", "_DfltOptnTp", "_CertfctnReqrdInd", "_CptlGn", "_IntrstAcrdNbOfDays"]
	@property
	def BaseDnmtn(self):
		return self._BaseDnmtn

	@BaseDnmtn.setter
	def BaseDnmtn(self, value):
		self._BaseDnmtn = value if type(value) != base_types.auto else self.make_default("BaseDnmtn")

	@BaseDnmtn.deleter
	def BaseDnmtn(self):
		del self._BaseDnmtn
		self._BaseDnmtn = None

	@property
	def BckEndOddLotSctiesQty(self):
		return self._BckEndOddLotSctiesQty

	@BckEndOddLotSctiesQty.setter
	def BckEndOddLotSctiesQty(self, value):
		self._BckEndOddLotSctiesQty = value if type(value) != base_types.auto else self.make_default("BckEndOddLotSctiesQty")

	@BckEndOddLotSctiesQty.deleter
	def BckEndOddLotSctiesQty(self):
		del self._BckEndOddLotSctiesQty
		self._BckEndOddLotSctiesQty = None

	@property
	def CertfctnReqrdInd(self):
		return self._CertfctnReqrdInd

	@CertfctnReqrdInd.setter
	def CertfctnReqrdInd(self, value):
		self._CertfctnReqrdInd = value if type(value) != base_types.auto else self.make_default("CertfctnReqrdInd")

	@CertfctnReqrdInd.deleter
	def CertfctnReqrdInd(self):
		del self._CertfctnReqrdInd
		self._CertfctnReqrdInd = None

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
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if type(value) != base_types.auto else self.make_default("ClctnMtd")

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = None

	@property
	def ConvsTp(self):
		return self._ConvsTp

	@ConvsTp.setter
	def ConvsTp(self, value):
		self._ConvsTp = value if type(value) != base_types.auto else self.make_default("ConvsTp")

	@ConvsTp.deleter
	def ConvsTp(self):
		del self._ConvsTp
		self._ConvsTp = None

	@property
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if type(value) != base_types.auto else self.make_default("CorpActnAddtlInf")

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = None

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
	def CptlGn(self):
		return self._CptlGn

	@CptlGn.setter
	def CptlGn(self, value):
		self._CptlGn = value if type(value) != base_types.auto else self.make_default("CptlGn")

	@CptlGn.deleter
	def CptlGn(self):
		del self._CptlGn
		self._CptlGn = None

	@property
	def DfltOptnNb(self):
		return self._DfltOptnNb

	@DfltOptnNb.setter
	def DfltOptnNb(self, value):
		self._DfltOptnNb = value if type(value) != base_types.auto else self.make_default("DfltOptnNb")

	@DfltOptnNb.deleter
	def DfltOptnNb(self):
		del self._DfltOptnNb
		self._DfltOptnNb = None

	@property
	def DfltOptnTp(self):
		return self._DfltOptnTp

	@DfltOptnTp.setter
	def DfltOptnTp(self, value):
		self._DfltOptnTp = value if type(value) != base_types.auto else self.make_default("DfltOptnTp")

	@DfltOptnTp.deleter
	def DfltOptnTp(self):
		del self._DfltOptnTp
		self._DfltOptnTp = None

	@property
	def DstrbtnTp(self):
		return self._DstrbtnTp

	@DstrbtnTp.setter
	def DstrbtnTp(self, value):
		self._DstrbtnTp = value if type(value) != base_types.auto else self.make_default("DstrbtnTp")

	@DstrbtnTp.deleter
	def DstrbtnTp(self):
		del self._DstrbtnTp
		self._DstrbtnTp = None

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
	def FrntEndOddLotSctiesQty(self):
		return self._FrntEndOddLotSctiesQty

	@FrntEndOddLotSctiesQty.setter
	def FrntEndOddLotSctiesQty(self, value):
		self._FrntEndOddLotSctiesQty = value if type(value) != base_types.auto else self.make_default("FrntEndOddLotSctiesQty")

	@FrntEndOddLotSctiesQty.deleter
	def FrntEndOddLotSctiesQty(self):
		del self._FrntEndOddLotSctiesQty
		self._FrntEndOddLotSctiesQty = None

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
	def IncrmtlDnmtn(self):
		return self._IncrmtlDnmtn

	@IncrmtlDnmtn.setter
	def IncrmtlDnmtn(self, value):
		self._IncrmtlDnmtn = value if type(value) != base_types.auto else self.make_default("IncrmtlDnmtn")

	@IncrmtlDnmtn.deleter
	def IncrmtlDnmtn(self):
		del self._IncrmtlDnmtn
		self._IncrmtlDnmtn = None

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
	def MinExrcblMltplSctiesQty(self):
		return self._MinExrcblMltplSctiesQty

	@MinExrcblMltplSctiesQty.setter
	def MinExrcblMltplSctiesQty(self, value):
		self._MinExrcblMltplSctiesQty = value if type(value) != base_types.auto else self.make_default("MinExrcblMltplSctiesQty")

	@MinExrcblMltplSctiesQty.deleter
	def MinExrcblMltplSctiesQty(self):
		del self._MinExrcblMltplSctiesQty
		self._MinExrcblMltplSctiesQty = None

	@property
	def MinExrcblSctiesQty(self):
		return self._MinExrcblSctiesQty

	@MinExrcblSctiesQty.setter
	def MinExrcblSctiesQty(self, value):
		self._MinExrcblSctiesQty = value if type(value) != base_types.auto else self.make_default("MinExrcblSctiesQty")

	@MinExrcblSctiesQty.deleter
	def MinExrcblSctiesQty(self):
		del self._MinExrcblSctiesQty
		self._MinExrcblSctiesQty = None

	@property
	def NewBrdLotSctiesQty(self):
		return self._NewBrdLotSctiesQty

	@NewBrdLotSctiesQty.setter
	def NewBrdLotSctiesQty(self, value):
		self._NewBrdLotSctiesQty = value if type(value) != base_types.auto else self.make_default("NewBrdLotSctiesQty")

	@NewBrdLotSctiesQty.deleter
	def NewBrdLotSctiesQty(self):
		del self._NewBrdLotSctiesQty
		self._NewBrdLotSctiesQty = None

	@property
	def NewDnmtnCcy(self):
		return self._NewDnmtnCcy

	@NewDnmtnCcy.setter
	def NewDnmtnCcy(self, value):
		self._NewDnmtnCcy = value if type(value) != base_types.auto else self.make_default("NewDnmtnCcy")

	@NewDnmtnCcy.deleter
	def NewDnmtnCcy(self):
		del self._NewDnmtnCcy
		self._NewDnmtnCcy = None

	@property
	def NewDnmtnSctiesQty(self):
		return self._NewDnmtnSctiesQty

	@NewDnmtnSctiesQty.setter
	def NewDnmtnSctiesQty(self, value):
		self._NewDnmtnSctiesQty = value if type(value) != base_types.auto else self.make_default("NewDnmtnSctiesQty")

	@NewDnmtnSctiesQty.deleter
	def NewDnmtnSctiesQty(self):
		del self._NewDnmtnSctiesQty
		self._NewDnmtnSctiesQty = None

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
	def PrtlElctnInd(self):
		return self._PrtlElctnInd

	@PrtlElctnInd.setter
	def PrtlElctnInd(self, value):
		self._PrtlElctnInd = value if type(value) != base_types.auto else self.make_default("PrtlElctnInd")

	@PrtlElctnInd.deleter
	def PrtlElctnInd(self):
		del self._PrtlElctnInd
		self._PrtlElctnInd = None

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
	def RedChrgsApldInd(self):
		return self._RedChrgsApldInd

	@RedChrgsApldInd.setter
	def RedChrgsApldInd(self, value):
		self._RedChrgsApldInd = value if type(value) != base_types.auto else self.make_default("RedChrgsApldInd")

	@RedChrgsApldInd.deleter
	def RedChrgsApldInd(self):
		del self._RedChrgsApldInd
		self._RedChrgsApldInd = None

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
	def SctiesQtySght(self):
		return self._SctiesQtySght

	@SctiesQtySght.setter
	def SctiesQtySght(self, value):
		self._SctiesQtySght = value if type(value) != base_types.auto else self.make_default("SctiesQtySght")

	@SctiesQtySght.deleter
	def SctiesQtySght(self):
		del self._SctiesQtySght
		self._SctiesQtySght = None

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

