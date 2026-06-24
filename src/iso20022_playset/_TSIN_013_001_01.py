# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceAssignmentAcknowledgementV01 import InvoiceAssignmentAcknowledgementV01

class TSIN_013_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsin.013.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_InvcAssgnmtAck"]
		@property
		def InvcAssgnmtAck(self):
			return self._InvcAssgnmtAck

		@InvcAssgnmtAck.setter
		def InvcAssgnmtAck(self, value):
			self._InvcAssgnmtAck = value if type(value) != base_types.auto else self.make_default("InvcAssgnmtAck")

		@InvcAssgnmtAck.deleter
		def InvcAssgnmtAck(self):
			del self._InvcAssgnmtAck
			self._InvcAssgnmtAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtAck', type=InvoiceAssignmentAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))