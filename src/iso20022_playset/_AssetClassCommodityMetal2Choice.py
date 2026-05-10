from . import base_types
from ._MetalCommodityPrecious2 import MetalCommodityPrecious2
from ._MetalCommodityNonPrecious2 import MetalCommodityNonPrecious2

class AssetClassCommodityMetal2Choice(base_types._BaseFieldType):

	__slots__ = ["_NonPrcs", "_Prcs"]
	@property
	def NonPrcs(self):
		return self._NonPrcs

	@NonPrcs.setter
	def NonPrcs(self, value):
		self._NonPrcs = value if type(value) != base_types.auto else self.make_default("NonPrcs")

	@NonPrcs.deleter
	def NonPrcs(self):
		del self._NonPrcs
		self._NonPrcs = None

	@property
	def Prcs(self):
		return self._Prcs

	@Prcs.setter
	def Prcs(self, value):
		self._Prcs = value if type(value) != base_types.auto else self.make_default("Prcs")

	@Prcs.deleter
	def Prcs(self):
		del self._Prcs
		self._Prcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonPrcs', type=MetalCommodityNonPrecious2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcs', type=MetalCommodityPrecious2, min=0, max=1, mutex_group=1, array=False),
	))

