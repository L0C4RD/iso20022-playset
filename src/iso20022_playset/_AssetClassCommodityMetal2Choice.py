# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MetalCommodityNonPrecious2
from . import MetalCommodityPrecious2

class AssetClassCommodityMetal2Choice(base_types._BaseFieldType):

	__slots__ = ["_NonPrcs", "_Prcs"]
	@property
	def NonPrcs(self):
		return self._NonPrcs

	@NonPrcs.setter
	def NonPrcs(self, value):
		self._NonPrcs = value if value is not None else base_types.UninitialisedField(self, 'NonPrcs', MetalCommodityNonPrecious2, False)

	@NonPrcs.deleter
	def NonPrcs(self):
		del self._NonPrcs
		self._NonPrcs = base_types.UninitialisedField(self, 'NonPrcs', MetalCommodityNonPrecious2, False)

	@property
	def Prcs(self):
		return self._Prcs

	@Prcs.setter
	def Prcs(self, value):
		self._Prcs = value if value is not None else base_types.UninitialisedField(self, 'Prcs', MetalCommodityPrecious2, False)

	@Prcs.deleter
	def Prcs(self):
		del self._Prcs
		self._Prcs = base_types.UninitialisedField(self, 'Prcs', MetalCommodityPrecious2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonPrcs', type=MetalCommodityNonPrecious2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcs', type=MetalCommodityPrecious2, min=0, max=1, mutex_group=1, array=False),
	))