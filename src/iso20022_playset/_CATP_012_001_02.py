# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMDepositRequestV02 import ATMDepositRequestV02

class CATP_012_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catp.012.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ATMDpstReq"]
		@property
		def ATMDpstReq(self):
			return self._ATMDpstReq

		@ATMDpstReq.setter
		def ATMDpstReq(self, value):
			self._ATMDpstReq = value if type(value) != base_types.auto else self.make_default("ATMDpstReq")

		@ATMDpstReq.deleter
		def ATMDpstReq(self):
			del self._ATMDpstReq
			self._ATMDpstReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstReq', type=ATMDepositRequestV02, min=1, max=1, mutex_group=None, array=False),
		))