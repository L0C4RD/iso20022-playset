# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToPayDebtorActivationAmendmentRequestV02

class REDA_071_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.071.001.02"
		_docname = "reda.071.001.02"

		__slots__ = ["_ReqToPayDbtrActvtnAmdmntReq"]
		@property
		def ReqToPayDbtrActvtnAmdmntReq(self):
			return self._ReqToPayDbtrActvtnAmdmntReq

		@ReqToPayDbtrActvtnAmdmntReq.setter
		def ReqToPayDbtrActvtnAmdmntReq(self, value):
			self._ReqToPayDbtrActvtnAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnAmdmntReq', RequestToPayDebtorActivationAmendmentRequestV02, False)

		@ReqToPayDbtrActvtnAmdmntReq.deleter
		def ReqToPayDbtrActvtnAmdmntReq(self):
			del self._ReqToPayDbtrActvtnAmdmntReq
			self._ReqToPayDbtrActvtnAmdmntReq = base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnAmdmntReq', RequestToPayDebtorActivationAmendmentRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnAmdmntReq', type=RequestToPayDebtorActivationAmendmentRequestV02, min=1, max=1, mutex_group=None, array=False),
		))