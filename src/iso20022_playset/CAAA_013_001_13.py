from . import base_types
from .AcceptorDiagnosticRequestV13 import AcceptorDiagnosticRequestV13

class CAAA_013_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrDgnstcReq"]
		@property
		def AccptrDgnstcReq(self):
			return self._AccptrDgnstcReq

		@AccptrDgnstcReq.setter
		def AccptrDgnstcReq(self, value):
			self._AccptrDgnstcReq = value if type(value) != auto else self.make_default("AccptrDgnstcReq")

		@AccptrDgnstcReq.deleter
		def AccptrDgnstcReq(self):
			del self._AccptrDgnstcReq
			self._AccptrDgnstcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrDgnstcReq', type=AcceptorDiagnosticRequestV13, min=1, max=1, mutex_group=None, array=False),
		))

