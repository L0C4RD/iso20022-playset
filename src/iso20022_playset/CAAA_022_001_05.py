from . import base_types
from .AcceptorNonFinancialRequestV05 import AcceptorNonFinancialRequestV05

class CAAA_022_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrNonFinReq"]
		@property
		def AccptrNonFinReq(self):
			return self._AccptrNonFinReq

		@AccptrNonFinReq.setter
		def AccptrNonFinReq(self, value):
			self._AccptrNonFinReq = value if type(value) != auto else self.make_default("AccptrNonFinReq")

		@AccptrNonFinReq.deleter
		def AccptrNonFinReq(self):
			del self._AccptrNonFinReq
			self._AccptrNonFinReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinReq', type=AcceptorNonFinancialRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

