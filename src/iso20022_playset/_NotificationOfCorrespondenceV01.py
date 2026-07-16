# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorrespondenceNotification1
from . import GroupHeader129
from . import SupplementaryData1

class NotificationOfCorrespondenceV01(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_NtfctnData", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader129, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader129, False)

	@property
	def NtfctnData(self):
		return self._NtfctnData

	@NtfctnData.setter
	def NtfctnData(self, value):
		self._NtfctnData = value if value is not None else base_types.UninitialisedField(self, 'NtfctnData', CorrespondenceNotification1, True)

	@NtfctnData.deleter
	def NtfctnData(self):
		del self._NtfctnData
		self._NtfctnData = base_types.UninitialisedField(self, 'NtfctnData', CorrespondenceNotification1, True)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnData', type=CorrespondenceNotification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))