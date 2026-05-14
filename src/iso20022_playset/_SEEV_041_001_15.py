from . import base_types
from ._CorporateActionInstructionCancellationRequestStatusAdviceV15 import CorporateActionInstructionCancellationRequestStatusAdviceV15

class SEEV_041_001_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnInstrCxlReqStsAdvc"]
		@property
		def CorpActnInstrCxlReqStsAdvc(self):
			return self._CorpActnInstrCxlReqStsAdvc

		@CorpActnInstrCxlReqStsAdvc.setter
		def CorpActnInstrCxlReqStsAdvc(self, value):
			self._CorpActnInstrCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnInstrCxlReqStsAdvc")

		@CorpActnInstrCxlReqStsAdvc.deleter
		def CorpActnInstrCxlReqStsAdvc(self):
			del self._CorpActnInstrCxlReqStsAdvc
			self._CorpActnInstrCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrCxlReqStsAdvc', type=CorporateActionInstructionCancellationRequestStatusAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))

