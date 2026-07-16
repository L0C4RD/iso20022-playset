# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReservationIdentification4

class CurrentOrDefaultReservation4Choice(base_types._BaseFieldType):

	__slots__ = ["_Cur", "_Dflt"]
	@property
	def Cur(self):
		return self._Cur

	@Cur.setter
	def Cur(self, value):
		self._Cur = value if value is not None else base_types.UninitialisedField(self, 'Cur', ReservationIdentification4, False)

	@Cur.deleter
	def Cur(self):
		del self._Cur
		self._Cur = base_types.UninitialisedField(self, 'Cur', ReservationIdentification4, False)

	@property
	def Dflt(self):
		return self._Dflt

	@Dflt.setter
	def Dflt(self, value):
		self._Dflt = value if value is not None else base_types.UninitialisedField(self, 'Dflt', ReservationIdentification4, False)

	@Dflt.deleter
	def Dflt(self):
		del self._Dflt
		self._Dflt = base_types.UninitialisedField(self, 'Dflt', ReservationIdentification4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cur', type=ReservationIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dflt', type=ReservationIdentification4, min=0, max=1, mutex_group=1, array=False),
	))