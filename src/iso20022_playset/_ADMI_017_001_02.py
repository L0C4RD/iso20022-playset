from . import base_types
from ._ProcessingRequestV02 import ProcessingRequestV02

class ADMI_017_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrcgReq"]
		@property
		def PrcgReq(self):
			return self._PrcgReq

		@PrcgReq.setter
		def PrcgReq(self, value):
			self._PrcgReq = value if type(value) != base_types.auto else self.make_default("PrcgReq")

		@PrcgReq.deleter
		def PrcgReq(self):
			del self._PrcgReq
			self._PrcgReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrcgReq', type=ProcessingRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

