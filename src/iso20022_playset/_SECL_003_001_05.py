# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TradeLegStatementV05 import TradeLegStatementV05

class SECL_003_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.003.001.05"
		_docname = "secl.003.001.05"

		__slots__ = ["_TradLegStmt"]
		@property
		def TradLegStmt(self):
			return self._TradLegStmt

		@TradLegStmt.setter
		def TradLegStmt(self, value):
			self._TradLegStmt = value if type(value) != base_types.auto else self.make_default("TradLegStmt")

		@TradLegStmt.deleter
		def TradLegStmt(self):
			del self._TradLegStmt
			self._TradLegStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegStmt', type=TradeLegStatementV05, min=1, max=1, mutex_group=None, array=False),
		))