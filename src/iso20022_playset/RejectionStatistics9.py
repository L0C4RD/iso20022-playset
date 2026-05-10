import base_types
import DetailedReportStatistics7
import DetailedTransactionStatistics7Choice
import CounterpartyData92

class RejectionStatistics9(base_types._BaseFieldType):

	__slots__ = ["_RptSttstcs", "_CtrPtyId", "_DerivSttstcs"]
	@property
	def RptSttstcs(self):
		return self._RptSttstcs

	@RptSttstcs.setter
	def RptSttstcs(self, value):
		self._RptSttstcs = value if type(value) != auto else self.make_default("RptSttstcs")

	@RptSttstcs.deleter
	def RptSttstcs(self):
		del self._RptSttstcs
		self._RptSttstcs = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def DerivSttstcs(self):
		return self._DerivSttstcs

	@DerivSttstcs.setter
	def DerivSttstcs(self, value):
		self._DerivSttstcs = value if type(value) != auto else self.make_default("DerivSttstcs")

	@DerivSttstcs.deleter
	def DerivSttstcs(self):
		del self._DerivSttstcs
		self._DerivSttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSttstcs', type=DetailedReportStatistics7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivSttstcs', type=DetailedTransactionStatistics7Choice, min=1, max=1, mutex_group=None, array=False),
	))

