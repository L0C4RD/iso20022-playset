from . import base_types
from .TransferOutInstructionV09 import TransferOutInstructionV09

class SESE_001_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfOutInstr"]
		@property
		def TrfOutInstr(self):
			return self._TrfOutInstr

		@TrfOutInstr.setter
		def TrfOutInstr(self, value):
			self._TrfOutInstr = value if type(value) != auto else self.make_default("TrfOutInstr")

		@TrfOutInstr.deleter
		def TrfOutInstr(self):
			del self._TrfOutInstr
			self._TrfOutInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutInstr', type=TransferOutInstructionV09, min=1, max=1, mutex_group=None, array=False),
		))

