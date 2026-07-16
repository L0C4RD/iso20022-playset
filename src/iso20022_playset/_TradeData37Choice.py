# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportPeriodActivity1Code
from . import ReuseDataReportCorrection15

class TradeData37Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_Stat"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if value is not None else base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity1Code, False)

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity1Code, False)

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if value is not None else base_types.UninitialisedField(self, 'Stat', ReuseDataReportCorrection15, True)

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = base_types.UninitialisedField(self, 'Stat', ReuseDataReportCorrection15, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Stat', type=ReuseDataReportCorrection15, min=1, max=None, mutex_group=1, array=True),
	))