from . import base_types
from ._InvoiceAssignmentStatusV01 import InvoiceAssignmentStatusV01

class TSIN_007_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcAssgnmtSts"]
		@property
		def InvcAssgnmtSts(self):
			return self._InvcAssgnmtSts

		@InvcAssgnmtSts.setter
		def InvcAssgnmtSts(self, value):
			self._InvcAssgnmtSts = value if type(value) != base_types.auto else self.make_default("InvcAssgnmtSts")

		@InvcAssgnmtSts.deleter
		def InvcAssgnmtSts(self):
			del self._InvcAssgnmtSts
			self._InvcAssgnmtSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtSts', type=InvoiceAssignmentStatusV01, min=1, max=1, mutex_group=None, array=False),
		))

