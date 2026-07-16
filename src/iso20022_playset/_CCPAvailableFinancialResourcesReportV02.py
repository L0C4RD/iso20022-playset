# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AvailableFinancialResourcesAmount2
from . import ReportingAssetBreakdown2
from . import SupplementaryData1

class CCPAvailableFinancialResourcesReportV02(base_types._BaseFieldType):

	__slots__ = ["_AvlblFinRsrcsAmt", "_OthrPrfnddRsrcs", "_SplmtryData"]
	@property
	def AvlblFinRsrcsAmt(self):
		return self._AvlblFinRsrcsAmt

	@AvlblFinRsrcsAmt.setter
	def AvlblFinRsrcsAmt(self, value):
		self._AvlblFinRsrcsAmt = value if value is not None else base_types.UninitialisedField(self, 'AvlblFinRsrcsAmt', AvailableFinancialResourcesAmount2, False)

	@AvlblFinRsrcsAmt.deleter
	def AvlblFinRsrcsAmt(self):
		del self._AvlblFinRsrcsAmt
		self._AvlblFinRsrcsAmt = base_types.UninitialisedField(self, 'AvlblFinRsrcsAmt', AvailableFinancialResourcesAmount2, False)

	@property
	def OthrPrfnddRsrcs(self):
		return self._OthrPrfnddRsrcs

	@OthrPrfnddRsrcs.setter
	def OthrPrfnddRsrcs(self, value):
		self._OthrPrfnddRsrcs = value if value is not None else base_types.UninitialisedField(self, 'OthrPrfnddRsrcs', ReportingAssetBreakdown2, False)

	@OthrPrfnddRsrcs.deleter
	def OthrPrfnddRsrcs(self):
		del self._OthrPrfnddRsrcs
		self._OthrPrfnddRsrcs = base_types.UninitialisedField(self, 'OthrPrfnddRsrcs', ReportingAssetBreakdown2, False)

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
		base_types.FieldEntry(name='AvlblFinRsrcsAmt', type=AvailableFinancialResourcesAmount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrfnddRsrcs', type=ReportingAssetBreakdown2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))