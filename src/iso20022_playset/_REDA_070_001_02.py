# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToPayDebtorActivationRequestV02

class REDA_070_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.070.001.02"
		_docname = "reda.070.001.02"

		__slots__ = ["_ReqToPayDbtrActvtnReq"]
		@property
		def ReqToPayDbtrActvtnReq(self):
			return self._ReqToPayDbtrActvtnReq

		@ReqToPayDbtrActvtnReq.setter
		def ReqToPayDbtrActvtnReq(self, value):
			self._ReqToPayDbtrActvtnReq = value if value is not None else base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnReq', RequestToPayDebtorActivationRequestV02, False)

		@ReqToPayDbtrActvtnReq.deleter
		def ReqToPayDbtrActvtnReq(self):
			del self._ReqToPayDbtrActvtnReq
			self._ReqToPayDbtrActvtnReq = base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnReq', RequestToPayDebtorActivationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnReq', type=RequestToPayDebtorActivationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))