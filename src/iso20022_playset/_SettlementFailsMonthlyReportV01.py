# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsDailyData3
from . import SettlementFailsData3
from . import SettlementFailsReportHeader2
from . import SupplementaryData1

class SettlementFailsMonthlyReportV01(base_types._BaseFieldType):

	__slots__ = ["_DalyData", "_MnthlyAggt", "_RptHdr", "_SplmtryData"]
	@property
	def DalyData(self):
		return self._DalyData

	@DalyData.setter
	def DalyData(self, value):
		self._DalyData = value if value is not None else base_types.UninitialisedField(self, 'DalyData', SettlementFailsDailyData3, True)

	@DalyData.deleter
	def DalyData(self):
		del self._DalyData
		self._DalyData = base_types.UninitialisedField(self, 'DalyData', SettlementFailsDailyData3, True)

	@property
	def MnthlyAggt(self):
		return self._MnthlyAggt

	@MnthlyAggt.setter
	def MnthlyAggt(self, value):
		self._MnthlyAggt = value if value is not None else base_types.UninitialisedField(self, 'MnthlyAggt', SettlementFailsData3, False)

	@MnthlyAggt.deleter
	def MnthlyAggt(self):
		del self._MnthlyAggt
		self._MnthlyAggt = base_types.UninitialisedField(self, 'MnthlyAggt', SettlementFailsData3, False)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', SettlementFailsReportHeader2, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', SettlementFailsReportHeader2, False)

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
		base_types.FieldEntry(name='DalyData', type=SettlementFailsDailyData3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MnthlyAggt', type=SettlementFailsData3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=SettlementFailsReportHeader2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))