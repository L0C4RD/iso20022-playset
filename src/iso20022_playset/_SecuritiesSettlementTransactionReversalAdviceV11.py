from . import base_types
from ._SettlementTypeAndIdentification29 import SettlementTypeAndIdentification29
from ._SettlementParties126 import SettlementParties126
from ._SettlementDetails215 import SettlementDetails215
from ._CashParties42 import CashParties42
from ._OtherAmounts46 import OtherAmounts46
from ._RegistrationParameters6 import RegistrationParameters6
from ._NetworkFee1 import NetworkFee1
from ._AdditionalParameters30 import AdditionalParameters30
from ._QuantityAndAccount115 import QuantityAndAccount115
from ._FinancialInstrumentAttributes111 import FinancialInstrumentAttributes111
from ._StandingSettlementInstruction20 import StandingSettlementInstruction20
from ._SecurityIdentification19 import SecurityIdentification19
from ._OtherParties43 import OtherParties43
from ._AmountAndDirection94 import AmountAndDirection94
from ._SecuritiesTradeDetails143 import SecuritiesTradeDetails143
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesSettlementTransactionReversalAdviceV11(base_types._BaseFieldType):

	__slots__ = ["_StgSttlmInstrDtls", "_SttlmParams", "_RcvgSttlmPties", "_TxIdDtls", "_TradDtls", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_QtyAndAcctDtls", "_AddtlPhysOrRegnDtls", "_SttldAmt", "_OthrAmts", "_DgtlNtwkFee", "_OthrBizPties", "_CshPties", "_ConfRef", "_AddtlParams", "_SplmtryData", "_FinInstrmId"]
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
	def TxIdDtls(self):
		return self._TxIdDtls

	@TxIdDtls.setter
	def TxIdDtls(self, value):
		self._TxIdDtls = value if type(value) != base_types.auto else self.make_default("TxIdDtls")

	@TxIdDtls.deleter
	def TxIdDtls(self):
		del self._TxIdDtls
		self._TxIdDtls = None

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
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if type(value) != base_types.auto else self.make_default("AddtlPhysOrRegnDtls")

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = None

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if type(value) != base_types.auto else self.make_default("SttldAmt")

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = None

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
	def ConfRef(self):
		return self._ConfRef

	@ConfRef.setter
	def ConfRef(self, value):
		self._ConfRef = value if type(value) != base_types.auto else self.make_default("ConfRef")

	@ConfRef.deleter
	def ConfRef(self):
		del self._ConfRef
		self._ConfRef = None

	@property
	def AddtlParams(self):
		return self._AddtlParams

	@AddtlParams.setter
	def AddtlParams(self, value):
		self._AddtlParams = value if type(value) != base_types.auto else self.make_default("AddtlParams")

	@AddtlParams.deleter
	def AddtlParams(self):
		del self._AddtlParams
		self._AddtlParams = None

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
		base_types.FieldEntry(name='StgSttlmInstrDtls', type=StandingSettlementInstruction20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails215, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdDtls', type=SettlementTypeAndIdentification29, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails143, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount115, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldAmt', type=AmountAndDirection94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlNtwkFee', type=NetworkFee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlParams', type=AdditionalParameters30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

