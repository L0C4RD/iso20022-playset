from . import base_types
from ._AgentCAStandingInstructionCancellationRequestV01 import AgentCAStandingInstructionCancellationRequestV01

class SEEV_026_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAStgInstrCxlReq"]
		@property
		def AgtCAStgInstrCxlReq(self):
			return self._AgtCAStgInstrCxlReq

		@AgtCAStgInstrCxlReq.setter
		def AgtCAStgInstrCxlReq(self, value):
			self._AgtCAStgInstrCxlReq = value if type(value) != base_types.auto else self.make_default("AgtCAStgInstrCxlReq")

		@AgtCAStgInstrCxlReq.deleter
		def AgtCAStgInstrCxlReq(self):
			del self._AgtCAStgInstrCxlReq
			self._AgtCAStgInstrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrCxlReq', type=AgentCAStandingInstructionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

