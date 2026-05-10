from . import base_types
from .ReturnTransactionV11 import ReturnTransactionV11

class CAMT_006_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrTx"]
		@property
		def RtrTx(self):
			return self._RtrTx

		@RtrTx.setter
		def RtrTx(self, value):
			self._RtrTx = value if type(value) != base_types.auto else self.make_default("RtrTx")

		@RtrTx.deleter
		def RtrTx(self):
			del self._RtrTx
			self._RtrTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrTx', type=ReturnTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))

