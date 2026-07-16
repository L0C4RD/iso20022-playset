# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValue5
from . import MessageHeader1
from . import SupplementaryData1
from . import SystemPartyIdentification2Choice

class CollateralValueCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CollVal", "_MsgHdr", "_PtyId", "_SplmtryData"]
	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if value is not None else base_types.UninitialisedField(self, 'CollVal', CollateralValue5, True)

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = base_types.UninitialisedField(self, 'CollVal', CollateralValue5, True)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollVal', type=CollateralValue5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))