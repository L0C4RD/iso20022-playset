# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgriculturalCommodityDairy1
from . import AgriculturalCommodityForestry1
from . import AgriculturalCommodityGrain2
from . import AgriculturalCommodityLiveStock1
from . import AgriculturalCommodityOilSeed1
from . import AgriculturalCommodityOliveOil2
from . import AgriculturalCommodityOther1
from . import AgriculturalCommodityPotato1
from . import AgriculturalCommoditySeafood1
from . import AgriculturalCommoditySoft1

class AssetClassCommodityAgricultural5Choice(base_types._BaseFieldType):

	__slots__ = ["_Dairy", "_Frstry", "_Grn", "_GrnOilSeed", "_LiveStock", "_OlvOil", "_Othr", "_Ptt", "_Sfd", "_Soft"]
	@property
	def Dairy(self):
		return self._Dairy

	@Dairy.setter
	def Dairy(self, value):
		self._Dairy = value if value is not None else base_types.UninitialisedField(self, 'Dairy', AgriculturalCommodityDairy1, False)

	@Dairy.deleter
	def Dairy(self):
		del self._Dairy
		self._Dairy = base_types.UninitialisedField(self, 'Dairy', AgriculturalCommodityDairy1, False)

	@property
	def Frstry(self):
		return self._Frstry

	@Frstry.setter
	def Frstry(self, value):
		self._Frstry = value if value is not None else base_types.UninitialisedField(self, 'Frstry', AgriculturalCommodityForestry1, False)

	@Frstry.deleter
	def Frstry(self):
		del self._Frstry
		self._Frstry = base_types.UninitialisedField(self, 'Frstry', AgriculturalCommodityForestry1, False)

	@property
	def Grn(self):
		return self._Grn

	@Grn.setter
	def Grn(self, value):
		self._Grn = value if value is not None else base_types.UninitialisedField(self, 'Grn', AgriculturalCommodityGrain2, False)

	@Grn.deleter
	def Grn(self):
		del self._Grn
		self._Grn = base_types.UninitialisedField(self, 'Grn', AgriculturalCommodityGrain2, False)

	@property
	def GrnOilSeed(self):
		return self._GrnOilSeed

	@GrnOilSeed.setter
	def GrnOilSeed(self, value):
		self._GrnOilSeed = value if value is not None else base_types.UninitialisedField(self, 'GrnOilSeed', AgriculturalCommodityOilSeed1, False)

	@GrnOilSeed.deleter
	def GrnOilSeed(self):
		del self._GrnOilSeed
		self._GrnOilSeed = base_types.UninitialisedField(self, 'GrnOilSeed', AgriculturalCommodityOilSeed1, False)

	@property
	def LiveStock(self):
		return self._LiveStock

	@LiveStock.setter
	def LiveStock(self, value):
		self._LiveStock = value if value is not None else base_types.UninitialisedField(self, 'LiveStock', AgriculturalCommodityLiveStock1, False)

	@LiveStock.deleter
	def LiveStock(self):
		del self._LiveStock
		self._LiveStock = base_types.UninitialisedField(self, 'LiveStock', AgriculturalCommodityLiveStock1, False)

	@property
	def OlvOil(self):
		return self._OlvOil

	@OlvOil.setter
	def OlvOil(self, value):
		self._OlvOil = value if value is not None else base_types.UninitialisedField(self, 'OlvOil', AgriculturalCommodityOliveOil2, False)

	@OlvOil.deleter
	def OlvOil(self):
		del self._OlvOil
		self._OlvOil = base_types.UninitialisedField(self, 'OlvOil', AgriculturalCommodityOliveOil2, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AgriculturalCommodityOther1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AgriculturalCommodityOther1, False)

	@property
	def Ptt(self):
		return self._Ptt

	@Ptt.setter
	def Ptt(self, value):
		self._Ptt = value if value is not None else base_types.UninitialisedField(self, 'Ptt', AgriculturalCommodityPotato1, False)

	@Ptt.deleter
	def Ptt(self):
		del self._Ptt
		self._Ptt = base_types.UninitialisedField(self, 'Ptt', AgriculturalCommodityPotato1, False)

	@property
	def Sfd(self):
		return self._Sfd

	@Sfd.setter
	def Sfd(self, value):
		self._Sfd = value if value is not None else base_types.UninitialisedField(self, 'Sfd', AgriculturalCommoditySeafood1, False)

	@Sfd.deleter
	def Sfd(self):
		del self._Sfd
		self._Sfd = base_types.UninitialisedField(self, 'Sfd', AgriculturalCommoditySeafood1, False)

	@property
	def Soft(self):
		return self._Soft

	@Soft.setter
	def Soft(self, value):
		self._Soft = value if value is not None else base_types.UninitialisedField(self, 'Soft', AgriculturalCommoditySoft1, False)

	@Soft.deleter
	def Soft(self):
		del self._Soft
		self._Soft = base_types.UninitialisedField(self, 'Soft', AgriculturalCommoditySoft1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dairy', type=AgriculturalCommodityDairy1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Frstry', type=AgriculturalCommodityForestry1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Grn', type=AgriculturalCommodityGrain2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GrnOilSeed', type=AgriculturalCommodityOilSeed1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LiveStock', type=AgriculturalCommodityLiveStock1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OlvOil', type=AgriculturalCommodityOliveOil2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=AgriculturalCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ptt', type=AgriculturalCommodityPotato1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sfd', type=AgriculturalCommoditySeafood1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Soft', type=AgriculturalCommoditySoft1, min=0, max=1, mutex_group=1, array=False),
	))