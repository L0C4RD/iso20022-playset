# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreedRate3
from . import AmountsAndValueDate8
from . import GeneralInformation9
from . import NonDeliverableForwardConditions1
from . import PostTradeEvent1
from . import RegulatoryReporting8
from . import SettlementParties120
from . import SupplementaryData1
from . import TradeAgreement14
from . import TradePartyIdentification8

class ForeignExchangeTradeInstructionV06(base_types._BaseFieldType):

	__slots__ = ["_AgrdRate", "_CtrPtySdId", "_CtrPtySdSttlmInstrs", "_NDFConds", "_OptnlGnlInf", "_PstTradEvt", "_RgltryRptg", "_SplmtryData", "_TradAmts", "_TradInf", "_TradgSdId", "_TradgSdSttlmInstrs"]
	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if value is not None else base_types.UninitialisedField(self, 'AgrdRate', AgreedRate3, False)

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = base_types.UninitialisedField(self, 'AgrdRate', AgreedRate3, False)

	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification8, False)

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = base_types.UninitialisedField(self, 'CtrPtySdId', TradePartyIdentification8, False)

	@property
	def CtrPtySdSttlmInstrs(self):
		return self._CtrPtySdSttlmInstrs

	@CtrPtySdSttlmInstrs.setter
	def CtrPtySdSttlmInstrs(self, value):
		self._CtrPtySdSttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySdSttlmInstrs', SettlementParties120, False)

	@CtrPtySdSttlmInstrs.deleter
	def CtrPtySdSttlmInstrs(self):
		del self._CtrPtySdSttlmInstrs
		self._CtrPtySdSttlmInstrs = base_types.UninitialisedField(self, 'CtrPtySdSttlmInstrs', SettlementParties120, False)

	@property
	def NDFConds(self):
		return self._NDFConds

	@NDFConds.setter
	def NDFConds(self, value):
		self._NDFConds = value if value is not None else base_types.UninitialisedField(self, 'NDFConds', NonDeliverableForwardConditions1, False)

	@NDFConds.deleter
	def NDFConds(self):
		del self._NDFConds
		self._NDFConds = base_types.UninitialisedField(self, 'NDFConds', NonDeliverableForwardConditions1, False)

	@property
	def OptnlGnlInf(self):
		return self._OptnlGnlInf

	@OptnlGnlInf.setter
	def OptnlGnlInf(self, value):
		self._OptnlGnlInf = value if value is not None else base_types.UninitialisedField(self, 'OptnlGnlInf', GeneralInformation9, False)

	@OptnlGnlInf.deleter
	def OptnlGnlInf(self):
		del self._OptnlGnlInf
		self._OptnlGnlInf = base_types.UninitialisedField(self, 'OptnlGnlInf', GeneralInformation9, False)

	@property
	def PstTradEvt(self):
		return self._PstTradEvt

	@PstTradEvt.setter
	def PstTradEvt(self, value):
		self._PstTradEvt = value if value is not None else base_types.UninitialisedField(self, 'PstTradEvt', PostTradeEvent1, False)

	@PstTradEvt.deleter
	def PstTradEvt(self):
		del self._PstTradEvt
		self._PstTradEvt = base_types.UninitialisedField(self, 'PstTradEvt', PostTradeEvent1, False)

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if value is not None else base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting8, False)

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting8, False)

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
	def TradAmts(self):
		return self._TradAmts

	@TradAmts.setter
	def TradAmts(self, value):
		self._TradAmts = value if value is not None else base_types.UninitialisedField(self, 'TradAmts', AmountsAndValueDate8, False)

	@TradAmts.deleter
	def TradAmts(self):
		del self._TradAmts
		self._TradAmts = base_types.UninitialisedField(self, 'TradAmts', AmountsAndValueDate8, False)

	@property
	def TradInf(self):
		return self._TradInf

	@TradInf.setter
	def TradInf(self, value):
		self._TradInf = value if value is not None else base_types.UninitialisedField(self, 'TradInf', TradeAgreement14, False)

	@TradInf.deleter
	def TradInf(self):
		del self._TradInf
		self._TradInf = base_types.UninitialisedField(self, 'TradInf', TradeAgreement14, False)

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if value is not None else base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification8, False)

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification8, False)

	@property
	def TradgSdSttlmInstrs(self):
		return self._TradgSdSttlmInstrs

	@TradgSdSttlmInstrs.setter
	def TradgSdSttlmInstrs(self, value):
		self._TradgSdSttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'TradgSdSttlmInstrs', SettlementParties120, False)

	@TradgSdSttlmInstrs.deleter
	def TradgSdSttlmInstrs(self):
		del self._TradgSdSttlmInstrs
		self._TradgSdSttlmInstrs = base_types.UninitialisedField(self, 'TradgSdSttlmInstrs', SettlementParties120, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdRate', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdSttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NDFConds', type=NonDeliverableForwardConditions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnlGnlInf', type=GeneralInformation9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTradEvt', type=PostTradeEvent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradAmts', type=AmountsAndValueDate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradInf', type=TradeAgreement14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdSttlmInstrs', type=SettlementParties120, min=0, max=1, mutex_group=None, array=False),
	))