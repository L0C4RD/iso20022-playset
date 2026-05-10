from . import base_types
from .RedemptionOrderConfirmationCancellationInstructionV02 import RedemptionOrderConfirmationCancellationInstructionV02

class SETR_051_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedOrdrConfCxlInstr"]
		@property
		def RedOrdrConfCxlInstr(self):
			return self._RedOrdrConfCxlInstr

		@RedOrdrConfCxlInstr.setter
		def RedOrdrConfCxlInstr(self, value):
			self._RedOrdrConfCxlInstr = value if type(value) != auto else self.make_default("RedOrdrConfCxlInstr")

		@RedOrdrConfCxlInstr.deleter
		def RedOrdrConfCxlInstr(self):
			del self._RedOrdrConfCxlInstr
			self._RedOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConfCxlInstr', type=RedemptionOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))

