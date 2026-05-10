import base_types
import GroupHeader117
import OriginalNotification16
import SupplementaryData1
import NotificationCancellationReason2

class NotificationToReceiveCancellationAdviceV09(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_GrpHdr", "_SplmtryData", "_OrgnlNtfctn"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def OrgnlNtfctn(self):
		return self._OrgnlNtfctn

	@OrgnlNtfctn.setter
	def OrgnlNtfctn(self, value):
		self._OrgnlNtfctn = value if type(value) != auto else self.make_default("OrgnlNtfctn")

	@OrgnlNtfctn.deleter
	def OrgnlNtfctn(self):
		del self._OrgnlNtfctn
		self._OrgnlNtfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=NotificationCancellationReason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlNtfctn', type=OriginalNotification16, min=1, max=1, mutex_group=None, array=False),
	))

