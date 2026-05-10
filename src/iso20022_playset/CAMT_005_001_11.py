from . import base_types
import GetTransactionV11

class CAMT_005_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetTx"]
		@property
		def GetTx(self):
			return self._GetTx

		@GetTx.setter
		def GetTx(self, value):
			self._GetTx = value if type(value) != auto else self.make_default("GetTx")

		@GetTx.deleter
		def GetTx(self):
			del self._GetTx
			self._GetTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetTx', type=GetTransactionV11, min=1, max=1, mutex_group=None, array=False),
		))

