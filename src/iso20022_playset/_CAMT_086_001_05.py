# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankServicesBillingStatementV05

class CAMT_086_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.086.001.05"
		_docname = "camt.086.001.05"

		__slots__ = ["_BkSvcsBllgStmt"]
		@property
		def BkSvcsBllgStmt(self):
			return self._BkSvcsBllgStmt

		@BkSvcsBllgStmt.setter
		def BkSvcsBllgStmt(self, value):
			self._BkSvcsBllgStmt = value if value is not None else base_types.UninitialisedField(self, 'BkSvcsBllgStmt', BankServicesBillingStatementV05, False)

		@BkSvcsBllgStmt.deleter
		def BkSvcsBllgStmt(self):
			del self._BkSvcsBllgStmt
			self._BkSvcsBllgStmt = base_types.UninitialisedField(self, 'BkSvcsBllgStmt', BankServicesBillingStatementV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkSvcsBllgStmt', type=BankServicesBillingStatementV05, min=1, max=1, mutex_group=None, array=False),
		))