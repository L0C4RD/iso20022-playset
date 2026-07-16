# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalResponseV03

class CATP_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.002.001.03"
		_docname = "catp.002.001.03"

		__slots__ = ["_ATMWdrwlRspn"]
		@property
		def ATMWdrwlRspn(self):
			return self._ATMWdrwlRspn

		@ATMWdrwlRspn.setter
		def ATMWdrwlRspn(self, value):
			self._ATMWdrwlRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlRspn', ATMWithdrawalResponseV03, False)

		@ATMWdrwlRspn.deleter
		def ATMWdrwlRspn(self):
			del self._ATMWdrwlRspn
			self._ATMWdrwlRspn = base_types.UninitialisedField(self, 'ATMWdrwlRspn', ATMWithdrawalResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlRspn', type=ATMWithdrawalResponseV03, min=1, max=1, mutex_group=None, array=False),
		))