from . import base_types
from .UnitOfMeasure5Choice import UnitOfMeasure5Choice
from .PositiveNumber import PositiveNumber

class ContractSize1(base_types._BaseFieldType):

	__slots__ = ["_Unit", "_LotSz"]
	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	@property
	def LotSz(self):
		return self._LotSz

	@LotSz.setter
	def LotSz(self, value):
		self._LotSz = value if type(value) != base_types.auto else self.make_default("LotSz")

	@LotSz.deleter
	def LotSz(self):
		del self._LotSz
		self._LotSz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Unit', type=UnitOfMeasure5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotSz', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
	))

