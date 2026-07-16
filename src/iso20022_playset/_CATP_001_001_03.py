# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalRequestV03

class CATP_001_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.001.001.03"
		_docname = "catp.001.001.03"

		__slots__ = ["_ATMWdrwlReq"]
		@property
		def ATMWdrwlReq(self):
			return self._ATMWdrwlReq

		@ATMWdrwlReq.setter
		def ATMWdrwlReq(self, value):
			self._ATMWdrwlReq = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlReq', ATMWithdrawalRequestV03, False)

		@ATMWdrwlReq.deleter
		def ATMWdrwlReq(self):
			del self._ATMWdrwlReq
			self._ATMWdrwlReq = base_types.UninitialisedField(self, 'ATMWdrwlReq', ATMWithdrawalRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlReq', type=ATMWithdrawalRequestV03, min=1, max=1, mutex_group=None, array=False),
		))