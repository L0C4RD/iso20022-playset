# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorrespondenceNotification1 import CorrespondenceNotification1
from ._GroupHeader129 import GroupHeader129
from ._SupplementaryData1 import SupplementaryData1

class NotificationOfCorrespondenceV01(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_NtfctnData", "_SplmtryData"]
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
	def NtfctnData(self):
		return self._NtfctnData

	@NtfctnData.setter
	def NtfctnData(self, value):
		self._NtfctnData = value if type(value) != base_types.auto else self.make_default("NtfctnData")

	@NtfctnData.deleter
	def NtfctnData(self):
		del self._NtfctnData
		self._NtfctnData = None

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnData', type=CorrespondenceNotification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))