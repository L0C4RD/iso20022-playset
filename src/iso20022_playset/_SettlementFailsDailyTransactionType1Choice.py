# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportPeriodActivity1Code
from . import SettlementFailsDailyTransactionType3

class SettlementFailsDailyTransactionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Data", "_DataSetActn"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', SettlementFailsDailyTransactionType3, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', SettlementFailsDailyTransactionType3, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=SettlementFailsDailyTransactionType3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
	))