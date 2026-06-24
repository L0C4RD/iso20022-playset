# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SwitchOrderConfirmationCancellationInstructionV03 import SwitchOrderConfirmationCancellationInstructionV03

class SETR_055_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.055.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SwtchOrdrConfCxlInstr"]
		@property
		def SwtchOrdrConfCxlInstr(self):
			return self._SwtchOrdrConfCxlInstr

		@SwtchOrdrConfCxlInstr.setter
		def SwtchOrdrConfCxlInstr(self, value):
			self._SwtchOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("SwtchOrdrConfCxlInstr")

		@SwtchOrdrConfCxlInstr.deleter
		def SwtchOrdrConfCxlInstr(self):
			del self._SwtchOrdrConfCxlInstr
			self._SwtchOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConfCxlInstr', type=SwitchOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))