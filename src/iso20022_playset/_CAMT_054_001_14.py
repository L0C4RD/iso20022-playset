# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankToCustomerDebitCreditNotificationV14

class CAMT_054_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.054.001.14"
		_docname = "camt.054.001.14"

		__slots__ = ["_BkToCstmrDbtCdtNtfctn"]
		@property
		def BkToCstmrDbtCdtNtfctn(self):
			return self._BkToCstmrDbtCdtNtfctn

		@BkToCstmrDbtCdtNtfctn.setter
		def BkToCstmrDbtCdtNtfctn(self, value):
			self._BkToCstmrDbtCdtNtfctn = value if value is not None else base_types.UninitialisedField(self, 'BkToCstmrDbtCdtNtfctn', BankToCustomerDebitCreditNotificationV14, False)

		@BkToCstmrDbtCdtNtfctn.deleter
		def BkToCstmrDbtCdtNtfctn(self):
			del self._BkToCstmrDbtCdtNtfctn
			self._BkToCstmrDbtCdtNtfctn = base_types.UninitialisedField(self, 'BkToCstmrDbtCdtNtfctn', BankToCustomerDebitCreditNotificationV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrDbtCdtNtfctn', type=BankToCustomerDebitCreditNotificationV14, min=1, max=1, mutex_group=None, array=False),
		))