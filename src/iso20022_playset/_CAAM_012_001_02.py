# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMExceptionAcknowledgementV02 import ATMExceptionAcknowledgementV02

class CAAM_012_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caam.012.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ATMXcptnAck"]
		@property
		def ATMXcptnAck(self):
			return self._ATMXcptnAck

		@ATMXcptnAck.setter
		def ATMXcptnAck(self, value):
			self._ATMXcptnAck = value if type(value) != base_types.auto else self.make_default("ATMXcptnAck")

		@ATMXcptnAck.deleter
		def ATMXcptnAck(self):
			del self._ATMXcptnAck
			self._ATMXcptnAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMXcptnAck', type=ATMExceptionAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))