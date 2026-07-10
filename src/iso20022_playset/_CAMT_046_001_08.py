# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GetReservationV08 import GetReservationV08

class CAMT_046_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.046.001.08"
		_docname = "camt.046.001.08"

		__slots__ = ["_GetRsvatn"]
		@property
		def GetRsvatn(self):
			return self._GetRsvatn

		@GetRsvatn.setter
		def GetRsvatn(self, value):
			self._GetRsvatn = value if type(value) != base_types.auto else self.make_default("GetRsvatn")

		@GetRsvatn.deleter
		def GetRsvatn(self):
			del self._GetRsvatn
			self._GetRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetRsvatn', type=GetReservationV08, min=1, max=1, mutex_group=None, array=False),
		))