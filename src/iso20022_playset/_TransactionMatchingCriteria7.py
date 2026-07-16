# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareActiveOrHistoricCurrencyAndAmount4
from . import CompareAmountAndDirection3
from . import CompareBenchmarkCode1
from . import CompareCommodityAssetClass4
from . import CompareDate3
from . import CompareDateTime3
from . import CompareDayCount1
from . import CompareDeliveryInterconnectionPoint1
from . import CompareDeliveryType1
from . import CompareDerivativeEvent1
from . import CompareEnergyDeliveryAttribute1
from . import CompareEnergyLoadType1
from . import CompareExchangeRate1
from . import CompareExchangeRateBasis1
from . import CompareFrequencyUnit1
from . import CompareISINIdentifier4
from . import CompareLongFraction19DecimalNumber1
from . import CompareMICIdentifier3
from . import CompareMasterAgreementType1
from . import CompareMax350Text1
from . import CompareMax50Text1
from . import CompareNumber5
from . import CompareNumber7
from . import CompareOptionStyle1
from . import CompareOptionType1
from . import CompareOtherPayment1
from . import ComparePercentageRate3
from . import ComparePostTradeRiskReduction2
from . import CompareReferenceParty1
from . import CompareReportingLevelType2
from . import CompareSeniorityType1
from . import CompareText2
from . import CompareTradeClearingObligation1
from . import CompareTradeClearingStatus3
from . import CompareTradeConfirmation2
from . import CompareTrancheIndicator1
from . import CompareTrueFalseIndicator3
from . import CompareUniqueTransactionIdentifier2
from . import CompareUnitPrice4
from . import CompareUnitPrice5
from . import CompareUnitPrice7
from . import CompareUnitPrice8

