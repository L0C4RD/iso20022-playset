import base_types
import TransportByRoad4
import TransportByRail4
import TransportByAir4
import TransportBySea5

class SingleTransport8(base_types._BaseFieldType):

	__slots__ = ["_TrnsprtByAir", "_TrnsprtByRoad", "_TrnsprtByRail", "_TrnsprtBySea"]
	@property
	def TrnsprtByAir(self):
		return self._TrnsprtByAir

	@TrnsprtByAir.setter
	def TrnsprtByAir(self, value):
		self._TrnsprtByAir = value if type(value) != auto else self.make_default("TrnsprtByAir")

	@TrnsprtByAir.deleter
	def TrnsprtByAir(self):
		del self._TrnsprtByAir
		self._TrnsprtByAir = None

	@property
	def TrnsprtByRoad(self):
		return self._TrnsprtByRoad

	@TrnsprtByRoad.setter
	def TrnsprtByRoad(self, value):
		self._TrnsprtByRoad = value if type(value) != auto else self.make_default("TrnsprtByRoad")

	@TrnsprtByRoad.deleter
	def TrnsprtByRoad(self):
		del self._TrnsprtByRoad
		self._TrnsprtByRoad = None

	@property
	def TrnsprtByRail(self):
		return self._TrnsprtByRail

	@TrnsprtByRail.setter
	def TrnsprtByRail(self, value):
		self._TrnsprtByRail = value if type(value) != auto else self.make_default("TrnsprtByRail")

	@TrnsprtByRail.deleter
	def TrnsprtByRail(self):
		del self._TrnsprtByRail
		self._TrnsprtByRail = None

	@property
	def TrnsprtBySea(self):
		return self._TrnsprtBySea

	@TrnsprtBySea.setter
	def TrnsprtBySea(self, value):
		self._TrnsprtBySea = value if type(value) != auto else self.make_default("TrnsprtBySea")

	@TrnsprtBySea.deleter
	def TrnsprtBySea(self):
		del self._TrnsprtBySea
		self._TrnsprtBySea = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsprtByAir', type=TransportByAir4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRoad', type=TransportByRoad4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtByRail', type=TransportByRail4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtBySea', type=TransportBySea5, min=0, max=None, mutex_group=None, array=True),
	))

