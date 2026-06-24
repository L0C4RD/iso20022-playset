# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountModificationInstructionV08 import AccountModificationInstructionV08

class ACMT_003_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AcctModInstr"]
		@property
		def AcctModInstr(self):
			return self._AcctModInstr

		@AcctModInstr.setter
		def AcctModInstr(self, value):
			self._AcctModInstr = value if type(value) != base_types.auto else self.make_default("AcctModInstr")

		@AcctModInstr.deleter
		def AcctModInstr(self):
			del self._AcctModInstr
			self._AcctModInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctModInstr', type=AccountModificationInstructionV08, min=1, max=1, mutex_group=None, array=False),
		))