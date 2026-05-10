import base_types
import InterestRateFrequency3Choice
import InterestComputationMethodFormat7
import SecuritiesTransactionPrice14Choice

class FixedRate10(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_DayCnt", "_PmtFrqcy"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def DayCnt(self):
		return self._DayCnt

	@DayCnt.setter
	def DayCnt(self, value):
		self._DayCnt = value if type(value) != auto else self.make_default("DayCnt")

	@DayCnt.deleter
	def DayCnt(self):
		del self._DayCnt
		self._DayCnt = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=SecuritiesTransactionPrice14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCnt', type=InterestComputationMethodFormat7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
	))

