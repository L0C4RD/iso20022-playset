import base_types
import CompareOptionType1
import CompareLongFraction19DecimalNumber1
import CompareText2
import CompareTradeConfirmation2
import CompareAmountAndDirection3
import CompareFrequencyUnit1
import CompareUnitPrice7
import CompareISINIdentifier4
import CompareOtherPayment1
import CompareMICIdentifier3
import CompareDeliveryInterconnectionPoint1
import CompareTradeClearingObligation1
import CompareDerivativeEvent1
import ComparePostTradeRiskReduction2
import CompareTrueFalseIndicator3
import CompareUnitPrice8
import CompareDayCount1
import CompareTrancheIndicator1
import CompareDateTime3
import CompareUnitPrice5
import CompareCommodityAssetClass4
import CompareUnitPrice4
import CompareUniqueTransactionIdentifier2
import ComparePercentageRate3
import CompareMasterAgreementType1
import CompareEnergyLoadType1
import CompareNumber5
import CompareSeniorityType1
import CompareDate3
import CompareActiveOrHistoricCurrencyAndAmount4
import CompareBenchmarkCode1
import CompareMax50Text1
import CompareNumber7
import CompareDeliveryType1
import CompareMax350Text1
import CompareOptionStyle1
import CompareReferenceParty1
import CompareTradeClearingStatus3
import CompareEnergyDeliveryAttribute1
import CompareReportingLevelType2
import CompareExchangeRate1
import CompareExchangeRateBasis1

