# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AllegementStatus3Choice
from . import AmountAndDirection88
from . import DeliveryReceiptType2Code
from . import FinancialInstrumentAttributes111
from . import Max35Text
from . import Max3Number
from . import OtherAmounts32
from . import OtherParties34
from . import PlaceOfClearingIdentification2
from . import PlaceOfTradeIdentification1
from . import Price10
from . import QuantityAndAccount114
from . import ReceiveDelivery1Code
from . import SecuritiesFinancingTransactionDetails54
from . import SecurityIdentification19
from . import SettlementDate17Choice
from . import SettlementDetails168
from . import SettlementParties126
from . import SupplementaryData1
from . import TradeDate8Choice
from . import TradeTransactionCondition5Choice
from . import TypeOfPrice29Choice
from . import UTIIdentifier

class SecuritiesTradeDetails141(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_CmonId", "_CollTxId", "_CtrPtyMktInfrstrctrTxId", "_DealPric", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_MktInfrstrctrTxId", "_NbOfDaysAcrd", "_OthrAmts", "_OthrBizPties", "_PlcOfClr", "_PlcOfTrad", "_Pmt", "_PoolId", "_PrcrTxId", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgDtls", "_SctiesMvmntTp", "_SplmtryData", "_Sts", "_SttlmAmt", "_SttlmDt", "_SttlmParams", "_TpOfPric", "_TradDt", "_TradId", "_TradTxCond", "_UnqTxIdr"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@property
	def CollTxId(self):
		return self._CollTxId

	@CollTxId.setter
	def CollTxId(self, value):
		self._CollTxId = value if value is not None else base_types.UninitialisedField(self, 'CollTxId', Max35Text, True)

	@CollTxId.deleter
	def CollTxId(self):
		del self._CollTxId
		self._CollTxId = base_types.UninitialisedField(self, 'CollTxId', Max35Text, True)

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price10, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price10, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

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
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

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
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts32, False)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts32, False)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties34, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties34, False)

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if value is not None else base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

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
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if value is not None else base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount114, False)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount114, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails54, False)

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails54, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', AllegementStatus3Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', AllegementStatus3Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection88, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection88, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails168, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails168, False)

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if value is not None else base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice29Choice, False)

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = base_types.UninitialisedField(self, 'TpOfPric', TypeOfPrice29Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount114, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancingTransactionDetails54, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=AllegementStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection88, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))