class TransactionMatchingCriteria7(base_types._BaseFieldType):

	__slots__ = ["_CcyFwdXchgRate", "_CcyXchgRate", "_CcyXchgRateBsis", "_CdtIndxFctr", "_CdtRefPty", "_CdtSnrty", "_CdtSrs", "_CdtTrch", "_CdtVrsn", "_Cmmdty", "_DerivEvt", "_Dlta", "_DlvryAttr", "_DlvryTp", "_EarlyTermntnDt", "_ExctnTmStmp", "_FctvDt", "_IntraGrp", "_IntrstFltgRateFrstLegCd", "_IntrstFltgRateFrstLegDayCnt", "_IntrstFltgRateFrstLegId", "_IntrstFltgRateFrstLegNm", "_IntrstFltgRateFrstLegPmtFrqcyUnit", "_IntrstFltgRateFrstLegPmtFrqcyVal", "_IntrstFltgRateFrstLegRefPrdUnit", "_IntrstFltgRateFrstLegRefPrdVal", "_IntrstFltgRateFrstLegRstFrqcyUnit", "_IntrstFltgRateFrstLegRstFrqcyVal", "_IntrstFltgRateFrstLegSprd", "_IntrstFltgRateScndLegCd", "_IntrstFltgRateScndLegDayCnt", "_IntrstFltgRateScndLegId", "_IntrstFltgRateScndLegNm", "_IntrstFltgRateScndLegPmtFrqcyUnit", "_IntrstFltgRateScndLegPmtFrqcyVal", "_IntrstFltgRateScndLegRefPrdUnit", "_IntrstFltgRateScndLegRefPrdVal", "_IntrstFltgRateScndLegRstFrqcyUnit", "_IntrstFltgRateScndLegRstFrqcyVal", "_IntrstFltgRateScndLegSprd", "_IntrstFxdRateFrstLeg", "_IntrstFxdRateFrstLegDayCnt", "_IntrstFxdRateFrstLegPmtFrqcyUnit", "_IntrstFxdRateFrstLegPmtFrqcyVal", "_IntrstFxdRateScndLegDayCnt", "_IntrstFxdRateScndLegPmtFrqcyUnit", "_IntrstFxdRateScndLegPmtFrqcyVal", "_IntrstRateFxdScndLeg", "_Lvl", "_MstrAgrmtTp", "_MstrAgrmtVrsn", "_NrgyDlvryPtOrZone", "_NrgyIntrCnnctnPt", "_NrgyLdTp", "_NtnlAmtFrstLeg", "_NtnlAmtFrstLegSchdlAmt", "_NtnlAmtFrstLegUadjstdEndDt", "_NtnlAmtFrstLegUadjstdFctvDt", "_NtnlAmtScndLeg", "_NtnlAmtScndLegSchdlAmt", "_NtnlAmtScndLegUadjstdEndDt", "_NtnlAmtScndLegUadjstdFctvDt", "_NtnlQtyFrstLeg", "_NtnlQtyFrstLegSchdlQty", "_NtnlQtyFrstLegUadjstdEndDt", "_NtnlQtyFrstLegUadjstdFctvDt", "_NtnlQtyScndLeg", "_NtnlQtyScndLegSchdlQty", "_NtnlQtyScndLegUadjstdEndDt", "_NtnlQtyScndLegUadjstdFctvDt", "_OptnExrcStyle", "_OptnMtrtyDtOfUndrlyg", "_OptnPrmAmt", "_OptnPrmPmtDt", "_OptnStrkPric", "_OptnStrkPricSchdlAmt", "_OptnStrkPricSchdlUadjstdEndDt", "_OptnStrkPricSchdlUadjstdFctvDt", "_OptnTp", "_OthrPmt", "_PackgPric", "_PackgSprd", "_PltfmIdr", "_PricSchdlUadjstdEndDt", "_PricSchdlUadjstdFctvDt", "_PrrUnqTxIdr", "_PstTradRskRdctn", "_RptTrckgNb", "_SbsqntPosUnqTxIdr", "_SttlmDt", "_TradClrOblgtn", "_TradClrSts", "_TradConf", "_TxPric", "_TxSchdlPric", "_UnqTxIdr", "_XprtnDt"]
	@property
	def CcyFwdXchgRate(self):
		return self._CcyFwdXchgRate

	@CcyFwdXchgRate.setter
	def CcyFwdXchgRate(self, value):
		self._CcyFwdXchgRate = value if value is not None else base_types.UninitialisedField(self, 'CcyFwdXchgRate', CompareExchangeRate1, False)

	@CcyFwdXchgRate.deleter
	def CcyFwdXchgRate(self):
		del self._CcyFwdXchgRate
		self._CcyFwdXchgRate = base_types.UninitialisedField(self, 'CcyFwdXchgRate', CompareExchangeRate1, False)

	@property
	def CcyXchgRate(self):
		return self._CcyXchgRate

	@CcyXchgRate.setter
	def CcyXchgRate(self, value):
		self._CcyXchgRate = value if value is not None else base_types.UninitialisedField(self, 'CcyXchgRate', CompareExchangeRate1, False)

	@CcyXchgRate.deleter
	def CcyXchgRate(self):
		del self._CcyXchgRate
		self._CcyXchgRate = base_types.UninitialisedField(self, 'CcyXchgRate', CompareExchangeRate1, False)

	@property
	def CcyXchgRateBsis(self):
		return self._CcyXchgRateBsis

	@CcyXchgRateBsis.setter
	def CcyXchgRateBsis(self, value):
		self._CcyXchgRateBsis = value if value is not None else base_types.UninitialisedField(self, 'CcyXchgRateBsis', CompareExchangeRateBasis1, False)

	@CcyXchgRateBsis.deleter
	def CcyXchgRateBsis(self):
		del self._CcyXchgRateBsis
		self._CcyXchgRateBsis = base_types.UninitialisedField(self, 'CcyXchgRateBsis', CompareExchangeRateBasis1, False)

	@property
	def CdtIndxFctr(self):
		return self._CdtIndxFctr

	@CdtIndxFctr.setter
	def CdtIndxFctr(self, value):
		self._CdtIndxFctr = value if value is not None else base_types.UninitialisedField(self, 'CdtIndxFctr', ComparePercentageRate3, False)

	@CdtIndxFctr.deleter
	def CdtIndxFctr(self):
		del self._CdtIndxFctr
		self._CdtIndxFctr = base_types.UninitialisedField(self, 'CdtIndxFctr', ComparePercentageRate3, False)

	@property
	def CdtRefPty(self):
		return self._CdtRefPty

	@CdtRefPty.setter
	def CdtRefPty(self, value):
		self._CdtRefPty = value if value is not None else base_types.UninitialisedField(self, 'CdtRefPty', CompareReferenceParty1, False)

	@CdtRefPty.deleter
	def CdtRefPty(self):
		del self._CdtRefPty
		self._CdtRefPty = base_types.UninitialisedField(self, 'CdtRefPty', CompareReferenceParty1, False)

	@property
	def CdtSnrty(self):
		return self._CdtSnrty

	@CdtSnrty.setter
	def CdtSnrty(self, value):
		self._CdtSnrty = value if value is not None else base_types.UninitialisedField(self, 'CdtSnrty', CompareSeniorityType1, False)

	@CdtSnrty.deleter
	def CdtSnrty(self):
		del self._CdtSnrty
		self._CdtSnrty = base_types.UninitialisedField(self, 'CdtSnrty', CompareSeniorityType1, False)

	@property
	def CdtSrs(self):
		return self._CdtSrs

	@CdtSrs.setter
	def CdtSrs(self, value):
		self._CdtSrs = value if value is not None else base_types.UninitialisedField(self, 'CdtSrs', CompareNumber7, False)

	@CdtSrs.deleter
	def CdtSrs(self):
		del self._CdtSrs
		self._CdtSrs = base_types.UninitialisedField(self, 'CdtSrs', CompareNumber7, False)

	@property
	def CdtTrch(self):
		return self._CdtTrch

	@CdtTrch.setter
	def CdtTrch(self, value):
		self._CdtTrch = value if value is not None else base_types.UninitialisedField(self, 'CdtTrch', CompareTrancheIndicator1, False)

	@CdtTrch.deleter
	def CdtTrch(self):
		del self._CdtTrch
		self._CdtTrch = base_types.UninitialisedField(self, 'CdtTrch', CompareTrancheIndicator1, False)

	@property
	def CdtVrsn(self):
		return self._CdtVrsn

	@CdtVrsn.setter
	def CdtVrsn(self, value):
		self._CdtVrsn = value if value is not None else base_types.UninitialisedField(self, 'CdtVrsn', CompareNumber7, False)

	@CdtVrsn.deleter
	def CdtVrsn(self):
		del self._CdtVrsn
		self._CdtVrsn = base_types.UninitialisedField(self, 'CdtVrsn', CompareNumber7, False)

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', CompareCommodityAssetClass4, False)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', CompareCommodityAssetClass4, False)

	@property
	def DerivEvt(self):
		return self._DerivEvt

	@DerivEvt.setter
	def DerivEvt(self, value):
		self._DerivEvt = value if value is not None else base_types.UninitialisedField(self, 'DerivEvt', CompareDerivativeEvent1, False)

	@DerivEvt.deleter
	def DerivEvt(self):
		del self._DerivEvt
		self._DerivEvt = base_types.UninitialisedField(self, 'DerivEvt', CompareDerivativeEvent1, False)

	@property
	def Dlta(self):
		return self._Dlta

	@Dlta.setter
	def Dlta(self, value):
		self._Dlta = value if value is not None else base_types.UninitialisedField(self, 'Dlta', CompareLongFraction19DecimalNumber1, False)

	@Dlta.deleter
	def Dlta(self):
		del self._Dlta
		self._Dlta = base_types.UninitialisedField(self, 'Dlta', CompareLongFraction19DecimalNumber1, False)

	@property
	def DlvryAttr(self):
		return self._DlvryAttr

	@DlvryAttr.setter
	def DlvryAttr(self, value):
		self._DlvryAttr = value if value is not None else base_types.UninitialisedField(self, 'DlvryAttr', CompareEnergyDeliveryAttribute1, True)

	@DlvryAttr.deleter
	def DlvryAttr(self):
		del self._DlvryAttr
		self._DlvryAttr = base_types.UninitialisedField(self, 'DlvryAttr', CompareEnergyDeliveryAttribute1, True)

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if value is not None else base_types.UninitialisedField(self, 'DlvryTp', CompareDeliveryType1, False)

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = base_types.UninitialisedField(self, 'DlvryTp', CompareDeliveryType1, False)

	@property
	def EarlyTermntnDt(self):
		return self._EarlyTermntnDt

	@EarlyTermntnDt.setter
	def EarlyTermntnDt(self, value):
		self._EarlyTermntnDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyTermntnDt', CompareDate3, False)

	@EarlyTermntnDt.deleter
	def EarlyTermntnDt(self):
		del self._EarlyTermntnDt
		self._EarlyTermntnDt = base_types.UninitialisedField(self, 'EarlyTermntnDt', CompareDate3, False)

	@property
	def ExctnTmStmp(self):
		return self._ExctnTmStmp

	@ExctnTmStmp.setter
	def ExctnTmStmp(self, value):
		self._ExctnTmStmp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTmStmp', CompareDateTime3, False)

	@ExctnTmStmp.deleter
	def ExctnTmStmp(self):
		del self._ExctnTmStmp
		self._ExctnTmStmp = base_types.UninitialisedField(self, 'ExctnTmStmp', CompareDateTime3, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', CompareDate3, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', CompareDate3, False)

	@property
	def IntraGrp(self):
		return self._IntraGrp

	@IntraGrp.setter
	def IntraGrp(self, value):
		self._IntraGrp = value if value is not None else base_types.UninitialisedField(self, 'IntraGrp', CompareTrueFalseIndicator3, False)

	@IntraGrp.deleter
	def IntraGrp(self):
		del self._IntraGrp
		self._IntraGrp = base_types.UninitialisedField(self, 'IntraGrp', CompareTrueFalseIndicator3, False)

	@property
	def IntrstFltgRateFrstLegCd(self):
		return self._IntrstFltgRateFrstLegCd

	@IntrstFltgRateFrstLegCd.setter
	def IntrstFltgRateFrstLegCd(self, value):
		self._IntrstFltgRateFrstLegCd = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegCd', CompareBenchmarkCode1, False)

	@IntrstFltgRateFrstLegCd.deleter
	def IntrstFltgRateFrstLegCd(self):
		del self._IntrstFltgRateFrstLegCd
		self._IntrstFltgRateFrstLegCd = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegCd', CompareBenchmarkCode1, False)

	@property
	def IntrstFltgRateFrstLegDayCnt(self):
		return self._IntrstFltgRateFrstLegDayCnt

	@IntrstFltgRateFrstLegDayCnt.setter
	def IntrstFltgRateFrstLegDayCnt(self, value):
		self._IntrstFltgRateFrstLegDayCnt = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegDayCnt', CompareDayCount1, False)

	@IntrstFltgRateFrstLegDayCnt.deleter
	def IntrstFltgRateFrstLegDayCnt(self):
		del self._IntrstFltgRateFrstLegDayCnt
		self._IntrstFltgRateFrstLegDayCnt = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegDayCnt', CompareDayCount1, False)

	@property
	def IntrstFltgRateFrstLegId(self):
		return self._IntrstFltgRateFrstLegId

	@IntrstFltgRateFrstLegId.setter
	def IntrstFltgRateFrstLegId(self, value):
		self._IntrstFltgRateFrstLegId = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegId', CompareISINIdentifier4, False)

	@IntrstFltgRateFrstLegId.deleter
	def IntrstFltgRateFrstLegId(self):
		del self._IntrstFltgRateFrstLegId
		self._IntrstFltgRateFrstLegId = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegId', CompareISINIdentifier4, False)

	@property
	def IntrstFltgRateFrstLegNm(self):
		return self._IntrstFltgRateFrstLegNm

	@IntrstFltgRateFrstLegNm.setter
	def IntrstFltgRateFrstLegNm(self, value):
		self._IntrstFltgRateFrstLegNm = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegNm', CompareMax350Text1, False)

	@IntrstFltgRateFrstLegNm.deleter
	def IntrstFltgRateFrstLegNm(self):
		del self._IntrstFltgRateFrstLegNm
		self._IntrstFltgRateFrstLegNm = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegNm', CompareMax350Text1, False)

	@property
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self):
		return self._IntrstFltgRateFrstLegPmtFrqcyUnit

	@IntrstFltgRateFrstLegPmtFrqcyUnit.setter
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self, value):
		self._IntrstFltgRateFrstLegPmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateFrstLegPmtFrqcyUnit.deleter
	def IntrstFltgRateFrstLegPmtFrqcyUnit(self):
		del self._IntrstFltgRateFrstLegPmtFrqcyUnit
		self._IntrstFltgRateFrstLegPmtFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateFrstLegPmtFrqcyVal(self):
		return self._IntrstFltgRateFrstLegPmtFrqcyVal

	@IntrstFltgRateFrstLegPmtFrqcyVal.setter
	def IntrstFltgRateFrstLegPmtFrqcyVal(self, value):
		self._IntrstFltgRateFrstLegPmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegPmtFrqcyVal', CompareNumber5, False)

	@IntrstFltgRateFrstLegPmtFrqcyVal.deleter
	def IntrstFltgRateFrstLegPmtFrqcyVal(self):
		del self._IntrstFltgRateFrstLegPmtFrqcyVal
		self._IntrstFltgRateFrstLegPmtFrqcyVal = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegPmtFrqcyVal', CompareNumber5, False)

	@property
	def IntrstFltgRateFrstLegRefPrdUnit(self):
		return self._IntrstFltgRateFrstLegRefPrdUnit

	@IntrstFltgRateFrstLegRefPrdUnit.setter
	def IntrstFltgRateFrstLegRefPrdUnit(self, value):
		self._IntrstFltgRateFrstLegRefPrdUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRefPrdUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateFrstLegRefPrdUnit.deleter
	def IntrstFltgRateFrstLegRefPrdUnit(self):
		del self._IntrstFltgRateFrstLegRefPrdUnit
		self._IntrstFltgRateFrstLegRefPrdUnit = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRefPrdUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateFrstLegRefPrdVal(self):
		return self._IntrstFltgRateFrstLegRefPrdVal

	@IntrstFltgRateFrstLegRefPrdVal.setter
	def IntrstFltgRateFrstLegRefPrdVal(self, value):
		self._IntrstFltgRateFrstLegRefPrdVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRefPrdVal', CompareNumber5, False)

	@IntrstFltgRateFrstLegRefPrdVal.deleter
	def IntrstFltgRateFrstLegRefPrdVal(self):
		del self._IntrstFltgRateFrstLegRefPrdVal
		self._IntrstFltgRateFrstLegRefPrdVal = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRefPrdVal', CompareNumber5, False)

	@property
	def IntrstFltgRateFrstLegRstFrqcyUnit(self):
		return self._IntrstFltgRateFrstLegRstFrqcyUnit

	@IntrstFltgRateFrstLegRstFrqcyUnit.setter
	def IntrstFltgRateFrstLegRstFrqcyUnit(self, value):
		self._IntrstFltgRateFrstLegRstFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRstFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateFrstLegRstFrqcyUnit.deleter
	def IntrstFltgRateFrstLegRstFrqcyUnit(self):
		del self._IntrstFltgRateFrstLegRstFrqcyUnit
		self._IntrstFltgRateFrstLegRstFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRstFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateFrstLegRstFrqcyVal(self):
		return self._IntrstFltgRateFrstLegRstFrqcyVal

	@IntrstFltgRateFrstLegRstFrqcyVal.setter
	def IntrstFltgRateFrstLegRstFrqcyVal(self, value):
		self._IntrstFltgRateFrstLegRstFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRstFrqcyVal', CompareNumber5, False)

	@IntrstFltgRateFrstLegRstFrqcyVal.deleter
	def IntrstFltgRateFrstLegRstFrqcyVal(self):
		del self._IntrstFltgRateFrstLegRstFrqcyVal
		self._IntrstFltgRateFrstLegRstFrqcyVal = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegRstFrqcyVal', CompareNumber5, False)

	@property
	def IntrstFltgRateFrstLegSprd(self):
		return self._IntrstFltgRateFrstLegSprd

	@IntrstFltgRateFrstLegSprd.setter
	def IntrstFltgRateFrstLegSprd(self, value):
		self._IntrstFltgRateFrstLegSprd = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegSprd', CompareUnitPrice8, False)

	@IntrstFltgRateFrstLegSprd.deleter
	def IntrstFltgRateFrstLegSprd(self):
		del self._IntrstFltgRateFrstLegSprd
		self._IntrstFltgRateFrstLegSprd = base_types.UninitialisedField(self, 'IntrstFltgRateFrstLegSprd', CompareUnitPrice8, False)

	@property
	def IntrstFltgRateScndLegCd(self):
		return self._IntrstFltgRateScndLegCd

	@IntrstFltgRateScndLegCd.setter
	def IntrstFltgRateScndLegCd(self, value):
		self._IntrstFltgRateScndLegCd = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegCd', CompareBenchmarkCode1, False)

	@IntrstFltgRateScndLegCd.deleter
	def IntrstFltgRateScndLegCd(self):
		del self._IntrstFltgRateScndLegCd
		self._IntrstFltgRateScndLegCd = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegCd', CompareBenchmarkCode1, False)

	@property
	def IntrstFltgRateScndLegDayCnt(self):
		return self._IntrstFltgRateScndLegDayCnt

	@IntrstFltgRateScndLegDayCnt.setter
	def IntrstFltgRateScndLegDayCnt(self, value):
		self._IntrstFltgRateScndLegDayCnt = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegDayCnt', CompareDayCount1, False)

	@IntrstFltgRateScndLegDayCnt.deleter
	def IntrstFltgRateScndLegDayCnt(self):
		del self._IntrstFltgRateScndLegDayCnt
		self._IntrstFltgRateScndLegDayCnt = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegDayCnt', CompareDayCount1, False)

	@property
	def IntrstFltgRateScndLegId(self):
		return self._IntrstFltgRateScndLegId

	@IntrstFltgRateScndLegId.setter
	def IntrstFltgRateScndLegId(self, value):
		self._IntrstFltgRateScndLegId = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegId', CompareISINIdentifier4, False)

	@IntrstFltgRateScndLegId.deleter
	def IntrstFltgRateScndLegId(self):
		del self._IntrstFltgRateScndLegId
		self._IntrstFltgRateScndLegId = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegId', CompareISINIdentifier4, False)

	@property
	def IntrstFltgRateScndLegNm(self):
		return self._IntrstFltgRateScndLegNm

	@IntrstFltgRateScndLegNm.setter
	def IntrstFltgRateScndLegNm(self, value):
		self._IntrstFltgRateScndLegNm = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegNm', CompareMax350Text1, False)

	@IntrstFltgRateScndLegNm.deleter
	def IntrstFltgRateScndLegNm(self):
		del self._IntrstFltgRateScndLegNm
		self._IntrstFltgRateScndLegNm = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegNm', CompareMax350Text1, False)

	@property
	def IntrstFltgRateScndLegPmtFrqcyUnit(self):
		return self._IntrstFltgRateScndLegPmtFrqcyUnit

	@IntrstFltgRateScndLegPmtFrqcyUnit.setter
	def IntrstFltgRateScndLegPmtFrqcyUnit(self, value):
		self._IntrstFltgRateScndLegPmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateScndLegPmtFrqcyUnit.deleter
	def IntrstFltgRateScndLegPmtFrqcyUnit(self):
		del self._IntrstFltgRateScndLegPmtFrqcyUnit
		self._IntrstFltgRateScndLegPmtFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateScndLegPmtFrqcyVal(self):
		return self._IntrstFltgRateScndLegPmtFrqcyVal

	@IntrstFltgRateScndLegPmtFrqcyVal.setter
	def IntrstFltgRateScndLegPmtFrqcyVal(self, value):
		self._IntrstFltgRateScndLegPmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegPmtFrqcyVal', CompareNumber5, False)

	@IntrstFltgRateScndLegPmtFrqcyVal.deleter
	def IntrstFltgRateScndLegPmtFrqcyVal(self):
		del self._IntrstFltgRateScndLegPmtFrqcyVal
		self._IntrstFltgRateScndLegPmtFrqcyVal = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegPmtFrqcyVal', CompareNumber5, False)

	@property
	def IntrstFltgRateScndLegRefPrdUnit(self):
		return self._IntrstFltgRateScndLegRefPrdUnit

	@IntrstFltgRateScndLegRefPrdUnit.setter
	def IntrstFltgRateScndLegRefPrdUnit(self, value):
		self._IntrstFltgRateScndLegRefPrdUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRefPrdUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateScndLegRefPrdUnit.deleter
	def IntrstFltgRateScndLegRefPrdUnit(self):
		del self._IntrstFltgRateScndLegRefPrdUnit
		self._IntrstFltgRateScndLegRefPrdUnit = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRefPrdUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateScndLegRefPrdVal(self):
		return self._IntrstFltgRateScndLegRefPrdVal

	@IntrstFltgRateScndLegRefPrdVal.setter
	def IntrstFltgRateScndLegRefPrdVal(self, value):
		self._IntrstFltgRateScndLegRefPrdVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRefPrdVal', CompareNumber5, False)

	@IntrstFltgRateScndLegRefPrdVal.deleter
	def IntrstFltgRateScndLegRefPrdVal(self):
		del self._IntrstFltgRateScndLegRefPrdVal
		self._IntrstFltgRateScndLegRefPrdVal = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRefPrdVal', CompareNumber5, False)

	@property
	def IntrstFltgRateScndLegRstFrqcyUnit(self):
		return self._IntrstFltgRateScndLegRstFrqcyUnit

	@IntrstFltgRateScndLegRstFrqcyUnit.setter
	def IntrstFltgRateScndLegRstFrqcyUnit(self, value):
		self._IntrstFltgRateScndLegRstFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRstFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFltgRateScndLegRstFrqcyUnit.deleter
	def IntrstFltgRateScndLegRstFrqcyUnit(self):
		del self._IntrstFltgRateScndLegRstFrqcyUnit
		self._IntrstFltgRateScndLegRstFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRstFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFltgRateScndLegRstFrqcyVal(self):
		return self._IntrstFltgRateScndLegRstFrqcyVal

	@IntrstFltgRateScndLegRstFrqcyVal.setter
	def IntrstFltgRateScndLegRstFrqcyVal(self, value):
		self._IntrstFltgRateScndLegRstFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRstFrqcyVal', CompareNumber5, False)

	@IntrstFltgRateScndLegRstFrqcyVal.deleter
	def IntrstFltgRateScndLegRstFrqcyVal(self):
		del self._IntrstFltgRateScndLegRstFrqcyVal
		self._IntrstFltgRateScndLegRstFrqcyVal = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegRstFrqcyVal', CompareNumber5, False)

	@property
	def IntrstFltgRateScndLegSprd(self):
		return self._IntrstFltgRateScndLegSprd

	@IntrstFltgRateScndLegSprd.setter
	def IntrstFltgRateScndLegSprd(self, value):
		self._IntrstFltgRateScndLegSprd = value if value is not None else base_types.UninitialisedField(self, 'IntrstFltgRateScndLegSprd', CompareUnitPrice8, False)

	@IntrstFltgRateScndLegSprd.deleter
	def IntrstFltgRateScndLegSprd(self):
		del self._IntrstFltgRateScndLegSprd
		self._IntrstFltgRateScndLegSprd = base_types.UninitialisedField(self, 'IntrstFltgRateScndLegSprd', CompareUnitPrice8, False)

	@property
	def IntrstFxdRateFrstLeg(self):
		return self._IntrstFxdRateFrstLeg

	@IntrstFxdRateFrstLeg.setter
	def IntrstFxdRateFrstLeg(self, value):
		self._IntrstFxdRateFrstLeg = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateFrstLeg', CompareUnitPrice7, False)

	@IntrstFxdRateFrstLeg.deleter
	def IntrstFxdRateFrstLeg(self):
		del self._IntrstFxdRateFrstLeg
		self._IntrstFxdRateFrstLeg = base_types.UninitialisedField(self, 'IntrstFxdRateFrstLeg', CompareUnitPrice7, False)

	@property
	def IntrstFxdRateFrstLegDayCnt(self):
		return self._IntrstFxdRateFrstLegDayCnt

	@IntrstFxdRateFrstLegDayCnt.setter
	def IntrstFxdRateFrstLegDayCnt(self, value):
		self._IntrstFxdRateFrstLegDayCnt = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegDayCnt', CompareDayCount1, False)

	@IntrstFxdRateFrstLegDayCnt.deleter
	def IntrstFxdRateFrstLegDayCnt(self):
		del self._IntrstFxdRateFrstLegDayCnt
		self._IntrstFxdRateFrstLegDayCnt = base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegDayCnt', CompareDayCount1, False)

	@property
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self):
		return self._IntrstFxdRateFrstLegPmtFrqcyUnit

	@IntrstFxdRateFrstLegPmtFrqcyUnit.setter
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self, value):
		self._IntrstFxdRateFrstLegPmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFxdRateFrstLegPmtFrqcyUnit.deleter
	def IntrstFxdRateFrstLegPmtFrqcyUnit(self):
		del self._IntrstFxdRateFrstLegPmtFrqcyUnit
		self._IntrstFxdRateFrstLegPmtFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFxdRateFrstLegPmtFrqcyVal(self):
		return self._IntrstFxdRateFrstLegPmtFrqcyVal

	@IntrstFxdRateFrstLegPmtFrqcyVal.setter
	def IntrstFxdRateFrstLegPmtFrqcyVal(self, value):
		self._IntrstFxdRateFrstLegPmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegPmtFrqcyVal', CompareNumber5, False)

	@IntrstFxdRateFrstLegPmtFrqcyVal.deleter
	def IntrstFxdRateFrstLegPmtFrqcyVal(self):
		del self._IntrstFxdRateFrstLegPmtFrqcyVal
		self._IntrstFxdRateFrstLegPmtFrqcyVal = base_types.UninitialisedField(self, 'IntrstFxdRateFrstLegPmtFrqcyVal', CompareNumber5, False)

	@property
	def IntrstFxdRateScndLegDayCnt(self):
		return self._IntrstFxdRateScndLegDayCnt

	@IntrstFxdRateScndLegDayCnt.setter
	def IntrstFxdRateScndLegDayCnt(self, value):
		self._IntrstFxdRateScndLegDayCnt = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateScndLegDayCnt', CompareDayCount1, False)

	@IntrstFxdRateScndLegDayCnt.deleter
	def IntrstFxdRateScndLegDayCnt(self):
		del self._IntrstFxdRateScndLegDayCnt
		self._IntrstFxdRateScndLegDayCnt = base_types.UninitialisedField(self, 'IntrstFxdRateScndLegDayCnt', CompareDayCount1, False)

	@property
	def IntrstFxdRateScndLegPmtFrqcyUnit(self):
		return self._IntrstFxdRateScndLegPmtFrqcyUnit

	@IntrstFxdRateScndLegPmtFrqcyUnit.setter
	def IntrstFxdRateScndLegPmtFrqcyUnit(self, value):
		self._IntrstFxdRateScndLegPmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateScndLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@IntrstFxdRateScndLegPmtFrqcyUnit.deleter
	def IntrstFxdRateScndLegPmtFrqcyUnit(self):
		del self._IntrstFxdRateScndLegPmtFrqcyUnit
		self._IntrstFxdRateScndLegPmtFrqcyUnit = base_types.UninitialisedField(self, 'IntrstFxdRateScndLegPmtFrqcyUnit', CompareFrequencyUnit1, False)

	@property
	def IntrstFxdRateScndLegPmtFrqcyVal(self):
		return self._IntrstFxdRateScndLegPmtFrqcyVal

	@IntrstFxdRateScndLegPmtFrqcyVal.setter
	def IntrstFxdRateScndLegPmtFrqcyVal(self, value):
		self._IntrstFxdRateScndLegPmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxdRateScndLegPmtFrqcyVal', CompareNumber5, False)

	@IntrstFxdRateScndLegPmtFrqcyVal.deleter
	def IntrstFxdRateScndLegPmtFrqcyVal(self):
		del self._IntrstFxdRateScndLegPmtFrqcyVal
		self._IntrstFxdRateScndLegPmtFrqcyVal = base_types.UninitialisedField(self, 'IntrstFxdRateScndLegPmtFrqcyVal', CompareNumber5, False)

	@property
	def IntrstRateFxdScndLeg(self):
		return self._IntrstRateFxdScndLeg

	@IntrstRateFxdScndLeg.setter
	def IntrstRateFxdScndLeg(self, value):
		self._IntrstRateFxdScndLeg = value if value is not None else base_types.UninitialisedField(self, 'IntrstRateFxdScndLeg', CompareUnitPrice7, False)

	@IntrstRateFxdScndLeg.deleter
	def IntrstRateFxdScndLeg(self):
		del self._IntrstRateFxdScndLeg
		self._IntrstRateFxdScndLeg = base_types.UninitialisedField(self, 'IntrstRateFxdScndLeg', CompareUnitPrice7, False)

	@property
	def Lvl(self):
		return self._Lvl

	@Lvl.setter
	def Lvl(self, value):
		self._Lvl = value if value is not None else base_types.UninitialisedField(self, 'Lvl', CompareReportingLevelType2, False)

	@Lvl.deleter
	def Lvl(self):
		del self._Lvl
		self._Lvl = base_types.UninitialisedField(self, 'Lvl', CompareReportingLevelType2, False)

	@property
	def MstrAgrmtTp(self):
		return self._MstrAgrmtTp

	@MstrAgrmtTp.setter
	def MstrAgrmtTp(self, value):
		self._MstrAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmtTp', CompareMasterAgreementType1, False)

	@MstrAgrmtTp.deleter
	def MstrAgrmtTp(self):
		del self._MstrAgrmtTp
		self._MstrAgrmtTp = base_types.UninitialisedField(self, 'MstrAgrmtTp', CompareMasterAgreementType1, False)

	@property
	def MstrAgrmtVrsn(self):
		return self._MstrAgrmtVrsn

	@MstrAgrmtVrsn.setter
	def MstrAgrmtVrsn(self, value):
		self._MstrAgrmtVrsn = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmtVrsn', CompareMax50Text1, False)

	@MstrAgrmtVrsn.deleter
	def MstrAgrmtVrsn(self):
		del self._MstrAgrmtVrsn
		self._MstrAgrmtVrsn = base_types.UninitialisedField(self, 'MstrAgrmtVrsn', CompareMax50Text1, False)

	@property
	def NrgyDlvryPtOrZone(self):
		return self._NrgyDlvryPtOrZone

	@NrgyDlvryPtOrZone.setter
	def NrgyDlvryPtOrZone(self, value):
		self._NrgyDlvryPtOrZone = value if value is not None else base_types.UninitialisedField(self, 'NrgyDlvryPtOrZone', CompareDeliveryInterconnectionPoint1, True)

	@NrgyDlvryPtOrZone.deleter
	def NrgyDlvryPtOrZone(self):
		del self._NrgyDlvryPtOrZone
		self._NrgyDlvryPtOrZone = base_types.UninitialisedField(self, 'NrgyDlvryPtOrZone', CompareDeliveryInterconnectionPoint1, True)

	@property
	def NrgyIntrCnnctnPt(self):
		return self._NrgyIntrCnnctnPt

	@NrgyIntrCnnctnPt.setter
	def NrgyIntrCnnctnPt(self, value):
		self._NrgyIntrCnnctnPt = value if value is not None else base_types.UninitialisedField(self, 'NrgyIntrCnnctnPt', CompareDeliveryInterconnectionPoint1, False)

	@NrgyIntrCnnctnPt.deleter
	def NrgyIntrCnnctnPt(self):
		del self._NrgyIntrCnnctnPt
		self._NrgyIntrCnnctnPt = base_types.UninitialisedField(self, 'NrgyIntrCnnctnPt', CompareDeliveryInterconnectionPoint1, False)

	@property
	def NrgyLdTp(self):
		return self._NrgyLdTp

	@NrgyLdTp.setter
	def NrgyLdTp(self, value):
		self._NrgyLdTp = value if value is not None else base_types.UninitialisedField(self, 'NrgyLdTp', CompareEnergyLoadType1, False)

	@NrgyLdTp.deleter
	def NrgyLdTp(self):
		del self._NrgyLdTp
		self._NrgyLdTp = base_types.UninitialisedField(self, 'NrgyLdTp', CompareEnergyLoadType1, False)

	@property
	def NtnlAmtFrstLeg(self):
		return self._NtnlAmtFrstLeg

	@NtnlAmtFrstLeg.setter
	def NtnlAmtFrstLeg(self, value):
		self._NtnlAmtFrstLeg = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtFrstLeg', CompareAmountAndDirection3, False)

	@NtnlAmtFrstLeg.deleter
	def NtnlAmtFrstLeg(self):
		del self._NtnlAmtFrstLeg
		self._NtnlAmtFrstLeg = base_types.UninitialisedField(self, 'NtnlAmtFrstLeg', CompareAmountAndDirection3, False)

	@property
	def NtnlAmtFrstLegSchdlAmt(self):
		return self._NtnlAmtFrstLegSchdlAmt

	@NtnlAmtFrstLegSchdlAmt.setter
	def NtnlAmtFrstLegSchdlAmt(self, value):
		self._NtnlAmtFrstLegSchdlAmt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtFrstLegSchdlAmt', CompareAmountAndDirection3, True)

	@NtnlAmtFrstLegSchdlAmt.deleter
	def NtnlAmtFrstLegSchdlAmt(self):
		del self._NtnlAmtFrstLegSchdlAmt
		self._NtnlAmtFrstLegSchdlAmt = base_types.UninitialisedField(self, 'NtnlAmtFrstLegSchdlAmt', CompareAmountAndDirection3, True)

	@property
	def NtnlAmtFrstLegUadjstdEndDt(self):
		return self._NtnlAmtFrstLegUadjstdEndDt

	@NtnlAmtFrstLegUadjstdEndDt.setter
	def NtnlAmtFrstLegUadjstdEndDt(self, value):
		self._NtnlAmtFrstLegUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtFrstLegUadjstdEndDt', CompareDate3, True)

	@NtnlAmtFrstLegUadjstdEndDt.deleter
	def NtnlAmtFrstLegUadjstdEndDt(self):
		del self._NtnlAmtFrstLegUadjstdEndDt
		self._NtnlAmtFrstLegUadjstdEndDt = base_types.UninitialisedField(self, 'NtnlAmtFrstLegUadjstdEndDt', CompareDate3, True)

	@property
	def NtnlAmtFrstLegUadjstdFctvDt(self):
		return self._NtnlAmtFrstLegUadjstdFctvDt

	@NtnlAmtFrstLegUadjstdFctvDt.setter
	def NtnlAmtFrstLegUadjstdFctvDt(self, value):
		self._NtnlAmtFrstLegUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtFrstLegUadjstdFctvDt', CompareDate3, True)

	@NtnlAmtFrstLegUadjstdFctvDt.deleter
	def NtnlAmtFrstLegUadjstdFctvDt(self):
		del self._NtnlAmtFrstLegUadjstdFctvDt
		self._NtnlAmtFrstLegUadjstdFctvDt = base_types.UninitialisedField(self, 'NtnlAmtFrstLegUadjstdFctvDt', CompareDate3, True)

	@property
	def NtnlAmtScndLeg(self):
		return self._NtnlAmtScndLeg

	@NtnlAmtScndLeg.setter
	def NtnlAmtScndLeg(self, value):
		self._NtnlAmtScndLeg = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtScndLeg', CompareAmountAndDirection3, False)

	@NtnlAmtScndLeg.deleter
	def NtnlAmtScndLeg(self):
		del self._NtnlAmtScndLeg
		self._NtnlAmtScndLeg = base_types.UninitialisedField(self, 'NtnlAmtScndLeg', CompareAmountAndDirection3, False)

	@property
	def NtnlAmtScndLegSchdlAmt(self):
		return self._NtnlAmtScndLegSchdlAmt

	@NtnlAmtScndLegSchdlAmt.setter
	def NtnlAmtScndLegSchdlAmt(self, value):
		self._NtnlAmtScndLegSchdlAmt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtScndLegSchdlAmt', CompareAmountAndDirection3, True)

	@NtnlAmtScndLegSchdlAmt.deleter
	def NtnlAmtScndLegSchdlAmt(self):
		del self._NtnlAmtScndLegSchdlAmt
		self._NtnlAmtScndLegSchdlAmt = base_types.UninitialisedField(self, 'NtnlAmtScndLegSchdlAmt', CompareAmountAndDirection3, True)

	@property
	def NtnlAmtScndLegUadjstdEndDt(self):
		return self._NtnlAmtScndLegUadjstdEndDt

	@NtnlAmtScndLegUadjstdEndDt.setter
	def NtnlAmtScndLegUadjstdEndDt(self, value):
		self._NtnlAmtScndLegUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtScndLegUadjstdEndDt', CompareDate3, True)

	@NtnlAmtScndLegUadjstdEndDt.deleter
	def NtnlAmtScndLegUadjstdEndDt(self):
		del self._NtnlAmtScndLegUadjstdEndDt
		self._NtnlAmtScndLegUadjstdEndDt = base_types.UninitialisedField(self, 'NtnlAmtScndLegUadjstdEndDt', CompareDate3, True)

	@property
	def NtnlAmtScndLegUadjstdFctvDt(self):
		return self._NtnlAmtScndLegUadjstdFctvDt

	@NtnlAmtScndLegUadjstdFctvDt.setter
	def NtnlAmtScndLegUadjstdFctvDt(self, value):
		self._NtnlAmtScndLegUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmtScndLegUadjstdFctvDt', CompareDate3, True)

	@NtnlAmtScndLegUadjstdFctvDt.deleter
	def NtnlAmtScndLegUadjstdFctvDt(self):
		del self._NtnlAmtScndLegUadjstdFctvDt
		self._NtnlAmtScndLegUadjstdFctvDt = base_types.UninitialisedField(self, 'NtnlAmtScndLegUadjstdFctvDt', CompareDate3, True)

	@property
	def NtnlQtyFrstLeg(self):
		return self._NtnlQtyFrstLeg

	@NtnlQtyFrstLeg.setter
	def NtnlQtyFrstLeg(self, value):
		self._NtnlQtyFrstLeg = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyFrstLeg', CompareLongFraction19DecimalNumber1, False)

	@NtnlQtyFrstLeg.deleter
	def NtnlQtyFrstLeg(self):
		del self._NtnlQtyFrstLeg
		self._NtnlQtyFrstLeg = base_types.UninitialisedField(self, 'NtnlQtyFrstLeg', CompareLongFraction19DecimalNumber1, False)

	@property
	def NtnlQtyFrstLegSchdlQty(self):
		return self._NtnlQtyFrstLegSchdlQty

	@NtnlQtyFrstLegSchdlQty.setter
	def NtnlQtyFrstLegSchdlQty(self, value):
		self._NtnlQtyFrstLegSchdlQty = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyFrstLegSchdlQty', CompareLongFraction19DecimalNumber1, True)

	@NtnlQtyFrstLegSchdlQty.deleter
	def NtnlQtyFrstLegSchdlQty(self):
		del self._NtnlQtyFrstLegSchdlQty
		self._NtnlQtyFrstLegSchdlQty = base_types.UninitialisedField(self, 'NtnlQtyFrstLegSchdlQty', CompareLongFraction19DecimalNumber1, True)

	@property
	def NtnlQtyFrstLegUadjstdEndDt(self):
		return self._NtnlQtyFrstLegUadjstdEndDt

	@NtnlQtyFrstLegUadjstdEndDt.setter
	def NtnlQtyFrstLegUadjstdEndDt(self, value):
		self._NtnlQtyFrstLegUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyFrstLegUadjstdEndDt', CompareDate3, True)

	@NtnlQtyFrstLegUadjstdEndDt.deleter
	def NtnlQtyFrstLegUadjstdEndDt(self):
		del self._NtnlQtyFrstLegUadjstdEndDt
		self._NtnlQtyFrstLegUadjstdEndDt = base_types.UninitialisedField(self, 'NtnlQtyFrstLegUadjstdEndDt', CompareDate3, True)

	@property
	def NtnlQtyFrstLegUadjstdFctvDt(self):
		return self._NtnlQtyFrstLegUadjstdFctvDt

	@NtnlQtyFrstLegUadjstdFctvDt.setter
	def NtnlQtyFrstLegUadjstdFctvDt(self, value):
		self._NtnlQtyFrstLegUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyFrstLegUadjstdFctvDt', CompareDate3, True)

	@NtnlQtyFrstLegUadjstdFctvDt.deleter
	def NtnlQtyFrstLegUadjstdFctvDt(self):
		del self._NtnlQtyFrstLegUadjstdFctvDt
		self._NtnlQtyFrstLegUadjstdFctvDt = base_types.UninitialisedField(self, 'NtnlQtyFrstLegUadjstdFctvDt', CompareDate3, True)

	@property
	def NtnlQtyScndLeg(self):
		return self._NtnlQtyScndLeg

	@NtnlQtyScndLeg.setter
	def NtnlQtyScndLeg(self, value):
		self._NtnlQtyScndLeg = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyScndLeg', CompareLongFraction19DecimalNumber1, False)

	@NtnlQtyScndLeg.deleter
	def NtnlQtyScndLeg(self):
		del self._NtnlQtyScndLeg
		self._NtnlQtyScndLeg = base_types.UninitialisedField(self, 'NtnlQtyScndLeg', CompareLongFraction19DecimalNumber1, False)

	@property
	def NtnlQtyScndLegSchdlQty(self):
		return self._NtnlQtyScndLegSchdlQty

	@NtnlQtyScndLegSchdlQty.setter
	def NtnlQtyScndLegSchdlQty(self, value):
		self._NtnlQtyScndLegSchdlQty = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyScndLegSchdlQty', CompareLongFraction19DecimalNumber1, True)

	@NtnlQtyScndLegSchdlQty.deleter
	def NtnlQtyScndLegSchdlQty(self):
		del self._NtnlQtyScndLegSchdlQty
		self._NtnlQtyScndLegSchdlQty = base_types.UninitialisedField(self, 'NtnlQtyScndLegSchdlQty', CompareLongFraction19DecimalNumber1, True)

	@property
	def NtnlQtyScndLegUadjstdEndDt(self):
		return self._NtnlQtyScndLegUadjstdEndDt

	@NtnlQtyScndLegUadjstdEndDt.setter
	def NtnlQtyScndLegUadjstdEndDt(self, value):
		self._NtnlQtyScndLegUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyScndLegUadjstdEndDt', CompareDate3, True)

	@NtnlQtyScndLegUadjstdEndDt.deleter
	def NtnlQtyScndLegUadjstdEndDt(self):
		del self._NtnlQtyScndLegUadjstdEndDt
		self._NtnlQtyScndLegUadjstdEndDt = base_types.UninitialisedField(self, 'NtnlQtyScndLegUadjstdEndDt', CompareDate3, True)

	@property
	def NtnlQtyScndLegUadjstdFctvDt(self):
		return self._NtnlQtyScndLegUadjstdFctvDt

	@NtnlQtyScndLegUadjstdFctvDt.setter
	def NtnlQtyScndLegUadjstdFctvDt(self, value):
		self._NtnlQtyScndLegUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'NtnlQtyScndLegUadjstdFctvDt', CompareDate3, True)

	@NtnlQtyScndLegUadjstdFctvDt.deleter
	def NtnlQtyScndLegUadjstdFctvDt(self):
		del self._NtnlQtyScndLegUadjstdFctvDt
		self._NtnlQtyScndLegUadjstdFctvDt = base_types.UninitialisedField(self, 'NtnlQtyScndLegUadjstdFctvDt', CompareDate3, True)

	@property
	def OptnExrcStyle(self):
		return self._OptnExrcStyle

	@OptnExrcStyle.setter
	def OptnExrcStyle(self, value):
		self._OptnExrcStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnExrcStyle', CompareOptionStyle1, True)

	@OptnExrcStyle.deleter
	def OptnExrcStyle(self):
		del self._OptnExrcStyle
		self._OptnExrcStyle = base_types.UninitialisedField(self, 'OptnExrcStyle', CompareOptionStyle1, True)

	@property
	def OptnMtrtyDtOfUndrlyg(self):
		return self._OptnMtrtyDtOfUndrlyg

	@OptnMtrtyDtOfUndrlyg.setter
	def OptnMtrtyDtOfUndrlyg(self, value):
		self._OptnMtrtyDtOfUndrlyg = value if value is not None else base_types.UninitialisedField(self, 'OptnMtrtyDtOfUndrlyg', CompareDate3, False)

	@OptnMtrtyDtOfUndrlyg.deleter
	def OptnMtrtyDtOfUndrlyg(self):
		del self._OptnMtrtyDtOfUndrlyg
		self._OptnMtrtyDtOfUndrlyg = base_types.UninitialisedField(self, 'OptnMtrtyDtOfUndrlyg', CompareDate3, False)

	@property
	def OptnPrmAmt(self):
		return self._OptnPrmAmt

	@OptnPrmAmt.setter
	def OptnPrmAmt(self, value):
		self._OptnPrmAmt = value if value is not None else base_types.UninitialisedField(self, 'OptnPrmAmt', CompareActiveOrHistoricCurrencyAndAmount4, False)

	@OptnPrmAmt.deleter
	def OptnPrmAmt(self):
		del self._OptnPrmAmt
		self._OptnPrmAmt = base_types.UninitialisedField(self, 'OptnPrmAmt', CompareActiveOrHistoricCurrencyAndAmount4, False)

	@property
	def OptnPrmPmtDt(self):
		return self._OptnPrmPmtDt

	@OptnPrmPmtDt.setter
	def OptnPrmPmtDt(self, value):
		self._OptnPrmPmtDt = value if value is not None else base_types.UninitialisedField(self, 'OptnPrmPmtDt', CompareDate3, False)

	@OptnPrmPmtDt.deleter
	def OptnPrmPmtDt(self):
		del self._OptnPrmPmtDt
		self._OptnPrmPmtDt = base_types.UninitialisedField(self, 'OptnPrmPmtDt', CompareDate3, False)

	@property
	def OptnStrkPric(self):
		return self._OptnStrkPric

	@OptnStrkPric.setter
	def OptnStrkPric(self, value):
		self._OptnStrkPric = value if value is not None else base_types.UninitialisedField(self, 'OptnStrkPric', CompareUnitPrice4, False)

	@OptnStrkPric.deleter
	def OptnStrkPric(self):
		del self._OptnStrkPric
		self._OptnStrkPric = base_types.UninitialisedField(self, 'OptnStrkPric', CompareUnitPrice4, False)

	@property
	def OptnStrkPricSchdlAmt(self):
		return self._OptnStrkPricSchdlAmt

	@OptnStrkPricSchdlAmt.setter
	def OptnStrkPricSchdlAmt(self, value):
		self._OptnStrkPricSchdlAmt = value if value is not None else base_types.UninitialisedField(self, 'OptnStrkPricSchdlAmt', CompareUnitPrice4, True)

	@OptnStrkPricSchdlAmt.deleter
	def OptnStrkPricSchdlAmt(self):
		del self._OptnStrkPricSchdlAmt
		self._OptnStrkPricSchdlAmt = base_types.UninitialisedField(self, 'OptnStrkPricSchdlAmt', CompareUnitPrice4, True)

	@property
	def OptnStrkPricSchdlUadjstdEndDt(self):
		return self._OptnStrkPricSchdlUadjstdEndDt

	@OptnStrkPricSchdlUadjstdEndDt.setter
	def OptnStrkPricSchdlUadjstdEndDt(self, value):
		self._OptnStrkPricSchdlUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'OptnStrkPricSchdlUadjstdEndDt', CompareDate3, True)

	@OptnStrkPricSchdlUadjstdEndDt.deleter
	def OptnStrkPricSchdlUadjstdEndDt(self):
		del self._OptnStrkPricSchdlUadjstdEndDt
		self._OptnStrkPricSchdlUadjstdEndDt = base_types.UninitialisedField(self, 'OptnStrkPricSchdlUadjstdEndDt', CompareDate3, True)

	@property
	def OptnStrkPricSchdlUadjstdFctvDt(self):
		return self._OptnStrkPricSchdlUadjstdFctvDt

	@OptnStrkPricSchdlUadjstdFctvDt.setter
	def OptnStrkPricSchdlUadjstdFctvDt(self, value):
		self._OptnStrkPricSchdlUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'OptnStrkPricSchdlUadjstdFctvDt', CompareDate3, True)

	@OptnStrkPricSchdlUadjstdFctvDt.deleter
	def OptnStrkPricSchdlUadjstdFctvDt(self):
		del self._OptnStrkPricSchdlUadjstdFctvDt
		self._OptnStrkPricSchdlUadjstdFctvDt = base_types.UninitialisedField(self, 'OptnStrkPricSchdlUadjstdFctvDt', CompareDate3, True)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CompareOptionType1, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CompareOptionType1, False)

	@property
	def OthrPmt(self):
		return self._OthrPmt

	@OthrPmt.setter
	def OthrPmt(self, value):
		self._OthrPmt = value if value is not None else base_types.UninitialisedField(self, 'OthrPmt', CompareOtherPayment1, True)

	@OthrPmt.deleter
	def OthrPmt(self):
		del self._OthrPmt
		self._OthrPmt = base_types.UninitialisedField(self, 'OthrPmt', CompareOtherPayment1, True)

	@property
	def PackgPric(self):
		return self._PackgPric

	@PackgPric.setter
	def PackgPric(self, value):
		self._PackgPric = value if value is not None else base_types.UninitialisedField(self, 'PackgPric', CompareUnitPrice5, False)

	@PackgPric.deleter
	def PackgPric(self):
		del self._PackgPric
		self._PackgPric = base_types.UninitialisedField(self, 'PackgPric', CompareUnitPrice5, False)

	@property
	def PackgSprd(self):
		return self._PackgSprd

	@PackgSprd.setter
	def PackgSprd(self, value):
		self._PackgSprd = value if value is not None else base_types.UninitialisedField(self, 'PackgSprd', CompareUnitPrice8, False)

	@PackgSprd.deleter
	def PackgSprd(self):
		del self._PackgSprd
		self._PackgSprd = base_types.UninitialisedField(self, 'PackgSprd', CompareUnitPrice8, False)

	@property
	def PltfmIdr(self):
		return self._PltfmIdr

	@PltfmIdr.setter
	def PltfmIdr(self, value):
		self._PltfmIdr = value if value is not None else base_types.UninitialisedField(self, 'PltfmIdr', CompareMICIdentifier3, False)

	@PltfmIdr.deleter
	def PltfmIdr(self):
		del self._PltfmIdr
		self._PltfmIdr = base_types.UninitialisedField(self, 'PltfmIdr', CompareMICIdentifier3, False)

	@property
	def PricSchdlUadjstdEndDt(self):
		return self._PricSchdlUadjstdEndDt

	@PricSchdlUadjstdEndDt.setter
	def PricSchdlUadjstdEndDt(self, value):
		self._PricSchdlUadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'PricSchdlUadjstdEndDt', CompareDate3, True)

	@PricSchdlUadjstdEndDt.deleter
	def PricSchdlUadjstdEndDt(self):
		del self._PricSchdlUadjstdEndDt
		self._PricSchdlUadjstdEndDt = base_types.UninitialisedField(self, 'PricSchdlUadjstdEndDt', CompareDate3, True)

	@property
	def PricSchdlUadjstdFctvDt(self):
		return self._PricSchdlUadjstdFctvDt

	@PricSchdlUadjstdFctvDt.setter
	def PricSchdlUadjstdFctvDt(self, value):
		self._PricSchdlUadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'PricSchdlUadjstdFctvDt', CompareDate3, True)

	@PricSchdlUadjstdFctvDt.deleter
	def PricSchdlUadjstdFctvDt(self):
		del self._PricSchdlUadjstdFctvDt
		self._PricSchdlUadjstdFctvDt = base_types.UninitialisedField(self, 'PricSchdlUadjstdFctvDt', CompareDate3, True)

	@property
	def PrrUnqTxIdr(self):
		return self._PrrUnqTxIdr

	@PrrUnqTxIdr.setter
	def PrrUnqTxIdr(self, value):
		self._PrrUnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'PrrUnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@PrrUnqTxIdr.deleter
	def PrrUnqTxIdr(self):
		del self._PrrUnqTxIdr
		self._PrrUnqTxIdr = base_types.UninitialisedField(self, 'PrrUnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@property
	def PstTradRskRdctn(self):
		return self._PstTradRskRdctn

	@PstTradRskRdctn.setter
	def PstTradRskRdctn(self, value):
		self._PstTradRskRdctn = value if value is not None else base_types.UninitialisedField(self, 'PstTradRskRdctn', ComparePostTradeRiskReduction2, False)

	@PstTradRskRdctn.deleter
	def PstTradRskRdctn(self):
		del self._PstTradRskRdctn
		self._PstTradRskRdctn = base_types.UninitialisedField(self, 'PstTradRskRdctn', ComparePostTradeRiskReduction2, False)

	@property
	def RptTrckgNb(self):
		return self._RptTrckgNb

	@RptTrckgNb.setter
	def RptTrckgNb(self, value):
		self._RptTrckgNb = value if value is not None else base_types.UninitialisedField(self, 'RptTrckgNb', CompareText2, False)

	@RptTrckgNb.deleter
	def RptTrckgNb(self):
		del self._RptTrckgNb
		self._RptTrckgNb = base_types.UninitialisedField(self, 'RptTrckgNb', CompareText2, False)

	@property
	def SbsqntPosUnqTxIdr(self):
		return self._SbsqntPosUnqTxIdr

	@SbsqntPosUnqTxIdr.setter
	def SbsqntPosUnqTxIdr(self, value):
		self._SbsqntPosUnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'SbsqntPosUnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@SbsqntPosUnqTxIdr.deleter
	def SbsqntPosUnqTxIdr(self):
		del self._SbsqntPosUnqTxIdr
		self._SbsqntPosUnqTxIdr = base_types.UninitialisedField(self, 'SbsqntPosUnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', CompareDate3, True)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', CompareDate3, True)

	@property
	def TradClrOblgtn(self):
		return self._TradClrOblgtn

	@TradClrOblgtn.setter
	def TradClrOblgtn(self, value):
		self._TradClrOblgtn = value if value is not None else base_types.UninitialisedField(self, 'TradClrOblgtn', CompareTradeClearingObligation1, False)

	@TradClrOblgtn.deleter
	def TradClrOblgtn(self):
		del self._TradClrOblgtn
		self._TradClrOblgtn = base_types.UninitialisedField(self, 'TradClrOblgtn', CompareTradeClearingObligation1, False)

	@property
	def TradClrSts(self):
		return self._TradClrSts

	@TradClrSts.setter
	def TradClrSts(self, value):
		self._TradClrSts = value if value is not None else base_types.UninitialisedField(self, 'TradClrSts', CompareTradeClearingStatus3, False)

	@TradClrSts.deleter
	def TradClrSts(self):
		del self._TradClrSts
		self._TradClrSts = base_types.UninitialisedField(self, 'TradClrSts', CompareTradeClearingStatus3, False)

	@property
	def TradConf(self):
		return self._TradConf

	@TradConf.setter
	def TradConf(self, value):
		self._TradConf = value if value is not None else base_types.UninitialisedField(self, 'TradConf', CompareTradeConfirmation2, False)

	@TradConf.deleter
	def TradConf(self):
		del self._TradConf
		self._TradConf = base_types.UninitialisedField(self, 'TradConf', CompareTradeConfirmation2, False)

	@property
	def TxPric(self):
		return self._TxPric

	@TxPric.setter
	def TxPric(self, value):
		self._TxPric = value if value is not None else base_types.UninitialisedField(self, 'TxPric', CompareUnitPrice5, False)

	@TxPric.deleter
	def TxPric(self):
		del self._TxPric
		self._TxPric = base_types.UninitialisedField(self, 'TxPric', CompareUnitPrice5, False)

	@property
	def TxSchdlPric(self):
		return self._TxSchdlPric

	@TxSchdlPric.setter
	def TxSchdlPric(self, value):
		self._TxSchdlPric = value if value is not None else base_types.UninitialisedField(self, 'TxSchdlPric', CompareUnitPrice5, True)

	@TxSchdlPric.deleter
	def TxSchdlPric(self):
		del self._TxSchdlPric
		self._TxSchdlPric = base_types.UninitialisedField(self, 'TxSchdlPric', CompareUnitPrice5, True)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', CompareUniqueTransactionIdentifier2, False)

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if value is not None else base_types.UninitialisedField(self, 'XprtnDt', CompareDate3, False)

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = base_types.UninitialisedField(self, 'XprtnDt', CompareDate3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyFwdXchgRate', type=CompareExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchgRate', type=CompareExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchgRateBsis', type=CompareExchangeRateBasis1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtIndxFctr', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRefPty', type=CompareReferenceParty1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtSnrty', type=CompareSeniorityType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtSrs', type=CompareNumber7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTrch', type=CompareTrancheIndicator1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtVrsn', type=CompareNumber7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=CompareCommodityAssetClass4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvt', type=CompareDerivativeEvent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dlta', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAttr', type=CompareEnergyDeliveryAttribute1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryTp', type=CompareDeliveryType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyTermntnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTmStmp', type=CompareDateTime3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraGrp', type=CompareTrueFalseIndicator3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegCd', type=CompareBenchmarkCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegId', type=CompareISINIdentifier4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegNm', type=CompareMax350Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRefPrdUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRefPrdVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRstFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegRstFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateFrstLegSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegCd', type=CompareBenchmarkCode1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegId', type=CompareISINIdentifier4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegNm', type=CompareMax350Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRefPrdUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRefPrdVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRstFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegRstFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFltgRateScndLegSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLeg', type=CompareUnitPrice7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateFrstLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegDayCnt', type=CompareDayCount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegPmtFrqcyUnit', type=CompareFrequencyUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxdRateScndLegPmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateFxdScndLeg', type=CompareUnitPrice7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lvl', type=CompareReportingLevelType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtTp', type=CompareMasterAgreementType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtVrsn', type=CompareMax50Text1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDlvryPtOrZone', type=CompareDeliveryInterconnectionPoint1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrgyIntrCnnctnPt', type=CompareDeliveryInterconnectionPoint1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyLdTp', type=CompareEnergyLoadType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLeg', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtFrstLegSchdlAmt', type=CompareAmountAndDirection3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtFrstLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtFrstLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtScndLeg', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmtScndLegSchdlAmt', type=CompareAmountAndDirection3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtScndLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmtScndLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyFrstLeg', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyFrstLegSchdlQty', type=CompareLongFraction19DecimalNumber1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyFrstLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyFrstLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyScndLeg', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQtyScndLegSchdlQty', type=CompareLongFraction19DecimalNumber1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyScndLegUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlQtyScndLegUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnExrcStyle', type=CompareOptionStyle1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnMtrtyDtOfUndrlyg', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrmAmt', type=CompareActiveOrHistoricCurrencyAndAmount4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPrmPmtDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStrkPric', type=CompareUnitPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStrkPricSchdlAmt', type=CompareUnitPrice4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnStrkPricSchdlUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnStrkPricSchdlUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnTp', type=CompareOptionType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmt', type=CompareOtherPayment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PackgPric', type=CompareUnitPrice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgSprd', type=CompareUnitPrice8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltfmIdr', type=CompareMICIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSchdlUadjstdEndDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricSchdlUadjstdFctvDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrrUnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctn', type=ComparePostTradeRiskReduction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTrckgNb', type=CompareText2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntPosUnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=CompareDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradClrOblgtn', type=CompareTradeClearingObligation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradClrSts', type=CompareTradeClearingStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradConf', type=CompareTradeConfirmation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxPric', type=CompareUnitPrice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSchdlPric', type=CompareUnitPrice5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqTxIdr', type=CompareUniqueTransactionIdentifier2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
	))