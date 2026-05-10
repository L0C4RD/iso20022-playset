from . import base_types
from ._AcceptorDiagnosticResponseV12 import AcceptorDiagnosticResponseV12

class CAAA_014_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrDgnstcRspn"]
		@property
		def AccptrDgnstcRspn(self):
			return self._AccptrDgnstcRspn

		@AccptrDgnstcRspn.setter
		def AccptrDgnstcRspn(self, value):
			self._AccptrDgnstcRspn = value if type(value) != base_types.auto else self.make_default("AccptrDgnstcRspn")

		@AccptrDgnstcRspn.deleter
		def AccptrDgnstcRspn(self):
			del self._AccptrDgnstcRspn
			self._AccptrDgnstcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrDgnstcRspn', type=AcceptorDiagnosticResponseV12, min=1, max=1, mutex_group=None, array=False),
		))

