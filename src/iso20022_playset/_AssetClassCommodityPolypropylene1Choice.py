# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PolypropyleneCommodityPlastic1

class AssetClassCommodityPolypropylene1Choice(base_types._BaseFieldType):

	__slots__ = ["_Plstc"]
	@property
	def Plstc(self):
		return self._Plstc

	@Plstc.setter
	def Plstc(self, value):
		self._Plstc = value if value is not None else base_types.UninitialisedField(self, 'Plstc', PolypropyleneCommodityPlastic1, False)

	@Plstc.deleter
	def Plstc(self):
		del self._Plstc
		self._Plstc = base_types.UninitialisedField(self, 'Plstc', PolypropyleneCommodityPlastic1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plstc', type=PolypropyleneCommodityPlastic1, min=0, max=1, mutex_group=1, array=False),
	))