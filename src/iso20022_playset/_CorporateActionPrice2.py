from . import base_types
from ._PriceFormat3Choice import PriceFormat3Choice

class CorporateActionPrice2(base_types._BaseFieldType):

	__slots__ = ["_MinPric", "_MaxPric"]
	@property
	def MaxPric(self):
		return self._MaxPric

	@MaxPric.setter
	def MaxPric(self, value):
		self._MaxPric = value if type(value) != base_types.auto else self.make_default("MaxPric")

	@MaxPric.deleter
	def MaxPric(self):
		del self._MaxPric
		self._MaxPric = None

	@property
	def MinPric(self):
		return self._MinPric

	@MinPric.setter
	def MinPric(self, value):
		self._MinPric = value if type(value) != base_types.auto else self.make_default("MinPric")

	@MinPric.deleter
	def MinPric(self):
		del self._MinPric
		self._MinPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxPric', type=PriceFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPric', type=PriceFormat3Choice, min=0, max=1, mutex_group=None, array=False),
	))

