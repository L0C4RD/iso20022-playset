# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FertilizerCommodityAmmonia1
from . import FertilizerCommodityDiammoniumPhosphate1
from . import FertilizerCommodityPotash1
from . import FertilizerCommoditySulphur1
from . import FertilizerCommodityUrea1
from . import FertilizerCommodityUreaAndAmmoniumNitrate1

class AssetClassCommodityFertilizer1Choice(base_types._BaseFieldType):

	__slots__ = ["_Ammn", "_DmmnmPhspht", "_Ptsh", "_Slphr", "_Urea", "_UreaAndAmmnmNtrt"]
	@property
	def Ammn(self):
		return self._Ammn

	@Ammn.setter
	def Ammn(self, value):
		self._Ammn = value if value is not None else base_types.UninitialisedField(self, 'Ammn', FertilizerCommodityAmmonia1, False)

	@Ammn.deleter
	def Ammn(self):
		del self._Ammn
		self._Ammn = base_types.UninitialisedField(self, 'Ammn', FertilizerCommodityAmmonia1, False)

	@property
	def DmmnmPhspht(self):
		return self._DmmnmPhspht

	@DmmnmPhspht.setter
	def DmmnmPhspht(self, value):
		self._DmmnmPhspht = value if value is not None else base_types.UninitialisedField(self, 'DmmnmPhspht', FertilizerCommodityDiammoniumPhosphate1, False)

	@DmmnmPhspht.deleter
	def DmmnmPhspht(self):
		del self._DmmnmPhspht
		self._DmmnmPhspht = base_types.UninitialisedField(self, 'DmmnmPhspht', FertilizerCommodityDiammoniumPhosphate1, False)

	@property
	def Ptsh(self):
		return self._Ptsh

	@Ptsh.setter
	def Ptsh(self, value):
		self._Ptsh = value if value is not None else base_types.UninitialisedField(self, 'Ptsh', FertilizerCommodityPotash1, False)

	@Ptsh.deleter
	def Ptsh(self):
		del self._Ptsh
		self._Ptsh = base_types.UninitialisedField(self, 'Ptsh', FertilizerCommodityPotash1, False)

	@property
	def Slphr(self):
		return self._Slphr

	@Slphr.setter
	def Slphr(self, value):
		self._Slphr = value if value is not None else base_types.UninitialisedField(self, 'Slphr', FertilizerCommoditySulphur1, False)

	@Slphr.deleter
	def Slphr(self):
		del self._Slphr
		self._Slphr = base_types.UninitialisedField(self, 'Slphr', FertilizerCommoditySulphur1, False)

	@property
	def Urea(self):
		return self._Urea

	@Urea.setter
	def Urea(self, value):
		self._Urea = value if value is not None else base_types.UninitialisedField(self, 'Urea', FertilizerCommodityUrea1, False)

	@Urea.deleter
	def Urea(self):
		del self._Urea
		self._Urea = base_types.UninitialisedField(self, 'Urea', FertilizerCommodityUrea1, False)

	@property
	def UreaAndAmmnmNtrt(self):
		return self._UreaAndAmmnmNtrt

	@UreaAndAmmnmNtrt.setter
	def UreaAndAmmnmNtrt(self, value):
		self._UreaAndAmmnmNtrt = value if value is not None else base_types.UninitialisedField(self, 'UreaAndAmmnmNtrt', FertilizerCommodityUreaAndAmmoniumNitrate1, False)

	@UreaAndAmmnmNtrt.deleter
	def UreaAndAmmnmNtrt(self):
		del self._UreaAndAmmnmNtrt
		self._UreaAndAmmnmNtrt = base_types.UninitialisedField(self, 'UreaAndAmmnmNtrt', FertilizerCommodityUreaAndAmmoniumNitrate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ammn', type=FertilizerCommodityAmmonia1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DmmnmPhspht', type=FertilizerCommodityDiammoniumPhosphate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ptsh', type=FertilizerCommodityPotash1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Slphr', type=FertilizerCommoditySulphur1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Urea', type=FertilizerCommodityUrea1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UreaAndAmmnmNtrt', type=FertilizerCommodityUreaAndAmmoniumNitrate1, min=0, max=1, mutex_group=1, array=False),
	))