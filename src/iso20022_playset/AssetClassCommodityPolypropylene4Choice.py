from . import base_types
from .PolypropyleneCommodityPlastic2 import PolypropyleneCommodityPlastic2
from .PolypropyleneCommodityOther2 import PolypropyleneCommodityOther2

class AssetClassCommodityPolypropylene4Choice(base_types._BaseFieldType):

	__slots__ = ["_Plstc", "_Othr"]
	@property
	def Plstc(self):
		return self._Plstc

	@Plstc.setter
	def Plstc(self, value):
		self._Plstc = value if type(value) != base_types.auto else self.make_default("Plstc")

	@Plstc.deleter
	def Plstc(self):
		del self._Plstc
		self._Plstc = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plstc', type=PolypropyleneCommodityPlastic2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=PolypropyleneCommodityOther2, min=0, max=1, mutex_group=1, array=False),
	))

