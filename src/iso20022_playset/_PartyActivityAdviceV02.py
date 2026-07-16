# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader1
from . import PartyStatement3
from . import SupplementaryData1

class PartyActivityAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_PtyActvty", "_SplmtryData"]
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
	def PtyActvty(self):
		return self._PtyActvty

	@PtyActvty.setter
	def PtyActvty(self, value):
		self._PtyActvty = value if value is not None else base_types.UninitialisedField(self, 'PtyActvty', PartyStatement3, False)

	@PtyActvty.deleter
	def PtyActvty(self):
		del self._PtyActvty
		self._PtyActvty = base_types.UninitialisedField(self, 'PtyActvty', PartyStatement3, False)

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyActvty', type=PartyStatement3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))