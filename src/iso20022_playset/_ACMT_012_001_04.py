# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountAdditionalInformationRequestV04 import AccountAdditionalInformationRequestV04

class ACMT_012_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.012.001.04"
		_docname = "acmt.012.001.04"

		__slots__ = ["_AcctAddtlInfReq"]
		@property
		def AcctAddtlInfReq(self):
			return self._AcctAddtlInfReq

		@AcctAddtlInfReq.setter
		def AcctAddtlInfReq(self, value):
			self._AcctAddtlInfReq = value if type(value) != base_types.auto else self.make_default("AcctAddtlInfReq")

		@AcctAddtlInfReq.deleter
		def AcctAddtlInfReq(self):
			del self._AcctAddtlInfReq
			self._AcctAddtlInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctAddtlInfReq', type=AccountAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))