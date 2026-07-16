# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingModificationInstructionV10

class SESE_036_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.036.001.10"
		_docname = "sese.036.001.10"

		__slots__ = ["_SctiesFincgModInstr"]
		@property
		def SctiesFincgModInstr(self):
			return self._SctiesFincgModInstr

		@SctiesFincgModInstr.setter
		def SctiesFincgModInstr(self, value):
			self._SctiesFincgModInstr = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgModInstr', SecuritiesFinancingModificationInstructionV10, False)

		@SctiesFincgModInstr.deleter
		def SctiesFincgModInstr(self):
			del self._SctiesFincgModInstr
			self._SctiesFincgModInstr = base_types.UninitialisedField(self, 'SctiesFincgModInstr', SecuritiesFinancingModificationInstructionV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgModInstr', type=SecuritiesFinancingModificationInstructionV10, min=1, max=1, mutex_group=None, array=False),
		))