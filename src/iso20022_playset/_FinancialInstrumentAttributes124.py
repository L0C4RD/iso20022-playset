# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import ClassificationType32Choice
from . import FinancialInstrumentQuantity18Choice
from . import FinancialInstrumentQuantity1Choice
from . import FormOfSecurity6Choice
from . import Frequency23Choice
from . import GenericIdentification37
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import InterestComputationMethodFormat4Choice
from . import MarketIdentification3Choice
from . import Max350Text
from . import Max35Text
from . import Number1Choice
from . import OptionStyle10Choice
from . import OptionType6Choice
from . import PercentageRate
from . import Price14
from . import Rating1
from . import YesNoIndicator

class FinancialInstrumentAttributes124(base_types._BaseFieldType):

	__slots__ = ["_CertNb", "_CllblInd", "_ClssfctnTp", "_ConvsDt", "_ConvsPric", "_ConvtblInd", "_CpnAttchdNb", "_CpnDt", "_CtrctSz", "_CurFctr", "_CvrdInd", "_DayCntBsis", "_DnmtnCcy", "_DtdDt", "_EndFctr", "_ExrcPric", "_FaceAmt", "_FinInstrmAttrAddtlDtls", "_FltgRateFxgDt", "_FrstPmtDt", "_IndxRateBsis", "_IntrstRate", "_IsseDt", "_MinExrcblMltplQty", "_MinExrcblQty", "_MinNmnlQty", "_MtrtyDt", "_NxtCllblDt", "_NxtFctr", "_NxtFctrDt", "_NxtIntrstRate", "_OddCpnInd", "_OptnStyle", "_OptnTp", "_PctgOfDebtClms", "_PlcOfListg", "_PmtFrqcy", "_PoolNb", "_PrvsFctr", "_PutblDt", "_PutblInd", "_Ratg", "_RedYldImpct", "_RegnForm", "_SbcptPric", "_TaxblIncmPerShr", "_VarblRateChngFrqcy", "_VarblRateInd", "_VrsnNb", "_WarrtAttchdOnDlvry", "_XpryDt", "_YldVar"]
	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', Max35Text, False)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', Max35Text, False)

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
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if value is not None else base_types.UninitialisedField(self, 'ConvsDt', ISODate, False)

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = base_types.UninitialisedField(self, 'ConvsDt', ISODate, False)

	@property
	def ConvsPric(self):
		return self._ConvsPric

	@ConvsPric.setter
	def ConvsPric(self, value):
		self._ConvsPric = value if value is not None else base_types.UninitialisedField(self, 'ConvsPric', Price14, False)

	@ConvsPric.deleter
	def ConvsPric(self):
		del self._ConvsPric
		self._ConvsPric = base_types.UninitialisedField(self, 'ConvsPric', Price14, False)

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if value is not None else base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@property
	def CpnAttchdNb(self):
		return self._CpnAttchdNb

	@CpnAttchdNb.setter
	def CpnAttchdNb(self, value):
		self._CpnAttchdNb = value if value is not None else base_types.UninitialisedField(self, 'CpnAttchdNb', Number1Choice, False)

	@CpnAttchdNb.deleter
	def CpnAttchdNb(self):
		del self._CpnAttchdNb
		self._CpnAttchdNb = base_types.UninitialisedField(self, 'CpnAttchdNb', Number1Choice, False)

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
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity18Choice, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', FinancialInstrumentQuantity18Choice, False)

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
	def CvrdInd(self):
		return self._CvrdInd

	@CvrdInd.setter
	def CvrdInd(self, value):
		self._CvrdInd = value if value is not None else base_types.UninitialisedField(self, 'CvrdInd', YesNoIndicator, False)

	@CvrdInd.deleter
	def CvrdInd(self):
		del self._CvrdInd
		self._CvrdInd = base_types.UninitialisedField(self, 'CvrdInd', YesNoIndicator, False)

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
	def EndFctr(self):
		return self._EndFctr

	@EndFctr.setter
	def EndFctr(self, value):
		self._EndFctr = value if value is not None else base_types.UninitialisedField(self, 'EndFctr', BaseOneRate, False)

	@EndFctr.deleter
	def EndFctr(self):
		del self._EndFctr
		self._EndFctr = base_types.UninitialisedField(self, 'EndFctr', BaseOneRate, False)

	@property
	def ExrcPric(self):
		return self._ExrcPric

	@ExrcPric.setter
	def ExrcPric(self, value):
		self._ExrcPric = value if value is not None else base_types.UninitialisedField(self, 'ExrcPric', Price14, False)

	@ExrcPric.deleter
	def ExrcPric(self):
		del self._ExrcPric
		self._ExrcPric = base_types.UninitialisedField(self, 'ExrcPric', Price14, False)

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if value is not None else base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAndAmount, False)

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = base_types.UninitialisedField(self, 'FaceAmt', ImpliedCurrencyAndAmount, False)

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
	def MinExrcblMltplQty(self):
		return self._MinExrcblMltplQty

	@MinExrcblMltplQty.setter
	def MinExrcblMltplQty(self, value):
		self._MinExrcblMltplQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblMltplQty', FinancialInstrumentQuantity1Choice, False)

	@MinExrcblMltplQty.deleter
	def MinExrcblMltplQty(self):
		del self._MinExrcblMltplQty
		self._MinExrcblMltplQty = base_types.UninitialisedField(self, 'MinExrcblMltplQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def MinExrcblQty(self):
		return self._MinExrcblQty

	@MinExrcblQty.setter
	def MinExrcblQty(self, value):
		self._MinExrcblQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblQty', FinancialInstrumentQuantity1Choice, False)

	@MinExrcblQty.deleter
	def MinExrcblQty(self):
		del self._MinExrcblQty
		self._MinExrcblQty = base_types.UninitialisedField(self, 'MinExrcblQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def MinNmnlQty(self):
		return self._MinNmnlQty

	@MinNmnlQty.setter
	def MinNmnlQty(self, value):
		self._MinNmnlQty = value if value is not None else base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity1Choice, False)

	@MinNmnlQty.deleter
	def MinNmnlQty(self):
		del self._MinNmnlQty
		self._MinNmnlQty = base_types.UninitialisedField(self, 'MinNmnlQty', FinancialInstrumentQuantity1Choice, False)

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
	def NxtFctrDt(self):
		return self._NxtFctrDt

	@NxtFctrDt.setter
	def NxtFctrDt(self, value):
		self._NxtFctrDt = value if value is not None else base_types.UninitialisedField(self, 'NxtFctrDt', ISODate, False)

	@NxtFctrDt.deleter
	def NxtFctrDt(self):
		del self._NxtFctrDt
		self._NxtFctrDt = base_types.UninitialisedField(self, 'NxtFctrDt', ISODate, False)

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
	def OddCpnInd(self):
		return self._OddCpnInd

	@OddCpnInd.setter
	def OddCpnInd(self, value):
		self._OddCpnInd = value if value is not None else base_types.UninitialisedField(self, 'OddCpnInd', YesNoIndicator, False)

	@OddCpnInd.deleter
	def OddCpnInd(self):
		del self._OddCpnInd
		self._OddCpnInd = base_types.UninitialisedField(self, 'OddCpnInd', YesNoIndicator, False)

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnStyle', OptionStyle10Choice, False)

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = base_types.UninitialisedField(self, 'OptnStyle', OptionStyle10Choice, False)

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
	def PctgOfDebtClms(self):
		return self._PctgOfDebtClms

	@PctgOfDebtClms.setter
	def PctgOfDebtClms(self, value):
		self._PctgOfDebtClms = value if value is not None else base_types.UninitialisedField(self, 'PctgOfDebtClms', PercentageRate, False)

	@PctgOfDebtClms.deleter
	def PctgOfDebtClms(self):
		del self._PctgOfDebtClms
		self._PctgOfDebtClms = base_types.UninitialisedField(self, 'PctgOfDebtClms', PercentageRate, False)

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
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if value is not None else base_types.UninitialisedField(self, 'Ratg', Rating1, False)

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = base_types.UninitialisedField(self, 'Ratg', Rating1, False)

	@property
	def RedYldImpct(self):
		return self._RedYldImpct

	@RedYldImpct.setter
	def RedYldImpct(self, value):
		self._RedYldImpct = value if value is not None else base_types.UninitialisedField(self, 'RedYldImpct', YesNoIndicator, False)

	@RedYldImpct.deleter
	def RedYldImpct(self):
		del self._RedYldImpct
		self._RedYldImpct = base_types.UninitialisedField(self, 'RedYldImpct', YesNoIndicator, False)

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
		self._SbcptPric = value if value is not None else base_types.UninitialisedField(self, 'SbcptPric', Price14, False)

	@SbcptPric.deleter
	def SbcptPric(self):
		del self._SbcptPric
		self._SbcptPric = base_types.UninitialisedField(self, 'SbcptPric', Price14, False)

	@property
	def TaxblIncmPerShr(self):
		return self._TaxblIncmPerShr

	@TaxblIncmPerShr.setter
	def TaxblIncmPerShr(self, value):
		self._TaxblIncmPerShr = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerShr', Price14, False)

	@TaxblIncmPerShr.deleter
	def TaxblIncmPerShr(self):
		del self._TaxblIncmPerShr
		self._TaxblIncmPerShr = base_types.UninitialisedField(self, 'TaxblIncmPerShr', Price14, False)

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
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if value is not None else base_types.UninitialisedField(self, 'VrsnNb', Number1Choice, False)

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = base_types.UninitialisedField(self, 'VrsnNb', Number1Choice, False)

	@property
	def WarrtAttchdOnDlvry(self):
		return self._WarrtAttchdOnDlvry

	@WarrtAttchdOnDlvry.setter
	def WarrtAttchdOnDlvry(self, value):
		self._WarrtAttchdOnDlvry = value if value is not None else base_types.UninitialisedField(self, 'WarrtAttchdOnDlvry', YesNoIndicator, False)

	@WarrtAttchdOnDlvry.deleter
	def WarrtAttchdOnDlvry(self):
		del self._WarrtAttchdOnDlvry
		self._WarrtAttchdOnDlvry = base_types.UninitialisedField(self, 'WarrtAttchdOnDlvry', YesNoIndicator, False)

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
	def YldVar(self):
		return self._YldVar

	@YldVar.setter
	def YldVar(self, value):
		self._YldVar = value if value is not None else base_types.UninitialisedField(self, 'YldVar', YesNoIndicator, False)

	@YldVar.deleter
	def YldVar(self):
		del self._YldVar
		self._YldVar = base_types.UninitialisedField(self, 'YldVar', YesNoIndicator, False)

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