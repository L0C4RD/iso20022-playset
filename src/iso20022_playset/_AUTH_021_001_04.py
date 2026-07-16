# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistrationAmendmentRequestV04

class AUTH_021_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.021.001.04"
		_docname = "auth.021.001.04"

		__slots__ = ["_CtrctRegnAmdmntReq"]
		@property
		def CtrctRegnAmdmntReq(self):
			return self._CtrctRegnAmdmntReq

		@CtrctRegnAmdmntReq.setter
		def CtrctRegnAmdmntReq(self, value):
			self._CtrctRegnAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnAmdmntReq', ContractRegistrationAmendmentRequestV04, False)

		@CtrctRegnAmdmntReq.deleter
		def CtrctRegnAmdmntReq(self):
			del self._CtrctRegnAmdmntReq
			self._CtrctRegnAmdmntReq = base_types.UninitialisedField(self, 'CtrctRegnAmdmntReq', ContractRegistrationAmendmentRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnAmdmntReq', type=ContractRegistrationAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))