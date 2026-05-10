from . import base_types
import InvoiceAssignmentNotificationV01

class TSIN_008_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcAssgnmtNtfctn"]
		@property
		def InvcAssgnmtNtfctn(self):
			return self._InvcAssgnmtNtfctn

		@InvcAssgnmtNtfctn.setter
		def InvcAssgnmtNtfctn(self, value):
			self._InvcAssgnmtNtfctn = value if type(value) != auto else self.make_default("InvcAssgnmtNtfctn")

		@InvcAssgnmtNtfctn.deleter
		def InvcAssgnmtNtfctn(self):
			del self._InvcAssgnmtNtfctn
			self._InvcAssgnmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtNtfctn', type=InvoiceAssignmentNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

