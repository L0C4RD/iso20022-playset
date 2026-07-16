# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeleteReservationV07

class CAMT_049_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.049.001.07"
		_docname = "camt.049.001.07"

		__slots__ = ["_DelRsvatn"]
		@property
		def DelRsvatn(self):
			return self._DelRsvatn

		@DelRsvatn.setter
		def DelRsvatn(self, value):
			self._DelRsvatn = value if value is not None else base_types.UninitialisedField(self, 'DelRsvatn', DeleteReservationV07, False)

		@DelRsvatn.deleter
		def DelRsvatn(self):
			del self._DelRsvatn
			self._DelRsvatn = base_types.UninitialisedField(self, 'DelRsvatn', DeleteReservationV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelRsvatn', type=DeleteReservationV07, min=1, max=1, mutex_group=None, array=False),
		))