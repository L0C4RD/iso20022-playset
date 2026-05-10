from . import base_types
from ._EnvironmentCommodityOther1 import EnvironmentCommodityOther1
from ._EnvironmentalCommodityCarbonRelated1 import EnvironmentalCommodityCarbonRelated1
from ._EnvironmentalCommodityEmission2 import EnvironmentalCommodityEmission2
from ._EnvironmentalCommodityWeather1 import EnvironmentalCommodityWeather1

class AssetClassCommodityEnvironmental2Choice(base_types._BaseFieldType):

	__slots__ = ["_CrbnRltd", "_Emssns", "_Othr", "_Wthr"]
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
		base_types.FieldEntry(name='CrbnRltd', type=EnvironmentalCommodityCarbonRelated1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Emssns', type=EnvironmentalCommodityEmission2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=EnvironmentCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wthr', type=EnvironmentalCommodityWeather1, min=0, max=1, mutex_group=1, array=False),
	))

