# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatisticsPerCounterparty18Choice
from . import SupplementaryData1

class DerivativesTradeRejectionStatisticalReportV04(base_types._BaseFieldType):

	__slots__ = ["_RjctnSttstcs", "_SplmtryData"]
	@property
	def RjctnSttstcs(self):
		return self._RjctnSttstcs

	@RjctnSttstcs.setter
	def RjctnSttstcs(self, value):
		self._RjctnSttstcs = value if value is not None else base_types.UninitialisedField(self, 'RjctnSttstcs', StatisticsPerCounterparty18Choice, False)

	@RjctnSttstcs.deleter
	def RjctnSttstcs(self):
		del self._RjctnSttstcs
		self._RjctnSttstcs = base_types.UninitialisedField(self, 'RjctnSttstcs', StatisticsPerCounterparty18Choice, False)

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
		base_types.FieldEntry(name='RjctnSttstcs', type=StatisticsPerCounterparty18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))