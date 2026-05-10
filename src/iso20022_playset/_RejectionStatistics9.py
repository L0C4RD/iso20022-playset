from . import base_types
from ._DetailedReportStatistics7 import DetailedReportStatistics7
from ._DetailedTransactionStatistics7Choice import DetailedTransactionStatistics7Choice
from ._CounterpartyData92 import CounterpartyData92

class RejectionStatistics9(base_types._BaseFieldType):

	__slots__ = ["_DerivSttstcs", "_RptSttstcs", "_CtrPtyId"]
	@property
	def DerivSttstcs(self):
		return self._DerivSttstcs

	@DerivSttstcs.setter
	def DerivSttstcs(self, value):
		self._DerivSttstcs = value if type(value) != base_types.auto else self.make_default("DerivSttstcs")

	@DerivSttstcs.deleter
	def DerivSttstcs(self):
		del self._DerivSttstcs
		self._DerivSttstcs = None

	@property
	def RptSttstcs(self):
		return self._RptSttstcs

	@RptSttstcs.setter
	def RptSttstcs(self, value):
		self._RptSttstcs = value if type(value) != base_types.auto else self.make_default("RptSttstcs")

	@RptSttstcs.deleter
	def RptSttstcs(self):
		del self._RptSttstcs
		self._RptSttstcs = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != base_types.auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivSttstcs', type=DetailedTransactionStatistics7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSttstcs', type=DetailedReportStatistics7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
	))

