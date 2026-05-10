from . import base_types
from ._Max35Text import Max35Text
from ._TradeData44 import TradeData44

class TradeDataReport2(base_types._BaseFieldType):

	__slots__ = ["_LkdRptId", "_TradData"]
	@property
	def LkdRptId(self):
		return self._LkdRptId

	@LkdRptId.setter
	def LkdRptId(self, value):
		self._LkdRptId = value if type(value) != base_types.auto else self.make_default("LkdRptId")

	@LkdRptId.deleter
	def LkdRptId(self):
		del self._LkdRptId
		self._LkdRptId = None

	@property
	def TradData(self):
		return self._TradData

	@TradData.setter
	def TradData(self, value):
		self._TradData = value if type(value) != base_types.auto else self.make_default("TradData")

	@TradData.deleter
	def TradData(self):
		del self._TradData
		self._TradData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdRptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradData', type=TradeData44, min=1, max=None, mutex_group=None, array=True),
	))

