from . import base_types
from ._AgriculturalCommodityDairy1 import AgriculturalCommodityDairy1
from ._AgriculturalCommodityForestry1 import AgriculturalCommodityForestry1
from ._AgriculturalCommodityGrain1 import AgriculturalCommodityGrain1
from ._AgriculturalCommodityLiveStock1 import AgriculturalCommodityLiveStock1
from ._AgriculturalCommodityOilSeed1 import AgriculturalCommodityOilSeed1
from ._AgriculturalCommodityOliveOil1 import AgriculturalCommodityOliveOil1
from ._AgriculturalCommodityPotato1 import AgriculturalCommodityPotato1
from ._AgriculturalCommoditySeafood1 import AgriculturalCommoditySeafood1
from ._AgriculturalCommoditySoft1 import AgriculturalCommoditySoft1

class AssetClassCommodityAgricultural1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dairy", "_Frstry", "_Grn", "_GrnOilSeed", "_LiveStock", "_OlvOil", "_Ptt", "_Sfd", "_Soft"]
	@property
	def Dairy(self):
		return self._Dairy

	@Dairy.setter
	def Dairy(self, value):
		self._Dairy = value if type(value) != base_types.auto else self.make_default("Dairy")

	@Dairy.deleter
	def Dairy(self):
		del self._Dairy
		self._Dairy = None

	@property
	def Frstry(self):
		return self._Frstry

	@Frstry.setter
	def Frstry(self, value):
		self._Frstry = value if type(value) != base_types.auto else self.make_default("Frstry")

	@Frstry.deleter
	def Frstry(self):
		del self._Frstry
		self._Frstry = None

	@property
	def Grn(self):
		return self._Grn

	@Grn.setter
	def Grn(self, value):
		self._Grn = value if type(value) != base_types.auto else self.make_default("Grn")

	@Grn.deleter
	def Grn(self):
		del self._Grn
		self._Grn = None

	@property
	def GrnOilSeed(self):
		return self._GrnOilSeed

	@GrnOilSeed.setter
	def GrnOilSeed(self, value):
		self._GrnOilSeed = value if type(value) != base_types.auto else self.make_default("GrnOilSeed")

	@GrnOilSeed.deleter
	def GrnOilSeed(self):
		del self._GrnOilSeed
		self._GrnOilSeed = None

	@property
	def LiveStock(self):
		return self._LiveStock

	@LiveStock.setter
	def LiveStock(self, value):
		self._LiveStock = value if type(value) != base_types.auto else self.make_default("LiveStock")

	@LiveStock.deleter
	def LiveStock(self):
		del self._LiveStock
		self._LiveStock = None

	@property
	def OlvOil(self):
		return self._OlvOil

	@OlvOil.setter
	def OlvOil(self, value):
		self._OlvOil = value if type(value) != base_types.auto else self.make_default("OlvOil")

	@OlvOil.deleter
	def OlvOil(self):
		del self._OlvOil
		self._OlvOil = None

	@property
	def Ptt(self):
		return self._Ptt

	@Ptt.setter
	def Ptt(self, value):
		self._Ptt = value if type(value) != base_types.auto else self.make_default("Ptt")

	@Ptt.deleter
	def Ptt(self):
		del self._Ptt
		self._Ptt = None

	@property
	def Sfd(self):
		return self._Sfd

	@Sfd.setter
	def Sfd(self, value):
		self._Sfd = value if type(value) != base_types.auto else self.make_default("Sfd")

	@Sfd.deleter
	def Sfd(self):
		del self._Sfd
		self._Sfd = None

	@property
	def Soft(self):
		return self._Soft

	@Soft.setter
	def Soft(self, value):
		self._Soft = value if type(value) != base_types.auto else self.make_default("Soft")

	@Soft.deleter
	def Soft(self):
		del self._Soft
		self._Soft = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dairy', type=AgriculturalCommodityDairy1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frstry', type=AgriculturalCommodityForestry1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Grn', type=AgriculturalCommodityGrain1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GrnOilSeed', type=AgriculturalCommodityOilSeed1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LiveStock', type=AgriculturalCommodityLiveStock1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OlvOil', type=AgriculturalCommodityOliveOil1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ptt', type=AgriculturalCommodityPotato1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sfd', type=AgriculturalCommoditySeafood1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Soft', type=AgriculturalCommoditySoft1, min=0, max=1, mutex_group=1, array=False),
	))

