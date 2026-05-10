import base_types
import PayInCallV02

class CAMT_061_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PayInCall"]
		@property
		def PayInCall(self):
			return self._PayInCall

		@PayInCall.setter
		def PayInCall(self, value):
			self._PayInCall = value if type(value) != auto else self.make_default("PayInCall")

		@PayInCall.deleter
		def PayInCall(self):
			del self._PayInCall
			self._PayInCall = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInCall', type=PayInCallV02, min=1, max=1, mutex_group=None, array=False),
		))

