# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransportByAir5
from . import TransportByRail5
from . import TransportByRoad5
from . import TransportBySea6

class SingleTransport7(base_types._BaseFieldType):

	__slots__ = ["_TrnsprtByAir", "_TrnsprtByRail", "_TrnsprtByRoad", "_TrnsprtBySea"]
	@property
	def TrnsprtByAir(self):
		return self._TrnsprtByAir

	@TrnsprtByAir.setter
	def TrnsprtByAir(self, value):
		self._TrnsprtByAir = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir5, True)

	@TrnsprtByAir.deleter
	def TrnsprtByAir(self):
		del self._TrnsprtByAir
		self._TrnsprtByAir = base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir5, True)

	@property
	def TrnsprtByRail(self):
		return self._TrnsprtByRail

	@TrnsprtByRail.setter
	def TrnsprtByRail(self, value):
		self._TrnsprtByRail = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail5, True)

	@TrnsprtByRail.deleter
	def TrnsprtByRail(self):
		del self._TrnsprtByRail
		self._TrnsprtByRail = base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail5, True)

	@property
	def TrnsprtByRoad(self):
		return self._TrnsprtByRoad

	@TrnsprtByRoad.setter
	def TrnsprtByRoad(self, value):
		self._TrnsprtByRoad = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad5, True)

	@TrnsprtByRoad.deleter
	def TrnsprtByRoad(self):
		del self._TrnsprtByRoad
		self._TrnsprtByRoad = base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad5, True)

	@property
	def TrnsprtBySea(self):
		return self._TrnsprtBySea

	@TrnsprtBySea.setter
	def TrnsprtBySea(self, value):
		self._TrnsprtBySea = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea6, True)

	@TrnsprtBySea.deleter
	def TrnsprtBySea(self):
		del self._TrnsprtBySea
		self._TrnsprtBySea = base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsprtByAir', type=TransportByAir5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRail', type=TransportByRail5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRoad', type=TransportByRoad5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtBySea', type=TransportBySea6, min=0, max=None, mutex_group=None, array=True),
	))