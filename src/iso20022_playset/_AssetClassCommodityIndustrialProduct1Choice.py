# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndustrialProductCommodityConstruction1
from . import IndustrialProductCommodityManufacturing1

class AssetClassCommodityIndustrialProduct1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cnstrctn", "_Manfctg"]
	@property
	def Cnstrctn(self):
		return self._Cnstrctn

	@Cnstrctn.setter
	def Cnstrctn(self, value):
		self._Cnstrctn = value if value is not None else base_types.UninitialisedField(self, 'Cnstrctn', IndustrialProductCommodityConstruction1, False)

	@Cnstrctn.deleter
	def Cnstrctn(self):
		del self._Cnstrctn
		self._Cnstrctn = base_types.UninitialisedField(self, 'Cnstrctn', IndustrialProductCommodityConstruction1, False)

	@property
	def Manfctg(self):
		return self._Manfctg

	@Manfctg.setter
	def Manfctg(self, value):
		self._Manfctg = value if value is not None else base_types.UninitialisedField(self, 'Manfctg', IndustrialProductCommodityManufacturing1, False)

	@Manfctg.deleter
	def Manfctg(self):
		del self._Manfctg
		self._Manfctg = base_types.UninitialisedField(self, 'Manfctg', IndustrialProductCommodityManufacturing1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnstrctn', type=IndustrialProductCommodityConstruction1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Manfctg', type=IndustrialProductCommodityManufacturing1, min=0, max=1, mutex_group=1, array=False),
	))