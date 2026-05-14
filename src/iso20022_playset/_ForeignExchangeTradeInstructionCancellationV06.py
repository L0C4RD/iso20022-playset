# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgreedRate3 import AgreedRate3
from ._AmountsAndValueDate8 import AmountsAndValueDate8
from ._GeneralInformation9 import GeneralInformation9
from ._NonDeliverableForwardConditions1 import NonDeliverableForwardConditions1
from ._PostTradeEvent1 import PostTradeEvent1
from ._RegulatoryReporting8 import RegulatoryReporting8
from ._SettlementParties120 import SettlementParties120
from ._SupplementaryData1 import SupplementaryData1
from ._TradeAgreement15 import TradeAgreement15
from ._TradePartyIdentification8 import TradePartyIdentification8

class ForeignExchangeTradeInstructionCancellationV06(base_types._BaseFieldType):

	__slots__ = ["_AgrdRate", "_CtrPtySdId", "_CtrPtySdSttlmInstrs", "_NDFConds", "_OptnlGnlInf", "_PstTradEvt", "_RgltryRptg", "_SplmtryData", "_TradAmts", "_TradInf", "_TradgSdId", "_TradgSdSttlmInstrs"]
	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if type(value) != base_types.auto else self.make_default("AgrdRate")

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = None

	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if type(value) != base_types.auto else self.make_default("CtrPtySdId")

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = None

	@property
	def CtrPtySdSttlmInstrs(self):
		return self._CtrPtySdSttlmInstrs

	@CtrPtySdSttlmInstrs.setter
	def CtrPtySdSttlmInstrs(self, value):
		self._CtrPtySdSttlmInstrs = value if type(value) != base_types.auto else self.make_default("CtrPtySdSttlmInstrs")

	@CtrPtySdSttlmInstrs.deleter
	def CtrPtySdSttlmInstrs(self):
		del self._CtrPtySdSttlmInstrs
		self._CtrPtySdSttlmInstrs = None

	@property
	def NDFConds(self):
		return self._NDFConds

	@NDFConds.setter
	def NDFConds(self, value):
		self._NDFConds = value if type(value) != base_types.auto else self.make_default("NDFConds")

	@NDFConds.deleter
	def NDFConds(self):
		del self._NDFConds
		self._NDFConds = None

	@property
	def OptnlGnlInf(self):
		return self._OptnlGnlInf

	@OptnlGnlInf.setter
	def OptnlGnlInf(self, value):
		self._OptnlGnlInf = value if type(value) != base_types.auto else self.make_default("OptnlGnlInf")

	@OptnlGnlInf.deleter
	def OptnlGnlInf(self):
		del self._OptnlGnlInf
		self._OptnlGnlInf = None

	@property
	def PstTradEvt(self):
		return self._PstTradEvt

	@PstTradEvt.setter
	def PstTradEvt(self, value):
		self._PstTradEvt = value if type(value) != base_types.auto else self.make_default("PstTradEvt")

	@PstTradEvt.deleter
	def PstTradEvt(self):
		del self._PstTradEvt
		self._PstTradEvt = None

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if type(value) != base_types.auto else self.make_default("RgltryRptg")

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = None

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
	def TradAmts(self):
		return self._TradAmts

	@TradAmts.setter
	def TradAmts(self, value):
		self._TradAmts = value if type(value) != base_types.auto else self.make_default("TradAmts")

	@TradAmts.deleter
	def TradAmts(self):
		del self._TradAmts
		self._TradAmts = None

	@property
	def TradInf(self):
		return self._TradInf

	@TradInf.setter
	def TradInf(self, value):
		self._TradInf = value if type(value) != base_types.auto else self.make_default("TradInf")

	@TradInf.deleter
	def TradInf(self):
		del self._TradInf
		self._TradInf = None

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if type(value) != base_types.auto else self.make_default("TradgSdId")

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = None

	@property
	def TradgSdSttlmInstrs(self):
		return self._TradgSdSttlmInstrs

	@TradgSdSttlmInstrs.setter
	def TradgSdSttlmInstrs(self, value):
		self._TradgSdSttlmInstrs = value if type(value) != base_types.auto else self.make_default("TradgSdSttlmInstrs")

	@TradgSdSttlmInstrs.deleter
	def TradgSdSttlmInstrs(self):
		del self._TradgSdSttlmInstrs
		self._TradgSdSttlmInstrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdRate', type=AgreedRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdSttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NDFConds', type=NonDeliverableForwardConditions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnlGnlInf', type=GeneralInformation9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradEvt', type=PostTradeEvent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradAmts', type=AmountsAndValueDate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradInf', type=TradeAgreement15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdSttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
	))