# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassProductType1Code
from . import AssetClassSubProductType20Code

class AgriculturalCommodityDairy2(base_types._BaseFieldType):

	__slots__ = ["_BasePdct", "_SubPdct"]
	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if value is not None else base_types.UninitialisedField(self, 'BasePdct', AssetClassProductType1Code, False)

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = base_types.UninitialisedField(self, 'BasePdct', AssetClassProductType1Code, False)

	@property
	def SubPdct(self):
		return self._SubPdct

	@SubPdct.setter
	def SubPdct(self, value):
		self._SubPdct = value if value is not None else base_types.UninitialisedField(self, 'SubPdct', AssetClassSubProductType20Code, False)

	@SubPdct.deleter
	def SubPdct(self):
		del self._SubPdct
		self._SubPdct = base_types.UninitialisedField(self, 'SubPdct', AssetClassSubProductType20Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=AssetClassSubProductType20Code, min=0, max=1, mutex_group=None, array=False),
	))