import base_types
import StandingSettlementInstructionV01

class REDA_056_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StgSttlmInstr"]
		@property
		def StgSttlmInstr(self):
			return self._StgSttlmInstr

		@StgSttlmInstr.setter
		def StgSttlmInstr(self, value):
			self._StgSttlmInstr = value if type(value) != auto else self.make_default("StgSttlmInstr")

		@StgSttlmInstr.deleter
		def StgSttlmInstr(self):
			del self._StgSttlmInstr
			self._StgSttlmInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstr', type=StandingSettlementInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))

