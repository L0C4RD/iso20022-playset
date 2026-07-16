# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyData92
from . import DetailedReportStatistics7
from . import DetailedTransactionStatistics7Choice

class RejectionStatistics9(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_DerivSttstcs", "_RptSttstcs"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData92, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData92, False)

	@property
	def DerivSttstcs(self):
		return self._DerivSttstcs

	@DerivSttstcs.setter
	def DerivSttstcs(self, value):
		self._DerivSttstcs = value if value is not None else base_types.UninitialisedField(self, 'DerivSttstcs', DetailedTransactionStatistics7Choice, False)

	@DerivSttstcs.deleter
	def DerivSttstcs(self):
		del self._DerivSttstcs
		self._DerivSttstcs = base_types.UninitialisedField(self, 'DerivSttstcs', DetailedTransactionStatistics7Choice, False)

	@property
	def RptSttstcs(self):
		return self._RptSttstcs

	@RptSttstcs.setter
	def RptSttstcs(self, value):
		self._RptSttstcs = value if value is not None else base_types.UninitialisedField(self, 'RptSttstcs', DetailedReportStatistics7, False)

	@RptSttstcs.deleter
	def RptSttstcs(self):
		del self._RptSttstcs
		self._RptSttstcs = base_types.UninitialisedField(self, 'RptSttstcs', DetailedReportStatistics7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivSttstcs', type=DetailedTransactionStatistics7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSttstcs', type=DetailedReportStatistics7, min=1, max=1, mutex_group=None, array=False),
	))