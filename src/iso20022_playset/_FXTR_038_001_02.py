# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02

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
			self._FXTradConfStsAdvcAck = value if value is not None else base_types.UninitialisedField(self, 'FXTradConfStsAdvcAck', ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02, False)

		@FXTradConfStsAdvcAck.deleter
		def FXTradConfStsAdvcAck(self):
			del self._FXTradConfStsAdvcAck
			self._FXTradConfStsAdvcAck = base_types.UninitialisedField(self, 'FXTradConfStsAdvcAck', ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfStsAdvcAck', type=ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))