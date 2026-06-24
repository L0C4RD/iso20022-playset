# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMWithdrawalRequestV03 import ATMWithdrawalRequestV03

class CATP_001_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catp.001.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ATMWdrwlReq"]
		@property
		def ATMWdrwlReq(self):
			return self._ATMWdrwlReq

		@ATMWdrwlReq.setter
		def ATMWdrwlReq(self, value):
			self._ATMWdrwlReq = value if type(value) != base_types.auto else self.make_default("ATMWdrwlReq")

		@ATMWdrwlReq.deleter
		def ATMWdrwlReq(self):
			del self._ATMWdrwlReq
			self._ATMWdrwlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlReq', type=ATMWithdrawalRequestV03, min=1, max=1, mutex_group=None, array=False),
		))