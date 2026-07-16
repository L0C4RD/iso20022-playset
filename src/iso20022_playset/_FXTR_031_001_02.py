# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeCaptureReportV02

class FXTR_031_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.031.001.02"
		_docname = "fxtr.031.001.02"

		__slots__ = ["_FXTradCaptrRpt"]
		@property
		def FXTradCaptrRpt(self):
			return self._FXTradCaptrRpt

		@FXTradCaptrRpt.setter
		def FXTradCaptrRpt(self, value):
			self._FXTradCaptrRpt = value if value is not None else base_types.UninitialisedField(self, 'FXTradCaptrRpt', ForeignExchangeTradeCaptureReportV02, False)

		@FXTradCaptrRpt.deleter
		def FXTradCaptrRpt(self):
			del self._FXTradCaptrRpt
			self._FXTradCaptrRpt = base_types.UninitialisedField(self, 'FXTradCaptrRpt', ForeignExchangeTradeCaptureReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRpt', type=ForeignExchangeTradeCaptureReportV02, min=1, max=1, mutex_group=None, array=False),
		))