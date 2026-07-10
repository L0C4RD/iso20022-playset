# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PriceReportV04 import PriceReportV04

class REDA_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.001.001.04"
		_docname = "reda.001.001.04"

		__slots__ = ["_PricRpt"]
		@property
		def PricRpt(self):
			return self._PricRpt

		@PricRpt.setter
		def PricRpt(self, value):
			self._PricRpt = value if type(value) != base_types.auto else self.make_default("PricRpt")

		@PricRpt.deleter
		def PricRpt(self):
			del self._PricRpt
			self._PricRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PricRpt', type=PriceReportV04, min=1, max=1, mutex_group=None, array=False),
		))