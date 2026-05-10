import base_types
import Max35Text
import Header23
import SupplementaryData1
import MessageIdentification1
import UnderlyingProductIdentifier1Code
import TradePartyIdentification9

class ForeignExchangeTradeConfirmationRequestCancellationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TradId", "_CtrPtyRoleId", "_Hdr", "_CxlReqId", "_TradgSdId", "_UndrlygPdctTp"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def CtrPtyRoleId(self):
		return self._CtrPtyRoleId

	@CtrPtyRoleId.setter
	def CtrPtyRoleId(self, value):
		self._CtrPtyRoleId = value if type(value) != auto else self.make_default("CtrPtyRoleId")

	@CtrPtyRoleId.deleter
	def CtrPtyRoleId(self):
		del self._CtrPtyRoleId
		self._CtrPtyRoleId = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def CxlReqId(self):
		return self._CxlReqId

	@CxlReqId.setter
	def CxlReqId(self, value):
		self._CxlReqId = value if type(value) != auto else self.make_default("CxlReqId")

	@CxlReqId.deleter
	def CxlReqId(self):
		del self._CxlReqId
		self._CxlReqId = None

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if type(value) != auto else self.make_default("TradgSdId")

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = None

	@property
	def UndrlygPdctTp(self):
		return self._UndrlygPdctTp

	@UndrlygPdctTp.setter
	def UndrlygPdctTp(self, value):
		self._UndrlygPdctTp = value if type(value) != auto else self.make_default("UndrlygPdctTp")

	@UndrlygPdctTp.deleter
	def UndrlygPdctTp(self):
		del self._UndrlygPdctTp
		self._UndrlygPdctTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRoleId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlReqId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygPdctTp', type=UnderlyingProductIdentifier1Code, min=1, max=1, mutex_group=None, array=False),
	))

