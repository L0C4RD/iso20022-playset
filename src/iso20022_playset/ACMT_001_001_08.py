from . import base_types
from .AccountOpeningInstructionV08 import AccountOpeningInstructionV08

class ACMT_001_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctOpngInstr"]
		@property
		def AcctOpngInstr(self):
			return self._AcctOpngInstr

		@AcctOpngInstr.setter
		def AcctOpngInstr(self, value):
			self._AcctOpngInstr = value if type(value) != auto else self.make_default("AcctOpngInstr")

		@AcctOpngInstr.deleter
		def AcctOpngInstr(self):
			del self._AcctOpngInstr
			self._AcctOpngInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngInstr', type=AccountOpeningInstructionV08, min=1, max=1, mutex_group=None, array=False),
		))

