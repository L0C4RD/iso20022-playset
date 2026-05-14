# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatisticsPerCounterparty16Choice import StatisticsPerCounterparty16Choice
from ._SupplementaryData1 import SupplementaryData1

class DerivativesTradeWarningsReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_WrnngsSttstcs"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def WrnngsSttstcs(self):
		return self._WrnngsSttstcs

	@WrnngsSttstcs.setter
	def WrnngsSttstcs(self, value):
		self._WrnngsSttstcs = value if type(value) != base_types.auto else self.make_default("WrnngsSttstcs")

	@WrnngsSttstcs.deleter
	def WrnngsSttstcs(self):
		del self._WrnngsSttstcs
		self._WrnngsSttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WrnngsSttstcs', type=StatisticsPerCounterparty16Choice, min=1, max=1, mutex_group=None, array=False),
	))