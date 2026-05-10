from . import base_types
from ._SettlementParties126 import SettlementParties126
from ._NetworkFee1 import NetworkFee1
from ._QuantityAndAccount117 import QuantityAndAccount117
from ._CashParties41 import CashParties41
from ._FinancialInstrumentAttributes111 import FinancialInstrumentAttributes111
from ._Linkages64 import Linkages64
from ._SecuritiesTradeDetails116 import SecuritiesTradeDetails116
from ._SecuritiesFinancingTransactionDetails56 import SecuritiesFinancingTransactionDetails56
from ._StandingSettlementInstruction20 import StandingSettlementInstruction20
from ._SecurityIdentification19 import SecurityIdentification19
from ._SettlementDetails148 import SettlementDetails148
from ._OtherParties43 import OtherParties43
from ._OtherAmounts45 import OtherAmounts45
from ._TransactionTypeAndAdditionalParameters21 import TransactionTypeAndAdditionalParameters21
from ._AmountAndDirection94 import AmountAndDirection94
from ._Max35Text import Max35Text
from ._NumberCount2Choice import NumberCount2Choice
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesFinancingInstructionV12(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_NbCounts", "_StgSttlmInstrDtls", "_RcvgSttlmPties", "_QtyAndAcctDtls", "_SttlmParams", "_DlvrgSttlmPties", "_CshPties", "_FinInstrmAttrbts", "_OpngSttlmAmt", "_Lnkgs", "_TradDtls", "_DgtlNtwkFee", "_OthrBizPties", "_TxTpAndAddtlParams", "_OthrAmts", "_SctiesFincgDtls", "_SplmtryData", "_FinInstrmId"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if type(value) != base_types.auto else self.make_default("NbCounts")

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = None

	@property
	def StgSttlmInstrDtls(self):
		return self._StgSttlmInstrDtls

	@StgSttlmInstrDtls.setter
	def StgSttlmInstrDtls(self, value):
		self._StgSttlmInstrDtls = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrDtls")

	@StgSttlmInstrDtls.deleter
	def StgSttlmInstrDtls(self):
		del self._StgSttlmInstrDtls
		self._StgSttlmInstrDtls = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if type(value) != base_types.auto else self.make_default("QtyAndAcctDtls")

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = None

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != base_types.auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if type(value) != base_types.auto else self.make_default("CshPties")

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = None

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	@property
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if type(value) != base_types.auto else self.make_default("OpngSttlmAmt")

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = None

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != base_types.auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if type(value) != base_types.auto else self.make_default("TradDtls")

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = None

	@property
	def DgtlNtwkFee(self):
		return self._DgtlNtwkFee

	@DgtlNtwkFee.setter
	def DgtlNtwkFee(self, value):
		self._DgtlNtwkFee = value if type(value) != base_types.auto else self.make_default("DgtlNtwkFee")

	@DgtlNtwkFee.deleter
	def DgtlNtwkFee(self):
		del self._DgtlNtwkFee
		self._DgtlNtwkFee = None

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if type(value) != base_types.auto else self.make_default("OthrBizPties")

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = None

	@property
	def TxTpAndAddtlParams(self):
		return self._TxTpAndAddtlParams

	@TxTpAndAddtlParams.setter
	def TxTpAndAddtlParams(self, value):
		self._TxTpAndAddtlParams = value if type(value) != base_types.auto else self.make_default("TxTpAndAddtlParams")

	@TxTpAndAddtlParams.deleter
	def TxTpAndAddtlParams(self):
		del self._TxTpAndAddtlParams
		self._TxTpAndAddtlParams = None

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if type(value) != base_types.auto else self.make_default("OthrAmts")

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = None

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if type(value) != base_types.auto else self.make_default("SctiesFincgDtls")

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbCounts', type=NumberCount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgSttlmInstrDtls', type=StandingSettlementInstruction20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages64, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails116, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlNtwkFee', type=NetworkFee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndAddtlParams', type=TransactionTypeAndAdditionalParameters21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancingTransactionDetails56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

