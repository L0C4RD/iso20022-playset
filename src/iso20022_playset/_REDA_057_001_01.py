from . import base_types
from ._StandingSettlementInstructionDeletionV01 import StandingSettlementInstructionDeletionV01

class REDA_057_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StgSttlmInstrDeltn"]
		@property
		def StgSttlmInstrDeltn(self):
			return self._StgSttlmInstrDeltn

		@StgSttlmInstrDeltn.setter
		def StgSttlmInstrDeltn(self, value):
			self._StgSttlmInstrDeltn = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrDeltn")

		@StgSttlmInstrDeltn.deleter
		def StgSttlmInstrDeltn(self):
			del self._StgSttlmInstrDeltn
			self._StgSttlmInstrDeltn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrDeltn', type=StandingSettlementInstructionDeletionV01, min=1, max=1, mutex_group=None, array=False),
		))

