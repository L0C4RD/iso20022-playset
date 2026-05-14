# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibleCounterpart3 import EligibleCounterpart3
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class EligibleCounterpartCSDCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ElgblCntrptCSD", "_MsgHdr", "_SplmtryData"]
	@property
	def ElgblCntrptCSD(self):
		return self._ElgblCntrptCSD

	@ElgblCntrptCSD.setter
	def ElgblCntrptCSD(self, value):
		self._ElgblCntrptCSD = value if type(value) != base_types.auto else self.make_default("ElgblCntrptCSD")

	@ElgblCntrptCSD.deleter
	def ElgblCntrptCSD(self):
		del self._ElgblCntrptCSD
		self._ElgblCntrptCSD = None

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
		base_types.FieldEntry(name='ElgblCntrptCSD', type=EligibleCounterpart3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))