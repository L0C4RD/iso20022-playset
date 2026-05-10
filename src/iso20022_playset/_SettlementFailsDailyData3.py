from . import base_types
from ._ISODate import ISODate
from ._SettlementFailsDailyInstrument3 import SettlementFailsDailyInstrument3

class SettlementFailsDailyData3(base_types._BaseFieldType):

	__slots__ = ["_DalyRcrd", "_RptgDt"]
	@property
	def DalyRcrd(self):
		return self._DalyRcrd

	@DalyRcrd.setter
	def DalyRcrd(self, value):
		self._DalyRcrd = value if type(value) != base_types.auto else self.make_default("DalyRcrd")

	@DalyRcrd.deleter
	def DalyRcrd(self):
		del self._DalyRcrd
		self._DalyRcrd = None

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != base_types.auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DalyRcrd', type=SettlementFailsDailyInstrument3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

