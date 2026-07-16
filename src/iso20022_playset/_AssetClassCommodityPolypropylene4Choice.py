# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PolypropyleneCommodityOther2
from . import PolypropyleneCommodityPlastic2

class AssetClassCommodityPolypropylene4Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Plstc"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', PolypropyleneCommodityOther2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', PolypropyleneCommodityOther2, False)

	@property
	def Plstc(self):
		return self._Plstc

	@Plstc.setter
	def Plstc(self, value):
		self._Plstc = value if value is not None else base_types.UninitialisedField(self, 'Plstc', PolypropyleneCommodityPlastic2, False)

	@Plstc.deleter
	def Plstc(self):
		del self._Plstc
		self._Plstc = base_types.UninitialisedField(self, 'Plstc', PolypropyleneCommodityPlastic2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=PolypropyleneCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Plstc', type=PolypropyleneCommodityPlastic2, min=0, max=1, mutex_group=1, array=False),
	))