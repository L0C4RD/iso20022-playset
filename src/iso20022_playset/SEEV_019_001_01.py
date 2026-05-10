from . import base_types
from .AgentCAMovementInstructionV01 import AgentCAMovementInstructionV01

class SEEV_019_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAMvmntInstr"]
		@property
		def AgtCAMvmntInstr(self):
			return self._AgtCAMvmntInstr

		@AgtCAMvmntInstr.setter
		def AgtCAMvmntInstr(self, value):
			self._AgtCAMvmntInstr = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntInstr")

		@AgtCAMvmntInstr.deleter
		def AgtCAMvmntInstr(self):
			del self._AgtCAMvmntInstr
			self._AgtCAMvmntInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntInstr', type=AgentCAMovementInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))

