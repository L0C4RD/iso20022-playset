from . import base_types
from .AcquirerToAcceptorBatchFileExchangeV02 import AcquirerToAcceptorBatchFileExchangeV02

class CAAA_027_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcqrrToAccptrBtchFileXchg"]
		@property
		def AcqrrToAccptrBtchFileXchg(self):
			return self._AcqrrToAccptrBtchFileXchg

		@AcqrrToAccptrBtchFileXchg.setter
		def AcqrrToAccptrBtchFileXchg(self, value):
			self._AcqrrToAccptrBtchFileXchg = value if type(value) != auto else self.make_default("AcqrrToAccptrBtchFileXchg")

		@AcqrrToAccptrBtchFileXchg.deleter
		def AcqrrToAccptrBtchFileXchg(self):
			del self._AcqrrToAccptrBtchFileXchg
			self._AcqrrToAccptrBtchFileXchg = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcqrrToAccptrBtchFileXchg', type=AcquirerToAcceptorBatchFileExchangeV02, min=1, max=1, mutex_group=None, array=False),
		))

