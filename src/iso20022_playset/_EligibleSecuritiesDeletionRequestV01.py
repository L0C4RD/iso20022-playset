# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibleSecurity5
from . import MessageHeader1
from . import SupplementaryData1

class EligibleSecuritiesDeletionRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ElgblScty", "_MsgHdr", "_SplmtryData"]
	@property
	def ElgblScty(self):
		return self._ElgblScty

	@ElgblScty.setter
	def ElgblScty(self, value):
		self._ElgblScty = value if value is not None else base_types.UninitialisedField(self, 'ElgblScty', EligibleSecurity5, True)

	@ElgblScty.deleter
	def ElgblScty(self):
		del self._ElgblScty
		self._ElgblScty = base_types.UninitialisedField(self, 'ElgblScty', EligibleSecurity5, True)

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
		base_types.FieldEntry(name='ElgblScty', type=EligibleSecurity5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))