from . import base_types
from ._EnvironmentalCommodityWeather2 import EnvironmentalCommodityWeather2
from ._EnvironmentalCommodityEmission3 import EnvironmentalCommodityEmission3
from ._EnvironmentCommodityOther2 import EnvironmentCommodityOther2
from ._EnvironmentalCommodityCarbonRelated2 import EnvironmentalCommodityCarbonRelated2

class AssetClassCommodityEnvironmental3Choice(base_types._BaseFieldType):

	__slots__ = ["_CrbnRltd", "_Emssns", "_Wthr", "_Othr"]
	@property
	def CrbnRltd(self):
		return self._CrbnRltd

	@CrbnRltd.setter
	def CrbnRltd(self, value):
		self._CrbnRltd = value if type(value) != base_types.auto else self.make_default("CrbnRltd")

	@CrbnRltd.deleter
	def CrbnRltd(self):
		del self._CrbnRltd
		self._CrbnRltd = None

	@property
	def Emssns(self):
		return self._Emssns

	@Emssns.setter
	def Emssns(self, value):
		self._Emssns = value if type(value) != base_types.auto else self.make_default("Emssns")

	@Emssns.deleter
	def Emssns(self):
		del self._Emssns
		self._Emssns = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Wthr(self):
		return self._Wthr

	@Wthr.setter
	def Wthr(self, value):
		self._Wthr = value if type(value) != base_types.auto else self.make_default("Wthr")

	@Wthr.deleter
	def Wthr(self):
		del self._Wthr
		self._Wthr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrbnRltd', type=EnvironmentalCommodityCarbonRelated2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Emssns', type=EnvironmentalCommodityEmission3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=EnvironmentCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wthr', type=EnvironmentalCommodityWeather2, min=0, max=1, mutex_group=1, array=False),
	))

