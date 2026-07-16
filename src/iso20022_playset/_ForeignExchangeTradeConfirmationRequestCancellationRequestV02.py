# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Header23
from . import Max35Text
from . import MessageIdentification1
from . import SupplementaryData1
from . import TradePartyIdentification9
from . import UnderlyingProductIdentifier1Code

class ForeignExchangeTradeConfirmationRequestCancellationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyRoleId", "_CxlReqId", "_Hdr", "_SplmtryData", "_TradId", "_TradgSdId", "_UndrlygPdctTp"]
	@property
	def CtrPtyRoleId(self):
		return self._CtrPtyRoleId

	@CtrPtyRoleId.setter
	def CtrPtyRoleId(self, value):
		self._CtrPtyRoleId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRoleId', TradePartyIdentification9, False)

	@CtrPtyRoleId.deleter
	def CtrPtyRoleId(self):
		del self._CtrPtyRoleId
		self._CtrPtyRoleId = base_types.UninitialisedField(self, 'CtrPtyRoleId', TradePartyIdentification9, False)

	@property
	def CxlReqId(self):
		return self._CxlReqId

	@CxlReqId.setter
	def CxlReqId(self, value):
		self._CxlReqId = value if value is not None else base_types.UninitialisedField(self, 'CxlReqId', MessageIdentification1, False)

	@CxlReqId.deleter
	def CxlReqId(self):
		del self._CxlReqId
		self._CxlReqId = base_types.UninitialisedField(self, 'CxlReqId', MessageIdentification1, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header23, False)

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
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if value is not None else base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = base_types.UninitialisedField(self, 'TradgSdId', TradePartyIdentification9, False)

	@property
	def UndrlygPdctTp(self):
		return self._UndrlygPdctTp

	@UndrlygPdctTp.setter
	def UndrlygPdctTp(self, value):
		self._UndrlygPdctTp = value if value is not None else base_types.UninitialisedField(self, 'UndrlygPdctTp', UnderlyingProductIdentifier1Code, False)

	@UndrlygPdctTp.deleter
	def UndrlygPdctTp(self):
		del self._UndrlygPdctTp
		self._UndrlygPdctTp = base_types.UninitialisedField(self, 'UndrlygPdctTp', UnderlyingProductIdentifier1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyRoleId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlReqId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygPdctTp', type=UnderlyingProductIdentifier1Code, min=1, max=1, mutex_group=None, array=False),
	))