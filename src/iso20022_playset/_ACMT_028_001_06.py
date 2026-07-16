# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchInformationResponseV06

class ACMT_028_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.028.001.06"
		_docname = "acmt.028.001.06"

		__slots__ = ["_AcctSwtchInfRspn"]
		@property
		def AcctSwtchInfRspn(self):
			return self._AcctSwtchInfRspn

		@AcctSwtchInfRspn.setter
		def AcctSwtchInfRspn(self, value):
			self._AcctSwtchInfRspn = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchInfRspn', AccountSwitchInformationResponseV06, False)

		@AcctSwtchInfRspn.deleter
		def AcctSwtchInfRspn(self):
			del self._AcctSwtchInfRspn
			self._AcctSwtchInfRspn = base_types.UninitialisedField(self, 'AcctSwtchInfRspn', AccountSwitchInformationResponseV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfRspn', type=AccountSwitchInformationResponseV06, min=1, max=1, mutex_group=None, array=False),
		))