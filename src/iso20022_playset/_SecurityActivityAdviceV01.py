# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MessageHeader1 import MessageHeader1
from ._Pagination1 import Pagination1
from ._SecurityStatement3 import SecurityStatement3
from ._SupplementaryData1 import SupplementaryData1

class SecurityActivityAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_Pgntn", "_SctyActvty", "_SplmtryData"]
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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def SctyActvty(self):
		return self._SctyActvty

	@SctyActvty.setter
	def SctyActvty(self, value):
		self._SctyActvty = value if type(value) != base_types.auto else self.make_default("SctyActvty")

	@SctyActvty.deleter
	def SctyActvty(self):
		del self._SctyActvty
		self._SctyActvty = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyActvty', type=SecurityStatement3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))