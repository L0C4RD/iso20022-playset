# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToPayCreditorEnrolmentRequestV02

class REDA_066_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.066.001.02"
		_docname = "reda.066.001.02"

		__slots__ = ["_ReqToPayCdtrEnrlmntReq"]
		@property
		def ReqToPayCdtrEnrlmntReq(self):
			return self._ReqToPayCdtrEnrlmntReq

		@ReqToPayCdtrEnrlmntReq.setter
		def ReqToPayCdtrEnrlmntReq(self, value):
			self._ReqToPayCdtrEnrlmntReq = value if value is not None else base_types.UninitialisedField(self, 'ReqToPayCdtrEnrlmntReq', RequestToPayCreditorEnrolmentRequestV02, False)

		@ReqToPayCdtrEnrlmntReq.deleter
		def ReqToPayCdtrEnrlmntReq(self):
			del self._ReqToPayCdtrEnrlmntReq
			self._ReqToPayCdtrEnrlmntReq = base_types.UninitialisedField(self, 'ReqToPayCdtrEnrlmntReq', RequestToPayCreditorEnrolmentRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntReq', type=RequestToPayCreditorEnrolmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))