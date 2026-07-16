# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionOrderConfirmationCancellationInstructionV03

class SETR_051_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.051.001.03"
		_docname = "setr.051.001.03"

		__slots__ = ["_RedOrdrConfCxlInstr"]
		@property
		def RedOrdrConfCxlInstr(self):
			return self._RedOrdrConfCxlInstr

		@RedOrdrConfCxlInstr.setter
		def RedOrdrConfCxlInstr(self, value):
			self._RedOrdrConfCxlInstr = value if value is not None else base_types.UninitialisedField(self, 'RedOrdrConfCxlInstr', RedemptionOrderConfirmationCancellationInstructionV03, False)

		@RedOrdrConfCxlInstr.deleter
		def RedOrdrConfCxlInstr(self):
			del self._RedOrdrConfCxlInstr
			self._RedOrdrConfCxlInstr = base_types.UninitialisedField(self, 'RedOrdrConfCxlInstr', RedemptionOrderConfirmationCancellationInstructionV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConfCxlInstr', type=RedemptionOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))