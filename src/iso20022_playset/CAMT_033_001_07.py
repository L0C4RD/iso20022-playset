from . import base_types
from .RequestForDuplicateV07 import RequestForDuplicateV07

class CAMT_033_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqForDplct"]
		@property
		def ReqForDplct(self):
			return self._ReqForDplct

		@ReqForDplct.setter
		def ReqForDplct(self, value):
			self._ReqForDplct = value if type(value) != auto else self.make_default("ReqForDplct")

		@ReqForDplct.deleter
		def ReqForDplct(self):
			del self._ReqForDplct
			self._ReqForDplct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForDplct', type=RequestForDuplicateV07, min=1, max=1, mutex_group=None, array=False),
		))

