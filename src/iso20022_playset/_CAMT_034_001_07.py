# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DuplicateV07 import DuplicateV07

class CAMT_034_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_Dplct"]
		@property
		def Dplct(self):
			return self._Dplct

		@Dplct.setter
		def Dplct(self, value):
			self._Dplct = value if type(value) != base_types.auto else self.make_default("Dplct")

		@Dplct.deleter
		def Dplct(self):
			del self._Dplct
			self._Dplct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Dplct', type=DuplicateV07, min=1, max=1, mutex_group=None, array=False),
		))