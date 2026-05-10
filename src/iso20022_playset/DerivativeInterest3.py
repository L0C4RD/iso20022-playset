from . import base_types
from .FloatingInterestRate8 import FloatingInterestRate8
from .InterestRate8Choice import InterestRate8Choice
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class DerivativeInterest3(base_types._BaseFieldType):

	__slots__ = ["_IntrstRate", "_FrstLegIntrstRate", "_OthrNtnlCcy", "_OthrLegIntrstRate"]
	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def FrstLegIntrstRate(self):
		return self._FrstLegIntrstRate

	@FrstLegIntrstRate.setter
	def FrstLegIntrstRate(self, value):
		self._FrstLegIntrstRate = value if type(value) != base_types.auto else self.make_default("FrstLegIntrstRate")

	@FrstLegIntrstRate.deleter
	def FrstLegIntrstRate(self):
		del self._FrstLegIntrstRate
		self._FrstLegIntrstRate = None

	@property
	def OthrNtnlCcy(self):
		return self._OthrNtnlCcy

	@OthrNtnlCcy.setter
	def OthrNtnlCcy(self, value):
		self._OthrNtnlCcy = value if type(value) != base_types.auto else self.make_default("OthrNtnlCcy")

	@OthrNtnlCcy.deleter
	def OthrNtnlCcy(self):
		del self._OthrNtnlCcy
		self._OthrNtnlCcy = None

	@property
	def OthrLegIntrstRate(self):
		return self._OthrLegIntrstRate

	@OthrLegIntrstRate.setter
	def OthrLegIntrstRate(self, value):
		self._OthrLegIntrstRate = value if type(value) != base_types.auto else self.make_default("OthrLegIntrstRate")

	@OthrLegIntrstRate.deleter
	def OthrLegIntrstRate(self):
		del self._OthrLegIntrstRate
		self._OthrLegIntrstRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstRate', type=FloatingInterestRate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstLegIntrstRate', type=InterestRate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrLegIntrstRate', type=InterestRate8Choice, min=0, max=1, mutex_group=None, array=False),
	))

