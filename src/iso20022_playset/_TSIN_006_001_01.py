from . import base_types
from ._InvoiceAssignmentRequestV01 import InvoiceAssignmentRequestV01

class TSIN_006_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcAssgnmtReq"]
		@property
		def InvcAssgnmtReq(self):
			return self._InvcAssgnmtReq

		@InvcAssgnmtReq.setter
		def InvcAssgnmtReq(self, value):
			self._InvcAssgnmtReq = value if type(value) != base_types.auto else self.make_default("InvcAssgnmtReq")

		@InvcAssgnmtReq.deleter
		def InvcAssgnmtReq(self):
			del self._InvcAssgnmtReq
			self._InvcAssgnmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtReq', type=InvoiceAssignmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

