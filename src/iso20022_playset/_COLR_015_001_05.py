# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InterestPaymentStatementV05 import InterestPaymentStatementV05

class COLR_015_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.015.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntrstPmtStmt"]
		@property
		def IntrstPmtStmt(self):
			return self._IntrstPmtStmt

		@IntrstPmtStmt.setter
		def IntrstPmtStmt(self, value):
			self._IntrstPmtStmt = value if type(value) != base_types.auto else self.make_default("IntrstPmtStmt")

		@IntrstPmtStmt.deleter
		def IntrstPmtStmt(self):
			del self._IntrstPmtStmt
			self._IntrstPmtStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtStmt', type=InterestPaymentStatementV05, min=1, max=1, mutex_group=None, array=False),
		))