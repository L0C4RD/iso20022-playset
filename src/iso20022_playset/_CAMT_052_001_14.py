# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BankToCustomerAccountReportV14 import BankToCustomerAccountReportV14

class CAMT_052_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.052.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BkToCstmrAcctRpt"]
		@property
		def BkToCstmrAcctRpt(self):
			return self._BkToCstmrAcctRpt

		@BkToCstmrAcctRpt.setter
		def BkToCstmrAcctRpt(self, value):
			self._BkToCstmrAcctRpt = value if type(value) != base_types.auto else self.make_default("BkToCstmrAcctRpt")

		@BkToCstmrAcctRpt.deleter
		def BkToCstmrAcctRpt(self):
			del self._BkToCstmrAcctRpt
			self._BkToCstmrAcctRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrAcctRpt', type=BankToCustomerAccountReportV14, min=1, max=1, mutex_group=None, array=False),
		))