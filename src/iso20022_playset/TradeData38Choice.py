from . import base_types
import CollateralMarginNew10
import ReportPeriodActivity1Code

class TradeData38Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_Stat"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if type(value) != auto else self.make_default("DataSetActn")

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = None

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if type(value) != auto else self.make_default("Stat")

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Stat', type=CollateralMarginNew10, min=1, max=None, mutex_group=1, array=True),
	))

