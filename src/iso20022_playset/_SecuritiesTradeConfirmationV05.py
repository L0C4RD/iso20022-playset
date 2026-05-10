from . import base_types
from ._Order24 import Order24
from ._AmountAndDirection28 import AmountAndDirection28
from ._NumberCount1Choice import NumberCount1Choice
from ._ConfirmationParties6 import ConfirmationParties6
from ._Clearing5 import Clearing5
from ._UnderlyingFinancialInstrument7 import UnderlyingFinancialInstrument7
from ._OtherPrices5 import OtherPrices5
from ._FinancialInstrumentAttributes124 import FinancialInstrumentAttributes124
from ._RegulatoryStipulations1 import RegulatoryStipulations1
from ._SettlementParties59 import SettlementParties59
from ._SecurityIdentification19 import SecurityIdentification19
from ._TwoLegTransactionDetails5 import TwoLegTransactionDetails5
from ._OtherAmounts16 import OtherAmounts16
from ._Linkages76 import Linkages76
from ._StandingSettlementInstruction13 import StandingSettlementInstruction13
from ._FinancialInstrumentStipulations4 import FinancialInstrumentStipulations4
from ._SettlementDetails213 import SettlementDetails213
from ._CashParties33 import CashParties33
from ._OtherParties32 import OtherParties32
from ._SupplementaryData1 import SupplementaryData1
from ._TransactiontIdentification4 import TransactiontIdentification4

class SecuritiesTradeConfirmationV05(base_types._BaseFieldType):

	__slots__ = ["_Stiptns", "_RcvgSttlmPties", "_StgSttlmInstr", "_ConfPties", "_DlvrgSttlmPties", "_SttlmAmt", "_OthrBizPties", "_RgltryStiptns", "_UndrlygFinInstrm", "_SttlmParams", "_CshPties", "_OthrAmts", "_ClrDtls", "_NbCnt", "_Refs", "_TwoLegTxDtls", "_TradDtls", "_OthrPrics", "_FinInstrmAttrbts", "_Id", "_SplmtryData", "_FinInstrmId"]
	@property
	def Stiptns(self):
		return self._Stiptns

	@Stiptns.setter
	def Stiptns(self, value):
		self._Stiptns = value if type(value) != base_types.auto else self.make_default("Stiptns")

	@Stiptns.deleter
	def Stiptns(self):
		del self._Stiptns
		self._Stiptns = None

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
	def StgSttlmInstr(self):
		return self._StgSttlmInstr

	@StgSttlmInstr.setter
	def StgSttlmInstr(self, value):
		self._StgSttlmInstr = value if type(value) != base_types.auto else self.make_default("StgSttlmInstr")

	@StgSttlmInstr.deleter
	def StgSttlmInstr(self):
		del self._StgSttlmInstr
		self._StgSttlmInstr = None

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if type(value) != base_types.auto else self.make_default("ConfPties")

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = None

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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

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
	def RgltryStiptns(self):
		return self._RgltryStiptns

	@RgltryStiptns.setter
	def RgltryStiptns(self, value):
		self._RgltryStiptns = value if type(value) != base_types.auto else self.make_default("RgltryStiptns")

	@RgltryStiptns.deleter
	def RgltryStiptns(self):
		del self._RgltryStiptns
		self._RgltryStiptns = None

	@property
	def UndrlygFinInstrm(self):
		return self._UndrlygFinInstrm

	@UndrlygFinInstrm.setter
	def UndrlygFinInstrm(self, value):
		self._UndrlygFinInstrm = value if type(value) != base_types.auto else self.make_default("UndrlygFinInstrm")

	@UndrlygFinInstrm.deleter
	def UndrlygFinInstrm(self):
		del self._UndrlygFinInstrm
		self._UndrlygFinInstrm = None

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
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if type(value) != base_types.auto else self.make_default("ClrDtls")

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = None

	@property
	def NbCnt(self):
		return self._NbCnt

	@NbCnt.setter
	def NbCnt(self, value):
		self._NbCnt = value if type(value) != base_types.auto else self.make_default("NbCnt")

	@NbCnt.deleter
	def NbCnt(self):
		del self._NbCnt
		self._NbCnt = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def TwoLegTxDtls(self):
		return self._TwoLegTxDtls

	@TwoLegTxDtls.setter
	def TwoLegTxDtls(self, value):
		self._TwoLegTxDtls = value if type(value) != base_types.auto else self.make_default("TwoLegTxDtls")

	@TwoLegTxDtls.deleter
	def TwoLegTxDtls(self):
		del self._TwoLegTxDtls
		self._TwoLegTxDtls = None

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
	def OthrPrics(self):
		return self._OthrPrics

	@OthrPrics.setter
	def OthrPrics(self, value):
		self._OthrPrics = value if type(value) != base_types.auto else self.make_default("OthrPrics")

	@OthrPrics.deleter
	def OthrPrics(self):
		del self._OthrPrics
		self._OthrPrics = None

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
		base_types.FieldEntry(name='Stiptns', type=FinancialInstrumentStipulations4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgSttlmInstr', type=StandingSettlementInstruction13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryStiptns', type=RegulatoryStipulations1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygFinInstrm', type=UnderlyingFinancialInstrument7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails213, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrDtls', type=Clearing5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbCnt', type=NumberCount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Linkages76, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TwoLegTxDtls', type=TwoLegTransactionDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=Order24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrics', type=OtherPrices5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

