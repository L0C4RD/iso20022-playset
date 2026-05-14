# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFICustomerDirectDebitV12 import FIToFICustomerDirectDebitV12

class PACS_003_001_12():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='FIToFICstmrDrctDbt', type=FIToFICustomerDirectDebitV12, min=1, max=1, mutex_group=None, array=False),
		))