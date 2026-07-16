# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionBulkOrderConfirmationCancellationInstructionV03

class SETR_053_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.053.001.03"
		_docname = "setr.053.001.03"

		__slots__ = ["_RedBlkOrdrConfCxlInstr"]
		@property
		def RedBlkOrdrConfCxlInstr(self):
			return self._RedBlkOrdrConfCxlInstr

		@RedBlkOrdrConfCxlInstr.setter
		def RedBlkOrdrConfCxlInstr(self, value):
			self._RedBlkOrdrConfCxlInstr = value if value is not None else base_types.UninitialisedField(self, 'RedBlkOrdrConfCxlInstr', RedemptionBulkOrderConfirmationCancellationInstructionV03, False)

		@RedBlkOrdrConfCxlInstr.deleter
		def RedBlkOrdrConfCxlInstr(self):
			del self._RedBlkOrdrConfCxlInstr
			self._RedBlkOrdrConfCxlInstr = base_types.UninitialisedField(self, 'RedBlkOrdrConfCxlInstr', RedemptionBulkOrderConfirmationCancellationInstructionV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrConfCxlInstr', type=RedemptionBulkOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))