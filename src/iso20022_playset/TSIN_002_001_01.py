import base_types
import InvoiceFinancingRequestStatusV01

class TSIN_002_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcFincgReqSts"]
		@property
		def InvcFincgReqSts(self):
			return self._InvcFincgReqSts

		@InvcFincgReqSts.setter
		def InvcFincgReqSts(self, value):
			self._InvcFincgReqSts = value if type(value) != auto else self.make_default("InvcFincgReqSts")

		@InvcFincgReqSts.deleter
		def InvcFincgReqSts(self):
			del self._InvcFincgReqSts
			self._InvcFincgReqSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgReqSts', type=InvoiceFinancingRequestStatusV01, min=1, max=1, mutex_group=None, array=False),
		))

