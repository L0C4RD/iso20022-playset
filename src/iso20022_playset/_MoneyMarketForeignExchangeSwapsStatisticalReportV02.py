# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeSwap3Choice
from . import MoneyMarketReportHeader1
from . import SupplementaryData1

class MoneyMarketForeignExchangeSwapsStatisticalReportV02(base_types._BaseFieldType):

	__slots__ = ["_FXSwpsRpt", "_RptHdr", "_SplmtryData"]
	@property
	def FXSwpsRpt(self):
		return self._FXSwpsRpt

	@FXSwpsRpt.setter
	def FXSwpsRpt(self, value):
		self._FXSwpsRpt = value if value is not None else base_types.UninitialisedField(self, 'FXSwpsRpt', ForeignExchangeSwap3Choice, False)

	@FXSwpsRpt.deleter
	def FXSwpsRpt(self):
		del self._FXSwpsRpt
		self._FXSwpsRpt = base_types.UninitialisedField(self, 'FXSwpsRpt', ForeignExchangeSwap3Choice, False)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', MoneyMarketReportHeader1, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', MoneyMarketReportHeader1, False)

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
		base_types.FieldEntry(name='FXSwpsRpt', type=ForeignExchangeSwap3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=MoneyMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))