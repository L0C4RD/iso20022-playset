# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingModificationInstructionV09 import SecuritiesFinancingModificationInstructionV09

class SESE_036_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.036.001.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesFincgModInstr"]
		@property
		def SctiesFincgModInstr(self):
			return self._SctiesFincgModInstr

		@SctiesFincgModInstr.setter
		def SctiesFincgModInstr(self, value):
			self._SctiesFincgModInstr = value if type(value) != base_types.auto else self.make_default("SctiesFincgModInstr")

		@SctiesFincgModInstr.deleter
		def SctiesFincgModInstr(self):
			del self._SctiesFincgModInstr
			self._SctiesFincgModInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgModInstr', type=SecuritiesFinancingModificationInstructionV09, min=1, max=1, mutex_group=None, array=False),
		))