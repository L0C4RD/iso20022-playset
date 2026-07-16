# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositCompletionAdviceV02

class CATP_014_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.014.001.02"
		_docname = "catp.014.001.02"

		__slots__ = ["_ATMDpstCmpltnAdvc"]
		@property
		def ATMDpstCmpltnAdvc(self):
			return self._ATMDpstCmpltnAdvc

		@ATMDpstCmpltnAdvc.setter
		def ATMDpstCmpltnAdvc(self, value):
			self._ATMDpstCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstCmpltnAdvc', ATMDepositCompletionAdviceV02, False)

		@ATMDpstCmpltnAdvc.deleter
		def ATMDpstCmpltnAdvc(self):
			del self._ATMDpstCmpltnAdvc
			self._ATMDpstCmpltnAdvc = base_types.UninitialisedField(self, 'ATMDpstCmpltnAdvc', ATMDepositCompletionAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstCmpltnAdvc', type=ATMDepositCompletionAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))