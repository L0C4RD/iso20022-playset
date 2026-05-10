from . import base_types
from .ReceiptV09 import ReceiptV09

class CAMT_025_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_Rct"]
		@property
		def Rct(self):
			return self._Rct

		@Rct.setter
		def Rct(self, value):
			self._Rct = value if type(value) != auto else self.make_default("Rct")

		@Rct.deleter
		def Rct(self):
			del self._Rct
			self._Rct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Rct', type=ReceiptV09, min=1, max=1, mutex_group=None, array=False),
		))

