from . import base_types
import TradeRecurrentQuery5
import TradeQueryCriteria10

class TradeReportQuery13Choice(base_types._BaseFieldType):

	__slots__ = ["_RcrntQry", "_AdHocQry"]
	@property
	def RcrntQry(self):
		return self._RcrntQry

	@RcrntQry.setter
	def RcrntQry(self, value):
		self._RcrntQry = value if type(value) != auto else self.make_default("RcrntQry")

	@RcrntQry.deleter
	def RcrntQry(self):
		del self._RcrntQry
		self._RcrntQry = None

	@property
	def AdHocQry(self):
		return self._AdHocQry

	@AdHocQry.setter
	def AdHocQry(self, value):
		self._AdHocQry = value if type(value) != auto else self.make_default("AdHocQry")

	@AdHocQry.deleter
	def AdHocQry(self):
		del self._AdHocQry
		self._AdHocQry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcrntQry', type=TradeRecurrentQuery5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AdHocQry', type=TradeQueryCriteria10, min=0, max=1, mutex_group=1, array=False),
	))