class TransactionMatchingCriteria7(base_types._BaseFieldType):

	__slots__ = ["_IntrstFltgRateScndLegId", "_NtnlAmtFrstLegUadjstdFctvDt", "_CcyFwdXchgRate", "_IntrstFltgRateScndLegRstFrqcyUnit", "_IntrstFxdRateScndLegPmtFrqcyUnit", "_IntrstFltgRateFrstLegSprd", "_DlvryAttr", "_IntrstFltgRateFrstLegRefPrdVal", "_IntrstFltgRateFrstLegPmtFrqcyVal", "_IntrstFltgRateScndLegRefPrdUnit", "_OptnPrmAmt", "_IntrstFltgRateScndLegDayCnt", "_CcyXchgRate", "_ExctnTmStmp", "_PrrUnqTxIdr", "_PltfmIdr", "_OptnStrkPric", "_IntrstFxdRateFrstLeg", "_IntraGrp", "_IntrstRateFxdScndLeg", "_UnqTxIdr", "_FctvDt", "_IntrstFxdRateFrstLegPmtFrqcyVal", "_IntrstFxdRateScndLegDayCnt", "_IntrstFltgRateFrstLegRstFrqcyUnit", "_NtnlAmtScndLegUadjstdFctvDt", "_IntrstFltgRateFrstLegNm", "_OptnTp", "_NtnlQtyScndLeg", "_PackgPric", "_NtnlQtyScndLegSchdlQty", "_XprtnDt", "_NtnlAmtFrstLeg", "_Lvl", "_NtnlAmtScndLegSchdlAmt", "_IntrstFltgRateFrstLegDayCnt", "_PstTradRskRdctn", "_CdtRefPty", "_TradClrSts", "_CdtVrsn", "_SttlmDt", "_OptnStrkPricSchdlUadjstdEndDt", "_TradConf", "_CdtIndxFctr", "_OptnPrmPmtDt", "_IntrstFltgRateFrstLegRstFrqcyVal", "_PackgSprd", "_NtnlAmtScndLegUadjstdEndDt", "_IntrstFltgRateFrstLegId", "_MstrAgrmtTp", "_DerivEvt", "_IntrstFltgRateScndLegNm", "_IntrstFltgRateScndLegCd", "_IntrstFltgRateScndLegSprd", "_NrgyLdTp", "_CdtSnrty", "_NrgyDlvryPtOrZone", "_IntrstFltgRateFrstLegCd", "_NtnlAmtFrstLegSchdlAmt", "_NtnlQtyFrstLegUadjstdFctvDt", "_IntrstFltgRateFrstLegPmtFrqcyUnit", "_NtnlAmtFrstLegUadjstdEndDt", "_TxSchdlPric", "_PricSchdlUadjstdFctvDt", "_EarlyTermntnDt", "_RptTrckgNb", "_DlvryTp", "_IntrstFxdRateScndLegPmtFrqcyVal", "_IntrstFltgRateScndLegPmtFrqcyUnit", "_CdtTrch", "_OptnMtrtyDtOfUndrlyg", "_NtnlQtyFrstLegUadjstdEndDt", "_IntrstFxdRateFrstLegPmtFrqcyUnit", "_OthrPmt", "_CdtSrs", "_Cmmdty", "_TxPric", "_IntrstFltgRateScndLegRefPrdVal", "_OptnExrcStyle", "_OptnStrkPricSchdlUadjstdFctvDt", "_NrgyIntrCnnctnPt", "_NtnlQtyScndLegUadjstdFctvDt", "_CcyXchgRateBsis", "_NtnlQtyFrstLeg", "_PricSchdlUadjstdEndDt", "_IntrstFltgRateScndLegRstFrqcyVal", "_NtnlQtyFrstLegSchdlQty", "_NtnlAmtScndLeg", "_MstrAgrmtVrsn", "_TradClrOblgtn", "_OptnStrkPricSchdlAmt", "_IntrstFxdRateFrstLegDayCnt", "_Dlta", "_NtnlQtyScndLegUadjstdEndDt", "_SbsqntPosUnqTxIdr", "_IntrstFltgRateFrstLegRefPrdUnit", "_IntrstFltgRateScndLegPmtFrqcyVal"]
	@property
	def IntrstFltgRateScndLegId(self):
		return self._IntrstFltgRateScndLegId

	@IntrstFltgRateScndLegId.setter
	def IntrstFltgRateScndLegId(self, value):
		self._IntrstFltgRateScndLegId = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegId")

	@IntrstFltgRateScndLegId.deleter
	def IntrstFltgRateScndLegId(self):
		del self._IntrstFltgRateScndLegId
		self._IntrstFltgRateScndLegId = None

	@property
	def NtnlAmtFrstLegUadjstdFctvDt(self):
		return self._NtnlAmtFrstLegUadjstdFctvDt

	@NtnlAmtFrstLegUadjstdFctvDt.setter
	def NtnlAmtFrstLegUadjstdFctvDt(self, value):
		self._NtnlAmtFrstLegUadjstdFctvDt = value if type(value) != auto else self.make_default("NtnlAmtFrstLegUadjstdFctvDt")

	@NtnlAmtFrstLegUadjstdFctvDt.deleter
	def NtnlAmtFrstLegUadjstdFctvDt(self):
		del self._NtnlAmtFrstLegUadjstdFctvDt
		self._NtnlAmtFrstLegUadjstdFctvDt = None

	@property
	def CcyFwdXchgRate(self):
		return self._CcyFwdXchgRate

	@CcyFwdXchgRate.setter
	def CcyFwdXchgRate(self, value):
		self._CcyFwdXchgRate = value if type(value) != auto else self.make_default("CcyFwdXchgRate")

	@CcyFwdXchgRate.deleter
	def CcyFwdXchgRate(self):
		del self._CcyFwdXchgRate
		self._CcyFwdXchgRate = None

	@property
	def IntrstFltgRateScndLegRstFrqcyUnit(self):
		return self._IntrstFltgRateScndLegRstFrqcyUnit

	@IntrstFltgRateScndLegRstFrqcyUnit.setter
	def IntrstFltgRateScndLegRstFrqcyUnit(self, value):
		self._IntrstFltgRateScndLegRstFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegRstFrqcyUnit")

	@IntrstFltgRateScndLegRstFrqcyUnit.deleter
	def IntrstFltgRateScndLegRstFrqcyUnit(self):
		del self._IntrstFltgRateScndLegRstFrqcyUnit
		self._IntrstFltgRateScndLegRstFrqcyUnit = None

	@property
	def IntrstFxdRateScndLegPmtFrqcyUnit(self):
		return self._IntrstFxdRateScndLegPmtFrqcyUnit

	@IntrstFxdRateScndLegPmtFrqcyUnit.setter
	def IntrstFxdRateScndLegPmtFrqcyUnit(self, value):
		self._IntrstFxdRateScndLegPmtFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFxdRateScndLegPmtFrqcyUnit")

	@IntrstFxdRateScndLegPmtFrqcyUnit.deleter
	def IntrstFxdRateScndLegPmtFrqcyUnit(self):
		del self._IntrstFxdRateScndLegPmtFrqcyUnit
		self._IntrstFxdRateScndLegPmtFrqcyUnit = None

	@property
	def IntrstFltgRateFrstLegSprd(self):
		return self._IntrstFltgRateFrstLegSprd

	@IntrstFltgRateFrstLegSprd.setter
	def IntrstFltgRateFrstLegSprd(self, value):
		self._IntrstFltgRateFrstLegSprd = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegSprd")

	@IntrstFltgRateFrstLegSprd.deleter
	def IntrstFltgRateFrstLegSprd(self):
		del self._IntrstFltgRateFrstLegSprd
		self._IntrstFltgRateFrstLegSprd = None

	@property
	def DlvryAttr(self):
		return self._DlvryAttr

	@DlvryAttr.setter
	def DlvryAttr(self, value):
		self._DlvryAttr = value if type(value) != auto else self.make_default("DlvryAttr")

	@DlvryAttr.deleter
	def DlvryAttr(self):
		del self._DlvryAttr
		self._DlvryAttr = None

	@property
	def IntrstFltgRateFrstLegRefPrdVal(self):
		return self._IntrstFltgRateFrstLegRefPrdVal

	@IntrstFltgRateFrstLegRefPrdVal.setter
	def IntrstFltgRateFrstLegRefPrdVal(self, value):
		self._IntrstFltgRateFrstLegRefPrdVal = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegRefPrdVal")

	@IntrstFltgRateFrstLegRefPrdVal.deleter
	def IntrstFltgRateFrstLegRefPrdVal(self):
		del self._IntrstFltgRateFrstLegRefPrdVal
		self._IntrstFltgRateFrstLegRefPrdVal = None

	@property
	def IntrstFltgRateFrstLegPmtFrqcyVal(self):
		return self._IntrstFltgRateFrstLegPmtFrqcyVal

	@IntrstFltgRateFrstLegPmtFrqcyVal.setter
	def IntrstFltgRateFrstLegPmtFrqcyVal(self, value):
		self._IntrstFltgRateFrstLegPmtFrqcyVal = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegPmtFrqcyVal")

	@IntrstFltgRateFrstLegPmtFrqcyVal.deleter
	def IntrstFltgRateFrstLegPmtFrqcyVal(self):
		del self._IntrstFltgRateFrstLegPmtFrqcyVal
		self._IntrstFltgRateFrstLegPmtFrqcyVal = None

	@property
	def IntrstFltgRateScndLegRefPrdUnit(self):
		return self._IntrstFltgRateScndLegRefPrdUnit

	@IntrstFltgRateScndLegRefPrdUnit.setter
	def IntrstFltgRateScndLegRefPrdUnit(self, value):
		self._IntrstFltgRateScndLegRefPrdUnit = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegRefPrdUnit")

	@IntrstFltgRateScndLegRefPrdUnit.deleter
	def IntrstFltgRateScndLegRefPrdUnit(self):
		del self._IntrstFltgRateScndLegRefPrdUnit
		self._IntrstFltgRateScndLegRefPrdUnit = None

	@property
	def OptnPrmAmt(self):
		return self._OptnPrmAmt

	@OptnPrmAmt.setter
	def OptnPrmAmt(self, value):
		self._OptnPrmAmt = value if type(value) != auto else self.make_default("OptnPrmAmt")

	@OptnPrmAmt.deleter
	def OptnPrmAmt(self):
		del self._OptnPrmAmt
		self._OptnPrmAmt = None

	@property
	def IntrstFltgRateScndLegDayCnt(self):
		return self._IntrstFltgRateScndLegDayCnt

	@IntrstFltgRateScndLegDayCnt.setter
	def IntrstFltgRateScndLegDayCnt(self, value):
		self._IntrstFltgRateScndLegDayCnt = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegDayCnt")

	@IntrstFltgRateScndLegDayCnt.deleter
	def IntrstFltgRateScndLegDayCnt(self):
		del self._IntrstFltgRateScndLegDayCnt
		self._IntrstFltgRateScndLegDayCnt = None

	@property
	def CcyXchgRate(self):
		return self._CcyXchgRate

	@CcyXchgRate.setter
	def CcyXchgRate(self, value):
		self._CcyXchgRate = value if type(value) != auto else self.make_default("CcyXchgRate")

	@CcyXchgRate.deleter
	def CcyXchgRate(self):
		del self._CcyXchgRate
		self._CcyXchgRate = None

	@property
	def ExctnTmStmp(self):
		return self._ExctnTmStmp

	@ExctnTmStmp.setter
	def ExctnTmStmp(self, value):
		self._ExctnTmStmp = value if type(value) != auto else self.make_default("ExctnTmStmp")

	@ExctnTmStmp.deleter
	def ExctnTmStmp(self):
		del self._ExctnTmStmp
		self._ExctnTmStmp = None

	@property
	def PrrUnqTxIdr(self):
		return self._PrrUnqTxIdr

	@PrrUnqTxIdr.setter
	def PrrUnqTxIdr(self, value):
		self._PrrUnqTxIdr = value if type(value) != auto else self.make_default("PrrUnqTxIdr")

	@PrrUnqTxIdr.deleter
	def PrrUnqTxIdr(self):
		del self._PrrUnqTxIdr
		self._PrrUnqTxIdr = None

	@property
	def PltfmIdr(self):
		return self._PltfmIdr

	@PltfmIdr.setter
	def PltfmIdr(self, value):
		self._PltfmIdr = value if type(value) != auto else self.make_default("PltfmIdr")

	@PltfmIdr.deleter
	def PltfmIdr(self):
		del self._PltfmIdr
		self._PltfmIdr = None

	@property
	def OptnStrkPric(self):
		return self._OptnStrkPric

	@OptnStrkPric.setter
	def OptnStrkPric(self, value):
		self._OptnStrkPric = value if type(value) != auto else self.make_default("OptnStrkPric")

	@OptnStrkPric.deleter
	def OptnStrkPric(self):
		del self._OptnStrkPric
		self._OptnStrkPric = None

	@property
	def IntrstFxdRateFrstLeg(self):
		return self._IntrstFxdRateFrstLeg

	@IntrstFxdRateFrstLeg.setter
	def IntrstFxdRateFrstLeg(self, value):
		self._IntrstFxdRateFrstLeg = value if type(value) != auto else self.make_default("IntrstFxdRateFrstLeg")

	@IntrstFxdRateFrstLeg.deleter
	def IntrstFxdRateFrstLeg(self):
		del self._IntrstFxdRateFrstLeg
		self._IntrstFxdRateFrstLeg = None

	@property
	def IntraGrp(self):
		return self._IntraGrp

	@IntraGrp.setter
	def IntraGrp(self, value):
		self._IntraGrp = value if type(value) != auto else self.make_default("IntraGrp")

	@IntraGrp.deleter
	def IntraGrp(self):
		del self._IntraGrp
		self._IntraGrp = None

	@property
	def IntrstRateFxdScndLeg(self):
		return self._IntrstRateFxdScndLeg

	@IntrstRateFxdScndLeg.setter
	def IntrstRateFxdScndLeg(self, value):
		self._IntrstRateFxdScndLeg = value if type(value) != auto else self.make_default("IntrstRateFxdScndLeg")

	@IntrstRateFxdScndLeg.deleter
	def IntrstRateFxdScndLeg(self):
		del self._IntrstRateFxdScndLeg
		self._IntrstRateFxdScndLeg = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

	@property
	def IntrstFxdRateFrstLegPmtFrqcyVal(self):
		return self._IntrstFxdRateFrstLegPmtFrqcyVal

	@IntrstFxdRateFrstLegPmtFrqcyVal.setter
	def IntrstFxdRateFrstLegPmtFrqcyVal(self, value):
		self._IntrstFxdRateFrstLegPmtFrqcyVal = value if type(value) != auto else self.make_default("IntrstFxdRateFrstLegPmtFrqcyVal")

	@IntrstFxdRateFrstLegPmtFrqcyVal.deleter
	def IntrstFxdRateFrstLegPmtFrqcyVal(self):
		del self._IntrstFxdRateFrstLegPmtFrqcyVal
		self._IntrstFxdRateFrstLegPmtFrqcyVal = None

	@property
	def IntrstFxdRateScndLegDayCnt(self):
		return self._IntrstFxdRateScndLegDayCnt

	@IntrstFxdRateScndLegDayCnt.setter
	def IntrstFxdRateScndLegDayCnt(self, value):
		self._IntrstFxdRateScndLegDayCnt = value if type(value) != auto else self.make_default("IntrstFxdRateScndLegDayCnt")

	@IntrstFxdRateScndLegDayCnt.deleter
	def IntrstFxdRateScndLegDayCnt(self):
		del self._IntrstFxdRateScndLegDayCnt
		self._IntrstFxdRateScndLegDayCnt = None

	@property
	def IntrstFltgRateFrstLegRstFrqcyUnit(self):
		return self._IntrstFltgRateFrstLegRstFrqcyUnit

	@IntrstFltgRateFrstLegRstFrqcyUnit.setter
	def IntrstFltgRateFrstLegRstFrqcyUnit(self, value):
		self._IntrstFltgRateFrstLegRstFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegRstFrqcyUnit")

	@IntrstFltgRateFrstLegRstFrqcyUnit.deleter
	def IntrstFltgRateFrstLegRstFrqcyUnit(self):
		del self._IntrstFltgRateFrstLegRstFrqcyUnit
		self._IntrstFltgRateFrstLegRstFrqcyUnit = None

	@property
	def NtnlAmtScndLegUadjstdFctvDt(self):
		return self._NtnlAmtScndLegUadjstdFctvDt

	@NtnlAmtScndLegUadjstdFctvDt.setter
	def NtnlAmtScndLegUadjstdFctvDt(self, value):
		self._NtnlAmtScndLegUadjstdFctvDt = value if type(value) != auto else self.make_default("NtnlAmtScndLegUadjstdFctvDt")

	@NtnlAmtScndLegUadjstdFctvDt.deleter
	def NtnlAmtScndLegUadjstdFctvDt(self):
		del self._NtnlAmtScndLegUadjstdFctvDt
		self._NtnlAmtScndLegUadjstdFctvDt = None

	@property
	def IntrstFltgRateFrstLegNm(self):
		return self._IntrstFltgRateFrstLegNm

	@IntrstFltgRateFrstLegNm.setter
	def IntrstFltgRateFrstLegNm(self, value):
		self._IntrstFltgRateFrstLegNm = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegNm")

	@IntrstFltgRateFrstLegNm.deleter
	def IntrstFltgRateFrstLegNm(self):
		del self._IntrstFltgRateFrstLegNm
		self._IntrstFltgRateFrstLegNm = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def NtnlQtyScndLeg(self):
		return self._NtnlQtyScndLeg

	@NtnlQtyScndLeg.setter
	def NtnlQtyScndLeg(self, value):
		self._NtnlQtyScndLeg = value if type(value) != auto else self.make_default("NtnlQtyScndLeg")

	@NtnlQtyScndLeg.deleter
	def NtnlQtyScndLeg(self):
		del self._NtnlQtyScndLeg
		self._NtnlQtyScndLeg = None

	@property
	def PackgPric(self):
		return self._PackgPric

	@PackgPric.setter
	def PackgPric(self, value):
		self._PackgPric = value if type(value) != auto else self.make_default("PackgPric")

	@PackgPric.deleter
	def PackgPric(self):
		del self._PackgPric
		self._PackgPric = None

	@property
	def NtnlQtyScndLegSchdlQty(self):
		return self._NtnlQtyScndLegSchdlQty

	@NtnlQtyScndLegSchdlQty.setter
	def NtnlQtyScndLegSchdlQty(self, value):
		self._NtnlQtyScndLegSchdlQty = value if type(value) != auto else self.make_default("NtnlQtyScndLegSchdlQty")

	@NtnlQtyScndLegSchdlQty.deleter
	def NtnlQtyScndLegSchdlQty(self):
		del self._NtnlQtyScndLegSchdlQty
		self._NtnlQtyScndLegSchdlQty = None

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	@property
	def NtnlAmtFrstLeg(self):
		return self._NtnlAmtFrstLeg

	@NtnlAmtFrstLeg.setter
	def NtnlAmtFrstLeg(self, value):
		self._NtnlAmtFrstLeg = value if type(value) != auto else self.make_default("NtnlAmtFrstLeg")

	@NtnlAmtFrstLeg.deleter
	def NtnlAmtFrstLeg(self):
		del self._NtnlAmtFrstLeg
		self._NtnlAmtFrstLeg = None

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if type(value) != auto else self.make_default("Lvl")

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = None

	@property
	def NtnlAmtScndLegSchdlAmt(self):
		return self._NtnlAmtScndLegSchdlAmt

	@NtnlAmtScndLegSchdlAmt.setter
	def NtnlAmtScndLegSchdlAmt(self, value):
		self._NtnlAmtScndLegSchdlAmt = value if type(value) != auto else self.make_default("NtnlAmtScndLegSchdlAmt")

	@NtnlAmtScndLegSchdlAmt.deleter
	def NtnlAmtScndLegSchdlAmt(self):
		del self._NtnlAmtScndLegSchdlAmt
		self._NtnlAmtScndLegSchdlAmt = None

	@property
	def IntrstFltgRateFrstLegDayCnt(self):
		return self._IntrstFltgRateFrstLegDayCnt

	@IntrstFltgRateFrstLegDayCnt.setter
	def IntrstFltgRateFrstLegDayCnt(self, value):
		self._IntrstFltgRateFrstLegDayCnt = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegDayCnt")

	@IntrstFltgRateFrstLegDayCnt.deleter
	def IntrstFltgRateFrstLegDayCnt(self):
		del self._IntrstFltgRateFrstLegDayCnt
		self._IntrstFltgRateFrstLegDayCnt = None

	@property
	def PstTradRskRdctn(self):
		return self._PstTradRskRdctn

	@PstTradRskRdctn.setter
	def PstTradRskRdctn(self, value):
		self._PstTradRskRdctn = value if type(value) != auto else self.make_default("PstTradRskRdctn")

	@PstTradRskRdctn.deleter
	def PstTradRskRdctn(self):
		del self._PstTradRskRdctn
		self._PstTradRskRdctn = None

	@property
	def CdtRefPty(self):
		return self._CdtRefPty

	@CdtRefPty.setter
	def CdtRefPty(self, value):
		self._CdtRefPty = value if type(value) != auto else self.make_default("CdtRefPty")

	@CdtRefPty.deleter
	def CdtRefPty(self):
		del self._CdtRefPty
		self._CdtRefPty = None

	@property
	def TradClrSts(self):
		return self._TradClrSts

	@TradClrSts.setter
	def TradClrSts(self, value):
		self._TradClrSts = value if type(value) != auto else self.make_default("TradClrSts")

	@TradClrSts.deleter
	def TradClrSts(self):
		del self._TradClrSts
		self._TradClrSts = None

	@property
	def CdtVrsn(self):
		return self._CdtVrsn

	@CdtVrsn.setter
	def CdtVrsn(self, value):
		self._CdtVrsn = value if type(value) != auto else self.make_default("CdtVrsn")

	@CdtVrsn.deleter
	def CdtVrsn(self):
		del self._CdtVrsn
		self._CdtVrsn = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def OptnStrkPricSchdlUadjstdEndDt(self):
		return self._OptnStrkPricSchdlUadjstdEndDt

	@OptnStrkPricSchdlUadjstdEndDt.setter
	def OptnStrkPricSchdlUadjstdEndDt(self, value):
		self._OptnStrkPricSchdlUadjstdEndDt = value if type(value) != auto else self.make_default("OptnStrkPricSchdlUadjstdEndDt")

	@OptnStrkPricSchdlUadjstdEndDt.deleter
	def OptnStrkPricSchdlUadjstdEndDt(self):
		del self._OptnStrkPricSchdlUadjstdEndDt
		self._OptnStrkPricSchdlUadjstdEndDt = None

	@property
	def TradConf(self):
		return self._TradConf

	@TradConf.setter
	def TradConf(self, value):
		self._TradConf = value if type(value) != auto else self.make_default("TradConf")

	@TradConf.deleter
	def TradConf(self):
		del self._TradConf
		self._TradConf = None

	@property
	def CdtIndxFctr(self):
		return self._CdtIndxFctr

	@CdtIndxFctr.setter
	def CdtIndxFctr(self, value):
		self._CdtIndxFctr = value if type(value) != auto else self.make_default("CdtIndxFctr")

	@CdtIndxFctr.deleter
	def CdtIndxFctr(self):
		del self._CdtIndxFctr
		self._CdtIndxFctr = None

	@property
	def OptnPrmPmtDt(self):
		return self._OptnPrmPmtDt

	@OptnPrmPmtDt.setter
	def OptnPrmPmtDt(self, value):
		self._OptnPrmPmtDt = value if type(value) != auto else self.make_default("OptnPrmPmtDt")

	@OptnPrmPmtDt.deleter
	def OptnPrmPmtDt(self):
		del self._OptnPrmPmtDt
		self._OptnPrmPmtDt = None

	@property
	def IntrstFltgRateFrstLegRstFrqcyVal(self):
		return self._IntrstFltgRateFrstLegRstFrqcyVal

	@IntrstFltgRateFrstLegRstFrqcyVal.setter
	def IntrstFltgRateFrstLegRstFrqcyVal(self, value):
		self._IntrstFltgRateFrstLegRstFrqcyVal = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegRstFrqcyVal")

	@IntrstFltgRateFrstLegRstFrqcyVal.deleter
	def IntrstFltgRateFrstLegRstFrqcyVal(self):
		del self._IntrstFltgRateFrstLegRstFrqcyVal
		self._IntrstFltgRateFrstLegRstFrqcyVal = None

	@property
	def PackgSprd(self):
		return self._PackgSprd

	@PackgSprd.setter
	def PackgSprd(self, value):
		self._PackgSprd = value if type(value) != auto else self.make_default("PackgSprd")

	@PackgSprd.deleter
	def PackgSprd(self):
		del self._PackgSprd
		self._PackgSprd = None

	@property
	def NtnlAmtScndLegUadjstdEndDt(self):
		return self._NtnlAmtScndLegUadjstdEndDt

	@NtnlAmtScndLegUadjstdEndDt.setter
	def NtnlAmtScndLegUadjstdEndDt(self, value):
		self._NtnlAmtScndLegUadjstdEndDt = value if type(value) != auto else self.make_default("NtnlAmtScndLegUadjstdEndDt")

	@NtnlAmtScndLegUadjstdEndDt.deleter
	def NtnlAmtScndLegUadjstdEndDt(self):
		del self._NtnlAmtScndLegUadjstdEndDt
		self._NtnlAmtScndLegUadjstdEndDt = None

	@property
	def IntrstFltgRateFrstLegId(self):
		return self._IntrstFltgRateFrstLegId

	@IntrstFltgRateFrstLegId.setter
	def IntrstFltgRateFrstLegId(self, value):
		self._IntrstFltgRateFrstLegId = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegId")

	@IntrstFltgRateFrstLegId.deleter
	def IntrstFltgRateFrstLegId(self):
		del self._IntrstFltgRateFrstLegId
		self._IntrstFltgRateFrstLegId = None

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
	def DerivEvt(self):
		return self._DerivEvt

	@DerivEvt.setter
	def DerivEvt(self, value):
		self._DerivEvt = value if type(value) != auto else self.make_default("DerivEvt")

	@DerivEvt.deleter
	def DerivEvt(self):
		del self._DerivEvt
		self._DerivEvt = None

	@property
	def IntrstFltgRateScndLegNm(self):
		return self._IntrstFltgRateScndLegNm

	@IntrstFltgRateScndLegNm.setter
	def IntrstFltgRateScndLegNm(self, value):
		self._IntrstFltgRateScndLegNm = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegNm")

	@IntrstFltgRateScndLegNm.deleter
	def IntrstFltgRateScndLegNm(self):
		del self._IntrstFltgRateScndLegNm
		self._IntrstFltgRateScndLegNm = None

	@property
	def IntrstFltgRateScndLegCd(self):
		return self._IntrstFltgRateScndLegCd

	@IntrstFltgRateScndLegCd.setter
	def IntrstFltgRateScndLegCd(self, value):
		self._IntrstFltgRateScndLegCd = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegCd")

	@IntrstFltgRateScndLegCd.deleter
	def IntrstFltgRateScndLegCd(self):
		del self._IntrstFltgRateScndLegCd
		self._IntrstFltgRateScndLegCd = None

	@property
	def IntrstFltgRateScndLegSprd(self):
		return self._IntrstFltgRateScndLegSprd

	@IntrstFltgRateScndLegSprd.setter
	def IntrstFltgRateScndLegSprd(self, value):
		self._IntrstFltgRateScndLegSprd = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegSprd")

	@IntrstFltgRateScndLegSprd.deleter
	def IntrstFltgRateScndLegSprd(self):
		del self._IntrstFltgRateScndLegSprd
		self._IntrstFltgRateScndLegSprd = None

	@property
	def NrgyLdTp(self):
		return self._NrgyLdTp

	@NrgyLdTp.setter
	def NrgyLdTp(self, value):
		self._NrgyLdTp = value if type(value) != auto else self.make_default("NrgyLdTp")

	@NrgyLdTp.deleter
	def NrgyLdTp(self):
		del self._NrgyLdTp
		self._NrgyLdTp = None

	@property
	def CdtSnrty(self):
		return self._CdtSnrty

	@CdtSnrty.setter
	def CdtSnrty(self, value):
		self._CdtSnrty = value if type(value) != auto else self.make_default("CdtSnrty")

	@CdtSnrty.deleter
	def CdtSnrty(self):
		del self._CdtSnrty
		self._CdtSnrty = None

	@property
	def NrgyDlvryPtOrZone(self):
		return self._NrgyDlvryPtOrZone

	@NrgyDlvryPtOrZone.setter
	def NrgyDlvryPtOrZone(self, value):
		self._NrgyDlvryPtOrZone = value if type(value) != auto else self.make_default("NrgyDlvryPtOrZone")

	@NrgyDlvryPtOrZone.deleter
	def NrgyDlvryPtOrZone(self):
		del self._NrgyDlvryPtOrZone
		self._NrgyDlvryPtOrZone = None

	@property
	def IntrstFltgRateFrstLegCd(self):
		return self._IntrstFltgRateFrstLegCd

	@IntrstFltgRateFrstLegCd.setter
	def IntrstFltgRateFrstLegCd(self, value):
		self._IntrstFltgRateFrstLegCd = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegCd")

	@IntrstFltgRateFrstLegCd.deleter
	def IntrstFltgRateFrstLegCd(self):
		del self._IntrstFltgRateFrstLegCd
		self._IntrstFltgRateFrstLegCd = None

	@property
	def NtnlAmtFrstLegSchdlAmt(self):
		return self._NtnlAmtFrstLegSchdlAmt

	@NtnlAmtFrstLegSchdlAmt.setter
	def NtnlAmtFrstLegSchdlAmt(self, value):
		self._NtnlAmtFrstLegSchdlAmt = value if type(value) != auto else self.make_default("NtnlAmtFrstLegSchdlAmt")

	@NtnlAmtFrstLegSchdlAmt.deleter
	def NtnlAmtFrstLegSchdlAmt(self):
		del self._NtnlAmtFrstLegSchdlAmt
		self._NtnlAmtFrstLegSchdlAmt = None

	@property
	def NtnlQtyFrstLegUadjstdFctvDt(self):
		return self._NtnlQtyFrstLegUadjstdFctvDt

	@NtnlQtyFrstLegUadjstdFctvDt.setter
	def NtnlQtyFrstLegUadjstdFctvDt(self, value):
		self._NtnlQtyFrstLegUadjstdFctvDt = value if type(value) != auto else self.make_default("NtnlQtyFrstLegUadjstdFctvDt")

	@NtnlQtyFrstLegUadjstdFctvDt.deleter
	def NtnlQtyFrstLegUadjstdFctvDt(self):
		del self._NtnlQtyFrstLegUadjstdFctvDt
		self._NtnlQtyFrstLegUadjstdFctvDt = None

	@property
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self):
		return self._IntrstFltgRateFrstLegPmtFrqcyUnit

	@IntrstFltgRateFrstLegPmtFrqcyUnit.setter
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self, value):
		self._IntrstFltgRateFrstLegPmtFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegPmtFrqcyUnit")

	@IntrstFltgRateFrstLegPmtFrqcyUnit.deleter
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self):
		del self._IntrstFltgRateFrstLegPmtFrqcyUnit
		self._IntrstFltgRateFrstLegPmtFrqcyUnit = None

	@property
	def NtnlAmtFrstLegUadjstdEndDt(self):
		return self._NtnlAmtFrstLegUadjstdEndDt

	@NtnlAmtFrstLegUadjstdEndDt.setter
	def NtnlAmtFrstLegUadjstdEndDt(self, value):
		self._NtnlAmtFrstLegUadjstdEndDt = value if type(value) != auto else self.make_default("NtnlAmtFrstLegUadjstdEndDt")

	@NtnlAmtFrstLegUadjstdEndDt.deleter
	def NtnlAmtFrstLegUadjstdEndDt(self):
		del self._NtnlAmtFrstLegUadjstdEndDt
		self._NtnlAmtFrstLegUadjstdEndDt = None

	@property
	def TxSchdlPric(self):
		return self._TxSchdlPric

	@TxSchdlPric.setter
	def TxSchdlPric(self, value):
		self._TxSchdlPric = value if type(value) != auto else self.make_default("TxSchdlPric")

	@TxSchdlPric.deleter
	def TxSchdlPric(self):
		del self._TxSchdlPric
		self._TxSchdlPric = None

	@property
	def PricSchdlUadjstdFctvDt(self):
		return self._PricSchdlUadjstdFctvDt

	@PricSchdlUadjstdFctvDt.setter
	def PricSchdlUadjstdFctvDt(self, value):
		self._PricSchdlUadjstdFctvDt = value if type(value) != auto else self.make_default("PricSchdlUadjstdFctvDt")

	@PricSchdlUadjstdFctvDt.deleter
	def PricSchdlUadjstdFctvDt(self):
		del self._PricSchdlUadjstdFctvDt
		self._PricSchdlUadjstdFctvDt = None

	@property
	def EarlyTermntnDt(self):
		return self._EarlyTermntnDt

	@EarlyTermntnDt.setter
	def EarlyTermntnDt(self, value):
		self._EarlyTermntnDt = value if type(value) != auto else self.make_default("EarlyTermntnDt")

	@EarlyTermntnDt.deleter
	def EarlyTermntnDt(self):
		del self._EarlyTermntnDt
		self._EarlyTermntnDt = None

	@property
	def RptTrckgNb(self):
		return self._RptTrckgNb

	@RptTrckgNb.setter
	def RptTrckgNb(self, value):
		self._RptTrckgNb = value if type(value) != auto else self.make_default("RptTrckgNb")

	@RptTrckgNb.deleter
	def RptTrckgNb(self):
		del self._RptTrckgNb
		self._RptTrckgNb = None

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if type(value) != auto else self.make_default("DlvryTp")

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = None

	@property
	def IntrstFxdRateScndLegPmtFrqcyVal(self):
		return self._IntrstFxdRateScndLegPmtFrqcyVal

	@IntrstFxdRateScndLegPmtFrqcyVal.setter
	def IntrstFxdRateScndLegPmtFrqcyVal(self, value):
		self._IntrstFxdRateScndLegPmtFrqcyVal = value if type(value) != auto else self.make_default("IntrstFxdRateScndLegPmtFrqcyVal")

	@IntrstFxdRateScndLegPmtFrqcyVal.deleter
	def IntrstFxdRateScndLegPmtFrqcyVal(self):
		del self._IntrstFxdRateScndLegPmtFrqcyVal
		self._IntrstFxdRateScndLegPmtFrqcyVal = None

	@property
	def IntrstFltgRateScndLegPmtFrqcyUnit(self):
		return self._IntrstFltgRateScndLegPmtFrqcyUnit

	@IntrstFltgRateScndLegPmtFrqcyUnit.setter
	def IntrstFltgRateScndLegPmtFrqcyUnit(self, value):
		self._IntrstFltgRateScndLegPmtFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegPmtFrqcyUnit")

	@IntrstFltgRateScndLegPmtFrqcyUnit.deleter
	def IntrstFltgRateScndLegPmtFrqcyUnit(self):
		del self._IntrstFltgRateScndLegPmtFrqcyUnit
		self._IntrstFltgRateScndLegPmtFrqcyUnit = None

	@property
	def CdtTrch(self):
		return self._CdtTrch

	@CdtTrch.setter
	def CdtTrch(self, value):
		self._CdtTrch = value if type(value) != auto else self.make_default("CdtTrch")

	@CdtTrch.deleter
	def CdtTrch(self):
		del self._CdtTrch
		self._CdtTrch = None

	@property
	def OptnMtrtyDtOfUndrlyg(self):
		return self._OptnMtrtyDtOfUndrlyg

	@OptnMtrtyDtOfUndrlyg.setter
	def OptnMtrtyDtOfUndrlyg(self, value):
		self._OptnMtrtyDtOfUndrlyg = value if type(value) != auto else self.make_default("OptnMtrtyDtOfUndrlyg")

	@OptnMtrtyDtOfUndrlyg.deleter
	def OptnMtrtyDtOfUndrlyg(self):
		del self._OptnMtrtyDtOfUndrlyg
		self._OptnMtrtyDtOfUndrlyg = None

	@property
	def NtnlQtyFrstLegUadjstdEndDt(self):
		return self._NtnlQtyFrstLegUadjstdEndDt

	@NtnlQtyFrstLegUadjstdEndDt.setter
	def NtnlQtyFrstLegUadjstdEndDt(self, value):
		self._NtnlQtyFrstLegUadjstdEndDt = value if type(value) != auto else self.make_default("NtnlQtyFrstLegUadjstdEndDt")

	@NtnlQtyFrstLegUadjstdEndDt.deleter
	def NtnlQtyFrstLegUadjstdEndDt(self):
		del self._NtnlQtyFrstLegUadjstdEndDt
		self._NtnlQtyFrstLegUadjstdEndDt = None

	@property
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self):
		return self._IntrstFxdRateFrstLegPmtFrqcyUnit

	@IntrstFxdRateFrstLegPmtFrqcyUnit.setter
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self, value):
		self._IntrstFxdRateFrstLegPmtFrqcyUnit = value if type(value) != auto else self.make_default("IntrstFxdRateFrstLegPmtFrqcyUnit")

	@IntrstFxdRateFrstLegPmtFrqcyUnit.deleter
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self):
		del self._IntrstFxdRateFrstLegPmtFrqcyUnit
		self._IntrstFxdRateFrstLegPmtFrqcyUnit = None

	@property
	def OthrPmt(self):
		return self._OthrPmt

	@OthrPmt.setter
	def OthrPmt(self, value):
		self._OthrPmt = value if type(value) != auto else self.make_default("OthrPmt")

	@OthrPmt.deleter
	def OthrPmt(self):
		del self._OthrPmt
		self._OthrPmt = None

	@property
	def CdtSrs(self):
		return self._CdtSrs

	@CdtSrs.setter
	def CdtSrs(self, value):
		self._CdtSrs = value if type(value) != auto else self.make_default("CdtSrs")

	@CdtSrs.deleter
	def CdtSrs(self):
		del self._CdtSrs
		self._CdtSrs = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	@property
	def TxPric(self):
		return self._TxPric

	@TxPric.setter
	def TxPric(self, value):
		self._TxPric = value if type(value) != auto else self.make_default("TxPric")

	@TxPric.deleter
	def TxPric(self):
		del self._TxPric
		self._TxPric = None

	@property
	def IntrstFltgRateScndLegRefPrdVal(self):
		return self._IntrstFltgRateScndLegRefPrdVal

	@IntrstFltgRateScndLegRefPrdVal.setter
	def IntrstFltgRateScndLegRefPrdVal(self, value):
		self._IntrstFltgRateScndLegRefPrdVal = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegRefPrdVal")

	@IntrstFltgRateScndLegRefPrdVal.deleter
	def IntrstFltgRateScndLegRefPrdVal(self):
		del self._IntrstFltgRateScndLegRefPrdVal
		self._IntrstFltgRateScndLegRefPrdVal = None

	@property
	def OptnExrcStyle(self):
		return self._OptnExrcStyle

	@OptnExrcStyle.setter
	def OptnExrcStyle(self, value):
		self._OptnExrcStyle = value if type(value) != auto else self.make_default("OptnExrcStyle")

	@OptnExrcStyle.deleter
	def OptnExrcStyle(self):
		del self._OptnExrcStyle
		self._OptnExrcStyle = None

	@property
	def OptnStrkPricSchdlUadjstdFctvDt(self):
		return self._OptnStrkPricSchdlUadjstdFctvDt

	@OptnStrkPricSchdlUadjstdFctvDt.setter
	def OptnStrkPricSchdlUadjstdFctvDt(self, value):
		self._OptnStrkPricSchdlUadjstdFctvDt = value if type(value) != auto else self.make_default("OptnStrkPricSchdlUadjstdFctvDt")

	@OptnStrkPricSchdlUadjstdFctvDt.deleter
	def OptnStrkPricSchdlUadjstdFctvDt(self):
		del self._OptnStrkPricSchdlUadjstdFctvDt
		self._OptnStrkPricSchdlUadjstdFctvDt = None

	@property
	def NrgyIntrCnnctnPt(self):
		return self._NrgyIntrCnnctnPt

	@NrgyIntrCnnctnPt.setter
	def NrgyIntrCnnctnPt(self, value):
		self._NrgyIntrCnnctnPt = value if type(value) != auto else self.make_default("NrgyIntrCnnctnPt")

	@NrgyIntrCnnctnPt.deleter
	def NrgyIntrCnnctnPt(self):
		del self._NrgyIntrCnnctnPt
		self._NrgyIntrCnnctnPt = None

	@property
	def NtnlQtyScndLegUadjstdFctvDt(self):
		return self._NtnlQtyScndLegUadjstdFctvDt

	@NtnlQtyScndLegUadjstdFctvDt.setter
	def NtnlQtyScndLegUadjstdFctvDt(self, value):
		self._NtnlQtyScndLegUadjstdFctvDt = value if type(value) != auto else self.make_default("NtnlQtyScndLegUadjstdFctvDt")

	@NtnlQtyScndLegUadjstdFctvDt.deleter
	def NtnlQtyScndLegUadjstdFctvDt(self):
		del self._NtnlQtyScndLegUadjstdFctvDt
		self._NtnlQtyScndLegUadjstdFctvDt = None

	@property
	def CcyXchgRateBsis(self):
		return self._CcyXchgRateBsis

	@CcyXchgRateBsis.setter
	def CcyXchgRateBsis(self, value):
		self._CcyXchgRateBsis = value if type(value) != auto else self.make_default("CcyXchgRateBsis")

	@CcyXchgRateBsis.deleter
	def CcyXchgRateBsis(self):
		del self._CcyXchgRateBsis
		self._CcyXchgRateBsis = None

	@property
	def NtnlQtyFrstLeg(self):
		return self._NtnlQtyFrstLeg

	@NtnlQtyFrstLeg.setter
	def NtnlQtyFrstLeg(self, value):
		self._NtnlQtyFrstLeg = value if type(value) != auto else self.make_default("NtnlQtyFrstLeg")

	@NtnlQtyFrstLeg.deleter
	def NtnlQtyFrstLeg(self):
		del self._NtnlQtyFrstLeg
		self._NtnlQtyFrstLeg = None

	@property
	def PricSchdlUadjstdEndDt(self):
		return self._PricSchdlUadjstdEndDt

	@PricSchdlUadjstdEndDt.setter
	def PricSchdlUadjstdEndDt(self, value):
		self._PricSchdlUadjstdEndDt = value if type(value) != auto else self.make_default("PricSchdlUadjstdEndDt")

	@PricSchdlUadjstdEndDt.deleter
	def PricSchdlUadjstdEndDt(self):
		del self._PricSchdlUadjstdEndDt
		self._PricSchdlUadjstdEndDt = None

	@property
	def IntrstFltgRateScndLegRstFrqcyVal(self):
		return self._IntrstFltgRateScndLegRstFrqcyVal

	@IntrstFltgRateScndLegRstFrqcyVal.setter
	def IntrstFltgRateScndLegRstFrqcyVal(self, value):
		self._IntrstFltgRateScndLegRstFrqcyVal = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegRstFrqcyVal")

	@IntrstFltgRateScndLegRstFrqcyVal.deleter
	def IntrstFltgRateScndLegRstFrqcyVal(self):
		del self._IntrstFltgRateScndLegRstFrqcyVal
		self._IntrstFltgRateScndLegRstFrqcyVal = None

	@property
	def NtnlQtyFrstLegSchdlQty(self):
		return self._NtnlQtyFrstLegSchdlQty

	@NtnlQtyFrstLegSchdlQty.setter
	def NtnlQtyFrstLegSchdlQty(self, value):
		self._NtnlQtyFrstLegSchdlQty = value if type(value) != auto else self.make_default("NtnlQtyFrstLegSchdlQty")

	@NtnlQtyFrstLegSchdlQty.deleter
	def NtnlQtyFrstLegSchdlQty(self):
		del self._NtnlQtyFrstLegSchdlQty
		self._NtnlQtyFrstLegSchdlQty = None

	@property
	def NtnlAmtScndLeg(self):
		return self._NtnlAmtScndLeg

	@NtnlAmtScndLeg.setter
	def NtnlAmtScndLeg(self, value):
		self._NtnlAmtScndLeg = value if type(value) != auto else self.make_default("NtnlAmtScndLeg")

	@NtnlAmtScndLeg.deleter
	def NtnlAmtScndLeg(self):
		del self._NtnlAmtScndLeg
		self._NtnlAmtScndLeg = None

	@property
	def MstrAgrmtVrsn(self):
		return self._MstrAgrmtVrsn

	@MstrAgrmtVrsn.setter
	def MstrAgrmtVrsn(self, value):
		self._MstrAgrmtVrsn = value if type(value) != auto else self.make_default("MstrAgrmtVrsn")

	@MstrAgrmtVrsn.deleter
	def MstrAgrmtVrsn(self):
		del self._MstrAgrmtVrsn
		self._MstrAgrmtVrsn = None

	@property
	def TradClrOblgtn(self):
		return self._TradClrOblgtn

	@TradClrOblgtn.setter
	def TradClrOblgtn(self, value):
		self._TradClrOblgtn = value if type(value) != auto else self.make_default("TradClrOblgtn")

	@TradClrOblgtn.deleter
	def TradClrOblgtn(self):
		del self._TradClrOblgtn
		self._TradClrOblgtn = None

	@property
	def OptnStrkPricSchdlAmt(self):
		return self._OptnStrkPricSchdlAmt

	@OptnStrkPricSchdlAmt.setter
	def OptnStrkPricSchdlAmt(self, value):
		self._OptnStrkPricSchdlAmt = value if type(value) != auto else self.make_default("OptnStrkPricSchdlAmt")

	@OptnStrkPricSchdlAmt.deleter
	def OptnStrkPricSchdlAmt(self):
		del self._OptnStrkPricSchdlAmt
		self._OptnStrkPricSchdlAmt = None

	@property
	def IntrstFxdRateFrstLegDayCnt(self):
		return self._IntrstFxdRateFrstLegDayCnt

	@IntrstFxdRateFrstLegDayCnt.setter
	def IntrstFxdRateFrstLegDayCnt(self, value):
		self._IntrstFxdRateFrstLegDayCnt = value if type(value) != auto else self.make_default("IntrstFxdRateFrstLegDayCnt")

	@IntrstFxdRateFrstLegDayCnt.deleter
	def IntrstFxdRateFrstLegDayCnt(self):
		del self._IntrstFxdRateFrstLegDayCnt
		self._IntrstFxdRateFrstLegDayCnt = None

	@property
	def Dlta(self):
		return self._Dlta

	@Dlta.setter
	def Dlta(self, value):
		self._Dlta = value if type(value) != auto else self.make_default("Dlta")

	@Dlta.deleter
	def Dlta(self):
		del self._Dlta
		self._Dlta = None

	@property
	def NtnlQtyScndLegUadjstdEndDt(self):
		return self._NtnlQtyScndLegUadjstdEndDt

	@NtnlQtyScndLegUadjstdEndDt.setter
	def NtnlQtyScndLegUadjstdEndDt(self, value):
		self._NtnlQtyScndLegUadjstdEndDt = value if type(value) != auto else self.make_default("NtnlQtyScndLegUadjstdEndDt")

	@NtnlQtyScndLegUadjstdEndDt.deleter
	def NtnlQtyScndLegUadjstdEndDt(self):
		del self._NtnlQtyScndLegUadjstdEndDt
		self._NtnlQtyScndLegUadjstdEndDt = None

	@property
	def SbsqntPosUnqTxIdr(self):
		return self._SbsqntPosUnqTxIdr

	@SbsqntPosUnqTxIdr.setter
	def SbsqntPosUnqTxIdr(self, value):
		self._SbsqntPosUnqTxIdr = value if type(value) != auto else self.make_default("SbsqntPosUnqTxIdr")

	@SbsqntPosUnqTxIdr.deleter
	def SbsqntPosUnqTxIdr(self):
		del self._SbsqntPosUnqTxIdr
		self._SbsqntPosUnqTxIdr = None

	@property
	def IntrstFltgRateFrstLegRefPrdUnit(self):
		return self._IntrstFltgRateFrstLegRefPrdUnit

	@IntrstFltgRateFrstLegRefPrdUnit.setter
	def IntrstFltgRateFrstLegRefPrdUnit(self, value):
		self._IntrstFltgRateFrstLegRefPrdUnit = value if type(value) != auto else self.make_default("IntrstFltgRateFrstLegRefPrdUnit")

	@IntrstFltgRateFrstLegRefPrdUnit.deleter
	def IntrstFltgRateFrstLegRefPrdUnit(self):
		del self._IntrstFltgRateFrstLegRefPrdUnit
		self._IntrstFltgRateFrstLegRefPrdUnit = None

	@property
	def IntrstFltgRateScndLegPmtFrqcyVal(self):
		return self._IntrstFltgRateScndLegPmtFrqcyVal

	@IntrstFltgRateScndLegPmtFrqcyVal.setter
	def IntrstFltgRateScndLegPmtFrqcyVal(self, value):
		self._IntrstFltgRateScndLegPmtFrqcyVal = value if type(value) != auto else self.make_default("IntrstFltgRateScndLegPmtFrqcyVal")

	@IntrstFltgRateScndLegPmtFrqcyVal.deleter
	def IntrstFltgRateScndLegPmtFrqcyVal(self):
		del self._IntrstFltgRateScndLegPmtFrqcyVal
		self._IntrstFltgRateScndLegPmtFrqcyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstFltgRateScndLegId', type=CompareISINIdentifier4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyFwdXchgRate', type=CompareExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRstFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAttr', type=CompareEnergyDeliveryAttribute1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRefPrdVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRefPrdUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrmAmt', type=CompareActiveOrHistoricCurrencyAndAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchgRate', type=CompareExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTmStmp', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrUnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltfmIdr', type=CompareMICIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStrkPric', type=CompareUnitPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLeg', type=CompareUnitPrice7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraGrp', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateFxdScndLeg', type=CompareUnitPrice7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRstFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtScndLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegNm', type=CompareMax350Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CompareOptionType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyScndLeg', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgPric', type=CompareUnitPrice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyScndLegSchdlQty', type=CompareLongFraction19DecimalNumber1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XprtnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLeg', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=CompareReportingLevelType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtScndLegSchdlAmt', type=CompareAmountAndDirection3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctn', type=ComparePostTradeRiskReduction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRefPty', type=CompareReferenceParty1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradClrSts', type=CompareTradeClearingStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtVrsn', type=CompareNumber7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnStrkPricSchdlUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradConf', type=CompareTradeConfirmation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtIndxFctr', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrmPmtDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRstFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtScndLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegId', type=CompareISINIdentifier4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtTp', type=CompareMasterAgreementType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvt', type=CompareDerivativeEvent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegNm', type=CompareMax350Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegCd', type=CompareBenchmarkCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyLdTp', type=CompareEnergyLoadType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtSnrty', type=CompareSeniorityType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDlvryPtOrZone', type=CompareDeliveryInterconnectionPoint1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegCd', type=CompareBenchmarkCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLegSchdlAmt', type=CompareAmountAndDirection3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyFrstLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSchdlPric', type=CompareUnitPrice5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricSchdlUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlyTermntnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTrckgNb', type=CompareText2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=CompareDeliveryType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTrch', type=CompareTrancheIndicator1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnMtrtyDtOfUndrlyg', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyFrstLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmt', type=CompareOtherPayment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtSrs', type=CompareNumber7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=CompareCommodityAssetClass4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxPric', type=CompareUnitPrice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRefPrdVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnExrcStyle', type=CompareOptionStyle1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnStrkPricSchdlUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrgyIntrCnnctnPt', type=CompareDeliveryInterconnectionPoint1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyScndLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyXchgRateBsis', type=CompareExchangeRateBasis1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyFrstLeg', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSchdlUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRstFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyFrstLegSchdlQty', type=CompareLongFraction19DecimalNumber1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtScndLeg', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtVrsn', type=CompareMax50Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradClrOblgtn', type=CompareTradeClearingObligation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStrkPricSchdlAmt', type=CompareUnitPrice4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dlta', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyScndLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbsqntPosUnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRefPrdUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
	))

