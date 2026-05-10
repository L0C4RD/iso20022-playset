from . import base_types
from .ReservationReport8 import ReservationReport8

class CurrentAndDefaultReservation6(base_types._BaseFieldType):

	__slots__ = ["_CurRsvatn", "_DfltRsvatn"]
	@property
	def CurRsvatn(self):
		return self._CurRsvatn

	@CurRsvatn.setter
	def CurRsvatn(self, value):
		self._CurRsvatn = value if type(value) != base_types.auto else self.make_default("CurRsvatn")

	@CurRsvatn.deleter
	def CurRsvatn(self):
		del self._CurRsvatn
		self._CurRsvatn = None

	@property
	def DfltRsvatn(self):
		return self._DfltRsvatn

	@DfltRsvatn.setter
	def DfltRsvatn(self, value):
		self._DfltRsvatn = value if type(value) != base_types.auto else self.make_default("DfltRsvatn")

	@DfltRsvatn.deleter
	def DfltRsvatn(self):
		del self._DfltRsvatn
		self._DfltRsvatn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurRsvatn', type=ReservationReport8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltRsvatn', type=ReservationReport8, min=0, max=None, mutex_group=None, array=True),
	))

