from . import base_types
from ._DetailedTransactionStatistics30 import DetailedTransactionStatistics30
from ._ReportPeriodActivity1Code import ReportPeriodActivity1Code

class DetailedTransactionStatistics7Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_DtldSttstcs"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if type(value) != base_types.auto else self.make_default("DataSetActn")

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = None

	@property
	def DtldSttstcs(self):
		return self._DtldSttstcs

	@DtldSttstcs.setter
	def DtldSttstcs(self, value):
		self._DtldSttstcs = value if type(value) != base_types.auto else self.make_default("DtldSttstcs")

	@DtldSttstcs.deleter
	def DtldSttstcs(self):
		del self._DtldSttstcs
		self._DtldSttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtldSttstcs', type=DetailedTransactionStatistics30, min=0, max=1, mutex_group=1, array=False),
	))

