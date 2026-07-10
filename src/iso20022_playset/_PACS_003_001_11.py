# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFICustomerDirectDebitV11 import FIToFICustomerDirectDebitV11

class PACS_003_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.003.001.11"
		_docname = "pacs.003.001.11"

		__slots__ = ["_FIToFICstmrDrctDbt"]
		@property
		def FIToFICstmrDrctDbt(self):
			return self._FIToFICstmrDrctDbt

		@FIToFICstmrDrctDbt.setter
		def FIToFICstmrDrctDbt(self, value):
			self._FIToFICstmrDrctDbt = value if type(value) != base_types.auto else self.make_default("FIToFICstmrDrctDbt")

		@FIToFICstmrDrctDbt.deleter
		def FIToFICstmrDrctDbt(self):
			del self._FIToFICstmrDrctDbt
			self._FIToFICstmrDrctDbt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFICstmrDrctDbt', type=FIToFICustomerDirectDebitV11, min=1, max=1, mutex_group=None, array=False),
		))