# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrderReport2Choice
from . import SecuritiesMarketReportHeader3
from . import SupplementaryData1

class OrderBookReportV01(base_types._BaseFieldType):

	__slots__ = ["_OrdrRpt", "_RptHdr", "_SplmtryData"]
	@property
	def OrdrRpt(self):
		return self._OrdrRpt

	@OrdrRpt.setter
	def OrdrRpt(self, value):
		self._OrdrRpt = value if value is not None else base_types.UninitialisedField(self, 'OrdrRpt', OrderReport2Choice, True)

	@OrdrRpt.deleter
	def OrdrRpt(self):
		del self._OrdrRpt
		self._OrdrRpt = base_types.UninitialisedField(self, 'OrdrRpt', OrderReport2Choice, True)

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if value is not None else base_types.UninitialisedField(self, 'RptHdr', SecuritiesMarketReportHeader3, False)

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = base_types.UninitialisedField(self, 'RptHdr', SecuritiesMarketReportHeader3, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRpt', type=OrderReport2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))