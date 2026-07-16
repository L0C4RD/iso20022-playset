# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatisticsPerCounterparty16Choice
from . import SupplementaryData1

class DerivativesTradeWarningsReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_WrnngsSttstcs"]
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

	@property
	def WrnngsSttstcs(self):
		return self._WrnngsSttstcs

	@WrnngsSttstcs.setter
	def WrnngsSttstcs(self, value):
		self._WrnngsSttstcs = value if value is not None else base_types.UninitialisedField(self, 'WrnngsSttstcs', StatisticsPerCounterparty16Choice, False)

	@WrnngsSttstcs.deleter
	def WrnngsSttstcs(self):
		del self._WrnngsSttstcs
		self._WrnngsSttstcs = base_types.UninitialisedField(self, 'WrnngsSttstcs', StatisticsPerCounterparty16Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WrnngsSttstcs', type=StatisticsPerCounterparty16Choice, min=1, max=1, mutex_group=None, array=False),
	))