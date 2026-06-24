# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionOrderConfirmationCancellationInstructionV03 import RedemptionOrderConfirmationCancellationInstructionV03

class SETR_051_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.051.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RedOrdrConfCxlInstr"]
		@property
		def RedOrdrConfCxlInstr(self):
			return self._RedOrdrConfCxlInstr

		@RedOrdrConfCxlInstr.setter
		def RedOrdrConfCxlInstr(self, value):
			self._RedOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("RedOrdrConfCxlInstr")

		@RedOrdrConfCxlInstr.deleter
		def RedOrdrConfCxlInstr(self):
			del self._RedOrdrConfCxlInstr
			self._RedOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConfCxlInstr', type=RedemptionOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))