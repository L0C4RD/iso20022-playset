from . import base_types
from .UnitOfMeasure3Choice import UnitOfMeasure3Choice
from .DecimalNumber import DecimalNumber

class Quantity10(base_types._BaseFieldType):

	__slots__ = ["_UnitOfMeasr", "_Val"]
	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

