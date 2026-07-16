# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection28
from . import CashParties33
from . import Clearing5
from . import ConfirmationParties6
from . import FinancialInstrumentAttributes124
from . import FinancialInstrumentStipulations4
from . import Linkages76
from . import NumberCount1Choice
from . import Order24
from . import OtherAmounts16
from . import OtherParties32
from . import OtherPrices5
from . import RegulatoryStipulations1
from . import SecurityIdentification19
from . import SettlementDetails213
from . import SettlementParties59
from . import StandingSettlementInstruction13
from . import SupplementaryData1
from . import TransactiontIdentification4
from . import TwoLegTransactionDetails5
from . import UnderlyingFinancialInstrument7

class SecuritiesTradeConfirmationV05(base_types._BaseFieldType):

	__slots__ = ["_ClrDtls", "_ConfPties", "_CshPties", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_Id", "_NbCnt", "_OthrAmts", "_OthrBizPties", "_OthrPrics", "_RcvgSttlmPties", "_Refs", "_RgltryStiptns", "_SplmtryData", "_StgSttlmInstr", "_Stiptns", "_SttlmAmt", "_SttlmParams", "_TradDtls", "_TwoLegTxDtls", "_UndrlygFinInstrm"]
	@property
	def ClrDtls(self):
		return self._ClrDtls

	@ClrDtls.setter
	def ClrDtls(self, value):
		self._ClrDtls = value if value is not None else base_types.UninitialisedField(self, 'ClrDtls', Clearing5, False)

	@ClrDtls.deleter
	def ClrDtls(self):
		del self._ClrDtls
		self._ClrDtls = base_types.UninitialisedField(self, 'ClrDtls', Clearing5, False)

	@property
	def ConfPties(self):
		return self._ConfPties

	@ConfPties.setter
	def ConfPties(self, value):
		self._ConfPties = value if value is not None else base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties6, True)

	@ConfPties.deleter
	def ConfPties(self):
		del self._ConfPties
		self._ConfPties = base_types.UninitialisedField(self, 'ConfPties', ConfirmationParties6, True)

	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if value is not None else base_types.UninitialisedField(self, 'CshPties', CashParties33, False)

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = base_types.UninitialisedField(self, 'CshPties', CashParties33, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties59, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties59, False)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes124, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes124, False)

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', TransactiontIdentification4, False)

	@property
	def NbCnt(self):
		return self._NbCnt

	@NbCnt.setter
	def NbCnt(self, value):
		self._NbCnt = value if value is not None else base_types.UninitialisedField(self, 'NbCnt', NumberCount1Choice, False)

	@NbCnt.deleter
	def NbCnt(self):
		del self._NbCnt
		self._NbCnt = base_types.UninitialisedField(self, 'NbCnt', NumberCount1Choice, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts16, True)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts16, True)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties32, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties32, False)

	@property
	def OthrPrics(self):
		return self._OthrPrics

	@OthrPrics.setter
	def OthrPrics(self, value):
		self._OthrPrics = value if value is not None else base_types.UninitialisedField(self, 'OthrPrics', OtherPrices5, True)

	@OthrPrics.deleter
	def OthrPrics(self):
		del self._OthrPrics
		self._OthrPrics = base_types.UninitialisedField(self, 'OthrPrics', OtherPrices5, True)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties59, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties59, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', Linkages76, True)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', Linkages76, True)

	@property
	def RgltryStiptns(self):
		return self._RgltryStiptns

	@RgltryStiptns.setter
	def RgltryStiptns(self, value):
		self._RgltryStiptns = value if value is not None else base_types.UninitialisedField(self, 'RgltryStiptns', RegulatoryStipulations1, False)

	@RgltryStiptns.deleter
	def RgltryStiptns(self):
		del self._RgltryStiptns
		self._RgltryStiptns = base_types.UninitialisedField(self, 'RgltryStiptns', RegulatoryStipulations1, False)

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
	def StgSttlmInstr(self):
		return self._StgSttlmInstr

	@StgSttlmInstr.setter
	def StgSttlmInstr(self, value):
		self._StgSttlmInstr = value if value is not None else base_types.UninitialisedField(self, 'StgSttlmInstr', StandingSettlementInstruction13, False)

	@StgSttlmInstr.deleter
	def StgSttlmInstr(self):
		del self._StgSttlmInstr
		self._StgSttlmInstr = base_types.UninitialisedField(self, 'StgSttlmInstr', StandingSettlementInstruction13, False)

	@property
	def Stiptns(self):
		return self._Stiptns

	@Stiptns.setter
	def Stiptns(self, value):
		self._Stiptns = value if value is not None else base_types.UninitialisedField(self, 'Stiptns', FinancialInstrumentStipulations4, False)

	@Stiptns.deleter
	def Stiptns(self):
		del self._Stiptns
		self._Stiptns = base_types.UninitialisedField(self, 'Stiptns', FinancialInstrumentStipulations4, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection28, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection28, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails213, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails213, False)

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', Order24, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', Order24, False)

	@property
	def TwoLegTxDtls(self):
		return self._TwoLegTxDtls

	@TwoLegTxDtls.setter
	def TwoLegTxDtls(self, value):
		self._TwoLegTxDtls = value if value is not None else base_types.UninitialisedField(self, 'TwoLegTxDtls', TwoLegTransactionDetails5, False)

	@TwoLegTxDtls.deleter
	def TwoLegTxDtls(self):
		del self._TwoLegTxDtls
		self._TwoLegTxDtls = base_types.UninitialisedField(self, 'TwoLegTxDtls', TwoLegTransactionDetails5, False)

	@property
	def UndrlygFinInstrm(self):
		return self._UndrlygFinInstrm

	@UndrlygFinInstrm.setter
	def UndrlygFinInstrm(self, value):
		self._UndrlygFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'UndrlygFinInstrm', UnderlyingFinancialInstrument7, True)

	@UndrlygFinInstrm.deleter
	def UndrlygFinInstrm(self):
		del self._UndrlygFinInstrm
		self._UndrlygFinInstrm = base_types.UninitialisedField(self, 'UndrlygFinInstrm', UnderlyingFinancialInstrument7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrDtls', type=Clearing5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfPties', type=ConfirmationParties6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshPties', type=CashParties33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=TransactiontIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbCnt', type=NumberCount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrics', type=OtherPrices5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Linkages76, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RgltryStiptns', type=RegulatoryStipulations1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgSttlmInstr', type=StandingSettlementInstruction13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stiptns', type=FinancialInstrumentStipulations4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails213, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=Order24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwoLegTxDtls', type=TwoLegTransactionDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygFinInstrm', type=UnderlyingFinancialInstrument7, min=0, max=None, mutex_group=None, array=True),
	))