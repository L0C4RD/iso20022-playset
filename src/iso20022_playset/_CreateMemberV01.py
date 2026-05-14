# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Member6 import Member6
from ._MemberIdentification3Choice import MemberIdentification3Choice
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class CreateMemberV01(base_types._BaseFieldType):

	__slots__ = ["_MmbId", "_MsgHdr", "_SplmtryData", "_ValSet"]
	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != base_types.auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

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

	@property
	def ValSet(self):
		return self._ValSet

	@ValSet.setter
	def ValSet(self, value):
		self._ValSet = value if type(value) != base_types.auto else self.make_default("ValSet")

	@ValSet.deleter
	def ValSet(self):
		del self._ValSet
		self._ValSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValSet', type=Member6, min=1, max=1, mutex_group=None, array=False),
	))