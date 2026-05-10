import base_types
import PartialFill4
import Price14
import MatchingStatus27Choice
import CallIn1Code
import Max350Text
import DateAndDateTime1Choice
import CashMarginOrder1Code
import AmountAndDirection29
import TradeTransactionCondition9Choice
import MarketIdentification93
import TradeType4Choice
import Max3Number
import Max35Text
import TypeOfPrice47Choice
import ChargeTaxBasisType2Choice
import BusinessProcessType2Choice
import DeliveryReceiptType2Code
import ISODate
import EUCapitalGainType3Choice
import QuantityBreakdown76
import YesNoIndicator
import PercentageRate
import Quantity6Choice
import PositionEffect2Code
import TradeDate7Choice
import TradeRegulatoryConditions1Code
import ISODateTime
import Side3Code
import SettlementDate16Choice
import Eligibility1Code
import YieldCalculation7
import RegistrationParameters3
import Reporting6Choice
import CurrencyToBuyOrSell1Choice
import InterestType2Code
import Commission24

class Order24(base_types._BaseFieldType):

	__slots__ = ["_PrcgDt", "_CshMrgn", "_CptlGnTp", "_BizPrcTp", "_Comssn", "_AcrdIntrstPctg", "_DerivCvrd", "_AddtlPhysOrRegnDtls", "_ClntOrdrId", "_NAVDt", "_IntrstTp", "_AddtlTradInstrPrcgInf", "_Sd", "_TradTxTp", "_DealPric", "_PlcOfTrad", "_SttlmDt", "_ListId", "_NbOfDaysAcrd", "_CcyToBuyOrSell", "_TradTxCond", "_PosFct", "_OrdrId", "_QtyBrkdwn", "_AcrdIntrstAmt", "_TradRgltryCondsTp", "_ConfQty", "_TpOfPric", "_Pmt", "_OrdrBookgDt", "_CallInTp", "_PreAdvc", "_OrdrOrgtrElgblty", "_ChrgTaxBsisTp", "_GvUpNbOfDays", "_MtchSts", "_YldTp", "_GrssTradAmt", "_Rptg", "_ScndryClntOrdrId", "_TradOrgtnDt", "_TradDt", "_PrtlFillDtls"]
	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if type(value) != auto else self.make_default("PrcgDt")

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = None

	@property
	def CshMrgn(self):
		return self._CshMrgn

	@CshMrgn.setter
	def CshMrgn(self, value):
		self._CshMrgn = value if type(value) != auto else self.make_default("CshMrgn")

	@CshMrgn.deleter
	def CshMrgn(self):
		del self._CshMrgn
		self._CshMrgn = None

	@property
	def CptlGnTp(self):
		return self._CptlGnTp

	@CptlGnTp.setter
	def CptlGnTp(self, value):
		self._CptlGnTp = value if type(value) != auto else self.make_default("CptlGnTp")

	@CptlGnTp.deleter
	def CptlGnTp(self):
		del self._CptlGnTp
		self._CptlGnTp = None

	@property
	def BizPrcTp(self):
		return self._BizPrcTp

	@BizPrcTp.setter
	def BizPrcTp(self, value):
		self._BizPrcTp = value if type(value) != auto else self.make_default("BizPrcTp")

	@BizPrcTp.deleter
	def BizPrcTp(self):
		del self._BizPrcTp
		self._BizPrcTp = None

	@property
	def Comssn(self):
		return self._Comssn

	@Comssn.setter
	def Comssn(self, value):
		self._Comssn = value if type(value) != auto else self.make_default("Comssn")

	@Comssn.deleter
	def Comssn(self):
		del self._Comssn
		self._Comssn = None

	@property
	def AcrdIntrstPctg(self):
		return self._AcrdIntrstPctg

	@AcrdIntrstPctg.setter
	def AcrdIntrstPctg(self, value):
		self._AcrdIntrstPctg = value if type(value) != auto else self.make_default("AcrdIntrstPctg")

	@AcrdIntrstPctg.deleter
	def AcrdIntrstPctg(self):
		del self._AcrdIntrstPctg
		self._AcrdIntrstPctg = None

	@property
	def DerivCvrd(self):
		return self._DerivCvrd

	@DerivCvrd.setter
	def DerivCvrd(self, value):
		self._DerivCvrd = value if type(value) != auto else self.make_default("DerivCvrd")

	@DerivCvrd.deleter
	def DerivCvrd(self):
		del self._DerivCvrd
		self._DerivCvrd = None

	@property
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if type(value) != auto else self.make_default("AddtlPhysOrRegnDtls")

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = None

	@property
	def ClntOrdrId(self):
		return self._ClntOrdrId

	@ClntOrdrId.setter
	def ClntOrdrId(self, value):
		self._ClntOrdrId = value if type(value) != auto else self.make_default("ClntOrdrId")

	@ClntOrdrId.deleter
	def ClntOrdrId(self):
		del self._ClntOrdrId
		self._ClntOrdrId = None

	@property
	def NAVDt(self):
		return self._NAVDt

	@NAVDt.setter
	def NAVDt(self, value):
		self._NAVDt = value if type(value) != auto else self.make_default("NAVDt")

	@NAVDt.deleter
	def NAVDt(self):
		del self._NAVDt
		self._NAVDt = None

	@property
	def IntrstTp(self):
		return self._IntrstTp

	@IntrstTp.setter
	def IntrstTp(self, value):
		self._IntrstTp = value if type(value) != auto else self.make_default("IntrstTp")

	@IntrstTp.deleter
	def IntrstTp(self):
		del self._IntrstTp
		self._IntrstTp = None

	@property
	def AddtlTradInstrPrcgInf(self):
		return self._AddtlTradInstrPrcgInf

	@AddtlTradInstrPrcgInf.setter
	def AddtlTradInstrPrcgInf(self, value):
		self._AddtlTradInstrPrcgInf = value if type(value) != auto else self.make_default("AddtlTradInstrPrcgInf")

	@AddtlTradInstrPrcgInf.deleter
	def AddtlTradInstrPrcgInf(self):
		del self._AddtlTradInstrPrcgInf
		self._AddtlTradInstrPrcgInf = None

	@property
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if type(value) != auto else self.make_default("Sd")

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = None

	@property
	def TradTxTp(self):
		return self._TradTxTp

	@TradTxTp.setter
	def TradTxTp(self, value):
		self._TradTxTp = value if type(value) != auto else self.make_default("TradTxTp")

	@TradTxTp.deleter
	def TradTxTp(self):
		del self._TradTxTp
		self._TradTxTp = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

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
	def ListId(self):
		return self._ListId

	@ListId.setter
	def ListId(self, value):
		self._ListId = value if type(value) != auto else self.make_default("ListId")

	@ListId.deleter
	def ListId(self):
		del self._ListId
		self._ListId = None

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def CcyToBuyOrSell(self):
		return self._CcyToBuyOrSell

	@CcyToBuyOrSell.setter
	def CcyToBuyOrSell(self, value):
		self._CcyToBuyOrSell = value if type(value) != auto else self.make_default("CcyToBuyOrSell")

	@CcyToBuyOrSell.deleter
	def CcyToBuyOrSell(self):
		del self._CcyToBuyOrSell
		self._CcyToBuyOrSell = None

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	@property
	def PosFct(self):
		return self._PosFct

	@PosFct.setter
	def PosFct(self, value):
		self._PosFct = value if type(value) != auto else self.make_default("PosFct")

	@PosFct.deleter
	def PosFct(self):
		del self._PosFct
		self._PosFct = None

	@property
	def OrdrId(self):
		return self._OrdrId

	@OrdrId.setter
	def OrdrId(self, value):
		self._OrdrId = value if type(value) != auto else self.make_default("OrdrId")

	@OrdrId.deleter
	def OrdrId(self):
		del self._OrdrId
		self._OrdrId = None

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def TradRgltryCondsTp(self):
		return self._TradRgltryCondsTp

	@TradRgltryCondsTp.setter
	def TradRgltryCondsTp(self, value):
		self._TradRgltryCondsTp = value if type(value) != auto else self.make_default("TradRgltryCondsTp")

	@TradRgltryCondsTp.deleter
	def TradRgltryCondsTp(self):
		del self._TradRgltryCondsTp
		self._TradRgltryCondsTp = None

	@property
	def ConfQty(self):
		return self._ConfQty

	@ConfQty.setter
	def ConfQty(self, value):
		self._ConfQty = value if type(value) != auto else self.make_default("ConfQty")

	@ConfQty.deleter
	def ConfQty(self):
		del self._ConfQty
		self._ConfQty = None

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if type(value) != auto else self.make_default("TpOfPric")

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def OrdrBookgDt(self):
		return self._OrdrBookgDt

	@OrdrBookgDt.setter
	def OrdrBookgDt(self, value):
		self._OrdrBookgDt = value if type(value) != auto else self.make_default("OrdrBookgDt")

	@OrdrBookgDt.deleter
	def OrdrBookgDt(self):
		del self._OrdrBookgDt
		self._OrdrBookgDt = None

	@property
	def CallInTp(self):
		return self._CallInTp

	@CallInTp.setter
	def CallInTp(self, value):
		self._CallInTp = value if type(value) != auto else self.make_default("CallInTp")

	@CallInTp.deleter
	def CallInTp(self):
		del self._CallInTp
		self._CallInTp = None

	@property
	def PreAdvc(self):
		return self._PreAdvc

	@PreAdvc.setter
	def PreAdvc(self, value):
		self._PreAdvc = value if type(value) != auto else self.make_default("PreAdvc")

	@PreAdvc.deleter
	def PreAdvc(self):
		del self._PreAdvc
		self._PreAdvc = None

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if type(value) != auto else self.make_default("OrdrOrgtrElgblty")

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = None

	@property
	def ChrgTaxBsisTp(self):
		return self._ChrgTaxBsisTp

	@ChrgTaxBsisTp.setter
	def ChrgTaxBsisTp(self, value):
		self._ChrgTaxBsisTp = value if type(value) != auto else self.make_default("ChrgTaxBsisTp")

	@ChrgTaxBsisTp.deleter
	def ChrgTaxBsisTp(self):
		del self._ChrgTaxBsisTp
		self._ChrgTaxBsisTp = None

	@property
	def GvUpNbOfDays(self):
		return self._GvUpNbOfDays

	@GvUpNbOfDays.setter
	def GvUpNbOfDays(self, value):
		self._GvUpNbOfDays = value if type(value) != auto else self.make_default("GvUpNbOfDays")

	@GvUpNbOfDays.deleter
	def GvUpNbOfDays(self):
		del self._GvUpNbOfDays
		self._GvUpNbOfDays = None

	@property
	def MtchSts(self):
		return self._MtchSts

	@MtchSts.setter
	def MtchSts(self, value):
		self._MtchSts = value if type(value) != auto else self.make_default("MtchSts")

	@MtchSts.deleter
	def MtchSts(self):
		del self._MtchSts
		self._MtchSts = None

	@property
	def YldTp(self):
		return self._YldTp

	@YldTp.setter
	def YldTp(self, value):
		self._YldTp = value if type(value) != auto else self.make_default("YldTp")

	@YldTp.deleter
	def YldTp(self):
		del self._YldTp
		self._YldTp = None

	@property
	def GrssTradAmt(self):
		return self._GrssTradAmt

	@GrssTradAmt.setter
	def GrssTradAmt(self, value):
		self._GrssTradAmt = value if type(value) != auto else self.make_default("GrssTradAmt")

	@GrssTradAmt.deleter
	def GrssTradAmt(self):
		del self._GrssTradAmt
		self._GrssTradAmt = None

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if type(value) != auto else self.make_default("Rptg")

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = None

	@property
	def ScndryClntOrdrId(self):
		return self._ScndryClntOrdrId

	@ScndryClntOrdrId.setter
	def ScndryClntOrdrId(self, value):
		self._ScndryClntOrdrId = value if type(value) != auto else self.make_default("ScndryClntOrdrId")

	@ScndryClntOrdrId.deleter
	def ScndryClntOrdrId(self):
		del self._ScndryClntOrdrId
		self._ScndryClntOrdrId = None

	@property
	def TradOrgtnDt(self):
		return self._TradOrgtnDt

	@TradOrgtnDt.setter
	def TradOrgtnDt(self, value):
		self._TradOrgtnDt = value if type(value) != auto else self.make_default("TradOrgtnDt")

	@TradOrgtnDt.deleter
	def TradOrgtnDt(self):
		del self._TradOrgtnDt
		self._TradOrgtnDt = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def PrtlFillDtls(self):
		return self._PrtlFillDtls

	@PrtlFillDtls.setter
	def PrtlFillDtls(self, value):
		self._PrtlFillDtls = value if type(value) != auto else self.make_default("PrtlFillDtls")

	@PrtlFillDtls.deleter
	def PrtlFillDtls(self):
		del self._PrtlFillDtls
		self._PrtlFillDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMrgn', type=CashMarginOrder1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGnTp', type=EUCapitalGainType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPrcTp', type=BusinessProcessType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Comssn', type=Commission24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivCvrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntOrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NAVDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstTp', type=InterestType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTradInstrPrcgInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=Side3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxTp', type=TradeType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToBuyOrSell', type=CurrencyToBuyOrSell1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition9Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PosFct', type=PositionEffect2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown76, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltryCondsTp', type=TradeRegulatoryConditions1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfQty', type=Quantity6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice47Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBookgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallInTp', type=CallIn1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreAdvc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=Eligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgTaxBsisTp', type=ChargeTaxBasisType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvUpNbOfDays', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldTp', type=YieldCalculation7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssTradAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rptg', type=Reporting6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndryClntOrdrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradOrgtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlFillDtls', type=PartialFill4, min=0, max=None, mutex_group=None, array=True),
	))

