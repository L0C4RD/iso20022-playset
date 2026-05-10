from . import base_types
from ._StandingSettlementInstructionCancellationV01 import StandingSettlementInstructionCancellationV01

class REDA_059_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StgSttlmInstrCxl"]
		@property
		def StgSttlmInstrCxl(self):
			return self._StgSttlmInstrCxl

		@StgSttlmInstrCxl.setter
		def StgSttlmInstrCxl(self, value):
			self._StgSttlmInstrCxl = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrCxl")

		@StgSttlmInstrCxl.deleter
		def StgSttlmInstrCxl(self):
			del self._StgSttlmInstrCxl
			self._StgSttlmInstrCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrCxl', type=StandingSettlementInstructionCancellationV01, min=1, max=1, mutex_group=None, array=False),
		))

