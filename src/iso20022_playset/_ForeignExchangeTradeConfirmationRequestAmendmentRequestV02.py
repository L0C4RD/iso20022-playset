from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._TradePartyIdentification9 import TradePartyIdentification9
from ._Trade9 import Trade9
from ._Period12 import Period12
from ._Header23 import Header23
from ._QueryTradeStatus1Code import QueryTradeStatus1Code
from ._MessageIdentification1 import MessageIdentification1
from ._Max35NumericText import Max35NumericText

class ForeignExchangeTradeConfirmationRequestAmendmentRequestV02(base_types._BaseFieldType):

	__slots__ = ["_AmdmntReqId", "_TradDtl", "_Hdr", "_TradgSdId", "_CtrPtySdId", "_QryStartNb", "_QryPrd", "_QryTradSts", "_SplmtryData"]
	@property
	def AmdmntReqId(self):
		return self._AmdmntReqId

	@AmdmntReqId.setter
	def AmdmntReqId(self, value):
		self._AmdmntReqId = value if type(value) != base_types.auto else self.make_default("AmdmntReqId")

	@AmdmntReqId.deleter
	def AmdmntReqId(self):
		del self._AmdmntReqId
		self._AmdmntReqId = None

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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def QryPrd(self):
		return self._QryPrd

	@QryPrd.setter
	def QryPrd(self, value):
		self._QryPrd = value if type(value) != base_types.auto else self.make_default("QryPrd")

	@QryPrd.deleter
	def QryPrd(self):
		del self._QryPrd
		self._QryPrd = None

	@property
	def QryStartNb(self):
		return self._QryStartNb

	@QryStartNb.setter
	def QryStartNb(self, value):
		self._QryStartNb = value if type(value) != base_types.auto else self.make_default("QryStartNb")

	@QryStartNb.deleter
	def QryStartNb(self):
		del self._QryStartNb
		self._QryStartNb = None

	@property
	def QryTradSts(self):
		return self._QryTradSts

	@QryTradSts.setter
	def QryTradSts(self, value):
		self._QryTradSts = value if type(value) != base_types.auto else self.make_default("QryTradSts")

	@QryTradSts.deleter
	def QryTradSts(self):
		del self._QryTradSts
		self._QryTradSts = None

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
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if type(value) != base_types.auto else self.make_default("TradDtl")

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPrd', type=Period12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTradSts', type=QueryTradeStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtl', type=Trade9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
	))

