# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitStructure6
from . import MessageHeader1
from . import SupplementaryData1

class CreateLimitV02(base_types._BaseFieldType):

	__slots__ = ["_LmtData", "_MsgHdr", "_SplmtryData"]
	@property
	def LmtData(self):
		return self._LmtData

	@LmtData.setter
	def LmtData(self, value):
		self._LmtData = value if value is not None else base_types.UninitialisedField(self, 'LmtData', LimitStructure6, True)

	@LmtData.deleter
	def LmtData(self):
		del self._LmtData
		self._LmtData = base_types.UninitialisedField(self, 'LmtData', LimitStructure6, True)

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
		base_types.FieldEntry(name='LmtData', type=LimitStructure6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))