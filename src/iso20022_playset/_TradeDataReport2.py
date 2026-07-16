# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TradeData44

class TradeDataReport2(base_types._BaseFieldType):

	__slots__ = ["_LkdRptId", "_TradData"]
	@property
	def LkdRptId(self):
		return self._LkdRptId

	@LkdRptId.setter
	def LkdRptId(self, value):
		self._LkdRptId = value if value is not None else base_types.UninitialisedField(self, 'LkdRptId', Max35Text, False)

	@LkdRptId.deleter
	def LkdRptId(self):
		del self._LkdRptId
		self._LkdRptId = base_types.UninitialisedField(self, 'LkdRptId', Max35Text, False)

	@property
	def TradData(self):
		return self._TradData

	@TradData.setter
	def TradData(self, value):
		self._TradData = value if value is not None else base_types.UninitialisedField(self, 'TradData', TradeData44, True)

	@TradData.deleter
	def TradData(self):
		del self._TradData
		self._TradData = base_types.UninitialisedField(self, 'TradData', TradeData44, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdRptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradData', type=TradeData44, min=1, max=None, mutex_group=None, array=True),
	))