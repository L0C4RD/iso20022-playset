import base_types
import InvoiceFinancingRequestV01

class TSIN_001_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcFincgReq"]
		@property
		def InvcFincgReq(self):
			return self._InvcFincgReq

		@InvcFincgReq.setter
		def InvcFincgReq(self, value):
			self._InvcFincgReq = value if type(value) != auto else self.make_default("InvcFincgReq")

		@InvcFincgReq.deleter
		def InvcFincgReq(self):
			del self._InvcFincgReq
			self._InvcFincgReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgReq', type=InvoiceFinancingRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

