from . import base_types
from ._PolypropyleneCommodityPlastic1 import PolypropyleneCommodityPlastic1

class AssetClassCommodityPolypropylene1Choice(base_types._BaseFieldType):

	__slots__ = ["_Plstc"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plstc', type=PolypropyleneCommodityPlastic1, min=0, max=1, mutex_group=1, array=False),
	))

