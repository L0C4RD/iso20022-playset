from . import base_types
import DecimalNumber
import PercentageRate

class Quantity42Choice(base_types._BaseFieldType):

	__slots__ = ["_TtlUnitsNb", "_TrfRate"]
	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	@property
	def TrfRate(self):
		return self._TrfRate

	@TrfRate.setter
	def TrfRate(self, value):
		self._TrfRate = value if type(value) != auto else self.make_default("TrfRate")

	@TrfRate.deleter
	def TrfRate(self):
		del self._TrfRate
		self._TrfRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrfRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

