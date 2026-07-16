# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesStatementQueryV09

class SEMT_021_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.021.001.09"
		_docname = "semt.021.001.09"

		__slots__ = ["_SctiesStmtQry"]
		@property
		def SctiesStmtQry(self):
			return self._SctiesStmtQry

		@SctiesStmtQry.setter
		def SctiesStmtQry(self, value):
			self._SctiesStmtQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesStmtQry', SecuritiesStatementQueryV09, False)

		@SctiesStmtQry.deleter
		def SctiesStmtQry(self):
			del self._SctiesStmtQry
			self._SctiesStmtQry = base_types.UninitialisedField(self, 'SctiesStmtQry', SecuritiesStatementQueryV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStmtQry', type=SecuritiesStatementQueryV09, min=1, max=1, mutex_group=None, array=False),
		))