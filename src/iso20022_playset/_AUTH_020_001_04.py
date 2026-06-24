# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationClosureRequestV04 import ContractRegistrationClosureRequestV04

class AUTH_020_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.020.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CtrctRegnClsrReq"]
		@property
		def CtrctRegnClsrReq(self):
			return self._CtrctRegnClsrReq

		@CtrctRegnClsrReq.setter
		def CtrctRegnClsrReq(self, value):
			self._CtrctRegnClsrReq = value if type(value) != base_types.auto else self.make_default("CtrctRegnClsrReq")

		@CtrctRegnClsrReq.deleter
		def CtrctRegnClsrReq(self):
			del self._CtrctRegnClsrReq
			self._CtrctRegnClsrReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnClsrReq', type=ContractRegistrationClosureRequestV04, min=1, max=1, mutex_group=None, array=False),
		))