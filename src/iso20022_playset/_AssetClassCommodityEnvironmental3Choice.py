# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EnvironmentCommodityOther2
from . import EnvironmentalCommodityCarbonRelated2
from . import EnvironmentalCommodityEmission3
from . import EnvironmentalCommodityWeather2

class AssetClassCommodityEnvironmental3Choice(base_types._BaseFieldType):

	__slots__ = ["_CrbnRltd", "_Emssns", "_Othr", "_Wthr"]
	@property
	def CrbnRltd(self):
		return self._CrbnRltd

	@CrbnRltd.setter
	def CrbnRltd(self, value):
		self._CrbnRltd = value if value is not None else base_types.UninitialisedField(self, 'CrbnRltd', EnvironmentalCommodityCarbonRelated2, False)

	@CrbnRltd.deleter
	def CrbnRltd(self):
		del self._CrbnRltd
		self._CrbnRltd = base_types.UninitialisedField(self, 'CrbnRltd', EnvironmentalCommodityCarbonRelated2, False)

	@property
	def Emssns(self):
		return self._Emssns

	@Emssns.setter
	def Emssns(self, value):
		self._Emssns = value if value is not None else base_types.UninitialisedField(self, 'Emssns', EnvironmentalCommodityEmission3, False)

	@Emssns.deleter
	def Emssns(self):
		del self._Emssns
		self._Emssns = base_types.UninitialisedField(self, 'Emssns', EnvironmentalCommodityEmission3, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', EnvironmentCommodityOther2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', EnvironmentCommodityOther2, False)

	@property
	def Wthr(self):
		return self._Wthr

	@Wthr.setter
	def Wthr(self, value):
		self._Wthr = value if value is not None else base_types.UninitialisedField(self, 'Wthr', EnvironmentalCommodityWeather2, False)

	@Wthr.deleter
	def Wthr(self):
		del self._Wthr
		self._Wthr = base_types.UninitialisedField(self, 'Wthr', EnvironmentalCommodityWeather2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrbnRltd', type=EnvironmentalCommodityCarbonRelated2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Emssns', type=EnvironmentalCommodityEmission3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=EnvironmentCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wthr', type=EnvironmentalCommodityWeather2, min=0, max=1, mutex_group=1, array=False),
	))