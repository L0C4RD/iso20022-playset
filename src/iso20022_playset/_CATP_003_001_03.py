# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMWithdrawalCompletionAdviceV03 import ATMWithdrawalCompletionAdviceV03

class CATP_003_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catp.003.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ATMWdrwlCmpltnAdvc"]
		@property
		def ATMWdrwlCmpltnAdvc(self):
			return self._ATMWdrwlCmpltnAdvc

		@ATMWdrwlCmpltnAdvc.setter
		def ATMWdrwlCmpltnAdvc(self, value):
			self._ATMWdrwlCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMWdrwlCmpltnAdvc")

		@ATMWdrwlCmpltnAdvc.deleter
		def ATMWdrwlCmpltnAdvc(self):
			del self._ATMWdrwlCmpltnAdvc
			self._ATMWdrwlCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlCmpltnAdvc', type=ATMWithdrawalCompletionAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))