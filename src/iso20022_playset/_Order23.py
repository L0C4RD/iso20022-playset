# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection29
from . import BusinessProcessType2Choice
from . import CallIn1Code
from . import CashMarginOrder1Code
from . import ChargeTaxBasisType2Choice
from . import Commission25
from . import CurrencyToBuyOrSell1Choice
from . import DateAndDateTime1Choice
from . import DeliveryReceiptType2Code
from . import EUCapitalGainType3Choice
from . import Eligibility1Code
from . import ISODate
from . import ISODateTime
from . import InterestType2Code
from . import MarketIdentification93
from . import MatchingStatus27Choice
from . import Max350Text
from . import Max35Text
from . import Max3Number
from . import PartialFill4
from . import PercentageRate
from . import PositionEffect2Code
from . import Price14
from . import Quantity6Choice
from . import QuantityBreakdown76
from . import RegistrationParameters3
from . import Reporting6Choice
from . import SecurityIdentification19
from . import SettlementDate16Choice
from . import Side3Code
from . import TradeDate7Choice
from . import TradeRegulatoryConditions1Code
from . import TradeTransactionCondition9Choice
from . import TradeType4Choice
from . import TypeOfPrice47Choice
from . import YesNoIndicator
from . import YieldCalculation7

class Order23(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AcrdIntrstPctg", "_AddtlPhysOrRegnDtls", "_AddtlTradInstrPrcgInf", "_BizPrcTp", "_CallInTp", "_CcyToBuyOrSell", "_ChrgTaxBsisTp", "_ClntOrdrId", "_Comssn", "_ConfQty", "_CptlGnTp", "_CshMrgn", "_DealPric", "_DerivCvrd", "_FinInstrmId", "_GrssTradAmt", "_GvUpNbOfDays", "_IntrstTp", "_ListId", "_MtchSts", "_NAVDt", "_NbOfDaysAcrd", "_OrdrBookgDt", "_OrdrId", "_OrdrOrgtrElgblty", "_PlcOfTrad", "_Pmt", "_PosFct", "_PrcgDt", "_PreAdvc", "_PrtlFillDtls", "_QtyBrkdwn", "_Rptg", "_ScndryClntOrdrId", "_Sd", "_SttlmDt", "_TpOfPric", "_TradDt", "_TradOrgtnDt", "_TradRgltryCondsTp", "_TradTxCond", "_TradTxTp", "_YldTp"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection29, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection29, False)

	@property
	def AcrdIntrstPctg(self):
		return self._AcrdIntrstPctg

	@AcrdIntrstPctg.setter
	def AcrdIntrstPctg(self, value):
		self._AcrdIntrstPctg = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstPctg', PercentageRate, False)

	@AcrdIntrstPctg.deleter
	def AcrdIntrstPctg(self):
		del self._AcrdIntrstPctg
		self._AcrdIntrstPctg = base_types.UninitialisedField(self, 'AcrdIntrstPctg', PercentageRate, False)

	@property
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlPhysOrRegnDtls', RegistrationParameters3, False)

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = base_types.UninitialisedField(self, 'AddtlPhysOrRegnDtls', RegistrationParameters3, False)

	@property
	def AddtlTradInstrPrcgInf(self):
		return self._AddtlTradInstrPrcgInf

	@AddtlTradInstrPrcgInf.setter
	def AddtlTradInstrPrcgInf(self, value):
		self._AddtlTradInstrPrcgInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlTradInstrPrcgInf', Max350Text, False)

	@AddtlTradInstrPrcgInf.deleter
	def AddtlTradInstrPrcgInf(self):
		del self._AddtlTradInstrPrcgInf
		self._AddtlTradInstrPrcgInf = base_types.UninitialisedField(self, 'AddtlTradInstrPrcgInf', Max350Text, False)

	@property
	def BizPrcTp(self):
		return self._BizPrcTp

	@BizPrcTp.setter
	def BizPrcTp(self, value):
		self._BizPrcTp = value if value is not None else base_types.UninitialisedField(self, 'BizPrcTp', BusinessProcessType2Choice, False)

	@BizPrcTp.deleter
	def BizPrcTp(self):
		del self._BizPrcTp
		self._BizPrcTp = base_types.UninitialisedField(self, 'BizPrcTp', BusinessProcessType2Choice, False)

	@property
	def CallInTp(self):
		return self._CallInTp

	@CallInTp.setter
	def CallInTp(self, value):
		self._CallInTp = value if value is not None else base_types.UninitialisedField(self, 'CallInTp', CallIn1Code, False)

	@CallInTp.deleter
	def CallInTp(self):
		del self._CallInTp
		self._CallInTp = base_types.UninitialisedField(self, 'CallInTp', CallIn1Code, False)

	@property
	def CcyToBuyOrSell(self):
		return self._CcyToBuyOrSell

	@CcyToBuyOrSell.setter
	def CcyToBuyOrSell(self, value):
		self._CcyToBuyOrSell = value if value is not None else base_types.UninitialisedField(self, 'CcyToBuyOrSell', CurrencyToBuyOrSell1Choice, False)

	@CcyToBuyOrSell.deleter
	def CcyToBuyOrSell(self):
		del self._CcyToBuyOrSell
		self._CcyToBuyOrSell = base_types.UninitialisedField(self, 'CcyToBuyOrSell', CurrencyToBuyOrSell1Choice, False)

	@property
	def ChrgTaxBsisTp(self):
		return self._ChrgTaxBsisTp

	@ChrgTaxBsisTp.setter
	def ChrgTaxBsisTp(self, value):
		self._ChrgTaxBsisTp = value if value is not None else base_types.UninitialisedField(self, 'ChrgTaxBsisTp', ChargeTaxBasisType2Choice, False)

	@ChrgTaxBsisTp.deleter
	def ChrgTaxBsisTp(self):
		del self._ChrgTaxBsisTp
		self._ChrgTaxBsisTp = base_types.UninitialisedField(self, 'ChrgTaxBsisTp', ChargeTaxBasisType2Choice, False)

	@property
	def ClntOrdrId(self):
		return self._ClntOrdrId

	@ClntOrdrId.setter
	def ClntOrdrId(self, value):
		self._ClntOrdrId = value if value is not None else base_types.UninitialisedField(self, 'ClntOrdrId', Max35Text, True)

	@ClntOrdrId.deleter
	def ClntOrdrId(self):
		del self._ClntOrdrId
		self._ClntOrdrId = base_types.UninitialisedField(self, 'ClntOrdrId', Max35Text, True)

	@property
	def Comssn(self):
		return self._Comssn

	@Comssn.setter
	def Comssn(self, value):
		self._Comssn = value if value is not None else base_types.UninitialisedField(self, 'Comssn', Commission25, False)

	@Comssn.deleter
	def Comssn(self):
		del self._Comssn
		self._Comssn = base_types.UninitialisedField(self, 'Comssn', Commission25, False)

	@property
	def ConfQty(self):
		return self._ConfQty

	@ConfQty.setter
	def ConfQty(self, value):
		self._ConfQty = value if value is not None else base_types.UninitialisedField(self, 'ConfQty', Quantity6Choice, False)

	@ConfQty.deleter
	def ConfQty(self):
		del self._ConfQty
		self._ConfQty = base_types.UninitialisedField(self, 'ConfQty', Quantity6Choice, False)

	@property
	def CptlGnTp(self):
		return self._CptlGnTp

	@CptlGnTp.setter
	def CptlGnTp(self, value):
		self._CptlGnTp = value if value is not None else base_types.UninitialisedField(self, 'CptlGnTp', EUCapitalGainType3Choice, False)

	@CptlGnTp.deleter
	def CptlGnTp(self):
		del self._CptlGnTp
		self._CptlGnTp = base_types.UninitialisedField(self, 'CptlGnTp', EUCapitalGainType3Choice, False)

	@property
	def CshMrgn(self):
		return self._CshMrgn

	@CshMrgn.setter
	def CshMrgn(self, value):
		self._CshMrgn = value if value is not None else base_types.UninitialisedField(self, 'CshMrgn', CashMarginOrder1Code, False)

	@CshMrgn.deleter
	def CshMrgn(self):
		del self._CshMrgn
		self._CshMrgn = base_types.UninitialisedField(self, 'CshMrgn', CashMarginOrder1Code, False)

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price14, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price14, False)

	@property
	def DerivCvrd(self):
		return self._DerivCvrd

	@DerivCvrd.setter
	def DerivCvrd(self, value):
		self._DerivCvrd = value if value is not None else base_types.UninitialisedField(self, 'DerivCvrd', YesNoIndicator, False)

	@DerivCvrd.deleter
	def DerivCvrd(self):
		del self._DerivCvrd
		self._DerivCvrd = base_types.UninitialisedField(self, 'DerivCvrd', YesNoIndicator, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def GrssTradAmt(self):
		return self._GrssTradAmt

	@GrssTradAmt.setter
	def GrssTradAmt(self, value):
		self._GrssTradAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssTradAmt', AmountAndDirection29, False)

	@GrssTradAmt.deleter
	def GrssTradAmt(self):
		del self._GrssTradAmt
		self._GrssTradAmt = base_types.UninitialisedField(self, 'GrssTradAmt', AmountAndDirection29, False)

	@property
	def GvUpNbOfDays(self):
		return self._GvUpNbOfDays

	@GvUpNbOfDays.setter
	def GvUpNbOfDays(self, value):
		self._GvUpNbOfDays = value if value is not None else base_types.UninitialisedField(self, 'GvUpNbOfDays', Max3Number, False)

	@GvUpNbOfDays.deleter
	def GvUpNbOfDays(self):
		del self._GvUpNbOfDays
		self._GvUpNbOfDays = base_types.UninitialisedField(self, 'GvUpNbOfDays', Max3Number, False)

	@property
	def IntrstTp(self):
		return self._IntrstTp

	@IntrstTp.setter
	def IntrstTp(self, value):
		self._IntrstTp = value if value is not None else base_types.UninitialisedField(self, 'IntrstTp', InterestType2Code, False)

	@IntrstTp.deleter
	def IntrstTp(self):
		del self._IntrstTp
		self._IntrstTp = base_types.UninitialisedField(self, 'IntrstTp', InterestType2Code, False)

	@property
	def ListId(self):
		return self._ListId

	@ListId.setter
	def ListId(self, value):
		self._ListId = value if value is not None else base_types.UninitialisedField(self, 'ListId', Max35Text, True)

	@ListId.deleter
	def ListId(self):
		del self._ListId
		self._ListId = base_types.UninitialisedField(self, 'ListId', Max35Text, True)

	@property
	def MtchSts(self):
		return self._MtchSts

	@MtchSts.setter
	def MtchSts(self, value):
		self._MtchSts = value if value is not None else base_types.UninitialisedField(self, 'MtchSts', MatchingStatus27Choice, False)

	@MtchSts.deleter
	def MtchSts(self):
		del self._MtchSts
		self._MtchSts = base_types.UninitialisedField(self, 'MtchSts', MatchingStatus27Choice, False)

	@property
	def NAVDt(self):
		return self._NAVDt

	@NAVDt.setter
	def NAVDt(self, value):
		self._NAVDt = value if value is not None else base_types.UninitialisedField(self, 'NAVDt', DateAndDateTime1Choice, False)

	@NAVDt.deleter
	def NAVDt(self):
		del self._NAVDt
		self._NAVDt = base_types.UninitialisedField(self, 'NAVDt', DateAndDateTime1Choice, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@property
	def OrdrBookgDt(self):
		return self._OrdrBookgDt

	@OrdrBookgDt.setter
	def OrdrBookgDt(self, value):
		self._OrdrBookgDt = value if value is not None else base_types.UninitialisedField(self, 'OrdrBookgDt', ISODate, False)

	@OrdrBookgDt.deleter
	def OrdrBookgDt(self):
		del self._OrdrBookgDt
		self._OrdrBookgDt = base_types.UninitialisedField(self, 'OrdrBookgDt', ISODate, False)

	@property
	def OrdrId(self):
		return self._OrdrId

	@OrdrId.setter
	def OrdrId(self, value):
		self._OrdrId = value if value is not None else base_types.UninitialisedField(self, 'OrdrId', Max35Text, True)

	@OrdrId.deleter
	def OrdrId(self):
		del self._OrdrId
		self._OrdrId = base_types.UninitialisedField(self, 'OrdrId', Max35Text, True)

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if value is not None else base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', Eligibility1Code, False)

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', Eligibility1Code, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification93, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification93, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def PosFct(self):
		return self._PosFct

	@PosFct.setter
	def PosFct(self, value):
		self._PosFct = value if value is not None else base_types.UninitialisedField(self, 'PosFct', PositionEffect2Code, False)

	@PosFct.deleter
	def PosFct(self):
		del self._PosFct
		self._PosFct = base_types.UninitialisedField(self, 'PosFct', PositionEffect2Code, False)

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if value is not None else base_types.UninitialisedField(self, 'PrcgDt', TradeDate7Choice, False)

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = base_types.UninitialisedField(self, 'PrcgDt', TradeDate7Choice, False)

	@property
	def PreAdvc(self):
		return self._PreAdvc

	@PreAdvc.setter
	def PreAdvc(self, value):
		self._PreAdvc = value if value is not None else base_types.UninitialisedField(self, 'PreAdvc', YesNoIndicator, False)

	@PreAdvc.deleter
	def PreAdvc(self):
		del self._PreAdvc
		self._PreAdvc = base_types.UninitialisedField(self, 'PreAdvc', YesNoIndicator, False)

	@property
	def PrtlFillDtls(self):
		return self._PrtlFillDtls

	@PrtlFillDtls.setter
	def PrtlFillDtls(self, value):
		self._PrtlFillDtls = value if value is not None else base_types.UninitialisedField(self, 'PrtlFillDtls', PartialFill4, True)

	@PrtlFillDtls.deleter
	def PrtlFillDtls(self):
		del self._PrtlFillDtls
		self._PrtlFillDtls = base_types.UninitialisedField(self, 'PrtlFillDtls', PartialFill4, True)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown76, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown76, True)

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if value is not None else base_types.UninitialisedField(self, 'Rptg', Reporting6Choice, True)

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = base_types.UninitialisedField(self, 'Rptg', Reporting6Choice, True)

	@property
	def ScndryClntOrdrId(self):
		return self._ScndryClntOrdrId

	@ScndryClntOrdrId.setter
	def ScndryClntOrdrId(self, value):
		self._ScndryClntOrdrId = value if value is not None else base_types.UninitialisedField(self, 'ScndryClntOrdrId', Max35Text, True)

	@ScndryClntOrdrId.deleter
	def ScndryClntOrdrId(self):
		del self._ScndryClntOrdrId
		self._ScndryClntOrdrId = base_types.UninitialisedField(self, 'ScndryClntOrdrId', Max35Text, True)

	@property
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if value is not None else base_types.UninitialisedField(self, 'Sd', Side3Code, False)

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = base_types.UninitialisedField(self, 'Sd', Side3Code, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', SettlementDate16Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', SettlementDate16Choice, False)

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if value is not None else base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice47Choice, False)

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice47Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate7Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate7Choice, False)

	@property
	def TradOrgtnDt(self):
		return self._TradOrgtnDt

	@TradOrgtnDt.setter
	def TradOrgtnDt(self, value):
		self._TradOrgtnDt = value if value is not None else base_types.UninitialisedField(self, 'TradOrgtnDt', ISODateTime, False)

	@TradOrgtnDt.deleter
	def TradOrgtnDt(self):
		del self._TradOrgtnDt
		self._TradOrgtnDt = base_types.UninitialisedField(self, 'TradOrgtnDt', ISODateTime, False)

	@property
	def TradRgltryCondsTp(self):
		return self._TradRgltryCondsTp

	@TradRgltryCondsTp.setter
	def TradRgltryCondsTp(self, value):
		self._TradRgltryCondsTp = value if value is not None else base_types.UninitialisedField(self, 'TradRgltryCondsTp', TradeRegulatoryConditions1Code, False)

	@TradRgltryCondsTp.deleter
	def TradRgltryCondsTp(self):
		del self._TradRgltryCondsTp
		self._TradRgltryCondsTp = base_types.UninitialisedField(self, 'TradRgltryCondsTp', TradeRegulatoryConditions1Code, False)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition9Choice, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition9Choice, True)

	@property
	def TradTxTp(self):
		return self._TradTxTp

	@TradTxTp.setter
	def TradTxTp(self, value):
		self._TradTxTp = value if value is not None else base_types.UninitialisedField(self, 'TradTxTp', TradeType4Choice, False)

	@TradTxTp.deleter
	def TradTxTp(self):
		del self._TradTxTp
		self._TradTxTp = base_types.UninitialisedField(self, 'TradTxTp', TradeType4Choice, False)

	@property
	def YldTp(self):
		return self._YldTp

	@YldTp.setter
	def YldTp(self, value):
		self._YldTp = value if value is not None else base_types.UninitialisedField(self, 'YldTp', YieldCalculation7, False)

	@YldTp.deleter
	def YldTp(self):
		del self._YldTp
		self._YldTp = base_types.UninitialisedField(self, 'YldTp', YieldCalculation7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTradInstrPrcgInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPrcTp', type=BusinessProcessType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallInTp', type=CallIn1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToBuyOrSell', type=CurrencyToBuyOrSell1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgTaxBsisTp', type=ChargeTaxBasisType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntOrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Comssn', type=Commission25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfQty', type=Quantity6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGnTp', type=EUCapitalGainType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMrgn', type=CashMarginOrder1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivCvrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssTradAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvUpNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstTp', type=InterestType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NAVDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBookgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=Eligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosFct', type=PositionEffect2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreAdvc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlFillDtls', type=PartialFill4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown76, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rptg', type=Reporting6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndryClntOrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sd', type=Side3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice47Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradOrgtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltryCondsTp', type=TradeRegulatoryConditions1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition9Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradTxTp', type=TradeType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldTp', type=YieldCalculation7, min=0, max=1, mutex_group=None, array=False),
	))