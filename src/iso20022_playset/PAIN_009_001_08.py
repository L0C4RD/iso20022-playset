from . import base_types
from .MandateInitiationRequestV08 import MandateInitiationRequestV08

class PAIN_009_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MndtInitnReq"]
		@property
		def MndtInitnReq(self):
			return self._MndtInitnReq

		@MndtInitnReq.setter
		def MndtInitnReq(self, value):
			self._MndtInitnReq = value if type(value) != base_types.auto else self.make_default("MndtInitnReq")

		@MndtInitnReq.deleter
		def MndtInitnReq(self):
			del self._MndtInitnReq
			self._MndtInitnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtInitnReq', type=MandateInitiationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))

