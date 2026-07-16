# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FertilizerCommodityAmmonia2
from . import FertilizerCommodityDiammoniumPhosphate2
from . import FertilizerCommodityOther2
from . import FertilizerCommodityPotash2
from . import FertilizerCommoditySulphur2
from . import FertilizerCommodityUrea2
from . import FertilizerCommodityUreaAndAmmoniumNitrate2

class AssetClassCommodityFertilizer4Choice(base_types._BaseFieldType):

	__slots__ = ["_Ammn", "_DmmnmPhspht", "_Othr", "_Ptsh", "_Slphr", "_Urea", "_UreaAndAmmnmNtrt"]
	@property
	def Ammn(self):
		return self._Ammn

	@Ammn.setter
	def Ammn(self, value):
		self._Ammn = value if value is not None else base_types.UninitialisedField(self, 'Ammn', FertilizerCommodityAmmonia2, False)

	@Ammn.deleter
	def Ammn(self):
		del self._Ammn
		self._Ammn = base_types.UninitialisedField(self, 'Ammn', FertilizerCommodityAmmonia2, False)

	@property
	def DmmnmPhspht(self):
		return self._DmmnmPhspht

	@DmmnmPhspht.setter
	def DmmnmPhspht(self, value):
		self._DmmnmPhspht = value if value is not None else base_types.UninitialisedField(self, 'DmmnmPhspht', FertilizerCommodityDiammoniumPhosphate2, False)

	@DmmnmPhspht.deleter
	def DmmnmPhspht(self):
		del self._DmmnmPhspht
		self._DmmnmPhspht = base_types.UninitialisedField(self, 'DmmnmPhspht', FertilizerCommodityDiammoniumPhosphate2, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', FertilizerCommodityOther2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', FertilizerCommodityOther2, False)

	@property
	def Ptsh(self):
		return self._Ptsh

	@Ptsh.setter
	def Ptsh(self, value):
		self._Ptsh = value if value is not None else base_types.UninitialisedField(self, 'Ptsh', FertilizerCommodityPotash2, False)

	@Ptsh.deleter
	def Ptsh(self):
		del self._Ptsh
		self._Ptsh = base_types.UninitialisedField(self, 'Ptsh', FertilizerCommodityPotash2, False)

	@property
	def Slphr(self):
		return self._Slphr

	@Slphr.setter
	def Slphr(self, value):
		self._Slphr = value if value is not None else base_types.UninitialisedField(self, 'Slphr', FertilizerCommoditySulphur2, False)

	@Slphr.deleter
	def Slphr(self):
		del self._Slphr
		self._Slphr = base_types.UninitialisedField(self, 'Slphr', FertilizerCommoditySulphur2, False)

	@property
	def Urea(self):
		return self._Urea

	@Urea.setter
	def Urea(self, value):
		self._Urea = value if value is not None else base_types.UninitialisedField(self, 'Urea', FertilizerCommodityUrea2, False)

	@Urea.deleter
	def Urea(self):
		del self._Urea
		self._Urea = base_types.UninitialisedField(self, 'Urea', FertilizerCommodityUrea2, False)

	@property
	def UreaAndAmmnmNtrt(self):
		return self._UreaAndAmmnmNtrt

	@UreaAndAmmnmNtrt.setter
	def UreaAndAmmnmNtrt(self, value):
		self._UreaAndAmmnmNtrt = value if value is not None else base_types.UninitialisedField(self, 'UreaAndAmmnmNtrt', FertilizerCommodityUreaAndAmmoniumNitrate2, False)

	@UreaAndAmmnmNtrt.deleter
	def UreaAndAmmnmNtrt(self):
		del self._UreaAndAmmnmNtrt
		self._UreaAndAmmnmNtrt = base_types.UninitialisedField(self, 'UreaAndAmmnmNtrt', FertilizerCommodityUreaAndAmmoniumNitrate2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ammn', type=FertilizerCommodityAmmonia2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DmmnmPhspht', type=FertilizerCommodityDiammoniumPhosphate2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=FertilizerCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ptsh', type=FertilizerCommodityPotash2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Slphr', type=FertilizerCommoditySulphur2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Urea', type=FertilizerCommodityUrea2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UreaAndAmmnmNtrt', type=FertilizerCommodityUreaAndAmmoniumNitrate2, min=0, max=1, mutex_group=1, array=False),
	))