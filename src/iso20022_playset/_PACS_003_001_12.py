# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FIToFICustomerDirectDebitV12

class PACS_003_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12"
		_docname = "pacs.003.001.12"

		__slots__ = ["_FIToFICstmrDrctDbt"]
		@property
		def FIToFICstmrDrctDbt(self):
			return self._FIToFICstmrDrctDbt

		@FIToFICstmrDrctDbt.setter
		def FIToFICstmrDrctDbt(self, value):
			self._FIToFICstmrDrctDbt = value if value is not None else base_types.UninitialisedField(self, 'FIToFICstmrDrctDbt', FIToFICustomerDirectDebitV12, False)

		@FIToFICstmrDrctDbt.deleter
		def FIToFICstmrDrctDbt(self):
			del self._FIToFICstmrDrctDbt
			self._FIToFICstmrDrctDbt = base_types.UninitialisedField(self, 'FIToFICstmrDrctDbt', FIToFICustomerDirectDebitV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFICstmrDrctDbt', type=FIToFICustomerDirectDebitV12, min=1, max=1, mutex_group=None, array=False),
		))