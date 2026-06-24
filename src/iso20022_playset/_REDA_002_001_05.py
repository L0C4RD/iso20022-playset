# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PriceReportCancellationV05 import PriceReportCancellationV05

class REDA_002_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.002.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_PricRptCxl"]
		@property
		def PricRptCxl(self):
			return self._PricRptCxl

		@PricRptCxl.setter
		def PricRptCxl(self, value):
			self._PricRptCxl = value if type(value) != base_types.auto else self.make_default("PricRptCxl")

		@PricRptCxl.deleter
		def PricRptCxl(self):
			del self._PricRptCxl
			self._PricRptCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PricRptCxl', type=PriceReportCancellationV05, min=1, max=1, mutex_group=None, array=False),
		))