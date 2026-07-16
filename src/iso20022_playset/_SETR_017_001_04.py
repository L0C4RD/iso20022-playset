# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrderCancellationStatusReportV04

class SETR_017_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.017.001.04"
		_docname = "setr.017.001.04"

		__slots__ = ["_OrdrCxlStsRpt"]
		@property
		def OrdrCxlStsRpt(self):
			return self._OrdrCxlStsRpt

		@OrdrCxlStsRpt.setter
		def OrdrCxlStsRpt(self, value):
			self._OrdrCxlStsRpt = value if value is not None else base_types.UninitialisedField(self, 'OrdrCxlStsRpt', OrderCancellationStatusReportV04, False)

		@OrdrCxlStsRpt.deleter
		def OrdrCxlStsRpt(self):
			del self._OrdrCxlStsRpt
			self._OrdrCxlStsRpt = base_types.UninitialisedField(self, 'OrdrCxlStsRpt', OrderCancellationStatusReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrCxlStsRpt', type=OrderCancellationStatusReportV04, min=1, max=1, mutex_group=None, array=False),
		))