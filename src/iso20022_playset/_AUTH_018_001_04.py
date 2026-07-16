# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistrationRequestV04

class AUTH_018_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.018.001.04"
		_docname = "auth.018.001.04"

		__slots__ = ["_CtrctRegnReq"]
		@property
		def CtrctRegnReq(self):
			return self._CtrctRegnReq

		@CtrctRegnReq.setter
		def CtrctRegnReq(self, value):
			self._CtrctRegnReq = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnReq', ContractRegistrationRequestV04, False)

		@CtrctRegnReq.deleter
		def CtrctRegnReq(self):
			del self._CtrctRegnReq
			self._CtrctRegnReq = base_types.UninitialisedField(self, 'CtrctRegnReq', ContractRegistrationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnReq', type=ContractRegistrationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))