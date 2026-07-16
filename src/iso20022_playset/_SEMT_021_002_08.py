# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesStatementQuery002V08

class SEMT_021_002_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.021.002.08"
		_docname = "semt.021.002.08"

		__slots__ = ["_SctiesStmtQry"]
		@property
		def SctiesStmtQry(self):
			return self._SctiesStmtQry

		@SctiesStmtQry.setter
		def SctiesStmtQry(self, value):
			self._SctiesStmtQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesStmtQry', SecuritiesStatementQuery002V08, False)

		@SctiesStmtQry.deleter
		def SctiesStmtQry(self):
			del self._SctiesStmtQry
			self._SctiesStmtQry = base_types.UninitialisedField(self, 'SctiesStmtQry', SecuritiesStatementQuery002V08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStmtQry', type=SecuritiesStatementQuery002V08, min=1, max=1, mutex_group=None, array=False),
		))