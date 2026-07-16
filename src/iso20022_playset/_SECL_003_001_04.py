# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeLegStatementV04

class SECL_003_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.003.001.04"
		_docname = "secl.003.001.04"

		__slots__ = ["_TradLegStmt"]
		@property
		def TradLegStmt(self):
			return self._TradLegStmt

		@TradLegStmt.setter
		def TradLegStmt(self, value):
			self._TradLegStmt = value if value is not None else base_types.UninitialisedField(self, 'TradLegStmt', TradeLegStatementV04, False)

		@TradLegStmt.deleter
		def TradLegStmt(self):
			del self._TradLegStmt
			self._TradLegStmt = base_types.UninitialisedField(self, 'TradLegStmt', TradeLegStatementV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegStmt', type=TradeLegStatementV04, min=1, max=1, mutex_group=None, array=False),
		))