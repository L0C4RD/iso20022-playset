# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InterestComputationMethodFormat7
from . import InterestRateFrequency3Choice
from . import SecuritiesTransactionPrice14Choice

class FixedRate10(base_types._BaseFieldType):

	__slots__ = ["_DayCnt", "_PmtFrqcy", "_Rate"]
	@property
	def DayCnt(self):
		return self._DayCnt

	@DayCnt.setter
	def DayCnt(self, value):
		self._DayCnt = value if value is not None else base_types.UninitialisedField(self, 'DayCnt', InterestComputationMethodFormat7, False)

	@DayCnt.deleter
	def DayCnt(self):
		del self._DayCnt
		self._DayCnt = base_types.UninitialisedField(self, 'DayCnt', InterestComputationMethodFormat7, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateFrequency3Choice, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateFrequency3Choice, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', SecuritiesTransactionPrice14Choice, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', SecuritiesTransactionPrice14Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCnt', type=InterestComputationMethodFormat7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=SecuritiesTransactionPrice14Choice, min=0, max=1, mutex_group=None, array=False),
	))