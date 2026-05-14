# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BankToCustomerAccountReportV13 import BankToCustomerAccountReportV13

class CAMT_052_001_13():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='BkToCstmrAcctRpt', type=BankToCustomerAccountReportV13, min=1, max=1, mutex_group=None, array=False),
		))