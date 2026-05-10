from . import base_types
from .ModifyTransactionV10 import ModifyTransactionV10

class CAMT_007_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ModfyTx"]
		@property
		def ModfyTx(self):
			return self._ModfyTx

		@ModfyTx.setter
		def ModfyTx(self, value):
			self._ModfyTx = value if type(value) != auto else self.make_default("ModfyTx")

		@ModfyTx.deleter
		def ModfyTx(self):
			del self._ModfyTx
			self._ModfyTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyTx', type=ModifyTransactionV10, min=1, max=1, mutex_group=None, array=False),
		))

