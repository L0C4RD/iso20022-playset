# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMDiagnosticResponseV02 import ATMDiagnosticResponseV02

class CAAM_006_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caam.006.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ATMDgnstcRspn"]
		@property
		def ATMDgnstcRspn(self):
			return self._ATMDgnstcRspn

		@ATMDgnstcRspn.setter
		def ATMDgnstcRspn(self, value):
			self._ATMDgnstcRspn = value if type(value) != base_types.auto else self.make_default("ATMDgnstcRspn")

		@ATMDgnstcRspn.deleter
		def ATMDgnstcRspn(self):
			del self._ATMDgnstcRspn
			self._ATMDgnstcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDgnstcRspn', type=ATMDiagnosticResponseV02, min=1, max=1, mutex_group=None, array=False),
		))