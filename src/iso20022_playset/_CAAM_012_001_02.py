# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMExceptionAcknowledgementV02

class CAAM_012_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.012.001.02"
		_docname = "caam.012.001.02"

		__slots__ = ["_ATMXcptnAck"]
		@property
		def ATMXcptnAck(self):
			return self._ATMXcptnAck

		@ATMXcptnAck.setter
		def ATMXcptnAck(self, value):
			self._ATMXcptnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMXcptnAck', ATMExceptionAcknowledgementV02, False)

		@ATMXcptnAck.deleter
		def ATMXcptnAck(self):
			del self._ATMXcptnAck
			self._ATMXcptnAck = base_types.UninitialisedField(self, 'ATMXcptnAck', ATMExceptionAcknowledgementV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMXcptnAck', type=ATMExceptionAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))