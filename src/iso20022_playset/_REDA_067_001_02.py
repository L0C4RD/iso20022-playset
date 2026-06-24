# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestToPayCreditorEnrolmentAmendmentRequestV02 import RequestToPayCreditorEnrolmentAmendmentRequestV02

class REDA_067_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.067.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ReqToPayCdtrEnrlmntAmdmntReq"]
		@property
		def ReqToPayCdtrEnrlmntAmdmntReq(self):
			return self._ReqToPayCdtrEnrlmntAmdmntReq

		@ReqToPayCdtrEnrlmntAmdmntReq.setter
		def ReqToPayCdtrEnrlmntAmdmntReq(self, value):
			self._ReqToPayCdtrEnrlmntAmdmntReq = value if type(value) != base_types.auto else self.make_default("ReqToPayCdtrEnrlmntAmdmntReq")

		@ReqToPayCdtrEnrlmntAmdmntReq.deleter
		def ReqToPayCdtrEnrlmntAmdmntReq(self):
			del self._ReqToPayCdtrEnrlmntAmdmntReq
			self._ReqToPayCdtrEnrlmntAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntAmdmntReq', type=RequestToPayCreditorEnrolmentAmendmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))