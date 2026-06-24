# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChargesPaymentNotificationV03 import ChargesPaymentNotificationV03

class CAMT_105_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.105.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ChrgsPmtNtfctn"]
		@property
		def ChrgsPmtNtfctn(self):
			return self._ChrgsPmtNtfctn

		@ChrgsPmtNtfctn.setter
		def ChrgsPmtNtfctn(self, value):
			self._ChrgsPmtNtfctn = value if type(value) != base_types.auto else self.make_default("ChrgsPmtNtfctn")

		@ChrgsPmtNtfctn.deleter
		def ChrgsPmtNtfctn(self):
			del self._ChrgsPmtNtfctn
			self._ChrgsPmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgsPmtNtfctn', type=ChargesPaymentNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))