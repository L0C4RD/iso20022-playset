# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceAssignmentNotificationV01 import InvoiceAssignmentNotificationV01

class TSIN_008_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsin.008.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_InvcAssgnmtNtfctn"]
		@property
		def InvcAssgnmtNtfctn(self):
			return self._InvcAssgnmtNtfctn

		@InvcAssgnmtNtfctn.setter
		def InvcAssgnmtNtfctn(self, value):
			self._InvcAssgnmtNtfctn = value if type(value) != base_types.auto else self.make_default("InvcAssgnmtNtfctn")

		@InvcAssgnmtNtfctn.deleter
		def InvcAssgnmtNtfctn(self):
			del self._InvcAssgnmtNtfctn
			self._InvcAssgnmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtNtfctn', type=InvoiceAssignmentNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))