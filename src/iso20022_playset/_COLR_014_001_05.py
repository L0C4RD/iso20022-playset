# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InterestPaymentResponseV05 import InterestPaymentResponseV05

class COLR_014_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.014.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_IntrstPmtRspn"]
		@property
		def IntrstPmtRspn(self):
			return self._IntrstPmtRspn

		@IntrstPmtRspn.setter
		def IntrstPmtRspn(self, value):
			self._IntrstPmtRspn = value if type(value) != base_types.auto else self.make_default("IntrstPmtRspn")

		@IntrstPmtRspn.deleter
		def IntrstPmtRspn(self):
			del self._IntrstPmtRspn
			self._IntrstPmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtRspn', type=InterestPaymentResponseV05, min=1, max=1, mutex_group=None, array=False),
		))