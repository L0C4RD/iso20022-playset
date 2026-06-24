# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMDepositCompletionAdviceV02 import ATMDepositCompletionAdviceV02

class CATP_014_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catp.014.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ATMDpstCmpltnAdvc"]
		@property
		def ATMDpstCmpltnAdvc(self):
			return self._ATMDpstCmpltnAdvc

		@ATMDpstCmpltnAdvc.setter
		def ATMDpstCmpltnAdvc(self, value):
			self._ATMDpstCmpltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMDpstCmpltnAdvc")

		@ATMDpstCmpltnAdvc.deleter
		def ATMDpstCmpltnAdvc(self):
			del self._ATMDpstCmpltnAdvc
			self._ATMDpstCmpltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstCmpltnAdvc', type=ATMDepositCompletionAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))