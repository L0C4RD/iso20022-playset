# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestForOrderConfirmationStatusReportV03 import RequestForOrderConfirmationStatusReportV03

class SETR_058_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.058.001.03"
		_docname = "setr.058.001.03"

		__slots__ = ["_ReqForOrdrConfStsRpt"]
		@property
		def ReqForOrdrConfStsRpt(self):
			return self._ReqForOrdrConfStsRpt

		@ReqForOrdrConfStsRpt.setter
		def ReqForOrdrConfStsRpt(self, value):
			self._ReqForOrdrConfStsRpt = value if type(value) != base_types.auto else self.make_default("ReqForOrdrConfStsRpt")

		@ReqForOrdrConfStsRpt.deleter
		def ReqForOrdrConfStsRpt(self):
			del self._ReqForOrdrConfStsRpt
			self._ReqForOrdrConfStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForOrdrConfStsRpt', type=RequestForOrderConfirmationStatusReportV03, min=1, max=1, mutex_group=None, array=False),
		))