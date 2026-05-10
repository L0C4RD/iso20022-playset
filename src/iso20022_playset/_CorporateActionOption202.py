from . import base_types
from .CorporateActionOption43Choice import CorporateActionOption43Choice
from .Quantity55Choice import Quantity55Choice
from .OptionNumber1Choice import OptionNumber1Choice

class CorporateActionOption202(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_OptnTp", "_InstdQty"]
	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if type(value) != base_types.auto else self.make_default("InstdQty")

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption43Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdQty', type=Quantity55Choice, min=1, max=1, mutex_group=None, array=False),
	))

