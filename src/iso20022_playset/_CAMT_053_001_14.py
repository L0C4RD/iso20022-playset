# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankToCustomerStatementV14

class CAMT_053_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.053.001.14"
		_docname = "camt.053.001.14"

		__slots__ = ["_BkToCstmrStmt"]
		@property
		def BkToCstmrStmt(self):
			return self._BkToCstmrStmt

		@BkToCstmrStmt.setter
		def BkToCstmrStmt(self, value):
			self._BkToCstmrStmt = value if value is not None else base_types.UninitialisedField(self, 'BkToCstmrStmt', BankToCustomerStatementV14, False)

		@BkToCstmrStmt.deleter
		def BkToCstmrStmt(self):
			del self._BkToCstmrStmt
			self._BkToCstmrStmt = base_types.UninitialisedField(self, 'BkToCstmrStmt', BankToCustomerStatementV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrStmt', type=BankToCustomerStatementV14, min=1, max=1, mutex_group=None, array=False),
		))