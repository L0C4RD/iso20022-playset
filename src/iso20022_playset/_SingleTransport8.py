# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransportByAir4
from . import TransportByRail4
from . import TransportByRoad4
from . import TransportBySea5

class SingleTransport8(base_types._BaseFieldType):

	__slots__ = ["_TrnsprtByAir", "_TrnsprtByRail", "_TrnsprtByRoad", "_TrnsprtBySea"]
	@property
	def TrnsprtByAir(self):
		return self._TrnsprtByAir

	@TrnsprtByAir.setter
	def TrnsprtByAir(self, value):
		self._TrnsprtByAir = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir4, True)

	@TrnsprtByAir.deleter
	def TrnsprtByAir(self):
		del self._TrnsprtByAir
		self._TrnsprtByAir = base_types.UninitialisedField(self, 'TrnsprtByAir', TransportByAir4, True)

	@property
	def TrnsprtByRail(self):
		return self._TrnsprtByRail

	@TrnsprtByRail.setter
	def TrnsprtByRail(self, value):
		self._TrnsprtByRail = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail4, True)

	@TrnsprtByRail.deleter
	def TrnsprtByRail(self):
		del self._TrnsprtByRail
		self._TrnsprtByRail = base_types.UninitialisedField(self, 'TrnsprtByRail', TransportByRail4, True)

	@property
	def TrnsprtByRoad(self):
		return self._TrnsprtByRoad

	@TrnsprtByRoad.setter
	def TrnsprtByRoad(self, value):
		self._TrnsprtByRoad = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad4, True)

	@TrnsprtByRoad.deleter
	def TrnsprtByRoad(self):
		del self._TrnsprtByRoad
		self._TrnsprtByRoad = base_types.UninitialisedField(self, 'TrnsprtByRoad', TransportByRoad4, True)

	@property
	def TrnsprtBySea(self):
		return self._TrnsprtBySea

	@TrnsprtBySea.setter
	def TrnsprtBySea(self, value):
		self._TrnsprtBySea = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea5, True)

	@TrnsprtBySea.deleter
	def TrnsprtBySea(self):
		del self._TrnsprtBySea
		self._TrnsprtBySea = base_types.UninitialisedField(self, 'TrnsprtBySea', TransportBySea5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsprtByAir', type=TransportByAir4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRail', type=TransportByRail4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRoad', type=TransportByRoad4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtBySea', type=TransportBySea5, min=0, max=None, mutex_group=None, array=True),
	))