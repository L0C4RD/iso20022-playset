from . import base_types
from .SubscriptionOrderConfirmationCancellationInstructionV02 import SubscriptionOrderConfirmationCancellationInstructionV02

class SETR_047_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptOrdrConfCxlInstr"]
		@property
		def SbcptOrdrConfCxlInstr(self):
			return self._SbcptOrdrConfCxlInstr

		@SbcptOrdrConfCxlInstr.setter
		def SbcptOrdrConfCxlInstr(self, value):
			self._SbcptOrdrConfCxlInstr = value if type(value) != auto else self.make_default("SbcptOrdrConfCxlInstr")

		@SbcptOrdrConfCxlInstr.deleter
		def SbcptOrdrConfCxlInstr(self):
			del self._SbcptOrdrConfCxlInstr
			self._SbcptOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConfCxlInstr', type=SubscriptionOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))

