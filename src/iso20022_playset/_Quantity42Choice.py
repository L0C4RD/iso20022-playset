# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import PercentageRate

class Quantity42Choice(base_types._BaseFieldType):

	__slots__ = ["_TrfRate", "_TtlUnitsNb"]
	@property
	def TrfRate(self):
		return self._TrfRate

	@TrfRate.setter
	def TrfRate(self, value):
		self._TrfRate = value if value is not None else base_types.UninitialisedField(self, 'TrfRate', PercentageRate, False)

	@TrfRate.deleter
	def TrfRate(self):
		del self._TrfRate
		self._TrfRate = base_types.UninitialisedField(self, 'TrfRate', PercentageRate, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrfRate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))