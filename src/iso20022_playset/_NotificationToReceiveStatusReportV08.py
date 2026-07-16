# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader121
from . import OriginalNotification15
from . import SupplementaryData1

class NotificationToReceiveStatusReportV08(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlNtfctnAndSts", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader121, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader121, False)

	@property
	def OrgnlNtfctnAndSts(self):
		return self._OrgnlNtfctnAndSts

	@OrgnlNtfctnAndSts.setter
	def OrgnlNtfctnAndSts(self, value):
		self._OrgnlNtfctnAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNtfctnAndSts', OriginalNotification15, False)

	@OrgnlNtfctnAndSts.deleter
	def OrgnlNtfctnAndSts(self):
		del self._OrgnlNtfctnAndSts
		self._OrgnlNtfctnAndSts = base_types.UninitialisedField(self, 'OrgnlNtfctnAndSts', OriginalNotification15, False)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader121, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtfctnAndSts', type=OriginalNotification15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))