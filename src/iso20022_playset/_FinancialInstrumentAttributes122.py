from . import base_types
from .Frequency27Choice import Frequency27Choice
from .PriceType5Choice import PriceType5Choice
from .InterestComputationMethodFormat5Choice import InterestComputationMethodFormat5Choice
from .OptionType7Choice import OptionType7Choice
from .YesNoIndicator import YesNoIndicator
from .Number23Choice import Number23Choice
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .GenericIdentification39 import GenericIdentification39
from .MarketIdentification4Choice import MarketIdentification4Choice
from .ISODate import ISODate
from .Price3 import Price3
from .SecuritiesPaymentStatus6Choice import SecuritiesPaymentStatus6Choice
from .FormOfSecurity7Choice import FormOfSecurity7Choice
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text
from .SecurityIdentification20 import SecurityIdentification20
from .BaseOneRate import BaseOneRate
from .ClassificationType33Choice import ClassificationType33Choice
from .PercentageRate import PercentageRate
from .OptionStyle9Choice import OptionStyle9Choice
from .FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice

class FinancialInstrumentAttributes122(base_types._BaseFieldType):

	__slots__ = ["_IntrstRate", "_CpnAttchdNb", "_VarblRateChngFrqcy", "_VarblRateInd", "_PmtFrqcy", "_CtrctSz", "_RegnForm", "_YldToMtrtyRate", "_PutblInd", "_PrvsFctr", "_CpnDt", "_UndrlygFinInstrmId", "_SbcptPric", "_OptnTp", "_DayCntBsis", "_PutblDt", "_MinNmnlQty", "_XpryDt", "_FrstPmtDt", "_NxtFctr", "_FinInstrmAttrAddtlDtls", "_OptnStyle", "_MktOrIndctvPric", "_PlcOfListg", "_PmtSts", "_ConvsPric", "_NxtCllblDt", "_PoolNb", "_StrkPric", "_FltgRateFxgDt", "_CurFctr", "_NxtIntrstRate", "_IndxRateBsis", "_CllblInd", "_DtdDt", "_MtrtyDt", "_IsseDt", "_ExrcPric", "_ClssfctnTp", "_DnmtnCcy"]
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
	def YldToMtrtyRate(self):
		return self._YldToMtrtyRate

	@YldToMtrtyRate.setter
	def YldToMtrtyRate(self, value):
		self._YldToMtrtyRate = value if type(value) != base_types.auto else self.make_default("YldToMtrtyRate")

	@YldToMtrtyRate.deleter
	def YldToMtrtyRate(self):
		del self._YldToMtrtyRate
		self._YldToMtrtyRate = None

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
	def UndrlygFinInstrmId(self):
		return self._UndrlygFinInstrmId

	@UndrlygFinInstrmId.setter
	def UndrlygFinInstrmId(self, value):
		self._UndrlygFinInstrmId = value if type(value) != base_types.auto else self.make_default("UndrlygFinInstrmId")

	@UndrlygFinInstrmId.deleter
	def UndrlygFinInstrmId(self):
		del self._UndrlygFinInstrmId
		self._UndrlygFinInstrmId = None

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
	def MktOrIndctvPric(self):
		return self._MktOrIndctvPric

	@MktOrIndctvPric.setter
	def MktOrIndctvPric(self, value):
		self._MktOrIndctvPric = value if type(value) != base_types.auto else self.make_default("MktOrIndctvPric")

	@MktOrIndctvPric.deleter
	def MktOrIndctvPric(self):
		del self._MktOrIndctvPric
		self._MktOrIndctvPric = None

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
	def PmtSts(self):
		return self._PmtSts

	@PmtSts.setter
	def PmtSts(self, value):
		self._PmtSts = value if type(value) != base_types.auto else self.make_default("PmtSts")

	@PmtSts.deleter
	def PmtSts(self):
		del self._PmtSts
		self._PmtSts = None

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
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if type(value) != base_types.auto else self.make_default("StrkPric")

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = None

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
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnAttchdNb', type=Number23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateChngFrqcy', type=Frequency27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnForm', type=FormOfSecurity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldToMtrtyRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygFinInstrmId', type=SecurityIdentification20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbcptPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNmnlQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktOrIndctvPric', type=PriceType5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSts', type=SecuritiesPaymentStatus6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolNb', type=GenericIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateFxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxRateBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcPric', type=Price3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

