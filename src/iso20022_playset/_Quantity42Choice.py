from . import base_types
from ._DecimalNumber import DecimalNumber
from ._PercentageRate import PercentageRate

class Quantity42Choice(base_types._BaseFieldType):

	__slots__ = ["_TrfRate", "_TtlUnitsNb"]
	@property
	def TrfRate(self):
		return self._TrfRate

	@TrfRate.setter
	def TrfRate(self, value):
		self._TrfRate = value if type(value) != base_types.auto else self.make_default("TrfRate")

	@TrfRate.deleter
	def TrfRate(self):
		del self._TrfRate
		self._TrfRate = None

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != base_types.auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrfRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

