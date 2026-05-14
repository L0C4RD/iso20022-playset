from . import base_types
from ._SubscriptionOrderConfirmationCancellationInstructionV03 import SubscriptionOrderConfirmationCancellationInstructionV03

class SETR_047_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptOrdrConfCxlInstr"]
		@property
		def SbcptOrdrConfCxlInstr(self):
			return self._SbcptOrdrConfCxlInstr

		@SbcptOrdrConfCxlInstr.setter
		def SbcptOrdrConfCxlInstr(self, value):
			self._SbcptOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("SbcptOrdrConfCxlInstr")

		@SbcptOrdrConfCxlInstr.deleter
		def SbcptOrdrConfCxlInstr(self):
			del self._SbcptOrdrConfCxlInstr
			self._SbcptOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConfCxlInstr', type=SubscriptionOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))

