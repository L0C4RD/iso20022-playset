# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReservationReport8

class CurrentAndDefaultReservation6(base_types._BaseFieldType):

	__slots__ = ["_CurRsvatn", "_DfltRsvatn"]
	@property
	def CurRsvatn(self):
		return self._CurRsvatn

	@CurRsvatn.setter
	def CurRsvatn(self, value):
		self._CurRsvatn = value if value is not None else base_types.UninitialisedField(self, 'CurRsvatn', ReservationReport8, True)

	@CurRsvatn.deleter
	def CurRsvatn(self):
		del self._CurRsvatn
		self._CurRsvatn = base_types.UninitialisedField(self, 'CurRsvatn', ReservationReport8, True)

	@property
	def DfltRsvatn(self):
		return self._DfltRsvatn

	@DfltRsvatn.setter
	def DfltRsvatn(self, value):
		self._DfltRsvatn = value if value is not None else base_types.UninitialisedField(self, 'DfltRsvatn', ReservationReport8, True)

	@DfltRsvatn.deleter
	def DfltRsvatn(self):
		del self._DfltRsvatn
		self._DfltRsvatn = base_types.UninitialisedField(self, 'DfltRsvatn', ReservationReport8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurRsvatn', type=ReservationReport8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltRsvatn', type=ReservationReport8, min=0, max=None, mutex_group=None, array=True),
	))