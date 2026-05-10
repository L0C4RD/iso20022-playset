import base_types
import PTRREvent2
import OptionOrSwaption11
import InterestRateLegs14
import DerivativeEvent6
import EnergySpecificAttribute9
import Max72Text
import UniqueTransactionIdentifier3Choice
import Max52Text
import TrueFalseIndicator
import MasterAgreement8
import NotionalAmountLegs5
import CurrencyExchange22
import TradeClearing11
import MICIdentifier
import FinancialInstrumentQuantity32Choice
import OtherPayment5
import TradeConfirmation4Choice
import CreditDerivative4
import CollateralPortfolioCode6Choice
import UniqueTransactionIdentifier2Choice
import PriceData2
import ISODateTime
import NotionalQuantityLegs5
import AssetClassCommodity7Choice
import PhysicalTransferType4Code
import ISODate
import AllocationIndicator1Code
import Package4

class TradeTransaction50(base_types._BaseFieldType):

	__slots__ = ["_ExctnTmStmp", "_TradAllcnSts", "_TradConf", "_PrrTxId", "_PstTradRskRdctnFlg", "_BlckTradElctn", "_MrrrOrTrggrTx", "_IntrstRate", "_OthrPmt", "_NtnlAmt", "_MstrAgrmt", "_TxId", "_NrgySpcfcAttrbts", "_DlvryTp", "_NtnlQty", "_EarlyTermntnDt", "_SbsqntTxId", "_PltfmIdr", "_NonStdsdTerm", "_Optn", "_TradClr", "_Ccy", "_SttlmDt", "_TxPric", "_LrgNtnlOffFcltyElctn", "_PstTradRskRdctnEvt", "_XprtnDt", "_DerivEvt", "_Packg", "_Cmmdty", "_FctvDt", "_Cmprssn", "_Cdt", "_Qty", "_RptTrckgNb", "_ScndryTxId", "_CollPrtflCd"]
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
	def TradAllcnSts(self):
		return self._TradAllcnSts

	@TradAllcnSts.setter
	def TradAllcnSts(self, value):
		self._TradAllcnSts = value if type(value) != auto else self.make_default("TradAllcnSts")

	@TradAllcnSts.deleter
	def TradAllcnSts(self):
		del self._TradAllcnSts
		self._TradAllcnSts = None

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
	def PrrTxId(self):
		return self._PrrTxId

	@PrrTxId.setter
	def PrrTxId(self, value):
		self._PrrTxId = value if type(value) != auto else self.make_default("PrrTxId")

	@PrrTxId.deleter
	def PrrTxId(self):
		del self._PrrTxId
		self._PrrTxId = None

	@property
	def PstTradRskRdctnFlg(self):
		return self._PstTradRskRdctnFlg

	@PstTradRskRdctnFlg.setter
	def PstTradRskRdctnFlg(self, value):
		self._PstTradRskRdctnFlg = value if type(value) != auto else self.make_default("PstTradRskRdctnFlg")

	@PstTradRskRdctnFlg.deleter
	def PstTradRskRdctnFlg(self):
		del self._PstTradRskRdctnFlg
		self._PstTradRskRdctnFlg = None

	@property
	def BlckTradElctn(self):
		return self._BlckTradElctn

	@BlckTradElctn.setter
	def BlckTradElctn(self, value):
		self._BlckTradElctn = value if type(value) != auto else self.make_default("BlckTradElctn")

	@BlckTradElctn.deleter
	def BlckTradElctn(self):
		del self._BlckTradElctn
		self._BlckTradElctn = None

	@property
	def MrrrOrTrggrTx(self):
		return self._MrrrOrTrggrTx

	@MrrrOrTrggrTx.setter
	def MrrrOrTrggrTx(self, value):
		self._MrrrOrTrggrTx = value if type(value) != auto else self.make_default("MrrrOrTrggrTx")

	@MrrrOrTrggrTx.deleter
	def MrrrOrTrggrTx(self):
		del self._MrrrOrTrggrTx
		self._MrrrOrTrggrTx = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

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
	def NtnlAmt(self):
		return self._NtnlAmt

	@NtnlAmt.setter
	def NtnlAmt(self, value):
		self._NtnlAmt = value if type(value) != auto else self.make_default("NtnlAmt")

	@NtnlAmt.deleter
	def NtnlAmt(self):
		del self._NtnlAmt
		self._NtnlAmt = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def NrgySpcfcAttrbts(self):
		return self._NrgySpcfcAttrbts

	@NrgySpcfcAttrbts.setter
	def NrgySpcfcAttrbts(self, value):
		self._NrgySpcfcAttrbts = value if type(value) != auto else self.make_default("NrgySpcfcAttrbts")

	@NrgySpcfcAttrbts.deleter
	def NrgySpcfcAttrbts(self):
		del self._NrgySpcfcAttrbts
		self._NrgySpcfcAttrbts = None

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
	def NtnlQty(self):
		return self._NtnlQty

	@NtnlQty.setter
	def NtnlQty(self, value):
		self._NtnlQty = value if type(value) != auto else self.make_default("NtnlQty")

	@NtnlQty.deleter
	def NtnlQty(self):
		del self._NtnlQty
		self._NtnlQty = None

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
	def SbsqntTxId(self):
		return self._SbsqntTxId

	@SbsqntTxId.setter
	def SbsqntTxId(self, value):
		self._SbsqntTxId = value if type(value) != auto else self.make_default("SbsqntTxId")

	@SbsqntTxId.deleter
	def SbsqntTxId(self):
		del self._SbsqntTxId
		self._SbsqntTxId = None

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
	def NonStdsdTerm(self):
		return self._NonStdsdTerm

	@NonStdsdTerm.setter
	def NonStdsdTerm(self, value):
		self._NonStdsdTerm = value if type(value) != auto else self.make_default("NonStdsdTerm")

	@NonStdsdTerm.deleter
	def NonStdsdTerm(self):
		del self._NonStdsdTerm
		self._NonStdsdTerm = None

	@property
	def Optn(self):
		return self._Optn

	@Optn.setter
	def Optn(self, value):
		self._Optn = value if type(value) != auto else self.make_default("Optn")

	@Optn.deleter
	def Optn(self):
		del self._Optn
		self._Optn = None

	@property
	def TradClr(self):
		return self._TradClr

	@TradClr.setter
	def TradClr(self, value):
		self._TradClr = value if type(value) != auto else self.make_default("TradClr")

	@TradClr.deleter
	def TradClr(self):
		del self._TradClr
		self._TradClr = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def LrgNtnlOffFcltyElctn(self):
		return self._LrgNtnlOffFcltyElctn

	@LrgNtnlOffFcltyElctn.setter
	def LrgNtnlOffFcltyElctn(self, value):
		self._LrgNtnlOffFcltyElctn = value if type(value) != auto else self.make_default("LrgNtnlOffFcltyElctn")

	@LrgNtnlOffFcltyElctn.deleter
	def LrgNtnlOffFcltyElctn(self):
		del self._LrgNtnlOffFcltyElctn
		self._LrgNtnlOffFcltyElctn = None

	@property
	def PstTradRskRdctnEvt(self):
		return self._PstTradRskRdctnEvt

	@PstTradRskRdctnEvt.setter
	def PstTradRskRdctnEvt(self, value):
		self._PstTradRskRdctnEvt = value if type(value) != auto else self.make_default("PstTradRskRdctnEvt")

	@PstTradRskRdctnEvt.deleter
	def PstTradRskRdctnEvt(self):
		del self._PstTradRskRdctnEvt
		self._PstTradRskRdctnEvt = None

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
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if type(value) != auto else self.make_default("Packg")

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = None

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
	def Cmprssn(self):
		return self._Cmprssn

	@Cmprssn.setter
	def Cmprssn(self, value):
		self._Cmprssn = value if type(value) != auto else self.make_default("Cmprssn")

	@Cmprssn.deleter
	def Cmprssn(self):
		del self._Cmprssn
		self._Cmprssn = None

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if type(value) != auto else self.make_default("Cdt")

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

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
	def ScndryTxId(self):
		return self._ScndryTxId

	@ScndryTxId.setter
	def ScndryTxId(self, value):
		self._ScndryTxId = value if type(value) != auto else self.make_default("ScndryTxId")

	@ScndryTxId.deleter
	def ScndryTxId(self):
		del self._ScndryTxId
		self._ScndryTxId = None

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if type(value) != auto else self.make_default("CollPrtflCd")

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctnTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAllcnSts', type=AllocationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradConf', type=TradeConfirmation4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrTxId', type=UniqueTransactionIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTradElctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrrrOrTrggrTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateLegs14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmt', type=OtherPayment5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtnlAmt', type=NotionalAmountLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgySpcfcAttrbts', type=EnergySpecificAttribute9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQty', type=NotionalQuantityLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyTermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntTxId', type=UniqueTransactionIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltfmIdr', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdsdTerm', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Optn', type=OptionOrSwaption11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradClr', type=TradeClearing11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyExchange22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxPric', type=PriceData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgNtnlOffFcltyElctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnEvt', type=PTRREvent2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvt', type=DerivativeEvent6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Packg', type=Package4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=AssetClassCommodity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmprssn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdt', type=CreditDerivative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTrckgNb', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryTxId', type=Max72Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode6Choice, min=0, max=1, mutex_group=None, array=False),
	))

