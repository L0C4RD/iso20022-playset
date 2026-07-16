# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import ClassificationType32Choice
from . import FinancialInstrumentQuantity33Choice
from . import FormOfSecurity6Choice
from . import Frequency23Choice
from . import GenericIdentification37
from . import ISODate
from . import InterestComputationMethodFormat4Choice
from . import MarketIdentification3Choice
from . import Max350Text
from . import Number22Choice
from . import OptionStyle8Choice
from . import OptionType6Choice
from . import PercentageRate
from . import Price7
from . import PriceType4Choice
from . import QuantityBreakdown60
from . import SecuritiesPaymentStatus5Choice
from . import SecurityIdentification19
from . import YesNoIndicator

class FinancialInstrumentAttributes112(base_types._BaseFieldType):

	__slots__ = ["_CllblInd", "_ClssfctnTp", "_ConvsPric", "_CpnAttchdNb", "_CpnDt", "_CtrctSz", "_CurFctr", "_DayCntBsis", "_DnmtnCcy", "_DtdDt", "_ExrcPric", "_FinInstrmAttrAddtlDtls", "_FltgRateFxgDt", "_FrstPmtDt", "_IndxRateBsis", "_IntrstRate", "_IsseDt", "_MinNmnlQty", "_MktOrIndctvPric", "_MtrtyDt", "_NxtCllblDt", "_NxtFctr", "_NxtIntrstRate", "_OptnStyle", "_OptnTp", "_PlcOfListg", "_PmtFrqcy", "_PmtSts", "_PoolNb", "_PrvsFctr", "_PutblDt", "_PutblInd", "_QtyBrkdwn", "_RegnForm", "_SbcptPric", "_StrkPric", "_UndrlygFinInstrmId", "_VarblRateChngFrqcy", "_VarblRateInd", "_XpryDt", "_YldToMtrtyRate"]
	@property
	def CllblInd(self):
		return self._CllblInd

	@CllblInd.setter
	def CllblInd(self, value):
		self._CllblInd = value if value is not None else base_types.UninitialisedField(self, 'CllblInd', YesNoIndicator, False)

	@CllblInd.deleter
	def CllblInd(self):
		del self._CllblInd
		self._CllblInd = base_types.UninitialisedField(self, 'CllblInd', YesNoIndicator, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType32Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType32Choice, False)

	@property
	def ConvsPric(self):
		return self._ConvsPric

	@ConvsPric.setter
	def ConvsPric(self, value):
		self._ConvsPric = value if value is not None else base_types.UninitialisedField(self, 'ConvsPric', Price7, False)

	@ConvsPric.deleter
	def ConvsPric(self):
		del self._ConvsPric
		self._ConvsPric = base_types.UninitialisedField(self, 'ConvsPric', Price7, False)

	@property
	def CpnAttchdNb(self):
		return self._CpnAttchdNb

	@CpnAttchdNb.setter
	def CpnAttchdNb(self, value):
		self._CpnAttchdNb = value if value is not None else base_types.UninitialisedField(self, 'CpnAttchdNb', Number22Choice, False)

	@CpnAttchdNb.deleter
	def CpnAttchdNb(self):
		del self._CpnAttchdNb
		self._CpnAttchdNb = base_types.UninitialisedField(self, 'CpnAttchdNb', Number22Choice, False)

	@property
	def CpnDt(self):
		return self._CpnDt

	@CpnDt.setter
	def CpnDt(self, value):
		self._CpnDt = value if value is not None else base_types.UninitialisedField(self, 'CpnDt', ISODate, False)

	@CpnDt.deleter
	def CpnDt(self):
		del self._CpnDt
		self._CpnDt = base_types.UninitialisedField(self, 'CpnDt', ISODate, False)

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity33Choice, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity33Choice, False)

	@property
	def CurFctr(self):
		return self._CurFctr

	@CurFctr.setter
	def CurFctr(self, value):
		self._CurFctr = value if value is not None else base_types.UninitialisedField(self, 'CurFctr', BaseOneRate, False)

	@CurFctr.deleter
	def CurFctr(self):
		del self._CurFctr
		self._CurFctr = base_types.UninitialisedField(self, 'CurFctr', BaseOneRate, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat4Choice, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat4Choice, False)

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if value is not None else base_types.UninitialisedField(self, 'DtdDt', ISODate, False)

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = base_types.UninitialisedField(self, 'DtdDt', ISODate, False)

	@property
	def ExrcPric(self):
		return self._ExrcPric

	@ExrcPric.setter
	def ExrcPric(self, value):
		self._ExrcPric = value if value is not None else base_types.UninitialisedField(self, 'ExrcPric', Price7, False)

	@ExrcPric.deleter
	def ExrcPric(self):
		del self._ExrcPric
		self._ExrcPric = base_types.UninitialisedField(self, 'ExrcPric', Price7, False)

	@property
	def FinInstrmAttrAddtlDtls(self):
		return self._FinInstrmAttrAddtlDtls

	@FinInstrmAttrAddtlDtls.setter
	def FinInstrmAttrAddtlDtls(self, value):
		self._FinInstrmAttrAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrAddtlDtls', Max350Text, False)

	@FinInstrmAttrAddtlDtls.deleter
	def FinInstrmAttrAddtlDtls(self):
		del self._FinInstrmAttrAddtlDtls
		self._FinInstrmAttrAddtlDtls = base_types.UninitialisedField(self, 'FinInstrmAttrAddtlDtls', Max350Text, False)

	@property
	def FltgRateFxgDt(self):
		return self._FltgRateFxgDt

	@FltgRateFxgDt.setter
	def FltgRateFxgDt(self, value):
		self._FltgRateFxgDt = value if value is not None else base_types.UninitialisedField(self, 'FltgRateFxgDt', ISODate, False)

	@FltgRateFxgDt.deleter
	def FltgRateFxgDt(self):
		del self._FltgRateFxgDt
		self._FltgRateFxgDt = base_types.UninitialisedField(self, 'FltgRateFxgDt', ISODate, False)

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

	@property
	def IndxRateBsis(self):
		return self._IndxRateBsis

	@IndxRateBsis.setter
	def IndxRateBsis(self, value):
		self._IndxRateBsis = value if value is not None else base_types.UninitialisedField(self, 'IndxRateBsis', PercentageRate, False)

	@IndxRateBsis.deleter
	def IndxRateBsis(self):
		del self._IndxRateBsis
		self._IndxRateBsis = base_types.UninitialisedField(self, 'IndxRateBsis', PercentageRate, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def MinNmnlQty(self):
		return self._MinNmnlQty

	@MinNmnlQty.setter
	def MinNmnlQty(self, value):
		self._MinNmnlQty = value if value is not None else base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity33Choice, False)

	@MinNmnlQty.deleter
	def MinNmnlQty(self):
		del self._MinNmnlQty
		self._MinNmnlQty = base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity33Choice, False)

	@property
	def MktOrIndctvPric(self):
		return self._MktOrIndctvPric

	@MktOrIndctvPric.setter
	def MktOrIndctvPric(self, value):
		self._MktOrIndctvPric = value if value is not None else base_types.UninitialisedField(self, 'MktOrIndctvPric', PriceType4Choice, False)

	@MktOrIndctvPric.deleter
	def MktOrIndctvPric(self):
		del self._MktOrIndctvPric
		self._MktOrIndctvPric = base_types.UninitialisedField(self, 'MktOrIndctvPric', PriceType4Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if value is not None else base_types.UninitialisedField(self, 'NxtCllblDt', ISODate, False)

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = base_types.UninitialisedField(self, 'NxtCllblDt', ISODate, False)

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if value is not None else base_types.UninitialisedField(self, 'NxtFctr', BaseOneRate, False)

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = base_types.UninitialisedField(self, 'NxtFctr', BaseOneRate, False)

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'NxtIntrstRate', PercentageRate, False)

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = base_types.UninitialisedField(self, 'NxtIntrstRate', PercentageRate, False)

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnStyle', OptionStyle8Choice, False)

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = base_types.UninitialisedField(self, 'OptnStyle', OptionStyle8Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification3Choice, False)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MarketIdentification3Choice, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency23Choice, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency23Choice, False)

	@property
	def PmtSts(self):
		return self._PmtSts

	@PmtSts.setter
	def PmtSts(self, value):
		self._PmtSts = value if value is not None else base_types.UninitialisedField(self, 'PmtSts', SecuritiesPaymentStatus5Choice, False)

	@PmtSts.deleter
	def PmtSts(self):
		del self._PmtSts
		self._PmtSts = base_types.UninitialisedField(self, 'PmtSts', SecuritiesPaymentStatus5Choice, False)

	@property
	def PoolNb(self):
		return self._PoolNb

	@PoolNb.setter
	def PoolNb(self, value):
		self._PoolNb = value if value is not None else base_types.UninitialisedField(self, 'PoolNb', GenericIdentification37, False)

	@PoolNb.deleter
	def PoolNb(self):
		del self._PoolNb
		self._PoolNb = base_types.UninitialisedField(self, 'PoolNb', GenericIdentification37, False)

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if value is not None else base_types.UninitialisedField(self, 'PrvsFctr', BaseOneRate, False)

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = base_types.UninitialisedField(self, 'PrvsFctr', BaseOneRate, False)

	@property
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if value is not None else base_types.UninitialisedField(self, 'PutblDt', ISODate, False)

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = base_types.UninitialisedField(self, 'PutblDt', ISODate, False)

	@property
	def PutblInd(self):
		return self._PutblInd

	@PutblInd.setter
	def PutblInd(self, value):
		self._PutblInd = value if value is not None else base_types.UninitialisedField(self, 'PutblInd', YesNoIndicator, False)

	@PutblInd.deleter
	def PutblInd(self):
		del self._PutblInd
		self._PutblInd = base_types.UninitialisedField(self, 'PutblInd', YesNoIndicator, False)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown60, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown60, True)

	@property
	def RegnForm(self):
		return self._RegnForm

	@RegnForm.setter
	def RegnForm(self, value):
		self._RegnForm = value if value is not None else base_types.UninitialisedField(self, 'RegnForm', FormOfSecurity6Choice, False)

	@RegnForm.deleter
	def RegnForm(self):
		del self._RegnForm
		self._RegnForm = base_types.UninitialisedField(self, 'RegnForm', FormOfSecurity6Choice, False)

	@property
	def SbcptPric(self):
		return self._SbcptPric

	@SbcptPric.setter
	def SbcptPric(self, value):
		self._SbcptPric = value if value is not None else base_types.UninitialisedField(self, 'SbcptPric', Price7, False)

	@SbcptPric.deleter
	def SbcptPric(self):
		del self._SbcptPric
		self._SbcptPric = base_types.UninitialisedField(self, 'SbcptPric', Price7, False)

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if value is not None else base_types.UninitialisedField(self, 'StrkPric', Price7, False)

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = base_types.UninitialisedField(self, 'StrkPric', Price7, False)

	@property
	def UndrlygFinInstrmId(self):
		return self._UndrlygFinInstrmId

	@UndrlygFinInstrmId.setter
	def UndrlygFinInstrmId(self, value):
		self._UndrlygFinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'UndrlygFinInstrmId', SecurityIdentification19, True)

	@UndrlygFinInstrmId.deleter
	def UndrlygFinInstrmId(self):
		del self._UndrlygFinInstrmId
		self._UndrlygFinInstrmId = base_types.UninitialisedField(self, 'UndrlygFinInstrmId', SecurityIdentification19, True)

	@property
	def VarblRateChngFrqcy(self):
		return self._VarblRateChngFrqcy

	@VarblRateChngFrqcy.setter
	def VarblRateChngFrqcy(self, value):
		self._VarblRateChngFrqcy = value if value is not None else base_types.UninitialisedField(self, 'VarblRateChngFrqcy', Frequency23Choice, False)

	@VarblRateChngFrqcy.deleter
	def VarblRateChngFrqcy(self):
		del self._VarblRateChngFrqcy
		self._VarblRateChngFrqcy = base_types.UninitialisedField(self, 'VarblRateChngFrqcy', Frequency23Choice, False)

	@property
	def VarblRateInd(self):
		return self._VarblRateInd

	@VarblRateInd.setter
	def VarblRateInd(self, value):
		self._VarblRateInd = value if value is not None else base_types.UninitialisedField(self, 'VarblRateInd', YesNoIndicator, False)

	@VarblRateInd.deleter
	def VarblRateInd(self):
		del self._VarblRateInd
		self._VarblRateInd = base_types.UninitialisedField(self, 'VarblRateInd', YesNoIndicator, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	@property
	def YldToMtrtyRate(self):
		return self._YldToMtrtyRate

	@YldToMtrtyRate.setter
	def YldToMtrtyRate(self, value):
		self._YldToMtrtyRate = value if value is not None else base_types.UninitialisedField(self, 'YldToMtrtyRate', PercentageRate, False)

	@YldToMtrtyRate.deleter
	def YldToMtrtyRate(self):
		del self._YldToMtrtyRate
		self._YldToMtrtyRate = base_types.UninitialisedField(self, 'YldToMtrtyRate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnAttchdNb', type=Number22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateFxgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxRateBsis', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNmnlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktOrIndctvPric', type=PriceType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSts', type=SecuritiesPaymentStatus5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown60, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnForm', type=FormOfSecurity6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygFinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VarblRateChngFrqcy', type=Frequency23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldToMtrtyRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))