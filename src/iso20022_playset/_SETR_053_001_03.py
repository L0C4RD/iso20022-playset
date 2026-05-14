from . import base_types
from ._RedemptionBulkOrderConfirmationCancellationInstructionV03 import RedemptionBulkOrderConfirmationCancellationInstructionV03

class SETR_053_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedBlkOrdrConfCxlInstr"]
		@property
		def RedBlkOrdrConfCxlInstr(self):
			return self._RedBlkOrdrConfCxlInstr

		@RedBlkOrdrConfCxlInstr.setter
		def RedBlkOrdrConfCxlInstr(self, value):
			self._RedBlkOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("RedBlkOrdrConfCxlInstr")

		@RedBlkOrdrConfCxlInstr.deleter
		def RedBlkOrdrConfCxlInstr(self):
			del self._RedBlkOrdrConfCxlInstr
			self._RedBlkOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrConfCxlInstr', type=RedemptionBulkOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))

