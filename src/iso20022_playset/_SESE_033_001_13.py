# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingInstructionV13

class SESE_033_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.033.001.13"
		_docname = "sese.033.001.13"

		__slots__ = ["_SctiesFincgInstr"]
		@property
		def SctiesFincgInstr(self):
			return self._SctiesFincgInstr

		@SctiesFincgInstr.setter
		def SctiesFincgInstr(self, value):
			self._SctiesFincgInstr = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgInstr', SecuritiesFinancingInstructionV13, False)

		@SctiesFincgInstr.deleter
		def SctiesFincgInstr(self):
			del self._SctiesFincgInstr
			self._SctiesFincgInstr = base_types.UninitialisedField(self, 'SctiesFincgInstr', SecuritiesFinancingInstructionV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgInstr', type=SecuritiesFinancingInstructionV13, min=1, max=1, mutex_group=None, array=False),
		))