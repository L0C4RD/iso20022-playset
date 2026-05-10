from . import base_types
from .Linkages50 import Linkages50
from .SettlementParties105 import SettlementParties105
from .RegistrationParameters7 import RegistrationParameters7
from .SettlementTypeAndIdentification28 import SettlementTypeAndIdentification28
from .SecuritiesTradeDetails128 import SecuritiesTradeDetails128
from .QuantityAndAccount108 import QuantityAndAccount108
from .OtherParties44 import OtherParties44
from .FinancialInstrumentAttributes122 import FinancialInstrumentAttributes122
from .AmountAndDirection96 import AmountAndDirection96
from .SecurityIdentification20 import SecurityIdentification20
from .StandingSettlementInstruction19 import StandingSettlementInstruction19
from .AdditionalParameters31 import AdditionalParameters31
from .SupplementaryData1 import SupplementaryData1
from .SettlementDetails211 import SettlementDetails211
from .OtherAmounts44 import OtherAmounts44
from .CashParties38 import CashParties38

class SecuritiesSettlementTransactionConfirmation002V11(base_types._BaseFieldType):

	__slots__ = ["_RcvgSttlmPties", "_CshPties", "_AddtlPhysOrRegnDtls", "_SttlmParams", "_TradDtls", "_StgSttlmInstrDtls", "_AddtlParams", "_OthrBizPties", "_OthrAmts", "_QtyAndAcctDtls", "_Lnkgs", "_DlvrgSttlmPties", "_TxIdDtls", "_FinInstrmAttrbts", "_SttldAmt", "_SplmtryData", "_FinInstrmId"]
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
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails211, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails128, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgSttlmInstrDtls', type=StandingSettlementInstruction19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlParams', type=AdditionalParameters31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount108, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages50, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdDtls', type=SettlementTypeAndIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldAmt', type=AmountAndDirection96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
	))

