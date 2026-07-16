# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeStatusReportV01

class TSRV_018_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.018.001.01"
		_docname = "tsrv.018.001.01"

		__slots__ = ["_TradStsRpt"]
		@property
		def TradStsRpt(self):
			return self._TradStsRpt

		@TradStsRpt.setter
		def TradStsRpt(self, value):
			self._TradStsRpt = value if value is not None else base_types.UninitialisedField(self, 'TradStsRpt', TradeStatusReportV01, False)

		@TradStsRpt.deleter
		def TradStsRpt(self):
			del self._TradStsRpt
			self._TradStsRpt = base_types.UninitialisedField(self, 'TradStsRpt', TradeStatusReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradStsRpt', type=TradeStatusReportV01, min=1, max=1, mutex_group=None, array=False),
		))