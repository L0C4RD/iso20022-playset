# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransportByAir2
from . import TransportByRail2
from . import TransportByRoad2
from . import TransportBySea4

class SingleTransport3(base_types._BaseFieldType):

	__slots__ = ["_TrnsprtByAir", "_TrnsprtByRail", "_TrnsprtByRoad", "_TrnsprtBySea"]
	@property
	def TrnsprtByAir(self):
		return self._TrnsprtByAir

	@TrnsprtByAir.setter
	def TrnsprtByAir(self, value):
		self._TrnsprtByAir = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir2, False)

	@TrnsprtByAir.deleter
	def TrnsprtByAir(self):
		del self._TrnsprtByAir
		self._TrnsprtByAir = base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir2, False)

	@property
	def TrnsprtByRail(self):
		return self._TrnsprtByRail

	@TrnsprtByRail.setter
	def TrnsprtByRail(self, value):
		self._TrnsprtByRail = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail2, False)

	@TrnsprtByRail.deleter
	def TrnsprtByRail(self):
		del self._TrnsprtByRail
		self._TrnsprtByRail = base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail2, False)

	@property
	def TrnsprtByRoad(self):
		return self._TrnsprtByRoad

	@TrnsprtByRoad.setter
	def TrnsprtByRoad(self, value):
		self._TrnsprtByRoad = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad2, False)

	@TrnsprtByRoad.deleter
	def TrnsprtByRoad(self):
		del self._TrnsprtByRoad
		self._TrnsprtByRoad = base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad2, False)

	@property
	def TrnsprtBySea(self):
		return self._TrnsprtBySea

	@TrnsprtBySea.setter
	def TrnsprtBySea(self, value):
		self._TrnsprtBySea = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea4, False)

	@TrnsprtBySea.deleter
	def TrnsprtBySea(self):
		del self._TrnsprtBySea
		self._TrnsprtBySea = base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsprtByAir', type=TransportByAir2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtByRail', type=TransportByRail2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtByRoad', type=TransportByRoad2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtBySea', type=TransportBySea4, min=0, max=1, mutex_group=None, array=False),
	))