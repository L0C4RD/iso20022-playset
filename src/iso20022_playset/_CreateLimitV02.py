# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LimitStructure6 import LimitStructure6
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class CreateLimitV02(base_types._BaseFieldType):

	__slots__ = ["_LmtData", "_MsgHdr", "_SplmtryData"]
	@property
	def LmtData(self):
		return self._LmtData

	@LmtData.setter
	def LmtData(self, value):
		self._LmtData = value if type(value) != base_types.auto else self.make_default("LmtData")

	@LmtData.deleter
	def LmtData(self):
		del self._LmtData
		self._LmtData = None

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != base_types.auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtData', type=LimitStructure6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))