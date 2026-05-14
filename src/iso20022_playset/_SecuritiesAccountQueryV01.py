# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MessageHeader2 import MessageHeader2
from ._SecuritiesAccountReturnCriteria1 import SecuritiesAccountReturnCriteria1
from ._SecuritiesAccountSearchCriteria2 import SecuritiesAccountSearchCriteria2
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesAccountQueryV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_RtrCrit", "_SchCrit", "_SplmtryData"]
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
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if type(value) != base_types.auto else self.make_default("RtrCrit")

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = None

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != base_types.auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=SecuritiesAccountReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SecuritiesAccountSearchCriteria2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))