from . import base_types
import PayInScheduleV03

class CAMT_062_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PayInSchdl"]
		@property
		def PayInSchdl(self):
			return self._PayInSchdl

		@PayInSchdl.setter
		def PayInSchdl(self, value):
			self._PayInSchdl = value if type(value) != auto else self.make_default("PayInSchdl")

		@PayInSchdl.deleter
		def PayInSchdl(self):
			del self._PayInSchdl
			self._PayInSchdl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PayInSchdl', type=PayInScheduleV03, min=1, max=1, mutex_group=None, array=False),
		))

