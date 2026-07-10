# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestForTransferStatusReportV09 import RequestForTransferStatusReportV09

class SESE_009_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.009.001.09"
		_docname = "sese.009.001.09"

		__slots__ = ["_ReqForTrfStsRpt"]
		@property
		def ReqForTrfStsRpt(self):
			return self._ReqForTrfStsRpt

		@ReqForTrfStsRpt.setter
		def ReqForTrfStsRpt(self, value):
			self._ReqForTrfStsRpt = value if type(value) != base_types.auto else self.make_default("ReqForTrfStsRpt")

		@ReqForTrfStsRpt.deleter
		def ReqForTrfStsRpt(self):
			del self._ReqForTrfStsRpt
			self._ReqForTrfStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForTrfStsRpt', type=RequestForTransferStatusReportV09, min=1, max=1, mutex_group=None, array=False),
		))