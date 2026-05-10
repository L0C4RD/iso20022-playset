from . import base_types
from ._TradeStateReport23 import TradeStateReport23
from ._ReportPeriodActivity1Code import ReportPeriodActivity1Code

class TradeData60Choice(base_types._BaseFieldType):

	__slots__ = ["_Stat", "_DataSetActn"]
	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if type(value) != base_types.auto else self.make_default("Stat")

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Stat', type=TradeStateReport23, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
	))

