from . import base_types
from .SwitchOrderConfirmationCancellationInstructionV02 import SwitchOrderConfirmationCancellationInstructionV02

class SETR_055_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SwtchOrdrConfCxlInstr"]
		@property
		def SwtchOrdrConfCxlInstr(self):
			return self._SwtchOrdrConfCxlInstr

		@SwtchOrdrConfCxlInstr.setter
		def SwtchOrdrConfCxlInstr(self, value):
			self._SwtchOrdrConfCxlInstr = value if type(value) != auto else self.make_default("SwtchOrdrConfCxlInstr")

		@SwtchOrdrConfCxlInstr.deleter
		def SwtchOrdrConfCxlInstr(self):
			del self._SwtchOrdrConfCxlInstr
			self._SwtchOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConfCxlInstr', type=SwitchOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))

