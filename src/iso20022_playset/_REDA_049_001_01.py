# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountLinkCreationRequestV01 import AccountLinkCreationRequestV01

class REDA_049_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.049.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctLkCreReq"]
		@property
		def AcctLkCreReq(self):
			return self._AcctLkCreReq

		@AcctLkCreReq.setter
		def AcctLkCreReq(self, value):
			self._AcctLkCreReq = value if type(value) != base_types.auto else self.make_default("AcctLkCreReq")

		@AcctLkCreReq.deleter
		def AcctLkCreReq(self):
			del self._AcctLkCreReq
			self._AcctLkCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkCreReq', type=AccountLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))