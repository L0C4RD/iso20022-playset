from . import base_types
from .IntraBalanceMovementInstructionV02 import IntraBalanceMovementInstructionV02

class CAMT_066_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntInstr"]
		@property
		def IntraBalMvmntInstr(self):
			return self._IntraBalMvmntInstr

		@IntraBalMvmntInstr.setter
		def IntraBalMvmntInstr(self, value):
			self._IntraBalMvmntInstr = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntInstr")

		@IntraBalMvmntInstr.deleter
		def IntraBalMvmntInstr(self):
			del self._IntraBalMvmntInstr
			self._IntraBalMvmntInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntInstr', type=IntraBalanceMovementInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))

