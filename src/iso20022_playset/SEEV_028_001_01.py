from . import base_types
import AgentCADeactivationInstructionV01

class SEEV_028_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCADeactvtnInstr"]
		@property
		def AgtCADeactvtnInstr(self):
			return self._AgtCADeactvtnInstr

		@AgtCADeactvtnInstr.setter
		def AgtCADeactvtnInstr(self, value):
			self._AgtCADeactvtnInstr = value if type(value) != auto else self.make_default("AgtCADeactvtnInstr")

		@AgtCADeactvtnInstr.deleter
		def AgtCADeactvtnInstr(self):
			del self._AgtCADeactvtnInstr
			self._AgtCADeactvtnInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnInstr', type=AgentCADeactivationInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))

