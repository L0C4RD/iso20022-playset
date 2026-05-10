from . import base_types
import ReservationIdentification4

class CurrentOrDefaultReservation4Choice(base_types._BaseFieldType):

	__slots__ = ["_Cur", "_Dflt"]
	@property
	def Cur(self):
		return self._Cur

	@Cur.setter
	def Cur(self, value):
		self._Cur = value if type(value) != auto else self.make_default("Cur")

	@Cur.deleter
	def Cur(self):
		del self._Cur
		self._Cur = None

	@property
	def Dflt(self):
		return self._Dflt

	@Dflt.setter
	def Dflt(self, value):
		self._Dflt = value if type(value) != auto else self.make_default("Dflt")

	@Dflt.deleter
	def Dflt(self):
		del self._Dflt
		self._Dflt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cur', type=ReservationIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dflt', type=ReservationIdentification4, min=0, max=1, mutex_group=1, array=False),
	))

