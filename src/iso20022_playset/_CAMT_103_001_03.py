# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreateReservationV03 import CreateReservationV03

class CAMT_103_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CretRsvatn"]
		@property
		def CretRsvatn(self):
			return self._CretRsvatn

		@CretRsvatn.setter
		def CretRsvatn(self, value):
			self._CretRsvatn = value if type(value) != base_types.auto else self.make_default("CretRsvatn")

		@CretRsvatn.deleter
		def CretRsvatn(self):
			del self._CretRsvatn
			self._CretRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretRsvatn', type=CreateReservationV03, min=1, max=1, mutex_group=None, array=False),
		))