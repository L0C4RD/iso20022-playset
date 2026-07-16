# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestForOrderStatusReportV05

class SETR_018_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.018.001.05"
		_docname = "setr.018.001.05"

		__slots__ = ["_ReqForOrdrStsRpt"]
		@property
		def ReqForOrdrStsRpt(self):
			return self._ReqForOrdrStsRpt

		@ReqForOrdrStsRpt.setter
		def ReqForOrdrStsRpt(self, value):
			self._ReqForOrdrStsRpt = value if value is not None else base_types.UninitialisedField(self, 'ReqForOrdrStsRpt', RequestForOrderStatusReportV05, False)

		@ReqForOrdrStsRpt.deleter
		def ReqForOrdrStsRpt(self):
			del self._ReqForOrdrStsRpt
			self._ReqForOrdrStsRpt = base_types.UninitialisedField(self, 'ReqForOrdrStsRpt', RequestForOrderStatusReportV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForOrdrStsRpt', type=RequestForOrderStatusReportV05, min=1, max=1, mutex_group=None, array=False),
		))