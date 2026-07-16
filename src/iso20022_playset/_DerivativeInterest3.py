# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import FloatingInterestRate8
from . import InterestRate8Choice

class DerivativeInterest3(base_types._BaseFieldType):

	__slots__ = ["_FrstLegIntrstRate", "_IntrstRate", "_OthrLegIntrstRate", "_OthrNtnlCcy"]
	@property
	def FrstLegIntrstRate(self):
		return self._FrstLegIntrstRate

	@FrstLegIntrstRate.setter
	def FrstLegIntrstRate(self, value):
		self._FrstLegIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'FrstLegIntrstRate', InterestRate8Choice, False)

	@FrstLegIntrstRate.deleter
	def FrstLegIntrstRate(self):
		del self._FrstLegIntrstRate
		self._FrstLegIntrstRate = base_types.UninitialisedField(self, 'FrstLegIntrstRate', InterestRate8Choice, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', FloatingInterestRate8, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', FloatingInterestRate8, False)

	@property
	def OthrLegIntrstRate(self):
		return self._OthrLegIntrstRate

	@OthrLegIntrstRate.setter
	def OthrLegIntrstRate(self, value):
		self._OthrLegIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'OthrLegIntrstRate', InterestRate8Choice, False)

	@OthrLegIntrstRate.deleter
	def OthrLegIntrstRate(self):
		del self._OthrLegIntrstRate
		self._OthrLegIntrstRate = base_types.UninitialisedField(self, 'OthrLegIntrstRate', InterestRate8Choice, False)

	@property
	def OthrNtnlCcy(self):
		return self._OthrNtnlCcy

	@OthrNtnlCcy.setter
	def OthrNtnlCcy(self, value):
		self._OthrNtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'OthrNtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@OthrNtnlCcy.deleter
	def OthrNtnlCcy(self):
		del self._OthrNtnlCcy
		self._OthrNtnlCcy = base_types.UninitialisedField(self, 'OthrNtnlCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstLegIntrstRate', type=InterestRate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=FloatingInterestRate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrLegIntrstRate', type=InterestRate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))