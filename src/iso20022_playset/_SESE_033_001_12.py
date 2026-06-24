# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingInstructionV12 import SecuritiesFinancingInstructionV12

class SESE_033_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.033.001.12"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesFincgInstr"]
		@property
		def SctiesFincgInstr(self):
			return self._SctiesFincgInstr

		@SctiesFincgInstr.setter
		def SctiesFincgInstr(self, value):
			self._SctiesFincgInstr = value if type(value) != base_types.auto else self.make_default("SctiesFincgInstr")

		@SctiesFincgInstr.deleter
		def SctiesFincgInstr(self):
			del self._SctiesFincgInstr
			self._SctiesFincgInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgInstr', type=SecuritiesFinancingInstructionV12, min=1, max=1, mutex_group=None, array=False),
		))