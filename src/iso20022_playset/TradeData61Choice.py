from . import base_types
import TradeReport34Choice
import ReportPeriodActivity1Code

class TradeData61Choice(base_types._BaseFieldType):

	__slots__ = ["_Rpt", "_DataSetActn"]
	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rpt', type=TradeReport34Choice, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
	))

