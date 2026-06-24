# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DeleteReservationV07 import DeleteReservationV07

class CAMT_049_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.049.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_DelRsvatn"]
		@property
		def DelRsvatn(self):
			return self._DelRsvatn

		@DelRsvatn.setter
		def DelRsvatn(self, value):
			self._DelRsvatn = value if type(value) != base_types.auto else self.make_default("DelRsvatn")

		@DelRsvatn.deleter
		def DelRsvatn(self):
			del self._DelRsvatn
			self._DelRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelRsvatn', type=DeleteReservationV07, min=1, max=1, mutex_group=None, array=False),
		))