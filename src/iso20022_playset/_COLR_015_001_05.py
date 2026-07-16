# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InterestPaymentStatementV05

class COLR_015_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05"
		_docname = "colr.015.001.05"

		__slots__ = ["_IntrstPmtStmt"]
		@property
		def IntrstPmtStmt(self):
			return self._IntrstPmtStmt

		@IntrstPmtStmt.setter
		def IntrstPmtStmt(self, value):
			self._IntrstPmtStmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtStmt', InterestPaymentStatementV05, False)

		@IntrstPmtStmt.deleter
		def IntrstPmtStmt(self):
			del self._IntrstPmtStmt
			self._IntrstPmtStmt = base_types.UninitialisedField(self, 'IntrstPmtStmt', InterestPaymentStatementV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtStmt', type=InterestPaymentStatementV05, min=1, max=1, mutex_group=None, array=False),
		))