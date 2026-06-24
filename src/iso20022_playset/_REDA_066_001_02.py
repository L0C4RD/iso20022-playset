# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RequestToPayCreditorEnrolmentRequestV02 import RequestToPayCreditorEnrolmentRequestV02

class REDA_066_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.066.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ReqToPayCdtrEnrlmntReq"]
		@property
		def ReqToPayCdtrEnrlmntReq(self):
			return self._ReqToPayCdtrEnrlmntReq

		@ReqToPayCdtrEnrlmntReq.setter
		def ReqToPayCdtrEnrlmntReq(self, value):
			self._ReqToPayCdtrEnrlmntReq = value if type(value) != base_types.auto else self.make_default("ReqToPayCdtrEnrlmntReq")

		@ReqToPayCdtrEnrlmntReq.deleter
		def ReqToPayCdtrEnrlmntReq(self):
			del self._ReqToPayCdtrEnrlmntReq
			self._ReqToPayCdtrEnrlmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayCdtrEnrlmntReq', type=RequestToPayCreditorEnrolmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))