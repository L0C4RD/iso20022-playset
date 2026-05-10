from . import base_types
from .SubscriptionBulkOrderConfirmationCancellationInstructionV02 import SubscriptionBulkOrderConfirmationCancellationInstructionV02

class SETR_049_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptBlkOrdrConfCxlInstr"]
		@property
		def SbcptBlkOrdrConfCxlInstr(self):
			return self._SbcptBlkOrdrConfCxlInstr

		@SbcptBlkOrdrConfCxlInstr.setter
		def SbcptBlkOrdrConfCxlInstr(self, value):
			self._SbcptBlkOrdrConfCxlInstr = value if type(value) != auto else self.make_default("SbcptBlkOrdrConfCxlInstr")

		@SbcptBlkOrdrConfCxlInstr.deleter
		def SbcptBlkOrdrConfCxlInstr(self):
			del self._SbcptBlkOrdrConfCxlInstr
			self._SbcptBlkOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConfCxlInstr', type=SubscriptionBulkOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))

