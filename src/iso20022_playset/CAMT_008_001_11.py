from . import base_types
from .CancelTransactionV11 import CancelTransactionV11

class CAMT_008_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CclTx"]
		@property
		def CclTx(self):
			return self._CclTx

		@CclTx.setter
		def CclTx(self, value):
			self._CclTx = value if type(value) != auto else self.make_default("CclTx")

		@CclTx.deleter
		def CclTx(self):
			del self._CclTx
			self._CclTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CclTx', type=CancelTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))

