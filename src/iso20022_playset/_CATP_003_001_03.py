# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalCompletionAdviceV03

class CATP_003_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.003.001.03"
		_docname = "catp.003.001.03"

		__slots__ = ["_ATMWdrwlCmpltnAdvc"]
		@property
		def ATMWdrwlCmpltnAdvc(self):
			return self._ATMWdrwlCmpltnAdvc

		@ATMWdrwlCmpltnAdvc.setter
		def ATMWdrwlCmpltnAdvc(self, value):
			self._ATMWdrwlCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAdvc', ATMWithdrawalCompletionAdviceV03, False)

		@ATMWdrwlCmpltnAdvc.deleter
		def ATMWdrwlCmpltnAdvc(self):
			del self._ATMWdrwlCmpltnAdvc
			self._ATMWdrwlCmpltnAdvc = base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAdvc', ATMWithdrawalCompletionAdviceV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlCmpltnAdvc', type=ATMWithdrawalCompletionAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))