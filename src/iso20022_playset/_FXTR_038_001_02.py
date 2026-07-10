# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02 import ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02

class FXTR_038_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.038.001.02"
		_docname = "fxtr.038.001.02"

		__slots__ = ["_FXTradConfStsAdvcAck"]
		@property
		def FXTradConfStsAdvcAck(self):
			return self._FXTradConfStsAdvcAck

		@FXTradConfStsAdvcAck.setter
		def FXTradConfStsAdvcAck(self, value):
			self._FXTradConfStsAdvcAck = value if type(value) != base_types.auto else self.make_default("FXTradConfStsAdvcAck")

		@FXTradConfStsAdvcAck.deleter
		def FXTradConfStsAdvcAck(self):
			del self._FXTradConfStsAdvcAck
			self._FXTradConfStsAdvcAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfStsAdvcAck', type=ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))