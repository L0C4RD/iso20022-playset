from . import base_types
from .SettlementFailsDailyCSD3 import SettlementFailsDailyCSD3
from .ReportPeriodActivity1Code import ReportPeriodActivity1Code

class SettlementFailsDailyCSD1Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_Data"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if type(value) != base_types.auto else self.make_default("DataSetActn")

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Data', type=SettlementFailsDailyCSD3, min=0, max=1, mutex_group=1, array=False),
	))

