import base_types
import CompareExposureType3
import ComparePercentageRate3
import CompareText2
import CompareUnitOfMeasure3
import CompareNumber5
import CompareDate3
import CompareDecimalNumber3
import CompareRateBasis3
import CompareNumber6
import CompareOrganisationIdentification6
import CompareTerminationOption3
import CompareMICIdentifier3
import CompareDeliveryMethod3
import CompareReportingLevelType3
import CompareTrueFalseIndicator3
import CompareBenchmarkCurveName3
import CompareInterestRate1
import SecurityCommodity7Choice
import CompareAgreementType2
import CompareClearingStatus3
import CompareDateTime3
import CompareInterestComputationMethod3
import CompareSpecialCollateral3
import CompareActiveOrHistoricCurrencyAndAmount3

class LoanMatchingCriteria9(base_types._BaseFieldType):

	__slots__ = ["_MinNtcePrd", "_TermntnOptn", "_FltgIntrstRefRate", "_PrncplAmtValDtAmt", "_FltgRbtRateTermUnit", "_LvlTp", "_FltgRbtRateTermVal", "_FltgIntrstRateTermUnit", "_FltgIntrstRatePmtFrqcyUnit", "_FltgIntrstRateRstFrqcyVal", "_FltgRbtRateRstFrqcyVal", "_CCP", "_DayCntBsis", "_PrncplAmtMtrtyDtAmt", "_UnqTradIdr", "_EarlstCallBckDt", "_ExctnDtTm", "_ClrSts", "_MrgnLnAttr", "_FltgRbtRefRate", "_LndgFee", "_BsisPtSprd", "_FltgRbtRatePmtFrqcyVal", "_FltgRbtRatePmtFrqcyUnit", "_FltgRateAdjstmntDt", "_GnlColl", "_UnitOfMeasr", "_FxdRbtRefRate", "_FltgRbtRateRstFrqcyUnit", "_MstrAgrmtTp", "_ValDt", "_MtrtyDt", "_CtrctTp", "_AsstTp", "_ShrtMktValAmt", "_DlvryByVal", "_FltgRateAdjstmnt", "_OutsdngMrgnLnAmt", "_FltgIntrstRateRstFrqcyUnit", "_TermntnDt", "_RbtRateBsisPtSprd", "_LnVal", "_OpnTerm", "_FltgIntrstRateTermVal", "_TradgVn", "_FxdIntrstRate", "_FltgIntrstRatePmtFrqcyVal", "_CollDlvryMtd", "_ClrDtTm"]
	@property
	def MinNtcePrd(self):
		return self._MinNtcePrd

	@MinNtcePrd.setter
	def MinNtcePrd(self, value):
		self._MinNtcePrd = value if type(value) != auto else self.make_default("MinNtcePrd")

	@MinNtcePrd.deleter
	def MinNtcePrd(self):
		del self._MinNtcePrd
		self._MinNtcePrd = None

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if type(value) != auto else self.make_default("TermntnOptn")

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = None

	@property
	def FltgIntrstRefRate(self):
		return self._FltgIntrstRefRate

	@FltgIntrstRefRate.setter
	def FltgIntrstRefRate(self, value):
		self._FltgIntrstRefRate = value if type(value) != auto else self.make_default("FltgIntrstRefRate")

	@FltgIntrstRefRate.deleter
	def FltgIntrstRefRate(self):
		del self._FltgIntrstRefRate
		self._FltgIntrstRefRate = None

	@property
	def PrncplAmtValDtAmt(self):
		return self._PrncplAmtValDtAmt

	@PrncplAmtValDtAmt.setter
	def PrncplAmtValDtAmt(self, value):
		self._PrncplAmtValDtAmt = value if type(value) != auto else self.make_default("PrncplAmtValDtAmt")

	@PrncplAmtValDtAmt.deleter
	def PrncplAmtValDtAmt(self):
		del self._PrncplAmtValDtAmt
		self._PrncplAmtValDtAmt = None

	@property
	def FltgRbtRateTermUnit(self):
		return self._FltgRbtRateTermUnit

	@FltgRbtRateTermUnit.setter
	def FltgRbtRateTermUnit(self, value):
		self._FltgRbtRateTermUnit = value if type(value) != auto else self.make_default("FltgRbtRateTermUnit")

	@FltgRbtRateTermUnit.deleter
	def FltgRbtRateTermUnit(self):
		del self._FltgRbtRateTermUnit
		self._FltgRbtRateTermUnit = None

	@property
	def LvlTp(self):
		return self._LvlTp

	@LvlTp.setter
	def LvlTp(self, value):
		self._LvlTp = value if type(value) != auto else self.make_default("LvlTp")

	@LvlTp.deleter
	def LvlTp(self):
		del self._LvlTp
		self._LvlTp = None

	@property
	def FltgRbtRateTermVal(self):
		return self._FltgRbtRateTermVal

	@FltgRbtRateTermVal.setter
	def FltgRbtRateTermVal(self, value):
		self._FltgRbtRateTermVal = value if type(value) != auto else self.make_default("FltgRbtRateTermVal")

	@FltgRbtRateTermVal.deleter
	def FltgRbtRateTermVal(self):
		del self._FltgRbtRateTermVal
		self._FltgRbtRateTermVal = None

	@property
	def FltgIntrstRateTermUnit(self):
		return self._FltgIntrstRateTermUnit

	@FltgIntrstRateTermUnit.setter
	def FltgIntrstRateTermUnit(self, value):
		self._FltgIntrstRateTermUnit = value if type(value) != auto else self.make_default("FltgIntrstRateTermUnit")

	@FltgIntrstRateTermUnit.deleter
	def FltgIntrstRateTermUnit(self):
		del self._FltgIntrstRateTermUnit
		self._FltgIntrstRateTermUnit = None

	@property
	def FltgIntrstRatePmtFrqcyUnit(self):
		return self._FltgIntrstRatePmtFrqcyUnit

	@FltgIntrstRatePmtFrqcyUnit.setter
	def FltgIntrstRatePmtFrqcyUnit(self, value):
		self._FltgIntrstRatePmtFrqcyUnit = value if type(value) != auto else self.make_default("FltgIntrstRatePmtFrqcyUnit")

	@FltgIntrstRatePmtFrqcyUnit.deleter
	def FltgIntrstRatePmtFrqcyUnit(self):
		del self._FltgIntrstRatePmtFrqcyUnit
		self._FltgIntrstRatePmtFrqcyUnit = None

	@property
	def FltgIntrstRateRstFrqcyVal(self):
		return self._FltgIntrstRateRstFrqcyVal

	@FltgIntrstRateRstFrqcyVal.setter
	def FltgIntrstRateRstFrqcyVal(self, value):
		self._FltgIntrstRateRstFrqcyVal = value if type(value) != auto else self.make_default("FltgIntrstRateRstFrqcyVal")

	@FltgIntrstRateRstFrqcyVal.deleter
	def FltgIntrstRateRstFrqcyVal(self):
		del self._FltgIntrstRateRstFrqcyVal
		self._FltgIntrstRateRstFrqcyVal = None

	@property
	def FltgRbtRateRstFrqcyVal(self):
		return self._FltgRbtRateRstFrqcyVal

	@FltgRbtRateRstFrqcyVal.setter
	def FltgRbtRateRstFrqcyVal(self, value):
		self._FltgRbtRateRstFrqcyVal = value if type(value) != auto else self.make_default("FltgRbtRateRstFrqcyVal")

	@FltgRbtRateRstFrqcyVal.deleter
	def FltgRbtRateRstFrqcyVal(self):
		del self._FltgRbtRateRstFrqcyVal
		self._FltgRbtRateRstFrqcyVal = None

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if type(value) != auto else self.make_default("CCP")

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def PrncplAmtMtrtyDtAmt(self):
		return self._PrncplAmtMtrtyDtAmt

	@PrncplAmtMtrtyDtAmt.setter
	def PrncplAmtMtrtyDtAmt(self, value):
		self._PrncplAmtMtrtyDtAmt = value if type(value) != auto else self.make_default("PrncplAmtMtrtyDtAmt")

	@PrncplAmtMtrtyDtAmt.deleter
	def PrncplAmtMtrtyDtAmt(self):
		del self._PrncplAmtMtrtyDtAmt
		self._PrncplAmtMtrtyDtAmt = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def EarlstCallBckDt(self):
		return self._EarlstCallBckDt

	@EarlstCallBckDt.setter
	def EarlstCallBckDt(self, value):
		self._EarlstCallBckDt = value if type(value) != auto else self.make_default("EarlstCallBckDt")

	@EarlstCallBckDt.deleter
	def EarlstCallBckDt(self):
		del self._EarlstCallBckDt
		self._EarlstCallBckDt = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if type(value) != auto else self.make_default("ClrSts")

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = None

	@property
	def MrgnLnAttr(self):
		return self._MrgnLnAttr

	@MrgnLnAttr.setter
	def MrgnLnAttr(self, value):
		self._MrgnLnAttr = value if type(value) != auto else self.make_default("MrgnLnAttr")

	@MrgnLnAttr.deleter
	def MrgnLnAttr(self):
		del self._MrgnLnAttr
		self._MrgnLnAttr = None

	@property
	def FltgRbtRefRate(self):
		return self._FltgRbtRefRate

	@FltgRbtRefRate.setter
	def FltgRbtRefRate(self, value):
		self._FltgRbtRefRate = value if type(value) != auto else self.make_default("FltgRbtRefRate")

	@FltgRbtRefRate.deleter
	def FltgRbtRefRate(self):
		del self._FltgRbtRefRate
		self._FltgRbtRefRate = None

	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if type(value) != auto else self.make_default("LndgFee")

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = None

	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if type(value) != auto else self.make_default("BsisPtSprd")

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = None

	@property
	def FltgRbtRatePmtFrqcyVal(self):
		return self._FltgRbtRatePmtFrqcyVal

	@FltgRbtRatePmtFrqcyVal.setter
	def FltgRbtRatePmtFrqcyVal(self, value):
		self._FltgRbtRatePmtFrqcyVal = value if type(value) != auto else self.make_default("FltgRbtRatePmtFrqcyVal")

	@FltgRbtRatePmtFrqcyVal.deleter
	def FltgRbtRatePmtFrqcyVal(self):
		del self._FltgRbtRatePmtFrqcyVal
		self._FltgRbtRatePmtFrqcyVal = None

	@property
	def FltgRbtRatePmtFrqcyUnit(self):
		return self._FltgRbtRatePmtFrqcyUnit

	@FltgRbtRatePmtFrqcyUnit.setter
	def FltgRbtRatePmtFrqcyUnit(self, value):
		self._FltgRbtRatePmtFrqcyUnit = value if type(value) != auto else self.make_default("FltgRbtRatePmtFrqcyUnit")

	@FltgRbtRatePmtFrqcyUnit.deleter
	def FltgRbtRatePmtFrqcyUnit(self):
		del self._FltgRbtRatePmtFrqcyUnit
		self._FltgRbtRatePmtFrqcyUnit = None

	@property
	def FltgRateAdjstmntDt(self):
		return self._FltgRateAdjstmntDt

	@FltgRateAdjstmntDt.setter
	def FltgRateAdjstmntDt(self, value):
		self._FltgRateAdjstmntDt = value if type(value) != auto else self.make_default("FltgRateAdjstmntDt")

	@FltgRateAdjstmntDt.deleter
	def FltgRateAdjstmntDt(self):
		del self._FltgRateAdjstmntDt
		self._FltgRateAdjstmntDt = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def FxdRbtRefRate(self):
		return self._FxdRbtRefRate

	@FxdRbtRefRate.setter
	def FxdRbtRefRate(self, value):
		self._FxdRbtRefRate = value if type(value) != auto else self.make_default("FxdRbtRefRate")

	@FxdRbtRefRate.deleter
	def FxdRbtRefRate(self):
		del self._FxdRbtRefRate
		self._FxdRbtRefRate = None

	@property
	def FltgRbtRateRstFrqcyUnit(self):
		return self._FltgRbtRateRstFrqcyUnit

	@FltgRbtRateRstFrqcyUnit.setter
	def FltgRbtRateRstFrqcyUnit(self, value):
		self._FltgRbtRateRstFrqcyUnit = value if type(value) != auto else self.make_default("FltgRbtRateRstFrqcyUnit")

	@FltgRbtRateRstFrqcyUnit.deleter
	def FltgRbtRateRstFrqcyUnit(self):
		del self._FltgRbtRateRstFrqcyUnit
		self._FltgRbtRateRstFrqcyUnit = None

	@property
	def MstrAgrmtTp(self):
		return self._MstrAgrmtTp

	@MstrAgrmtTp.setter
	def MstrAgrmtTp(self, value):
		self._MstrAgrmtTp = value if type(value) != auto else self.make_default("MstrAgrmtTp")

	@MstrAgrmtTp.deleter
	def MstrAgrmtTp(self):
		del self._MstrAgrmtTp
		self._MstrAgrmtTp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if type(value) != auto else self.make_default("CtrctTp")

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = None

	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	@property
	def ShrtMktValAmt(self):
		return self._ShrtMktValAmt

	@ShrtMktValAmt.setter
	def ShrtMktValAmt(self, value):
		self._ShrtMktValAmt = value if type(value) != auto else self.make_default("ShrtMktValAmt")

	@ShrtMktValAmt.deleter
	def ShrtMktValAmt(self):
		del self._ShrtMktValAmt
		self._ShrtMktValAmt = None

	@property
	def DlvryByVal(self):
		return self._DlvryByVal

	@DlvryByVal.setter
	def DlvryByVal(self, value):
		self._DlvryByVal = value if type(value) != auto else self.make_default("DlvryByVal")

	@DlvryByVal.deleter
	def DlvryByVal(self):
		del self._DlvryByVal
		self._DlvryByVal = None

	@property
	def FltgRateAdjstmnt(self):
		return self._FltgRateAdjstmnt

	@FltgRateAdjstmnt.setter
	def FltgRateAdjstmnt(self, value):
		self._FltgRateAdjstmnt = value if type(value) != auto else self.make_default("FltgRateAdjstmnt")

	@FltgRateAdjstmnt.deleter
	def FltgRateAdjstmnt(self):
		del self._FltgRateAdjstmnt
		self._FltgRateAdjstmnt = None

	@property
	def OutsdngMrgnLnAmt(self):
		return self._OutsdngMrgnLnAmt

	@OutsdngMrgnLnAmt.setter
	def OutsdngMrgnLnAmt(self, value):
		self._OutsdngMrgnLnAmt = value if type(value) != auto else self.make_default("OutsdngMrgnLnAmt")

	@OutsdngMrgnLnAmt.deleter
	def OutsdngMrgnLnAmt(self):
		del self._OutsdngMrgnLnAmt
		self._OutsdngMrgnLnAmt = None

	@property
	def FltgIntrstRateRstFrqcyUnit(self):
		return self._FltgIntrstRateRstFrqcyUnit

	@FltgIntrstRateRstFrqcyUnit.setter
	def FltgIntrstRateRstFrqcyUnit(self, value):
		self._FltgIntrstRateRstFrqcyUnit = value if type(value) != auto else self.make_default("FltgIntrstRateRstFrqcyUnit")

	@FltgIntrstRateRstFrqcyUnit.deleter
	def FltgIntrstRateRstFrqcyUnit(self):
		del self._FltgIntrstRateRstFrqcyUnit
		self._FltgIntrstRateRstFrqcyUnit = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def RbtRateBsisPtSprd(self):
		return self._RbtRateBsisPtSprd

	@RbtRateBsisPtSprd.setter
	def RbtRateBsisPtSprd(self, value):
		self._RbtRateBsisPtSprd = value if type(value) != auto else self.make_default("RbtRateBsisPtSprd")

	@RbtRateBsisPtSprd.deleter
	def RbtRateBsisPtSprd(self):
		del self._RbtRateBsisPtSprd
		self._RbtRateBsisPtSprd = None

	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if type(value) != auto else self.make_default("LnVal")

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = None

	@property
	def OpnTerm(self):
		return self._OpnTerm

	@OpnTerm.setter
	def OpnTerm(self, value):
		self._OpnTerm = value if type(value) != auto else self.make_default("OpnTerm")

	@OpnTerm.deleter
	def OpnTerm(self):
		del self._OpnTerm
		self._OpnTerm = None

	@property
	def FltgIntrstRateTermVal(self):
		return self._FltgIntrstRateTermVal

	@FltgIntrstRateTermVal.setter
	def FltgIntrstRateTermVal(self, value):
		self._FltgIntrstRateTermVal = value if type(value) != auto else self.make_default("FltgIntrstRateTermVal")

	@FltgIntrstRateTermVal.deleter
	def FltgIntrstRateTermVal(self):
		del self._FltgIntrstRateTermVal
		self._FltgIntrstRateTermVal = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if type(value) != auto else self.make_default("FxdIntrstRate")

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = None

	@property
	def FltgIntrstRatePmtFrqcyVal(self):
		return self._FltgIntrstRatePmtFrqcyVal

	@FltgIntrstRatePmtFrqcyVal.setter
	def FltgIntrstRatePmtFrqcyVal(self, value):
		self._FltgIntrstRatePmtFrqcyVal = value if type(value) != auto else self.make_default("FltgIntrstRatePmtFrqcyVal")

	@FltgIntrstRatePmtFrqcyVal.deleter
	def FltgIntrstRatePmtFrqcyVal(self):
		del self._FltgIntrstRatePmtFrqcyVal
		self._FltgIntrstRatePmtFrqcyVal = None

	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if type(value) != auto else self.make_default("CollDlvryMtd")

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = None

	@property
	def ClrDtTm(self):
		return self._ClrDtTm

	@ClrDtTm.setter
	def ClrDtTm(self, value):
		self._ClrDtTm = value if type(value) != auto else self.make_default("ClrDtTm")

	@ClrDtTm.deleter
	def ClrDtTm(self):
		del self._ClrDtTm
		self._ClrDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinNtcePrd', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=CompareTerminationOption3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtValDtAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LvlTp', type=CompareReportingLevelType3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateTermVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=CompareInterestComputationMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtMtrtyDtAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=CompareText2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstCallBckDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=CompareClearingStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAttr', type=CompareInterestRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FltgRbtRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgFee', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRatePmtFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateAdjstmntDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GnlColl', type=CompareSpecialCollateral3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=CompareUnitOfMeasure3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdRbtRefRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtTp', type=CompareAgreementType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=CompareExposureType3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstTp', type=SecurityCommodity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryByVal', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateAdjstmnt', type=ComparePercentageRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RbtRateBsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnVal', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTerm', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=CompareMICIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdIntrstRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDlvryMtd', type=CompareDeliveryMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
	))

