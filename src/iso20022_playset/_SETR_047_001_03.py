# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionOrderConfirmationCancellationInstructionV03

class SETR_047_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.047.001.03"
		_docname = "setr.047.001.03"

		__slots__ = ["_SbcptOrdrConfCxlInstr"]
		@property
		def SbcptOrdrConfCxlInstr(self):
			return self._SbcptOrdrConfCxlInstr

		@SbcptOrdrConfCxlInstr.setter
		def SbcptOrdrConfCxlInstr(self, value):
			self._SbcptOrdrConfCxlInstr = value if value is not None else base_types.UninitialisedField(self, 'SbcptOrdrConfCxlInstr', SubscriptionOrderConfirmationCancellationInstructionV03, False)

		@SbcptOrdrConfCxlInstr.deleter
		def SbcptOrdrConfCxlInstr(self):
			del self._SbcptOrdrConfCxlInstr
			self._SbcptOrdrConfCxlInstr = base_types.UninitialisedField(self, 'SbcptOrdrConfCxlInstr', SubscriptionOrderConfirmationCancellationInstructionV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConfCxlInstr', type=SubscriptionOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))