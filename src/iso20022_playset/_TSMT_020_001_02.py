# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MisMatchAcceptanceV02 import MisMatchAcceptanceV02

class TSMT_020_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MisMtchAccptnc"]
		@property
		def MisMtchAccptnc(self):
			return self._MisMtchAccptnc

		@MisMtchAccptnc.setter
		def MisMtchAccptnc(self, value):
			self._MisMtchAccptnc = value if type(value) != base_types.auto else self.make_default("MisMtchAccptnc")

		@MisMtchAccptnc.deleter
		def MisMtchAccptnc(self):
			del self._MisMtchAccptnc
			self._MisMtchAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchAccptnc', type=MisMatchAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))