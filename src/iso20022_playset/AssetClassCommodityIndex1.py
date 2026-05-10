import base_types
import AssetClassProductType16Code

class AssetClassCommodityIndex1(base_types._BaseFieldType):

	__slots__ = ["_BasePdct"]
	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if type(value) != auto else self.make_default("BasePdct")

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType16Code, min=1, max=1, mutex_group=None, array=False),
	))

