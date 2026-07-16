# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FIToFICustomerCreditTransferV14

class PACS_008_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"
		_docname = "pacs.008.001.14"

		__slots__ = ["_FIToFICstmrCdtTrf"]
		@property
		def FIToFICstmrCdtTrf(self):
			return self._FIToFICstmrCdtTrf

		@FIToFICstmrCdtTrf.setter
		def FIToFICstmrCdtTrf(self, value):
			self._FIToFICstmrCdtTrf = value if value is not None else base_types.UninitialisedField(self, 'FIToFICstmrCdtTrf', FIToFICustomerCreditTransferV14, False)

		@FIToFICstmrCdtTrf.deleter
		def FIToFICstmrCdtTrf(self):
			del self._FIToFICstmrCdtTrf
			self._FIToFICstmrCdtTrf = base_types.UninitialisedField(self, 'FIToFICstmrCdtTrf', FIToFICustomerCreditTransferV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFICstmrCdtTrf', type=FIToFICustomerCreditTransferV14, min=1, max=1, mutex_group=None, array=False),
		))