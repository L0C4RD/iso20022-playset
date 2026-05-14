# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MisMatchRejectionV02 import MisMatchRejectionV02

class TSMT_022_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MisMtchRjctn"]
		@property
		def MisMtchRjctn(self):
			return self._MisMtchRjctn

		@MisMtchRjctn.setter
		def MisMtchRjctn(self, value):
			self._MisMtchRjctn = value if type(value) != base_types.auto else self.make_default("MisMtchRjctn")

		@MisMtchRjctn.deleter
		def MisMtchRjctn(self):
			del self._MisMtchRjctn
			self._MisMtchRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchRjctn', type=MisMatchRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))