# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionBulkOrderConfirmationCancellationInstructionV02 import RedemptionBulkOrderConfirmationCancellationInstructionV02

class SETR_053_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.053.001.02"
		_docname = "setr.053.001.02"

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
			base_types.FieldEntry(name='RedBlkOrdrConfCxlInstr', type=RedemptionBulkOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))