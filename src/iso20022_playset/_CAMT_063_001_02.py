# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PayInEventAcknowledgementV02 import PayInEventAcknowledgementV02

class CAMT_063_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.063.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_PayInEvtAck"]
		@property
		def PayInEvtAck(self):
			return self._PayInEvtAck

		@PayInEvtAck.setter
		def PayInEvtAck(self, value):
			self._PayInEvtAck = value if type(value) != base_types.auto else self.make_default("PayInEvtAck")

		@PayInEvtAck.deleter
		def PayInEvtAck(self):
			del self._PayInEvtAck
			self._PayInEvtAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInEvtAck', type=PayInEventAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))