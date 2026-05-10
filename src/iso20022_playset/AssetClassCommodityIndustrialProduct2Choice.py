from . import base_types
import IndustrialProductCommodityManufacturing2
import IndustrialProductCommodityConstruction2

class AssetClassCommodityIndustrialProduct2Choice(base_types._BaseFieldType):

	__slots__ = ["_Cnstrctn", "_Manfctg"]
	@property
	def Cnstrctn(self):
		return self._Cnstrctn

	@Cnstrctn.setter
	def Cnstrctn(self, value):
		self._Cnstrctn = value if type(value) != auto else self.make_default("Cnstrctn")

	@Cnstrctn.deleter
	def Cnstrctn(self):
		del self._Cnstrctn
		self._Cnstrctn = None

	@property
	def Manfctg(self):
		return self._Manfctg

	@Manfctg.setter
	def Manfctg(self, value):
		self._Manfctg = value if type(value) != auto else self.make_default("Manfctg")

	@Manfctg.deleter
	def Manfctg(self):
		del self._Manfctg
		self._Manfctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnstrctn', type=IndustrialProductCommodityConstruction2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Manfctg', type=IndustrialProductCommodityManufacturing2, min=0, max=1, mutex_group=1, array=False),
	))

