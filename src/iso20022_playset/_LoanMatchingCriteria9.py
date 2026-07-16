# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareActiveOrHistoricCurrencyAndAmount3
from . import CompareAgreementType2
from . import CompareBenchmarkCurveName3
from . import CompareClearingStatus3
from . import CompareDate3
from . import CompareDateTime3
from . import CompareDecimalNumber3
from . import CompareDeliveryMethod3
from . import CompareExposureType3
from . import CompareInterestComputationMethod3
from . import CompareInterestRate1
from . import CompareMICIdentifier3
from . import CompareNumber5
from . import CompareNumber6
from . import CompareOrganisationIdentification6
from . import ComparePercentageRate3
from . import CompareRateBasis3
from . import CompareReportingLevelType3
from . import CompareSpecialCollateral3
from . import CompareTerminationOption3
from . import CompareText2
from . import CompareTrueFalseIndicator3
from . import CompareUnitOfMeasure3
from . import SecurityCommodity7Choice

class LoanMatchingCriteria9(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_BsisPtSprd", "_CCP", "_ClrDtTm", "_ClrSts", "_CollDlvryMtd", "_CtrctTp", "_DayCntBsis", "_DlvryByVal", "_EarlstCallBckDt", "_ExctnDtTm", "_FltgIntrstRatePmtFrqcyUnit", "_FltgIntrstRatePmtFrqcyVal", "_FltgIntrstRateRstFrqcyUnit", "_FltgIntrstRateRstFrqcyVal", "_FltgIntrstRateTermUnit", "_FltgIntrstRateTermVal", "_FltgIntrstRefRate", "_FltgRateAdjstmnt", "_FltgRateAdjstmntDt", "_FltgRbtRatePmtFrqcyUnit", "_FltgRbtRatePmtFrqcyVal", "_FltgRbtRateRstFrqcyUnit", "_FltgRbtRateRstFrqcyVal", "_FltgRbtRateTermUnit", "_FltgRbtRateTermVal", "_FltgRbtRefRate", "_FxdIntrstRate", "_FxdRbtRefRate", "_GnlColl", "_LnVal", "_LndgFee", "_LvlTp", "_MinNtcePrd", "_MrgnLnAttr", "_MstrAgrmtTp", "_MtrtyDt", "_OpnTerm", "_OutsdngMrgnLnAmt", "_PrncplAmtMtrtyDtAmt", "_PrncplAmtValDtAmt", "_RbtRateBsisPtSprd", "_ShrtMktValAmt", "_TermntnDt", "_TermntnOptn", "_TradgVn", "_UnitOfMeasr", "_UnqTradIdr", "_ValDt"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if value is not None else base_types.UninitialisedField(self, 'AsstTp', SecurityCommodity7Choice, False)

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = base_types.UninitialisedField(self, 'AsstTp', SecurityCommodity7Choice, False)

	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if value is not None else base_types.UninitialisedField(self, 'BsisPtSprd', CompareDecimalNumber3, False)

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = base_types.UninitialisedField(self, 'BsisPtSprd', CompareDecimalNumber3, False)

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if value is not None else base_types.UninitialisedField(self, 'CCP', CompareOrganisationIdentification6, False)

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = base_types.UninitialisedField(self, 'CCP', CompareOrganisationIdentification6, False)

	@property
	def ClrDtTm(self):
		return self._ClrDtTm

	@ClrDtTm.setter
	def ClrDtTm(self, value):
		self._ClrDtTm = value if value is not None else base_types.UninitialisedField(self, 'ClrDtTm', CompareDateTime3, False)

	@ClrDtTm.deleter
	def ClrDtTm(self):
		del self._ClrDtTm
		self._ClrDtTm = base_types.UninitialisedField(self, 'ClrDtTm', CompareDateTime3, False)

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if value is not None else base_types.UninitialisedField(self, 'ClrSts', CompareClearingStatus3, False)

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = base_types.UninitialisedField(self, 'ClrSts', CompareClearingStatus3, False)

	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'CollDlvryMtd', CompareDeliveryMethod3, False)

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = base_types.UninitialisedField(self, 'CollDlvryMtd', CompareDeliveryMethod3, False)

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctTp', CompareExposureType3, False)

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = base_types.UninitialisedField(self, 'CtrctTp', CompareExposureType3, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', CompareInterestComputationMethod3, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', CompareInterestComputationMethod3, False)

	@property
	def DlvryByVal(self):
		return self._DlvryByVal

	@DlvryByVal.setter
	def DlvryByVal(self, value):
		self._DlvryByVal = value if value is not None else base_types.UninitialisedField(self, 'DlvryByVal', CompareTrueFalseIndicator3, False)

	@DlvryByVal.deleter
	def DlvryByVal(self):
		del self._DlvryByVal
		self._DlvryByVal = base_types.UninitialisedField(self, 'DlvryByVal', CompareTrueFalseIndicator3, False)

	@property
	def EarlstCallBckDt(self):
		return self._EarlstCallBckDt

	@EarlstCallBckDt.setter
	def EarlstCallBckDt(self, value):
		self._EarlstCallBckDt = value if value is not None else base_types.UninitialisedField(self, 'EarlstCallBckDt', CompareDate3, False)

	@EarlstCallBckDt.deleter
	def EarlstCallBckDt(self):
		del self._EarlstCallBckDt
		self._EarlstCallBckDt = base_types.UninitialisedField(self, 'EarlstCallBckDt', CompareDate3, False)

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ExctnDtTm', CompareDateTime3, False)

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = base_types.UninitialisedField(self, 'ExctnDtTm', CompareDateTime3, False)

	@property
	def FltgIntrstRatePmtFrqcyUnit(self):
		return self._FltgIntrstRatePmtFrqcyUnit

	@FltgIntrstRatePmtFrqcyUnit.setter
	def FltgIntrstRatePmtFrqcyUnit(self, value):
		self._FltgIntrstRatePmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyUnit', CompareRateBasis3, False)

	@FltgIntrstRatePmtFrqcyUnit.deleter
	def FltgIntrstRatePmtFrqcyUnit(self):
		del self._FltgIntrstRatePmtFrqcyUnit
		self._FltgIntrstRatePmtFrqcyUnit = base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRatePmtFrqcyVal(self):
		return self._FltgIntrstRatePmtFrqcyVal

	@FltgIntrstRatePmtFrqcyVal.setter
	def FltgIntrstRatePmtFrqcyVal(self, value):
		self._FltgIntrstRatePmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyVal', CompareNumber5, False)

	@FltgIntrstRatePmtFrqcyVal.deleter
	def FltgIntrstRatePmtFrqcyVal(self):
		del self._FltgIntrstRatePmtFrqcyVal
		self._FltgIntrstRatePmtFrqcyVal = base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyVal', CompareNumber5, False)

	@property
	def FltgIntrstRateRstFrqcyUnit(self):
		return self._FltgIntrstRateRstFrqcyUnit

	@FltgIntrstRateRstFrqcyUnit.setter
	def FltgIntrstRateRstFrqcyUnit(self, value):
		self._FltgIntrstRateRstFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyUnit', CompareRateBasis3, False)

	@FltgIntrstRateRstFrqcyUnit.deleter
	def FltgIntrstRateRstFrqcyUnit(self):
		del self._FltgIntrstRateRstFrqcyUnit
		self._FltgIntrstRateRstFrqcyUnit = base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRateRstFrqcyVal(self):
		return self._FltgIntrstRateRstFrqcyVal

	@FltgIntrstRateRstFrqcyVal.setter
	def FltgIntrstRateRstFrqcyVal(self, value):
		self._FltgIntrstRateRstFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyVal', CompareNumber6, False)

	@FltgIntrstRateRstFrqcyVal.deleter
	def FltgIntrstRateRstFrqcyVal(self):
		del self._FltgIntrstRateRstFrqcyVal
		self._FltgIntrstRateRstFrqcyVal = base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyVal', CompareNumber6, False)

	@property
	def FltgIntrstRateTermUnit(self):
		return self._FltgIntrstRateTermUnit

	@FltgIntrstRateTermUnit.setter
	def FltgIntrstRateTermUnit(self, value):
		self._FltgIntrstRateTermUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateTermUnit', CompareRateBasis3, False)

	@FltgIntrstRateTermUnit.deleter
	def FltgIntrstRateTermUnit(self):
		del self._FltgIntrstRateTermUnit
		self._FltgIntrstRateTermUnit = base_types.UninitialisedField(self, 'FltgIntrstRateTermUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRateTermVal(self):
		return self._FltgIntrstRateTermVal

	@FltgIntrstRateTermVal.setter
	def FltgIntrstRateTermVal(self, value):
		self._FltgIntrstRateTermVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateTermVal', CompareNumber5, False)

	@FltgIntrstRateTermVal.deleter
	def FltgIntrstRateTermVal(self):
		del self._FltgIntrstRateTermVal
		self._FltgIntrstRateTermVal = base_types.UninitialisedField(self, 'FltgIntrstRateTermVal', CompareNumber5, False)

	@property
	def FltgIntrstRefRate(self):
		return self._FltgIntrstRefRate

	@FltgIntrstRefRate.setter
	def FltgIntrstRefRate(self, value):
		self._FltgIntrstRefRate = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRefRate', CompareBenchmarkCurveName3, False)

	@FltgIntrstRefRate.deleter
	def FltgIntrstRefRate(self):
		del self._FltgIntrstRefRate
		self._FltgIntrstRefRate = base_types.UninitialisedField(self, 'FltgIntrstRefRate', CompareBenchmarkCurveName3, False)

	@property
	def FltgRateAdjstmnt(self):
		return self._FltgRateAdjstmnt

	@FltgRateAdjstmnt.setter
	def FltgRateAdjstmnt(self, value):
		self._FltgRateAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'FltgRateAdjstmnt', ComparePercentageRate3, True)

	@FltgRateAdjstmnt.deleter
	def FltgRateAdjstmnt(self):
		del self._FltgRateAdjstmnt
		self._FltgRateAdjstmnt = base_types.UninitialisedField(self, 'FltgRateAdjstmnt', ComparePercentageRate3, True)

	@property
	def FltgRateAdjstmntDt(self):
		return self._FltgRateAdjstmntDt

	@FltgRateAdjstmntDt.setter
	def FltgRateAdjstmntDt(self, value):
		self._FltgRateAdjstmntDt = value if value is not None else base_types.UninitialisedField(self, 'FltgRateAdjstmntDt', CompareDate3, True)

	@FltgRateAdjstmntDt.deleter
	def FltgRateAdjstmntDt(self):
		del self._FltgRateAdjstmntDt
		self._FltgRateAdjstmntDt = base_types.UninitialisedField(self, 'FltgRateAdjstmntDt', CompareDate3, True)

	@property
	def FltgRbtRatePmtFrqcyUnit(self):
		return self._FltgRbtRatePmtFrqcyUnit

	@FltgRbtRatePmtFrqcyUnit.setter
	def FltgRbtRatePmtFrqcyUnit(self, value):
		self._FltgRbtRatePmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRatePmtFrqcyUnit', CompareRateBasis3, False)

	@FltgRbtRatePmtFrqcyUnit.deleter
	def FltgRbtRatePmtFrqcyUnit(self):
		del self._FltgRbtRatePmtFrqcyUnit
		self._FltgRbtRatePmtFrqcyUnit = base_types.UninitialisedField(self, 'FltgRbtRatePmtFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgRbtRatePmtFrqcyVal(self):
		return self._FltgRbtRatePmtFrqcyVal

	@FltgRbtRatePmtFrqcyVal.setter
	def FltgRbtRatePmtFrqcyVal(self, value):
		self._FltgRbtRatePmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRatePmtFrqcyVal', CompareNumber6, False)

	@FltgRbtRatePmtFrqcyVal.deleter
	def FltgRbtRatePmtFrqcyVal(self):
		del self._FltgRbtRatePmtFrqcyVal
		self._FltgRbtRatePmtFrqcyVal = base_types.UninitialisedField(self, 'FltgRbtRatePmtFrqcyVal', CompareNumber6, False)

	@property
	def FltgRbtRateRstFrqcyUnit(self):
		return self._FltgRbtRateRstFrqcyUnit

	@FltgRbtRateRstFrqcyUnit.setter
	def FltgRbtRateRstFrqcyUnit(self, value):
		self._FltgRbtRateRstFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRateRstFrqcyUnit', CompareRateBasis3, False)

	@FltgRbtRateRstFrqcyUnit.deleter
	def FltgRbtRateRstFrqcyUnit(self):
		del self._FltgRbtRateRstFrqcyUnit
		self._FltgRbtRateRstFrqcyUnit = base_types.UninitialisedField(self, 'FltgRbtRateRstFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgRbtRateRstFrqcyVal(self):
		return self._FltgRbtRateRstFrqcyVal

	@FltgRbtRateRstFrqcyVal.setter
	def FltgRbtRateRstFrqcyVal(self, value):
		self._FltgRbtRateRstFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRateRstFrqcyVal', CompareNumber6, False)

	@FltgRbtRateRstFrqcyVal.deleter
	def FltgRbtRateRstFrqcyVal(self):
		del self._FltgRbtRateRstFrqcyVal
		self._FltgRbtRateRstFrqcyVal = base_types.UninitialisedField(self, 'FltgRbtRateRstFrqcyVal', CompareNumber6, False)

	@property
	def FltgRbtRateTermUnit(self):
		return self._FltgRbtRateTermUnit

	@FltgRbtRateTermUnit.setter
	def FltgRbtRateTermUnit(self, value):
		self._FltgRbtRateTermUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRateTermUnit', CompareRateBasis3, False)

	@FltgRbtRateTermUnit.deleter
	def FltgRbtRateTermUnit(self):
		del self._FltgRbtRateTermUnit
		self._FltgRbtRateTermUnit = base_types.UninitialisedField(self, 'FltgRbtRateTermUnit', CompareRateBasis3, False)

	@property
	def FltgRbtRateTermVal(self):
		return self._FltgRbtRateTermVal

	@FltgRbtRateTermVal.setter
	def FltgRbtRateTermVal(self, value):
		self._FltgRbtRateTermVal = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRateTermVal', CompareNumber6, False)

	@FltgRbtRateTermVal.deleter
	def FltgRbtRateTermVal(self):
		del self._FltgRbtRateTermVal
		self._FltgRbtRateTermVal = base_types.UninitialisedField(self, 'FltgRbtRateTermVal', CompareNumber6, False)

	@property
	def FltgRbtRefRate(self):
		return self._FltgRbtRefRate

	@FltgRbtRefRate.setter
	def FltgRbtRefRate(self, value):
		self._FltgRbtRefRate = value if value is not None else base_types.UninitialisedField(self, 'FltgRbtRefRate', CompareBenchmarkCurveName3, False)

	@FltgRbtRefRate.deleter
	def FltgRbtRefRate(self):
		del self._FltgRbtRefRate
		self._FltgRbtRefRate = base_types.UninitialisedField(self, 'FltgRbtRefRate', CompareBenchmarkCurveName3, False)

	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'FxdIntrstRate', ComparePercentageRate3, False)

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = base_types.UninitialisedField(self, 'FxdIntrstRate', ComparePercentageRate3, False)

	@property
	def FxdRbtRefRate(self):
		return self._FxdRbtRefRate

	@FxdRbtRefRate.setter
	def FxdRbtRefRate(self, value):
		self._FxdRbtRefRate = value if value is not None else base_types.UninitialisedField(self, 'FxdRbtRefRate', ComparePercentageRate3, False)

	@FxdRbtRefRate.deleter
	def FxdRbtRefRate(self):
		del self._FxdRbtRefRate
		self._FxdRbtRefRate = base_types.UninitialisedField(self, 'FxdRbtRefRate', ComparePercentageRate3, False)

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if value is not None else base_types.UninitialisedField(self, 'GnlColl', CompareSpecialCollateral3, False)

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = base_types.UninitialisedField(self, 'GnlColl', CompareSpecialCollateral3, False)

	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if value is not None else base_types.UninitialisedField(self, 'LnVal', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = base_types.UninitialisedField(self, 'LnVal', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if value is not None else base_types.UninitialisedField(self, 'LndgFee', ComparePercentageRate3, False)

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = base_types.UninitialisedField(self, 'LndgFee', ComparePercentageRate3, False)

	@property
	def LvlTp(self):
		return self._LvlTp

	@LvlTp.setter
	def LvlTp(self, value):
		self._LvlTp = value if value is not None else base_types.UninitialisedField(self, 'LvlTp', CompareReportingLevelType3, False)

	@LvlTp.deleter
	def LvlTp(self):
		del self._LvlTp
		self._LvlTp = base_types.UninitialisedField(self, 'LvlTp', CompareReportingLevelType3, False)

	@property
	def MinNtcePrd(self):
		return self._MinNtcePrd

	@MinNtcePrd.setter
	def MinNtcePrd(self, value):
		self._MinNtcePrd = value if value is not None else base_types.UninitialisedField(self, 'MinNtcePrd', CompareNumber5, False)

	@MinNtcePrd.deleter
	def MinNtcePrd(self):
		del self._MinNtcePrd
		self._MinNtcePrd = base_types.UninitialisedField(self, 'MinNtcePrd', CompareNumber5, False)

	@property
	def MrgnLnAttr(self):
		return self._MrgnLnAttr

	@MrgnLnAttr.setter
	def MrgnLnAttr(self, value):
		self._MrgnLnAttr = value if value is not None else base_types.UninitialisedField(self, 'MrgnLnAttr', CompareInterestRate1, True)

	@MrgnLnAttr.deleter
	def MrgnLnAttr(self):
		del self._MrgnLnAttr
		self._MrgnLnAttr = base_types.UninitialisedField(self, 'MrgnLnAttr', CompareInterestRate1, True)

	@property
	def MstrAgrmtTp(self):
		return self._MstrAgrmtTp

	@MstrAgrmtTp.setter
	def MstrAgrmtTp(self, value):
		self._MstrAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmtTp', CompareAgreementType2, False)

	@MstrAgrmtTp.deleter
	def MstrAgrmtTp(self):
		del self._MstrAgrmtTp
		self._MstrAgrmtTp = base_types.UninitialisedField(self, 'MstrAgrmtTp', CompareAgreementType2, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', CompareDate3, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', CompareDate3, False)

	@property
	def OpnTerm(self):
		return self._OpnTerm

	@OpnTerm.setter
	def OpnTerm(self, value):
		self._OpnTerm = value if value is not None else base_types.UninitialisedField(self, 'OpnTerm', CompareTrueFalseIndicator3, False)

	@OpnTerm.deleter
	def OpnTerm(self):
		del self._OpnTerm
		self._OpnTerm = base_types.UninitialisedField(self, 'OpnTerm', CompareTrueFalseIndicator3, False)

	@property
	def OutsdngMrgnLnAmt(self):
		return self._OutsdngMrgnLnAmt

	@OutsdngMrgnLnAmt.setter
	def OutsdngMrgnLnAmt(self, value):
		self._OutsdngMrgnLnAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngMrgnLnAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@OutsdngMrgnLnAmt.deleter
	def OutsdngMrgnLnAmt(self):
		del self._OutsdngMrgnLnAmt
		self._OutsdngMrgnLnAmt = base_types.UninitialisedField(self, 'OutsdngMrgnLnAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@property
	def PrncplAmtMtrtyDtAmt(self):
		return self._PrncplAmtMtrtyDtAmt

	@PrncplAmtMtrtyDtAmt.setter
	def PrncplAmtMtrtyDtAmt(self, value):
		self._PrncplAmtMtrtyDtAmt = value if value is not None else base_types.UninitialisedField(self, 'PrncplAmtMtrtyDtAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@PrncplAmtMtrtyDtAmt.deleter
	def PrncplAmtMtrtyDtAmt(self):
		del self._PrncplAmtMtrtyDtAmt
		self._PrncplAmtMtrtyDtAmt = base_types.UninitialisedField(self, 'PrncplAmtMtrtyDtAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@property
	def PrncplAmtValDtAmt(self):
		return self._PrncplAmtValDtAmt

	@PrncplAmtValDtAmt.setter
	def PrncplAmtValDtAmt(self, value):
		self._PrncplAmtValDtAmt = value if value is not None else base_types.UninitialisedField(self, 'PrncplAmtValDtAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@PrncplAmtValDtAmt.deleter
	def PrncplAmtValDtAmt(self):
		del self._PrncplAmtValDtAmt
		self._PrncplAmtValDtAmt = base_types.UninitialisedField(self, 'PrncplAmtValDtAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@property
	def RbtRateBsisPtSprd(self):
		return self._RbtRateBsisPtSprd

	@RbtRateBsisPtSprd.setter
	def RbtRateBsisPtSprd(self, value):
		self._RbtRateBsisPtSprd = value if value is not None else base_types.UninitialisedField(self, 'RbtRateBsisPtSprd', CompareDecimalNumber3, False)

	@RbtRateBsisPtSprd.deleter
	def RbtRateBsisPtSprd(self):
		del self._RbtRateBsisPtSprd
		self._RbtRateBsisPtSprd = base_types.UninitialisedField(self, 'RbtRateBsisPtSprd', CompareDecimalNumber3, False)

	@property
	def ShrtMktValAmt(self):
		return self._ShrtMktValAmt

	@ShrtMktValAmt.setter
	def ShrtMktValAmt(self, value):
		self._ShrtMktValAmt = value if value is not None else base_types.UninitialisedField(self, 'ShrtMktValAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@ShrtMktValAmt.deleter
	def ShrtMktValAmt(self):
		del self._ShrtMktValAmt
		self._ShrtMktValAmt = base_types.UninitialisedField(self, 'ShrtMktValAmt', CompareActiveOrHistoricCurrencyAndAmount3, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', CompareDate3, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', CompareDate3, False)

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if value is not None else base_types.UninitialisedField(self, 'TermntnOptn', CompareTerminationOption3, False)

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = base_types.UninitialisedField(self, 'TermntnOptn', CompareTerminationOption3, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', CompareMICIdentifier3, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', CompareMICIdentifier3, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', CompareUnitOfMeasure3, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', CompareUnitOfMeasure3, False)

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTradIdr', CompareText2, False)

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = base_types.UninitialisedField(self, 'UnqTradIdr', CompareText2, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', CompareDate3, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', CompareDate3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=SecurityCommodity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=CompareOrganisationIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=CompareClearingStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDlvryMtd', type=CompareDeliveryMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=CompareExposureType3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=CompareInterestComputationMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryByVal', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstCallBckDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateAdjstmnt', type=ComparePercentageRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FltgRateAdjstmntDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FltgRbtRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRatePmtFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRateTermVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRbtRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdIntrstRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdRbtRefRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=CompareSpecialCollateral3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnVal', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgFee', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LvlTp', type=CompareReportingLevelType3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNtcePrd', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAttr', type=CompareInterestRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrAgrmtTp', type=CompareAgreementType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTerm', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngMrgnLnAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtMtrtyDtAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtValDtAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RbtRateBsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtMktValAmt', type=CompareActiveOrHistoricCurrencyAndAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=CompareTerminationOption3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=CompareMICIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=CompareUnitOfMeasure3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=CompareText2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
	))