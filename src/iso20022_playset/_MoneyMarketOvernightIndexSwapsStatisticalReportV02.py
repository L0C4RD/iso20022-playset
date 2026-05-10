from . import base_types
from ._OvernightIndexSwap4Choice import OvernightIndexSwap4Choice
from ._SupplementaryData1 import SupplementaryData1
from ._MoneyMarketReportHeader1 import MoneyMarketReportHeader1

class MoneyMarketOvernightIndexSwapsStatisticalReportV02(base_types._BaseFieldType):

	__slots__ = ["_RptHdr", "_OvrnghtIndxSwpsRpt", "_SplmtryData"]
	@property
	def OvrnghtIndxSwpsRpt(self):
		return self._OvrnghtIndxSwpsRpt

	@OvrnghtIndxSwpsRpt.setter
	def OvrnghtIndxSwpsRpt(self, value):
		self._OvrnghtIndxSwpsRpt = value if type(value) != base_types.auto else self.make_default("OvrnghtIndxSwpsRpt")

	@OvrnghtIndxSwpsRpt.deleter
	def OvrnghtIndxSwpsRpt(self):
		del self._OvrnghtIndxSwpsRpt
		self._OvrnghtIndxSwpsRpt = None

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != base_types.auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OvrnghtIndxSwpsRpt', type=OvernightIndexSwap4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptHdr', type=MoneyMarketReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

