import base_types
import AgentCADeactivationCancellationRequestV01

class SEEV_029_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCADeactvtnCxlReq"]
		@property
		def AgtCADeactvtnCxlReq(self):
			return self._AgtCADeactvtnCxlReq

		@AgtCADeactvtnCxlReq.setter
		def AgtCADeactvtnCxlReq(self, value):
			self._AgtCADeactvtnCxlReq = value if type(value) != auto else self.make_default("AgtCADeactvtnCxlReq")

		@AgtCADeactvtnCxlReq.deleter
		def AgtCADeactvtnCxlReq(self):
			del self._AgtCADeactvtnCxlReq
			self._AgtCADeactvtnCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnCxlReq', type=AgentCADeactivationCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

