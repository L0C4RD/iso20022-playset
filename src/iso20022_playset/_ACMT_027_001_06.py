# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchInformationRequestV06 import AccountSwitchInformationRequestV06

class ACMT_027_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchInfReq"]
		@property
		def AcctSwtchInfReq(self):
			return self._AcctSwtchInfReq

		@AcctSwtchInfReq.setter
		def AcctSwtchInfReq(self, value):
			self._AcctSwtchInfReq = value if type(value) != base_types.auto else self.make_default("AcctSwtchInfReq")

		@AcctSwtchInfReq.deleter
		def AcctSwtchInfReq(self):
			del self._AcctSwtchInfReq
			self._AcctSwtchInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfReq', type=AccountSwitchInformationRequestV06, min=1, max=1, mutex_group=None, array=False),
		))