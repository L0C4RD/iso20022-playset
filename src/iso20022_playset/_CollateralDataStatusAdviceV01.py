# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralStatusReason1 import CollateralStatusReason1
from ._CollateralStatusReason2 import CollateralStatusReason2
from ._MessageHeader12 import MessageHeader12
from ._SupplementaryData1 import SupplementaryData1

class CollateralDataStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_StsRsn", "_StsRsnAndFinInstrm"]
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
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def StsRsnAndFinInstrm(self):
		return self._StsRsnAndFinInstrm

	@StsRsnAndFinInstrm.setter
	def StsRsnAndFinInstrm(self, value):
		self._StsRsnAndFinInstrm = value if type(value) != base_types.auto else self.make_default("StsRsnAndFinInstrm")

	@StsRsnAndFinInstrm.deleter
	def StsRsnAndFinInstrm(self):
		del self._StsRsnAndFinInstrm
		self._StsRsnAndFinInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsRsn', type=CollateralStatusReason1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnAndFinInstrm', type=CollateralStatusReason2, min=0, max=1, mutex_group=None, array=False),
	))