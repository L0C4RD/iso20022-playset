# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GroupHeader117 import GroupHeader117
from ._NotificationCancellationReason2 import NotificationCancellationReason2
from ._OriginalNotification18 import OriginalNotification18
from ._SupplementaryData1 import SupplementaryData1

class NotificationToReceiveCancellationAdviceV10(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_GrpHdr", "_OrgnlNtfctn", "_SplmtryData"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def OrgnlNtfctn(self):
		return self._OrgnlNtfctn

	@OrgnlNtfctn.setter
	def OrgnlNtfctn(self, value):
		self._OrgnlNtfctn = value if type(value) != base_types.auto else self.make_default("OrgnlNtfctn")

	@OrgnlNtfctn.deleter
	def OrgnlNtfctn(self):
		del self._OrgnlNtfctn
		self._OrgnlNtfctn = None

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
		base_types.FieldEntry(name='CxlRsn', type=NotificationCancellationReason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctn', type=OriginalNotification18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))