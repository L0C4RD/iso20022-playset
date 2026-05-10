from . import base_types
from ._NotificationToReceiveStatusReportV08 import NotificationToReceiveStatusReportV08

class CAMT_059_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NtfctnToRcvStsRpt"]
		@property
		def NtfctnToRcvStsRpt(self):
			return self._NtfctnToRcvStsRpt

		@NtfctnToRcvStsRpt.setter
		def NtfctnToRcvStsRpt(self, value):
			self._NtfctnToRcvStsRpt = value if type(value) != base_types.auto else self.make_default("NtfctnToRcvStsRpt")

		@NtfctnToRcvStsRpt.deleter
		def NtfctnToRcvStsRpt(self):
			del self._NtfctnToRcvStsRpt
			self._NtfctnToRcvStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvStsRpt', type=NotificationToReceiveStatusReportV08, min=1, max=1, mutex_group=None, array=False),
		))

