import base_types
import ReturnReservationV08

class CAMT_047_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrRsvatn"]
		@property
		def RtrRsvatn(self):
			return self._RtrRsvatn

		@RtrRsvatn.setter
		def RtrRsvatn(self, value):
			self._RtrRsvatn = value if type(value) != auto else self.make_default("RtrRsvatn")

		@RtrRsvatn.deleter
		def RtrRsvatn(self):
			del self._RtrRsvatn
			self._RtrRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrRsvatn', type=ReturnReservationV08, min=1, max=1, mutex_group=None, array=False),
		))

