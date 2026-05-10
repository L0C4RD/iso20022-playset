from . import base_types
import PayInEventAcknowledgementV02

class CAMT_063_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PayInEvtAck"]
		@property
		def PayInEvtAck(self):
			return self._PayInEvtAck

		@PayInEvtAck.setter
		def PayInEvtAck(self, value):
			self._PayInEvtAck = value if type(value) != auto else self.make_default("PayInEvtAck")

		@PayInEvtAck.deleter
		def PayInEvtAck(self):
			del self._PayInEvtAck
			self._PayInEvtAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInEvtAck', type=PayInEventAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))

