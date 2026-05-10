from . import base_types
from .PolypropyleneCommodityPlastic1 import PolypropyleneCommodityPlastic1
from .PolypropyleneCommodityOther1 import PolypropyleneCommodityOther1

class AssetClassCommodityPolypropylene3Choice(base_types._BaseFieldType):

	__slots__ = ["_Plstc", "_Othr"]
	@property
	def Plstc(self):
		return self._Plstc

	@Plstc.setter
	def Plstc(self, value):
		self._Plstc = value if type(value) != auto else self.make_default("Plstc")

	@Plstc.deleter
	def Plstc(self):
		del self._Plstc
		self._Plstc = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plstc', type=PolypropyleneCommodityPlastic1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=PolypropyleneCommodityOther1, min=0, max=1, mutex_group=1, array=False),
	))

