# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReturnReservationV08 import ReturnReservationV08

class CAMT_047_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.047.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RtrRsvatn"]
		@property
		def RtrRsvatn(self):
			return self._RtrRsvatn

		@RtrRsvatn.setter
		def RtrRsvatn(self, value):
			self._RtrRsvatn = value if type(value) != base_types.auto else self.make_default("RtrRsvatn")

		@RtrRsvatn.deleter
		def RtrRsvatn(self):
			del self._RtrRsvatn
			self._RtrRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrRsvatn', type=ReturnReservationV08, min=1, max=1, mutex_group=None, array=False),
		))