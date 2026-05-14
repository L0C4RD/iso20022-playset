from . import base_types
from ._BankToCustomerDebitCreditNotificationV14 import BankToCustomerDebitCreditNotificationV14

class CAMT_054_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BkToCstmrDbtCdtNtfctn"]
		@property
		def BkToCstmrDbtCdtNtfctn(self):
			return self._BkToCstmrDbtCdtNtfctn

		@BkToCstmrDbtCdtNtfctn.setter
		def BkToCstmrDbtCdtNtfctn(self, value):
			self._BkToCstmrDbtCdtNtfctn = value if type(value) != base_types.auto else self.make_default("BkToCstmrDbtCdtNtfctn")

		@BkToCstmrDbtCdtNtfctn.deleter
		def BkToCstmrDbtCdtNtfctn(self):
			del self._BkToCstmrDbtCdtNtfctn
			self._BkToCstmrDbtCdtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BkToCstmrDbtCdtNtfctn', type=BankToCustomerDebitCreditNotificationV14, min=1, max=1, mutex_group=None, array=False),
		))

