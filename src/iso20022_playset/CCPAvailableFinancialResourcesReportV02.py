from . import base_types
from .AvailableFinancialResourcesAmount2 import AvailableFinancialResourcesAmount2
from .ReportingAssetBreakdown2 import ReportingAssetBreakdown2
from .SupplementaryData1 import SupplementaryData1

class CCPAvailableFinancialResourcesReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_AvlblFinRsrcsAmt", "_OthrPrfnddRsrcs"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def AvlblFinRsrcsAmt(self):
		return self._AvlblFinRsrcsAmt

	@AvlblFinRsrcsAmt.setter
	def AvlblFinRsrcsAmt(self, value):
		self._AvlblFinRsrcsAmt = value if type(value) != auto else self.make_default("AvlblFinRsrcsAmt")

	@AvlblFinRsrcsAmt.deleter
	def AvlblFinRsrcsAmt(self):
		del self._AvlblFinRsrcsAmt
		self._AvlblFinRsrcsAmt = None

	@property
	def OthrPrfnddRsrcs(self):
		return self._OthrPrfnddRsrcs

	@OthrPrfnddRsrcs.setter
	def OthrPrfnddRsrcs(self, value):
		self._OthrPrfnddRsrcs = value if type(value) != auto else self.make_default("OthrPrfnddRsrcs")

	@OthrPrfnddRsrcs.deleter
	def OthrPrfnddRsrcs(self):
		del self._OthrPrfnddRsrcs
		self._OthrPrfnddRsrcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AvlblFinRsrcsAmt', type=AvailableFinancialResourcesAmount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrfnddRsrcs', type=ReportingAssetBreakdown2, min=0, max=1, mutex_group=None, array=False),
	))

