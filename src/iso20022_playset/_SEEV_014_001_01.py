from . import base_types
from ._AgentCAElectionCancellationRequestV01 import AgentCAElectionCancellationRequestV01

class SEEV_014_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAElctnCxlReq"]
		@property
		def AgtCAElctnCxlReq(self):
			return self._AgtCAElctnCxlReq

		@AgtCAElctnCxlReq.setter
		def AgtCAElctnCxlReq(self, value):
			self._AgtCAElctnCxlReq = value if type(value) != base_types.auto else self.make_default("AgtCAElctnCxlReq")

		@AgtCAElctnCxlReq.deleter
		def AgtCAElctnCxlReq(self):
			del self._AgtCAElctnCxlReq
			self._AgtCAElctnCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnCxlReq', type=AgentCAElectionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

