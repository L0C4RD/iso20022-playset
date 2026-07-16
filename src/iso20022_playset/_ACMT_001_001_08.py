# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOpeningInstructionV08

class ACMT_001_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08"
		_docname = "acmt.001.001.08"

		__slots__ = ["_AcctOpngInstr"]
		@property
		def AcctOpngInstr(self):
			return self._AcctOpngInstr

		@AcctOpngInstr.setter
		def AcctOpngInstr(self, value):
			self._AcctOpngInstr = value if value is not None else base_types.UninitialisedField(self, 'AcctOpngInstr', AccountOpeningInstructionV08, False)

		@AcctOpngInstr.deleter
		def AcctOpngInstr(self):
			del self._AcctOpngInstr
			self._AcctOpngInstr = base_types.UninitialisedField(self, 'AcctOpngInstr', AccountOpeningInstructionV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngInstr', type=AccountOpeningInstructionV08, min=1, max=1, mutex_group=None, array=False),
		))