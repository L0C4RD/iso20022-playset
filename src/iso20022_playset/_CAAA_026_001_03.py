from . import base_types
from ._AcceptorToAcquirerBatchFileExchangeV03 import AcceptorToAcquirerBatchFileExchangeV03

class CAAA_026_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrToAcqrrBtchFileXchg"]
		@property
		def AccptrToAcqrrBtchFileXchg(self):
			return self._AccptrToAcqrrBtchFileXchg

		@AccptrToAcqrrBtchFileXchg.setter
		def AccptrToAcqrrBtchFileXchg(self, value):
			self._AccptrToAcqrrBtchFileXchg = value if type(value) != base_types.auto else self.make_default("AccptrToAcqrrBtchFileXchg")

		@AccptrToAcqrrBtchFileXchg.deleter
		def AccptrToAcqrrBtchFileXchg(self):
			del self._AccptrToAcqrrBtchFileXchg
			self._AccptrToAcqrrBtchFileXchg = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrToAcqrrBtchFileXchg', type=AcceptorToAcquirerBatchFileExchangeV03, min=1, max=1, mutex_group=None, array=False),
		))

