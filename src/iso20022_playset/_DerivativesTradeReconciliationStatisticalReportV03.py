# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatisticsPerCounterparty19Choice
from . import SupplementaryData1

class DerivativesTradeReconciliationStatisticalReportV03(base_types._BaseFieldType):

	__slots__ = ["_RcncltnSttstcs", "_SplmtryData"]
	@property
	def RcncltnSttstcs(self):
		return self._RcncltnSttstcs

	@RcncltnSttstcs.setter
	def RcncltnSttstcs(self, value):
		self._RcncltnSttstcs = value if value is not None else base_types.UninitialisedField(self, 'RcncltnSttstcs', StatisticsPerCounterparty19Choice, False)

	@RcncltnSttstcs.deleter
	def RcncltnSttstcs(self):
		del self._RcncltnSttstcs
		self._RcncltnSttstcs = base_types.UninitialisedField(self, 'RcncltnSttstcs', StatisticsPerCounterparty19Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnSttstcs', type=StatisticsPerCounterparty19Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))