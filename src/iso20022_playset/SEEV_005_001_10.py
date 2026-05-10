from . import base_types
from .MeetingInstructionCancellationRequestV10 import MeetingInstructionCancellationRequestV10

class SEEV_005_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgInstrCxlReq"]
		@property
		def MtgInstrCxlReq(self):
			return self._MtgInstrCxlReq

		@MtgInstrCxlReq.setter
		def MtgInstrCxlReq(self, value):
			self._MtgInstrCxlReq = value if type(value) != auto else self.make_default("MtgInstrCxlReq")

		@MtgInstrCxlReq.deleter
		def MtgInstrCxlReq(self):
			del self._MtgInstrCxlReq
			self._MtgInstrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstrCxlReq', type=MeetingInstructionCancellationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))

