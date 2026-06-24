# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFICustomerCreditTransferV14 import FIToFICustomerCreditTransferV14

class PACS_008_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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
			base_types.FieldEntry(name='FIToFICstmrCdtTrf', type=FIToFICustomerCreditTransferV14, min=1, max=1, mutex_group=None, array=False),
		))