# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionBulkOrderConfirmationCancellationInstructionV03

class SETR_049_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.049.001.03"
		_docname = "setr.049.001.03"

		__slots__ = ["_SbcptBlkOrdrConfCxlInstr"]
		@property
		def SbcptBlkOrdrConfCxlInstr(self):
			return self._SbcptBlkOrdrConfCxlInstr

		@SbcptBlkOrdrConfCxlInstr.setter
		def SbcptBlkOrdrConfCxlInstr(self, value):
			self._SbcptBlkOrdrConfCxlInstr = value if value is not None else base_types.UninitialisedField(self, 'SbcptBlkOrdrConfCxlInstr', SubscriptionBulkOrderConfirmationCancellationInstructionV03, False)

		@SbcptBlkOrdrConfCxlInstr.deleter
		def SbcptBlkOrdrConfCxlInstr(self):
			del self._SbcptBlkOrdrConfCxlInstr
			self._SbcptBlkOrdrConfCxlInstr = base_types.UninitialisedField(self, 'SbcptBlkOrdrConfCxlInstr', SubscriptionBulkOrderConfirmationCancellationInstructionV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConfCxlInstr', type=SubscriptionBulkOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))