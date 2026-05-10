from . import base_types
from .MultilateralSettlementRequestV02 import MultilateralSettlementRequestV02

class PACS_029_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MulSttlmReq"]
		@property
		def MulSttlmReq(self):
			return self._MulSttlmReq

		@MulSttlmReq.setter
		def MulSttlmReq(self, value):
			self._MulSttlmReq = value if type(value) != base_types.auto else self.make_default("MulSttlmReq")

		@MulSttlmReq.deleter
		def MulSttlmReq(self):
			del self._MulSttlmReq
			self._MulSttlmReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MulSttlmReq', type=MultilateralSettlementRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

