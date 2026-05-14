# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentReturnV15 import PaymentReturnV15

class PACS_004_001_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PmtRtr"]
		@property
		def PmtRtr(self):
			return self._PmtRtr

		@PmtRtr.setter
		def PmtRtr(self, value):
			self._PmtRtr = value if type(value) != base_types.auto else self.make_default("PmtRtr")

		@PmtRtr.deleter
		def PmtRtr(self):
			del self._PmtRtr
			self._PmtRtr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtRtr', type=PaymentReturnV15, min=1, max=1, mutex_group=None, array=False),
		))