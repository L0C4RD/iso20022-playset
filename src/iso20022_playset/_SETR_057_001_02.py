# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrderConfirmationStatusReportV02

class SETR_057_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.057.001.02"
		_docname = "setr.057.001.02"

		__slots__ = ["_OrdrConfStsRpt"]
		@property
		def OrdrConfStsRpt(self):
			return self._OrdrConfStsRpt

		@OrdrConfStsRpt.setter
		def OrdrConfStsRpt(self, value):
			self._OrdrConfStsRpt = value if value is not None else base_types.UninitialisedField(self, 'OrdrConfStsRpt', OrderConfirmationStatusReportV02, False)

		@OrdrConfStsRpt.deleter
		def OrdrConfStsRpt(self):
			del self._OrdrConfStsRpt
			self._OrdrConfStsRpt = base_types.UninitialisedField(self, 'OrdrConfStsRpt', OrderConfirmationStatusReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrConfStsRpt', type=OrderConfirmationStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))