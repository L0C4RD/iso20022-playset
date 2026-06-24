# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountOpeningInstructionV08 import AccountOpeningInstructionV08

class ACMT_001_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctOpngInstr"]
		@property
		def AcctOpngInstr(self):
			return self._AcctOpngInstr

		@AcctOpngInstr.setter
		def AcctOpngInstr(self, value):
			self._AcctOpngInstr = value if type(value) != base_types.auto else self.make_default("AcctOpngInstr")

		@AcctOpngInstr.deleter
		def AcctOpngInstr(self):
			del self._AcctOpngInstr
			self._AcctOpngInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngInstr', type=AccountOpeningInstructionV08, min=1, max=1, mutex_group=None, array=False),
		))