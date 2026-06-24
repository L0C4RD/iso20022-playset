# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TradeStatusReportV01 import TradeStatusReportV01

class TSRV_018_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.018.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TradStsRpt"]
		@property
		def TradStsRpt(self):
			return self._TradStsRpt

		@TradStsRpt.setter
		def TradStsRpt(self, value):
			self._TradStsRpt = value if type(value) != base_types.auto else self.make_default("TradStsRpt")

		@TradStsRpt.deleter
		def TradStsRpt(self):
			del self._TradStsRpt
			self._TradStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradStsRpt', type=TradeStatusReportV01, min=1, max=1, mutex_group=None, array=False),
		))