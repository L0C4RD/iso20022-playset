# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AllocationIndicator1Code
from . import AssetClassCommodity7Choice
from . import CollateralPortfolioCode6Choice
from . import CreditDerivative4
from . import CurrencyExchange22
from . import DerivativeEvent6
from . import EnergySpecificAttribute9
from . import FinancialInstrumentQuantity32Choice
from . import ISODate
from . import ISODateTime
from . import InterestRateLegs14
from . import MICIdentifier
from . import MasterAgreement8
from . import Max52Text
from . import Max72Text
from . import NotionalAmountLegs5
from . import NotionalQuantityLegs5
from . import OptionOrSwaption11
from . import OtherPayment5
from . import PTRREvent2
from . import Package4
from . import PhysicalTransferType4Code
from . import PriceData2
from . import TradeClearing11
from . import TradeConfirmation4Choice
from . import TrueFalseIndicator
from . import UniqueTransactionIdentifier2Choice
from . import UniqueTransactionIdentifier3Choice

class TradeTransaction50(base_types._BaseFieldType):

	__slots__ = ["_BlckTradElctn", "_Ccy", "_Cdt", "_Cmmdty", "_Cmprssn", "_CollPrtflCd", "_DerivEvt", "_DlvryTp", "_EarlyTermntnDt", "_ExctnTmStmp", "_FctvDt", "_IntrstRate", "_LrgNtnlOffFcltyElctn", "_MrrrOrTrggrTx", "_MstrAgrmt", "_NonStdsdTerm", "_NrgySpcfcAttrbts", "_NtnlAmt", "_NtnlQty", "_Optn", "_OthrPmt", "_Packg", "_PltfmIdr", "_PrrTxId", "_PstTradRskRdctnEvt", "_PstTradRskRdctnFlg", "_Qty", "_RptTrckgNb", "_SbsqntTxId", "_ScndryTxId", "_SttlmDt", "_TradAllcnSts", "_TradClr", "_TradConf", "_TxId", "_TxPric", "_XprtnDt"]
	@property
	def BlckTradElctn(self):
		return self._BlckTradElctn

	@BlckTradElctn.setter
	def BlckTradElctn(self, value):
		self._BlckTradElctn = value if value is not None else base_types.UninitialisedField(self, 'BlckTradElctn', TrueFalseIndicator, False)

	@BlckTradElctn.deleter
	def BlckTradElctn(self):
		del self._BlckTradElctn
		self._BlckTradElctn = base_types.UninitialisedField(self, 'BlckTradElctn', TrueFalseIndicator, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', CurrencyExchange22, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', CurrencyExchange22, False)

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if value is not None else base_types.UninitialisedField(self, 'Cdt', CreditDerivative4, False)

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = base_types.UninitialisedField(self, 'Cdt', CreditDerivative4, False)

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', AssetClassCommodity7Choice, False)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', AssetClassCommodity7Choice, False)

	@property
	def Cmprssn(self):
		return self._Cmprssn

	@Cmprssn.setter
	def Cmprssn(self, value):
		self._Cmprssn = value if value is not None else base_types.UninitialisedField(self, 'Cmprssn', TrueFalseIndicator, False)

	@Cmprssn.deleter
	def Cmprssn(self):
		del self._Cmprssn
		self._Cmprssn = base_types.UninitialisedField(self, 'Cmprssn', TrueFalseIndicator, False)

	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode6Choice, False)

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode6Choice, False)

	@property
	def DerivEvt(self):
		return self._DerivEvt

	@DerivEvt.setter
	def DerivEvt(self, value):
		self._DerivEvt = value if value is not None else base_types.UninitialisedField(self, 'DerivEvt', DerivativeEvent6, False)

	@DerivEvt.deleter
	def DerivEvt(self):
		del self._DerivEvt
		self._DerivEvt = base_types.UninitialisedField(self, 'DerivEvt', DerivativeEvent6, False)

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if value is not None else base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@property
	def EarlyTermntnDt(self):
		return self._EarlyTermntnDt

	@EarlyTermntnDt.setter
	def EarlyTermntnDt(self, value):
		self._EarlyTermntnDt = value if value is not None else base_types.UninitialisedField(self, 'EarlyTermntnDt', ISODate, False)

	@EarlyTermntnDt.deleter
	def EarlyTermntnDt(self):
		del self._EarlyTermntnDt
		self._EarlyTermntnDt = base_types.UninitialisedField(self, 'EarlyTermntnDt', ISODate, False)

	@property
	def ExctnTmStmp(self):
		return self._ExctnTmStmp

	@ExctnTmStmp.setter
	def ExctnTmStmp(self, value):
		self._ExctnTmStmp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTmStmp', ISODateTime, False)

	@ExctnTmStmp.deleter
	def ExctnTmStmp(self):
		del self._ExctnTmStmp
		self._ExctnTmStmp = base_types.UninitialisedField(self, 'ExctnTmStmp', ISODateTime, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', ISODate, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRateLegs14, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRateLegs14, False)

	@property
	def LrgNtnlOffFcltyElctn(self):
		return self._LrgNtnlOffFcltyElctn

	@LrgNtnlOffFcltyElctn.setter
	def LrgNtnlOffFcltyElctn(self, value):
		self._LrgNtnlOffFcltyElctn = value if value is not None else base_types.UninitialisedField(self, 'LrgNtnlOffFcltyElctn', TrueFalseIndicator, False)

	@LrgNtnlOffFcltyElctn.deleter
	def LrgNtnlOffFcltyElctn(self):
		del self._LrgNtnlOffFcltyElctn
		self._LrgNtnlOffFcltyElctn = base_types.UninitialisedField(self, 'LrgNtnlOffFcltyElctn', TrueFalseIndicator, False)

	@property
	def MrrrOrTrggrTx(self):
		return self._MrrrOrTrggrTx

	@MrrrOrTrggrTx.setter
	def MrrrOrTrggrTx(self, value):
		self._MrrrOrTrggrTx = value if value is not None else base_types.UninitialisedField(self, 'MrrrOrTrggrTx', TrueFalseIndicator, False)

	@MrrrOrTrggrTx.deleter
	def MrrrOrTrggrTx(self):
		del self._MrrrOrTrggrTx
		self._MrrrOrTrggrTx = base_types.UninitialisedField(self, 'MrrrOrTrggrTx', TrueFalseIndicator, False)

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement8, False)

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement8, False)

	@property
	def NonStdsdTerm(self):
		return self._NonStdsdTerm

	@NonStdsdTerm.setter
	def NonStdsdTerm(self, value):
		self._NonStdsdTerm = value if value is not None else base_types.UninitialisedField(self, 'NonStdsdTerm', TrueFalseIndicator, False)

	@NonStdsdTerm.deleter
	def NonStdsdTerm(self):
		del self._NonStdsdTerm
		self._NonStdsdTerm = base_types.UninitialisedField(self, 'NonStdsdTerm', TrueFalseIndicator, False)

	@property
	def NrgySpcfcAttrbts(self):
		return self._NrgySpcfcAttrbts

	@NrgySpcfcAttrbts.setter
	def NrgySpcfcAttrbts(self, value):
		self._NrgySpcfcAttrbts = value if value is not None else base_types.UninitialisedField(self, 'NrgySpcfcAttrbts', EnergySpecificAttribute9, False)

	@NrgySpcfcAttrbts.deleter
	def NrgySpcfcAttrbts(self):
		del self._NrgySpcfcAttrbts
		self._NrgySpcfcAttrbts = base_types.UninitialisedField(self, 'NrgySpcfcAttrbts', EnergySpecificAttribute9, False)

	@property
	def NtnlAmt(self):
		return self._NtnlAmt

	@NtnlAmt.setter
	def NtnlAmt(self, value):
		self._NtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmt', NotionalAmountLegs5, False)

	@NtnlAmt.deleter
	def NtnlAmt(self):
		del self._NtnlAmt
		self._NtnlAmt = base_types.UninitialisedField(self, 'NtnlAmt', NotionalAmountLegs5, False)

	@property
	def NtnlQty(self):
		return self._NtnlQty

	@NtnlQty.setter
	def NtnlQty(self, value):
		self._NtnlQty = value if value is not None else base_types.UninitialisedField(self, 'NtnlQty', NotionalQuantityLegs5, False)

	@NtnlQty.deleter
	def NtnlQty(self):
		del self._NtnlQty
		self._NtnlQty = base_types.UninitialisedField(self, 'NtnlQty', NotionalQuantityLegs5, False)

	@property
	def Optn(self):
		return self._Optn

	@Optn.setter
	def Optn(self, value):
		self._Optn = value if value is not None else base_types.UninitialisedField(self, 'Optn', OptionOrSwaption11, False)

	@Optn.deleter
	def Optn(self):
		del self._Optn
		self._Optn = base_types.UninitialisedField(self, 'Optn', OptionOrSwaption11, False)

	@property
	def OthrPmt(self):
		return self._OthrPmt

	@OthrPmt.setter
	def OthrPmt(self, value):
		self._OthrPmt = value if value is not None else base_types.UninitialisedField(self, 'OthrPmt', OtherPayment5, True)

	@OthrPmt.deleter
	def OthrPmt(self):
		del self._OthrPmt
		self._OthrPmt = base_types.UninitialisedField(self, 'OthrPmt', OtherPayment5, True)

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if value is not None else base_types.UninitialisedField(self, 'Packg', Package4, False)

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = base_types.UninitialisedField(self, 'Packg', Package4, False)

	@property
	def PltfmIdr(self):
		return self._PltfmIdr

	@PltfmIdr.setter
	def PltfmIdr(self, value):
		self._PltfmIdr = value if value is not None else base_types.UninitialisedField(self, 'PltfmIdr', MICIdentifier, False)

	@PltfmIdr.deleter
	def PltfmIdr(self):
		del self._PltfmIdr
		self._PltfmIdr = base_types.UninitialisedField(self, 'PltfmIdr', MICIdentifier, False)

	@property
	def PrrTxId(self):
		return self._PrrTxId

	@PrrTxId.setter
	def PrrTxId(self, value):
		self._PrrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrrTxId', UniqueTransactionIdentifier3Choice, False)

	@PrrTxId.deleter
	def PrrTxId(self):
		del self._PrrTxId
		self._PrrTxId = base_types.UninitialisedField(self, 'PrrTxId', UniqueTransactionIdentifier3Choice, False)

	@property
	def PstTradRskRdctnEvt(self):
		return self._PstTradRskRdctnEvt

	@PstTradRskRdctnEvt.setter
	def PstTradRskRdctnEvt(self, value):
		self._PstTradRskRdctnEvt = value if value is not None else base_types.UninitialisedField(self, 'PstTradRskRdctnEvt', PTRREvent2, False)

	@PstTradRskRdctnEvt.deleter
	def PstTradRskRdctnEvt(self):
		del self._PstTradRskRdctnEvt
		self._PstTradRskRdctnEvt = base_types.UninitialisedField(self, 'PstTradRskRdctnEvt', PTRREvent2, False)

	@property
	def PstTradRskRdctnFlg(self):
		return self._PstTradRskRdctnFlg

	@PstTradRskRdctnFlg.setter
	def PstTradRskRdctnFlg(self, value):
		self._PstTradRskRdctnFlg = value if value is not None else base_types.UninitialisedField(self, 'PstTradRskRdctnFlg', TrueFalseIndicator, False)

	@PstTradRskRdctnFlg.deleter
	def PstTradRskRdctnFlg(self):
		del self._PstTradRskRdctnFlg
		self._PstTradRskRdctnFlg = base_types.UninitialisedField(self, 'PstTradRskRdctnFlg', TrueFalseIndicator, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity32Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity32Choice, False)

	@property
	def RptTrckgNb(self):
		return self._RptTrckgNb

	@RptTrckgNb.setter
	def RptTrckgNb(self, value):
		self._RptTrckgNb = value if value is not None else base_types.UninitialisedField(self, 'RptTrckgNb', Max52Text, False)

	@RptTrckgNb.deleter
	def RptTrckgNb(self):
		del self._RptTrckgNb
		self._RptTrckgNb = base_types.UninitialisedField(self, 'RptTrckgNb', Max52Text, False)

	@property
	def SbsqntTxId(self):
		return self._SbsqntTxId

	@SbsqntTxId.setter
	def SbsqntTxId(self, value):
		self._SbsqntTxId = value if value is not None else base_types.UninitialisedField(self, 'SbsqntTxId', UniqueTransactionIdentifier3Choice, False)

	@SbsqntTxId.deleter
	def SbsqntTxId(self):
		del self._SbsqntTxId
		self._SbsqntTxId = base_types.UninitialisedField(self, 'SbsqntTxId', UniqueTransactionIdentifier3Choice, False)

	@property
	def ScndryTxId(self):
		return self._ScndryTxId

	@ScndryTxId.setter
	def ScndryTxId(self, value):
		self._ScndryTxId = value if value is not None else base_types.UninitialisedField(self, 'ScndryTxId', Max72Text, False)

	@ScndryTxId.deleter
	def ScndryTxId(self):
		del self._ScndryTxId
		self._ScndryTxId = base_types.UninitialisedField(self, 'ScndryTxId', Max72Text, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, True)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, True)

	@property
	def TradAllcnSts(self):
		return self._TradAllcnSts

	@TradAllcnSts.setter
	def TradAllcnSts(self, value):
		self._TradAllcnSts = value if value is not None else base_types.UninitialisedField(self, 'TradAllcnSts', AllocationIndicator1Code, False)

	@TradAllcnSts.deleter
	def TradAllcnSts(self):
		del self._TradAllcnSts
		self._TradAllcnSts = base_types.UninitialisedField(self, 'TradAllcnSts', AllocationIndicator1Code, False)

	@property
	def TradClr(self):
		return self._TradClr

	@TradClr.setter
	def TradClr(self, value):
		self._TradClr = value if value is not None else base_types.UninitialisedField(self, 'TradClr', TradeClearing11, False)

	@TradClr.deleter
	def TradClr(self):
		del self._TradClr
		self._TradClr = base_types.UninitialisedField(self, 'TradClr', TradeClearing11, False)

	@property
	def TradConf(self):
		return self._TradConf

	@TradConf.setter
	def TradConf(self, value):
		self._TradConf = value if value is not None else base_types.UninitialisedField(self, 'TradConf', TradeConfirmation4Choice, False)

	@TradConf.deleter
	def TradConf(self):
		del self._TradConf
		self._TradConf = base_types.UninitialisedField(self, 'TradConf', TradeConfirmation4Choice, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', UniqueTransactionIdentifier2Choice, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', UniqueTransactionIdentifier2Choice, False)

	@property
	def TxPric(self):
		return self._TxPric

	@TxPric.setter
	def TxPric(self, value):
		self._TxPric = value if value is not None else base_types.UninitialisedField(self, 'TxPric', PriceData2, False)

	@TxPric.deleter
	def TxPric(self):
		del self._TxPric
		self._TxPric = base_types.UninitialisedField(self, 'TxPric', PriceData2, False)

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if value is not None else base_types.UninitialisedField(self, 'XprtnDt', ISODate, False)

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = base_types.UninitialisedField(self, 'XprtnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckTradElctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyExchange22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdt', type=CreditDerivative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmmdty', type=AssetClassCommodity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmprssn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivEvt', type=DerivativeEvent6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyTermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateLegs14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgNtnlOffFcltyElctn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrrrOrTrggrTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdsdTerm', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgySpcfcAttrbts', type=EnergySpecificAttribute9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlAmt', type=NotionalAmountLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQty', type=NotionalQuantityLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Optn', type=OptionOrSwaption11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmt', type=OtherPayment5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Packg', type=Package4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltfmIdr', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrrTxId', type=UniqueTransactionIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnEvt', type=PTRREvent2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTrckgNb', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntTxId', type=UniqueTransactionIdentifier3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryTxId', type=Max72Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradAllcnSts', type=AllocationIndicator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradClr', type=TradeClearing11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradConf', type=TradeConfirmation4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxPric', type=PriceData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))