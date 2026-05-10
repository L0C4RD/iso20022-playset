from . import base_types
from .GetAccountV08 import GetAccountV08

class CAMT_003_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_GetAcct"]
		@property
		def GetAcct(self):
			return self._GetAcct

		@GetAcct.setter
		def GetAcct(self, value):
			self._GetAcct = value if type(value) != auto else self.make_default("GetAcct")

		@GetAcct.deleter
		def GetAcct(self):
			del self._GetAcct
			self._GetAcct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetAcct', type=GetAccountV08, min=1, max=1, mutex_group=None, array=False),
		))

