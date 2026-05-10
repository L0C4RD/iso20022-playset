from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .GroupHeader121 import GroupHeader121
from .OriginalNotification15 import OriginalNotification15

class NotificationToReceiveStatusReportV08(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_OrgnlNtfctnAndSts"]
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
	def OrgnlNtfctnAndSts(self):
		return self._OrgnlNtfctnAndSts

	@OrgnlNtfctnAndSts.setter
	def OrgnlNtfctnAndSts(self, value):
		self._OrgnlNtfctnAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlNtfctnAndSts")

	@OrgnlNtfctnAndSts.deleter
	def OrgnlNtfctnAndSts(self):
		del self._OrgnlNtfctnAndSts
		self._OrgnlNtfctnAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader121, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlNtfctnAndSts', type=OriginalNotification15, min=1, max=1, mutex_group=None, array=False),
	))

