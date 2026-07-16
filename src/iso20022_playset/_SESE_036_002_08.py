# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingModificationInstruction002V08

class SESE_036_002_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.036.002.08"
		_docname = "sese.036.002.08"

		__slots__ = ["_SctiesFincgModInstr"]
		@property
		def SctiesFincgModInstr(self):
			return self._SctiesFincgModInstr

		@SctiesFincgModInstr.setter
		def SctiesFincgModInstr(self, value):
			self._SctiesFincgModInstr = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgModInstr', SecuritiesFinancingModificationInstruction002V08, False)

		@SctiesFincgModInstr.deleter
		def SctiesFincgModInstr(self):
			del self._SctiesFincgModInstr
			self._SctiesFincgModInstr = base_types.UninitialisedField(self, 'SctiesFincgModInstr', SecuritiesFinancingModificationInstruction002V08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgModInstr', type=SecuritiesFinancingModificationInstruction002V08, min=1, max=1, mutex_group=None, array=False),
		))