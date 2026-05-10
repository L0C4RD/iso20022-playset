from . import base_types
from ._PositionSetTotal2 import PositionSetTotal2

class PositionSetBuyerAndSeller2(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_Sellr"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != base_types.auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=PositionSetTotal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PositionSetTotal2, min=0, max=1, mutex_group=None, array=False),
	))

