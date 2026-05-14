# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionOrderV04 import RedemptionOrderV04

class SETR_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedOrdr"]
		@property
		def RedOrdr(self):
			return self._RedOrdr

		@RedOrdr.setter
		def RedOrdr(self, value):
			self._RedOrdr = value if type(value) != base_types.auto else self.make_default("RedOrdr")

		@RedOrdr.deleter
		def RedOrdr(self):
			del self._RedOrdr
			self._RedOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdr', type=RedemptionOrderV04, min=1, max=1, mutex_group=None, array=False),
		))