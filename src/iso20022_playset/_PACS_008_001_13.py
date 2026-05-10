from . import base_types
from .FIToFICustomerCreditTransferV13 import FIToFICustomerCreditTransferV13

class PACS_008_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIToFICstmrCdtTrf"]
		@property
		def FIToFICstmrCdtTrf(self):
			return self._FIToFICstmrCdtTrf

		@FIToFICstmrCdtTrf.setter
		def FIToFICstmrCdtTrf(self, value):
			self._FIToFICstmrCdtTrf = value if type(value) != base_types.auto else self.make_default("FIToFICstmrCdtTrf")

		@FIToFICstmrCdtTrf.deleter
		def FIToFICstmrCdtTrf(self):
			del self._FIToFICstmrCdtTrf
			self._FIToFICstmrCdtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFICstmrCdtTrf', type=FIToFICustomerCreditTransferV13, min=1, max=1, mutex_group=None, array=False),
		))

