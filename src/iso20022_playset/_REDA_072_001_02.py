# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToPayDebtorActivationCancellationRequestV02

class REDA_072_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.072.001.02"
		_docname = "reda.072.001.02"

		__slots__ = ["_ReqToPayDbtrActvtnCxlReq"]
		@property
		def ReqToPayDbtrActvtnCxlReq(self):
			return self._ReqToPayDbtrActvtnCxlReq

		@ReqToPayDbtrActvtnCxlReq.setter
		def ReqToPayDbtrActvtnCxlReq(self, value):
			self._ReqToPayDbtrActvtnCxlReq = value if value is not None else base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnCxlReq', RequestToPayDebtorActivationCancellationRequestV02, False)

		@ReqToPayDbtrActvtnCxlReq.deleter
		def ReqToPayDbtrActvtnCxlReq(self):
			del self._ReqToPayDbtrActvtnCxlReq
			self._ReqToPayDbtrActvtnCxlReq = base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnCxlReq', RequestToPayDebtorActivationCancellationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnCxlReq', type=RequestToPayDebtorActivationCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))