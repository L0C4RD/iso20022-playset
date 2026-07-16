# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchInformationRequestV05

class ACMT_027_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05"
		_docname = "acmt.027.001.05"

		__slots__ = ["_AcctSwtchInfReq"]
		@property
		def AcctSwtchInfReq(self):
			return self._AcctSwtchInfReq

		@AcctSwtchInfReq.setter
		def AcctSwtchInfReq(self, value):
			self._AcctSwtchInfReq = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchInfReq', AccountSwitchInformationRequestV05, False)

		@AcctSwtchInfReq.deleter
		def AcctSwtchInfReq(self):
			del self._AcctSwtchInfReq
			self._AcctSwtchInfReq = base_types.UninitialisedField(self, 'AcctSwtchInfReq', AccountSwitchInformationRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfReq', type=AccountSwitchInformationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))