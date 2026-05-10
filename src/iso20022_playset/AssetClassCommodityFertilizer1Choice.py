from . import base_types
from .FertilizerCommodityAmmonia1 import FertilizerCommodityAmmonia1
from .FertilizerCommoditySulphur1 import FertilizerCommoditySulphur1
from .FertilizerCommodityDiammoniumPhosphate1 import FertilizerCommodityDiammoniumPhosphate1
from .FertilizerCommodityUreaAndAmmoniumNitrate1 import FertilizerCommodityUreaAndAmmoniumNitrate1
from .FertilizerCommodityPotash1 import FertilizerCommodityPotash1
from .FertilizerCommodityUrea1 import FertilizerCommodityUrea1

class AssetClassCommodityFertilizer1Choice(base_types._BaseFieldType):

	__slots__ = ["_UreaAndAmmnmNtrt", "_Ammn", "_Urea", "_Slphr", "_DmmnmPhspht", "_Ptsh"]
	@property
	def UreaAndAmmnmNtrt(self):
		return self._UreaAndAmmnmNtrt

	@UreaAndAmmnmNtrt.setter
	def UreaAndAmmnmNtrt(self, value):
		self._UreaAndAmmnmNtrt = value if type(value) != auto else self.make_default("UreaAndAmmnmNtrt")

	@UreaAndAmmnmNtrt.deleter
	def UreaAndAmmnmNtrt(self):
		del self._UreaAndAmmnmNtrt
		self._UreaAndAmmnmNtrt = None

	@property
	def Ammn(self):
		return self._Ammn

	@Ammn.setter
	def Ammn(self, value):
		self._Ammn = value if type(value) != auto else self.make_default("Ammn")

	@Ammn.deleter
	def Ammn(self):
		del self._Ammn
		self._Ammn = None

	@property
	def Urea(self):
		return self._Urea

	@Urea.setter
	def Urea(self, value):
		self._Urea = value if type(value) != auto else self.make_default("Urea")

	@Urea.deleter
	def Urea(self):
		del self._Urea
		self._Urea = None

	@property
	def Slphr(self):
		return self._Slphr

	@Slphr.setter
	def Slphr(self, value):
		self._Slphr = value if type(value) != auto else self.make_default("Slphr")

	@Slphr.deleter
	def Slphr(self):
		del self._Slphr
		self._Slphr = None

	@property
	def DmmnmPhspht(self):
		return self._DmmnmPhspht

	@DmmnmPhspht.setter
	def DmmnmPhspht(self, value):
		self._DmmnmPhspht = value if type(value) != auto else self.make_default("DmmnmPhspht")

	@DmmnmPhspht.deleter
	def DmmnmPhspht(self):
		del self._DmmnmPhspht
		self._DmmnmPhspht = None

	@property
	def Ptsh(self):
		return self._Ptsh

	@Ptsh.setter
	def Ptsh(self, value):
		self._Ptsh = value if type(value) != auto else self.make_default("Ptsh")

	@Ptsh.deleter
	def Ptsh(self):
		del self._Ptsh
		self._Ptsh = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UreaAndAmmnmNtrt', type=FertilizerCommodityUreaAndAmmoniumNitrate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ammn', type=FertilizerCommodityAmmonia1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Urea', type=FertilizerCommodityUrea1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Slphr', type=FertilizerCommoditySulphur1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DmmnmPhspht', type=FertilizerCommodityDiammoniumPhosphate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ptsh', type=FertilizerCommodityPotash1, min=0, max=1, mutex_group=1, array=False),
	))

