# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EnvironmentalCommodityCarbonRelated1
from . import EnvironmentalCommodityEmission1
from . import EnvironmentalCommodityWeather1

class AssetClassCommodityEnvironmental1Choice(base_types._BaseFieldType):

	__slots__ = ["_CrbnRltd", "_Emssns", "_Wthr"]
	@property
	def CrbnRltd(self):
		return self._CrbnRltd

	@CrbnRltd.setter
	def CrbnRltd(self, value):
		self._CrbnRltd = value if value is not None else base_types.UninitialisedField(self, 'CrbnRltd', EnvironmentalCommodityCarbonRelated1, False)

	@CrbnRltd.deleter
	def CrbnRltd(self):
		del self._CrbnRltd
		self._CrbnRltd = base_types.UninitialisedField(self, 'CrbnRltd', EnvironmentalCommodityCarbonRelated1, False)

	@property
	def Emssns(self):
		return self._Emssns

	@Emssns.setter
	def Emssns(self, value):
		self._Emssns = value if value is not None else base_types.UninitialisedField(self, 'Emssns', EnvironmentalCommodityEmission1, False)

	@Emssns.deleter
	def Emssns(self):
		del self._Emssns
		self._Emssns = base_types.UninitialisedField(self, 'Emssns', EnvironmentalCommodityEmission1, False)

	@property
	def Wthr(self):
		return self._Wthr

	@Wthr.setter
	def Wthr(self, value):
		self._Wthr = value if value is not None else base_types.UninitialisedField(self, 'Wthr', EnvironmentalCommodityWeather1, False)

	@Wthr.deleter
	def Wthr(self):
		del self._Wthr
		self._Wthr = base_types.UninitialisedField(self, 'Wthr', EnvironmentalCommodityWeather1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrbnRltd', type=EnvironmentalCommodityCarbonRelated1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Emssns', type=EnvironmentalCommodityEmission1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wthr', type=EnvironmentalCommodityWeather1, min=0, max=1, mutex_group=1, array=False),
	))