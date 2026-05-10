from . import base_types
from .PercentageRate import PercentageRate
from .PercentageRangeBoundary1 import PercentageRangeBoundary1
from .FromToPercentageRange1 import FromToPercentageRange1

class PercentageRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_FrTo", "_Fr", "_NEQ", "_EQ", "_To"]
	@property
	def FrTo(self):
		return self._FrTo

	@FrTo.setter
	def FrTo(self, value):
		self._FrTo = value if type(value) != base_types.auto else self.make_default("FrTo")

	@FrTo.deleter
	def FrTo(self):
		del self._FrTo
		self._FrTo = None

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
	def NEQ(self):
		return self._NEQ

	@NEQ.setter
	def NEQ(self, value):
		self._NEQ = value if type(value) != base_types.auto else self.make_default("NEQ")

	@NEQ.deleter
	def NEQ(self):
		del self._NEQ
		self._NEQ = None

	@property
	def EQ(self):
		return self._EQ

	@EQ.setter
	def EQ(self, value):
		self._EQ = value if type(value) != base_types.auto else self.make_default("EQ")

	@EQ.deleter
	def EQ(self):
		del self._EQ
		self._EQ = None

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
		base_types.FieldEntry(name='FrTo', type=FromToPercentageRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fr', type=PercentageRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQ', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EQ', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='To', type=PercentageRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
	))

