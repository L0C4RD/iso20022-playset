# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BankToCustomerAccountReportV13

class CAMT_052_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.052.001.13"
		_docname = "camt.052.001.13"

		__slots__ = ["_BkToCstmrAcctRpt"]
		@property
		def BkToCstmrAcctRpt(self):
			return self._BkToCstmrAcctRpt

		@BkToCstmrAcctRpt.setter
		def BkToCstmrAcctRpt(self, value):
			self._BkToCstmrAcctRpt = value if value is not None else base_types.UninitialisedField(self, 'BkToCstmrAcctRpt', BankToCustomerAccountReportV13, False)

		@BkToCstmrAcctRpt.deleter
		def BkToCstmrAcctRpt(self):
			del self._BkToCstmrAcctRpt
			self._BkToCstmrAcctRpt = base_types.UninitialisedField(self, 'BkToCstmrAcctRpt', BankToCustomerAccountReportV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrAcctRpt', type=BankToCustomerAccountReportV13, min=1, max=1, mutex_group=None, array=False),
		))