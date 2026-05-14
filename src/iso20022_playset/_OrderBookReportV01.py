# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._OrderReport2Choice import OrderReport2Choice
from ._SecuritiesMarketReportHeader3 import SecuritiesMarketReportHeader3
from ._SupplementaryData1 import SupplementaryData1

class OrderBookReportV01(base_types._BaseFieldType):

	__slots__ = ["_OrdrRpt", "_RptHdr", "_SplmtryData"]
	@property
	def OrdrRpt(self):
		return self._OrdrRpt

	@OrdrRpt.setter
	def OrdrRpt(self, value):
		self._OrdrRpt = value if type(value) != base_types.auto else self.make_default("OrdrRpt")

	@OrdrRpt.deleter
	def OrdrRpt(self):
		del self._OrdrRpt
		self._OrdrRpt = None

	@property
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != base_types.auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRpt', type=OrderReport2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=SecuritiesMarketReportHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))