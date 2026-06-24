# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BankToCustomerStatementV14 import BankToCustomerStatementV14

class CAMT_053_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.053.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BkToCstmrStmt"]
		@property
		def BkToCstmrStmt(self):
			return self._BkToCstmrStmt

		@BkToCstmrStmt.setter
		def BkToCstmrStmt(self, value):
			self._BkToCstmrStmt = value if type(value) != base_types.auto else self.make_default("BkToCstmrStmt")

		@BkToCstmrStmt.deleter
		def BkToCstmrStmt(self):
			del self._BkToCstmrStmt
			self._BkToCstmrStmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrStmt', type=BankToCustomerStatementV14, min=1, max=1, mutex_group=None, array=False),
		))