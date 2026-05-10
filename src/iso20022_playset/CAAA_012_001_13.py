from . import base_types
import AcceptorBatchTransferResponseV13

class CAAA_012_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrBtchTrfRspn"]
		@property
		def AccptrBtchTrfRspn(self):
			return self._AccptrBtchTrfRspn

		@AccptrBtchTrfRspn.setter
		def AccptrBtchTrfRspn(self, value):
			self._AccptrBtchTrfRspn = value if type(value) != auto else self.make_default("AccptrBtchTrfRspn")

		@AccptrBtchTrfRspn.deleter
		def AccptrBtchTrfRspn(self):
			del self._AccptrBtchTrfRspn
			self._AccptrBtchTrfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrBtchTrfRspn', type=AcceptorBatchTransferResponseV13, min=1, max=1, mutex_group=None, array=False),
		))

