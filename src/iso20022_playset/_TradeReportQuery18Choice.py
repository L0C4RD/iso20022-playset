from . import base_types
from ._TradeRecurrentQuery7 import TradeRecurrentQuery7
from ._TradeQueryCriteria14 import TradeQueryCriteria14

class TradeReportQuery18Choice(base_types._BaseFieldType):

	__slots__ = ["_RcrntQry", "_AdHocQry"]
	@property
	def AdHocQry(self):
		return self._AdHocQry

	@AdHocQry.setter
	def AdHocQry(self, value):
		self._AdHocQry = value if type(value) != base_types.auto else self.make_default("AdHocQry")

	@AdHocQry.deleter
	def AdHocQry(self):
		del self._AdHocQry
		self._AdHocQry = None

	@property
	def RcrntQry(self):
		return self._RcrntQry

	@RcrntQry.setter
	def RcrntQry(self, value):
		self._RcrntQry = value if type(value) != base_types.auto else self.make_default("RcrntQry")

	@RcrntQry.deleter
	def RcrntQry(self):
		del self._RcrntQry
		self._RcrntQry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdHocQry', type=TradeQueryCriteria14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcrntQry', type=TradeRecurrentQuery7, min=0, max=1, mutex_group=1, array=False),
	))

