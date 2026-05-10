from . import base_types
from ._AccountModificationInstructionV08 import AccountModificationInstructionV08

class ACMT_003_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctModInstr"]
		@property
		def AcctModInstr(self):
			return self._AcctModInstr

		@AcctModInstr.setter
		def AcctModInstr(self, value):
			self._AcctModInstr = value if type(value) != base_types.auto else self.make_default("AcctModInstr")

		@AcctModInstr.deleter
		def AcctModInstr(self):
			del self._AcctModInstr
			self._AcctModInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctModInstr', type=AccountModificationInstructionV08, min=1, max=1, mutex_group=None, array=False),
		))

