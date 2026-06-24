# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceAssignmentStatusV01 import InvoiceAssignmentStatusV01

class TSIN_007_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsin.007.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_InvcAssgnmtSts"]
		@property
		def InvcAssgnmtSts(self):
			return self._InvcAssgnmtSts

		@InvcAssgnmtSts.setter
		def InvcAssgnmtSts(self, value):
			self._InvcAssgnmtSts = value if type(value) != base_types.auto else self.make_default("InvcAssgnmtSts")

		@InvcAssgnmtSts.deleter
		def InvcAssgnmtSts(self):
			del self._InvcAssgnmtSts
			self._InvcAssgnmtSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtSts', type=InvoiceAssignmentStatusV01, min=1, max=1, mutex_group=None, array=False),
		))