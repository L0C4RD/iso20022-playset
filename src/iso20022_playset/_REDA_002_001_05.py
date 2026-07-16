# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceReportCancellationV05

class REDA_002_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.002.001.05"
		_docname = "reda.002.001.05"

		__slots__ = ["_PricRptCxl"]
		@property
		def PricRptCxl(self):
			return self._PricRptCxl

		@PricRptCxl.setter
		def PricRptCxl(self, value):
			self._PricRptCxl = value if value is not None else base_types.UninitialisedField(self, 'PricRptCxl', PriceReportCancellationV05, False)

		@PricRptCxl.deleter
		def PricRptCxl(self):
			del self._PricRptCxl
			self._PricRptCxl = base_types.UninitialisedField(self, 'PricRptCxl', PriceReportCancellationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PricRptCxl', type=PriceReportCancellationV05, min=1, max=1, mutex_group=None, array=False),
		))