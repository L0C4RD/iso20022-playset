# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SwitchOrderConfirmationCancellationInstructionV02

class SETR_055_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.055.001.02"
		_docname = "setr.055.001.02"

		__slots__ = ["_SwtchOrdrConfCxlInstr"]
		@property
		def SwtchOrdrConfCxlInstr(self):
			return self._SwtchOrdrConfCxlInstr

		@SwtchOrdrConfCxlInstr.setter
		def SwtchOrdrConfCxlInstr(self, value):
			self._SwtchOrdrConfCxlInstr = value if value is not None else base_types.UninitialisedField(self, 'SwtchOrdrConfCxlInstr', SwitchOrderConfirmationCancellationInstructionV02, False)

		@SwtchOrdrConfCxlInstr.deleter
		def SwtchOrdrConfCxlInstr(self):
			del self._SwtchOrdrConfCxlInstr
			self._SwtchOrdrConfCxlInstr = base_types.UninitialisedField(self, 'SwtchOrdrConfCxlInstr', SwitchOrderConfirmationCancellationInstructionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConfCxlInstr', type=SwitchOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))