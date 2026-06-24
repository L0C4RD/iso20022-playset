# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractRegistrationAmendmentRequestV04 import ContractRegistrationAmendmentRequestV04

class AUTH_021_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.021.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CtrctRegnAmdmntReq"]
		@property
		def CtrctRegnAmdmntReq(self):
			return self._CtrctRegnAmdmntReq

		@CtrctRegnAmdmntReq.setter
		def CtrctRegnAmdmntReq(self, value):
			self._CtrctRegnAmdmntReq = value if type(value) != base_types.auto else self.make_default("CtrctRegnAmdmntReq")

		@CtrctRegnAmdmntReq.deleter
		def CtrctRegnAmdmntReq(self):
			del self._CtrctRegnAmdmntReq
			self._CtrctRegnAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnAmdmntReq', type=ContractRegistrationAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))