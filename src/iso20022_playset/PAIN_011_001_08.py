from . import base_types
from .MandateCancellationRequestV08 import MandateCancellationRequestV08

class PAIN_011_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MndtCxlReq"]
		@property
		def MndtCxlReq(self):
			return self._MndtCxlReq

		@MndtCxlReq.setter
		def MndtCxlReq(self, value):
			self._MndtCxlReq = value if type(value) != base_types.auto else self.make_default("MndtCxlReq")

		@MndtCxlReq.deleter
		def MndtCxlReq(self):
			del self._MndtCxlReq
			self._MndtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtCxlReq', type=MandateCancellationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))

