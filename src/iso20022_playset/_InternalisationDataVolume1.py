from . import base_types
from .Max20PositiveNumber import Max20PositiveNumber
from .Max20PositiveDecimalNumber import Max20PositiveDecimalNumber

class InternalisationDataVolume1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Vol"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if type(value) != base_types.auto else self.make_default("Vol")

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max20PositiveDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
	))

