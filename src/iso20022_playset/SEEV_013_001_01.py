import base_types
import AgentCAElectionAmendmentRequestV01

class SEEV_013_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAElctnAmdmntReq"]
		@property
		def AgtCAElctnAmdmntReq(self):
			return self._AgtCAElctnAmdmntReq

		@AgtCAElctnAmdmntReq.setter
		def AgtCAElctnAmdmntReq(self, value):
			self._AgtCAElctnAmdmntReq = value if type(value) != auto else self.make_default("AgtCAElctnAmdmntReq")

		@AgtCAElctnAmdmntReq.deleter
		def AgtCAElctnAmdmntReq(self):
			del self._AgtCAElctnAmdmntReq
			self._AgtCAElctnAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAmdmntReq', type=AgentCAElectionAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

