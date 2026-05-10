from . import base_types
from .StandingSettlementInstructionStatusAdviceV01 import StandingSettlementInstructionStatusAdviceV01

class REDA_058_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StgSttlmInstrStsAdvc"]
		@property
		def StgSttlmInstrStsAdvc(self):
			return self._StgSttlmInstrStsAdvc

		@StgSttlmInstrStsAdvc.setter
		def StgSttlmInstrStsAdvc(self, value):
			self._StgSttlmInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrStsAdvc")

		@StgSttlmInstrStsAdvc.deleter
		def StgSttlmInstrStsAdvc(self):
			del self._StgSttlmInstrStsAdvc
			self._StgSttlmInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrStsAdvc', type=StandingSettlementInstructionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

