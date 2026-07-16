# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MonthlyResult1
from . import SupplementaryData1

class CCPBackTestingResultReportV01(base_types._BaseFieldType):

	__slots__ = ["_MnthlyRslt", "_SplmtryData"]
	@property
	def MnthlyRslt(self):
		return self._MnthlyRslt

	@MnthlyRslt.setter
	def MnthlyRslt(self, value):
		self._MnthlyRslt = value if value is not None else base_types.UninitialisedField(self, 'MnthlyRslt', MonthlyResult1, True)

	@MnthlyRslt.deleter
	def MnthlyRslt(self):
		del self._MnthlyRslt
		self._MnthlyRslt = base_types.UninitialisedField(self, 'MnthlyRslt', MonthlyResult1, True)

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
		base_types.FieldEntry(name='MnthlyRslt', type=MonthlyResult1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))