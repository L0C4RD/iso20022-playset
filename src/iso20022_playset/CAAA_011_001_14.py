from . import base_types
from .AcceptorBatchTransferV14 import AcceptorBatchTransferV14

class CAAA_011_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrBtchTrf"]
		@property
		def AccptrBtchTrf(self):
			return self._AccptrBtchTrf

		@AccptrBtchTrf.setter
		def AccptrBtchTrf(self, value):
			self._AccptrBtchTrf = value if type(value) != auto else self.make_default("AccptrBtchTrf")

		@AccptrBtchTrf.deleter
		def AccptrBtchTrf(self):
			del self._AccptrBtchTrf
			self._AccptrBtchTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrBtchTrf', type=AcceptorBatchTransferV14, min=1, max=1, mutex_group=None, array=False),
		))

