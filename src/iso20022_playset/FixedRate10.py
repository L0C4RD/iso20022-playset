from . import base_types
from .SecuritiesTransactionPrice14Choice import SecuritiesTransactionPrice14Choice
from .InterestComputationMethodFormat7 import InterestComputationMethodFormat7
from .InterestRateFrequency3Choice import InterestRateFrequency3Choice

class FixedRate10(base_types._BaseFieldType):

	__slots__ = ["_DayCnt", "_Rate", "_PmtFrqcy"]
	@property
	def DayCnt(self):
		return self._DayCnt

	@DayCnt.setter
	def DayCnt(self, value):
		self._DayCnt = value if type(value) != base_types.auto else self.make_default("DayCnt")

	@DayCnt.deleter
	def DayCnt(self):
		del self._DayCnt
		self._DayCnt = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCnt', type=InterestComputationMethodFormat7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=SecuritiesTransactionPrice14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
	))

