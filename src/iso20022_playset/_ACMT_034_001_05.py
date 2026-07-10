# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchRequestPaymentV05 import AccountSwitchRequestPaymentV05

class ACMT_034_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.034.001.05"
		_docname = "acmt.034.001.05"

		__slots__ = ["_AcctSwtchReqPmt"]
		@property
		def AcctSwtchReqPmt(self):
			return self._AcctSwtchReqPmt

		@AcctSwtchReqPmt.setter
		def AcctSwtchReqPmt(self, value):
			self._AcctSwtchReqPmt = value if type(value) != base_types.auto else self.make_default("AcctSwtchReqPmt")

		@AcctSwtchReqPmt.deleter
		def AcctSwtchReqPmt(self):
			del self._AcctSwtchReqPmt
			self._AcctSwtchReqPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqPmt', type=AccountSwitchRequestPaymentV05, min=1, max=1, mutex_group=None, array=False),
		))