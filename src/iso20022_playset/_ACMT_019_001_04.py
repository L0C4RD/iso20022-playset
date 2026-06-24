# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountClosingRequestV04 import AccountClosingRequestV04

class ACMT_019_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:acmt.019.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AcctClsgReq"]
		@property
		def AcctClsgReq(self):
			return self._AcctClsgReq

		@AcctClsgReq.setter
		def AcctClsgReq(self, value):
			self._AcctClsgReq = value if type(value) != base_types.auto else self.make_default("AcctClsgReq")

		@AcctClsgReq.deleter
		def AcctClsgReq(self):
			del self._AcctClsgReq
			self._AcctClsgReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgReq', type=AccountClosingRequestV04, min=1, max=1, mutex_group=None, array=False),
		))