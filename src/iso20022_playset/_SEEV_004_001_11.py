from . import base_types
from ._MeetingInstructionV11 import MeetingInstructionV11

class SEEV_004_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgInstr"]
		@property
		def MtgInstr(self):
			return self._MtgInstr

		@MtgInstr.setter
		def MtgInstr(self, value):
			self._MtgInstr = value if type(value) != base_types.auto else self.make_default("MtgInstr")

		@MtgInstr.deleter
		def MtgInstr(self):
			del self._MtgInstr
			self._MtgInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstr', type=MeetingInstructionV11, min=1, max=1, mutex_group=None, array=False),
		))

