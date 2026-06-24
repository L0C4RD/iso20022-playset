# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesStatementQueryV08 import SecuritiesStatementQueryV08

class SEMT_021_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.021.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesStmtQry"]
		@property
		def SctiesStmtQry(self):
			return self._SctiesStmtQry

		@SctiesStmtQry.setter
		def SctiesStmtQry(self, value):
			self._SctiesStmtQry = value if type(value) != base_types.auto else self.make_default("SctiesStmtQry")

		@SctiesStmtQry.deleter
		def SctiesStmtQry(self):
			del self._SctiesStmtQry
			self._SctiesStmtQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStmtQry', type=SecuritiesStatementQueryV08, min=1, max=1, mutex_group=None, array=False),
		))