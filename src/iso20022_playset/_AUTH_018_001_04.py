# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationRequestV04 import ContractRegistrationRequestV04

class AUTH_018_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.018.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CtrctRegnReq"]
		@property
		def CtrctRegnReq(self):
			return self._CtrctRegnReq

		@CtrctRegnReq.setter
		def CtrctRegnReq(self, value):
			self._CtrctRegnReq = value if type(value) != base_types.auto else self.make_default("CtrctRegnReq")

		@CtrctRegnReq.deleter
		def CtrctRegnReq(self):
			del self._CtrctRegnReq
			self._CtrctRegnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnReq', type=ContractRegistrationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))