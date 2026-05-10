from . import base_types
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._GenericIdentification37 import GenericIdentification37
from ._PercentageRate import PercentageRate
from ._Frequency23Choice import Frequency23Choice
from ._OptionType6Choice import OptionType6Choice
from ._Number1Choice import Number1Choice
from ._FormOfSecurity6Choice import FormOfSecurity6Choice
from ._MarketIdentification3Choice import MarketIdentification3Choice
from ._FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from ._ISODate import ISODate
from ._OptionStyle10Choice import OptionStyle10Choice
from ._YesNoIndicator import YesNoIndicator
from ._BaseOneRate import BaseOneRate
from ._Rating1 import Rating1
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._Price14 import Price14
from ._InterestComputationMethodFormat4Choice import InterestComputationMethodFormat4Choice
from ._Max35Text import Max35Text
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max350Text import Max350Text
from ._ClassificationType32Choice import ClassificationType32Choice

class FinancialInstrumentAttributes124(base_types._BaseFieldType):

	__slots__ = ["_CllblInd", "_OptnTp", "_EndFctr", "_IndxRateBsis", "_ExrcPric", "_RegnForm", "_NxtCllblDt", "_IntrstRate", "_ConvtblInd", "_PutblDt", "_ClssfctnTp", "_PrvsFctr", "_ConvsPric", "_MinNmnlQty", "_NxtFctr", "_PctgOfDebtClms", "_WarrtAttchdOnDlvry", "_NxtFctrDt", "_XpryDt", "_IsseDt", "_MinExrcblMltplQty", "_NxtIntrstRate", "_CpnDt", "_CurFctr", "_CpnAttchdNb", "_PoolNb", "_DtdDt", "_VrsnNb", "_CvrdInd", "_PutblInd", "_CertNb", "_PlcOfListg", "_SbcptPric", "_FaceAmt", "_VarblRateChngFrqcy", "_FrstPmtDt", "_MinExrcblQty", "_CtrctSz", "_OptnStyle", "_ConvsDt", "_FltgRateFxgDt", "_OddCpnInd", "_MtrtyDt", "_YldVar", "_TaxblIncmPerShr", "_DnmtnCcy", "_PmtFrqcy", "_VarblRateInd", "_DayCntBsis", "_FinInstrmAttrAddtlDtls", "_RedYldImpct", "_Ratg"]
	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	@property
	def CllblInd(self):
		return self._CllblInd

	@CllblInd.setter
	def CllblInd(self, value):
		self._CllblInd = value if type(value) != base_types.auto else self.make_default("CllblInd")

	@CllblInd.deleter
	def CllblInd(self):
		del self._CllblInd
		self._CllblInd = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if type(value) != base_types.auto else self.make_default("ConvsDt")

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = None

	@property
	def ConvsPric(self):
		return self._ConvsPric

	@ConvsPric.setter
	def ConvsPric(self, value):
		self._ConvsPric = value if type(value) != base_types.auto else self.make_default("ConvsPric")

	@ConvsPric.deleter
	def ConvsPric(self):
		del self._ConvsPric
		self._ConvsPric = None

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if type(value) != base_types.auto else self.make_default("ConvtblInd")

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = None

	@property
	def CpnAttchdNb(self):
		return self._CpnAttchdNb

	@CpnAttchdNb.setter
	def CpnAttchdNb(self, value):
		self._CpnAttchdNb = value if type(value) != base_types.auto else self.make_default("CpnAttchdNb")

	@CpnAttchdNb.deleter
	def CpnAttchdNb(self):
		del self._CpnAttchdNb
		self._CpnAttchdNb = None

	@property
	def CpnDt(self):
		return self._CpnDt

	@CpnDt.setter
	def CpnDt(self, value):
		self._CpnDt = value if type(value) != base_types.auto else self.make_default("CpnDt")

	@CpnDt.deleter
	def CpnDt(self):
		del self._CpnDt
		self._CpnDt = None

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if type(value) != base_types.auto else self.make_default("CtrctSz")

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = None

	@property
	def CurFctr(self):
		return self._CurFctr

	@CurFctr.setter
	def CurFctr(self, value):
		self._CurFctr = value if type(value) != base_types.auto else self.make_default("CurFctr")

	@CurFctr.deleter
	def CurFctr(self):
		del self._CurFctr
		self._CurFctr = None

	@property
	def CvrdInd(self):
		return self._CvrdInd

	@CvrdInd.setter
	def CvrdInd(self, value):
		self._CvrdInd = value if type(value) != base_types.auto else self.make_default("CvrdInd")

	@CvrdInd.deleter
	def CvrdInd(self):
		del self._CvrdInd
		self._CvrdInd = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != base_types.auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if type(value) != base_types.auto else self.make_default("DtdDt")

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = None

	@property
	def EndFctr(self):
		return self._EndFctr

	@EndFctr.setter
	def EndFctr(self, value):
		self._EndFctr = value if type(value) != base_types.auto else self.make_default("EndFctr")

	@EndFctr.deleter
	def EndFctr(self):
		del self._EndFctr
		self._EndFctr = None

	@property
	def ExrcPric(self):
		return self._ExrcPric

	@ExrcPric.setter
	def ExrcPric(self, value):
		self._ExrcPric = value if type(value) != base_types.auto else self.make_default("ExrcPric")

	@ExrcPric.deleter
	def ExrcPric(self):
		del self._ExrcPric
		self._ExrcPric = None

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if type(value) != base_types.auto else self.make_default("FaceAmt")

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = None

	@property
	def FinInstrmAttrAddtlDtls(self):
		return self._FinInstrmAttrAddtlDtls

	@FinInstrmAttrAddtlDtls.setter
	def FinInstrmAttrAddtlDtls(self, value):
		self._FinInstrmAttrAddtlDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrAddtlDtls")

	@FinInstrmAttrAddtlDtls.deleter
	def FinInstrmAttrAddtlDtls(self):
		del self._FinInstrmAttrAddtlDtls
		self._FinInstrmAttrAddtlDtls = None

	@property
	def FltgRateFxgDt(self):
		return self._FltgRateFxgDt

	@FltgRateFxgDt.setter
	def FltgRateFxgDt(self, value):
		self._FltgRateFxgDt = value if type(value) != base_types.auto else self.make_default("FltgRateFxgDt")

	@FltgRateFxgDt.deleter
	def FltgRateFxgDt(self):
		del self._FltgRateFxgDt
		self._FltgRateFxgDt = None

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if type(value) != base_types.auto else self.make_default("FrstPmtDt")

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = None

	@property
	def IndxRateBsis(self):
		return self._IndxRateBsis

	@IndxRateBsis.setter
	def IndxRateBsis(self, value):
		self._IndxRateBsis = value if type(value) != base_types.auto else self.make_default("IndxRateBsis")

	@IndxRateBsis.deleter
	def IndxRateBsis(self):
		del self._IndxRateBsis
		self._IndxRateBsis = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def MinExrcblMltplQty(self):
		return self._MinExrcblMltplQty

	@MinExrcblMltplQty.setter
	def MinExrcblMltplQty(self, value):
		self._MinExrcblMltplQty = value if type(value) != base_types.auto else self.make_default("MinExrcblMltplQty")

	@MinExrcblMltplQty.deleter
	def MinExrcblMltplQty(self):
		del self._MinExrcblMltplQty
		self._MinExrcblMltplQty = None

	@property
	def MinExrcblQty(self):
		return self._MinExrcblQty

	@MinExrcblQty.setter
	def MinExrcblQty(self, value):
		self._MinExrcblQty = value if type(value) != base_types.auto else self.make_default("MinExrcblQty")

	@MinExrcblQty.deleter
	def MinExrcblQty(self):
		del self._MinExrcblQty
		self._MinExrcblQty = None

	@property
	def MinNmnlQty(self):
		return self._MinNmnlQty

	@MinNmnlQty.setter
	def MinNmnlQty(self, value):
		self._MinNmnlQty = value if type(value) != base_types.auto else self.make_default("MinNmnlQty")

	@MinNmnlQty.deleter
	def MinNmnlQty(self):
		del self._MinNmnlQty
		self._MinNmnlQty = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if type(value) != base_types.auto else self.make_default("NxtCllblDt")

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = None

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if type(value) != base_types.auto else self.make_default("NxtFctr")

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = None

	@property
	def NxtFctrDt(self):
		return self._NxtFctrDt

	@NxtFctrDt.setter
	def NxtFctrDt(self, value):
		self._NxtFctrDt = value if type(value) != base_types.auto else self.make_default("NxtFctrDt")

	@NxtFctrDt.deleter
	def NxtFctrDt(self):
		del self._NxtFctrDt
		self._NxtFctrDt = None

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if type(value) != base_types.auto else self.make_default("NxtIntrstRate")

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = None

	@property
	def OddCpnInd(self):
		return self._OddCpnInd

	@OddCpnInd.setter
	def OddCpnInd(self, value):
		self._OddCpnInd = value if type(value) != base_types.auto else self.make_default("OddCpnInd")

	@OddCpnInd.deleter
	def OddCpnInd(self):
		del self._OddCpnInd
		self._OddCpnInd = None

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if type(value) != base_types.auto else self.make_default("OptnStyle")

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def PctgOfDebtClms(self):
		return self._PctgOfDebtClms

	@PctgOfDebtClms.setter
	def PctgOfDebtClms(self, value):
		self._PctgOfDebtClms = value if type(value) != base_types.auto else self.make_default("PctgOfDebtClms")

	@PctgOfDebtClms.deleter
	def PctgOfDebtClms(self):
		del self._PctgOfDebtClms
		self._PctgOfDebtClms = None

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if type(value) != base_types.auto else self.make_default("PlcOfListg")

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def PoolNb(self):
		return self._PoolNb

	@PoolNb.setter
	def PoolNb(self, value):
		self._PoolNb = value if type(value) != base_types.auto else self.make_default("PoolNb")

	@PoolNb.deleter
	def PoolNb(self):
		del self._PoolNb
		self._PoolNb = None

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if type(value) != base_types.auto else self.make_default("PrvsFctr")

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = None

	@property
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if type(value) != base_types.auto else self.make_default("PutblDt")

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = None

	@property
	def PutblInd(self):
		return self._PutblInd

	@PutblInd.setter
	def PutblInd(self, value):
		self._PutblInd = value if type(value) != base_types.auto else self.make_default("PutblInd")

	@PutblInd.deleter
	def PutblInd(self):
		del self._PutblInd
		self._PutblInd = None

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if type(value) != base_types.auto else self.make_default("Ratg")

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = None

	@property
	def RedYldImpct(self):
		return self._RedYldImpct

	@RedYldImpct.setter
	def RedYldImpct(self, value):
		self._RedYldImpct = value if type(value) != base_types.auto else self.make_default("RedYldImpct")

	@RedYldImpct.deleter
	def RedYldImpct(self):
		del self._RedYldImpct
		self._RedYldImpct = None

	@property
	def RegnForm(self):
		return self._RegnForm

	@RegnForm.setter
	def RegnForm(self, value):
		self._RegnForm = value if type(value) != base_types.auto else self.make_default("RegnForm")

	@RegnForm.deleter
	def RegnForm(self):
		del self._RegnForm
		self._RegnForm = None

	@property
	def SbcptPric(self):
		return self._SbcptPric

	@SbcptPric.setter
	def SbcptPric(self, value):
		self._SbcptPric = value if type(value) != base_types.auto else self.make_default("SbcptPric")

	@SbcptPric.deleter
	def SbcptPric(self):
		del self._SbcptPric
		self._SbcptPric = None

	@property
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerShr")

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = None

	@property
	def VarblRateChngFrqcy(self):
		return self._VarblRateChngFrqcy

	@VarblRateChngFrqcy.setter
	def VarblRateChngFrqcy(self, value):
		self._VarblRateChngFrqcy = value if type(value) != base_types.auto else self.make_default("VarblRateChngFrqcy")

	@VarblRateChngFrqcy.deleter
	def VarblRateChngFrqcy(self):
		del self._VarblRateChngFrqcy
		self._VarblRateChngFrqcy = None

	@property
	def VarblRateInd(self):
		return self._VarblRateInd

	@VarblRateInd.setter
	def VarblRateInd(self, value):
		self._VarblRateInd = value if type(value) != base_types.auto else self.make_default("VarblRateInd")

	@VarblRateInd.deleter
	def VarblRateInd(self):
		del self._VarblRateInd
		self._VarblRateInd = None

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if type(value) != base_types.auto else self.make_default("VrsnNb")

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = None

	@property
	def WarrtAttchdOnDlvry(self):
		return self._WarrtAttchdOnDlvry

	@WarrtAttchdOnDlvry.setter
	def WarrtAttchdOnDlvry(self, value):
		self._WarrtAttchdOnDlvry = value if type(value) != base_types.auto else self.make_default("WarrtAttchdOnDlvry")

	@WarrtAttchdOnDlvry.deleter
	def WarrtAttchdOnDlvry(self):
		del self._WarrtAttchdOnDlvry
		self._WarrtAttchdOnDlvry = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def YldVar(self):
		return self._YldVar

	@YldVar.setter
	def YldVar(self, value):
		self._YldVar = value if type(value) != base_types.auto else self.make_default("YldVar")

	@YldVar.deleter
	def YldVar(self):
		del self._YldVar
		self._YldVar = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnAttchdNb', type=Number1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateFxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxRateBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblMltplQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNmnlQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OddCpnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfDebtClms', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=Rating1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedYldImpct', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnForm', type=FormOfSecurity6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerShr', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateChngFrqcy', type=Frequency23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Number1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WarrtAttchdOnDlvry', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldVar', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

