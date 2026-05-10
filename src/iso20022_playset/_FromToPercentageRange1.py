from . import base_types
from ._PercentageRangeBoundary1 import PercentageRangeBoundary1

class FromToPercentageRange1(base_types._BaseFieldType):

	__slots__ = ["_To", "_Fr"]
	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != base_types.auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if type(value) != base_types.auto else self.make_default("To")

	@To.deleter
	def To(self):
		del self._To
		self._To = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fr', type=PercentageRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=PercentageRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
	))

