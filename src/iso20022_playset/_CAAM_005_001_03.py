# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMDiagnosticRequestV03 import ATMDiagnosticRequestV03

class CAAM_005_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caam.005.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ATMDgnstcReq"]
		@property
		def ATMDgnstcReq(self):
			return self._ATMDgnstcReq

		@ATMDgnstcReq.setter
		def ATMDgnstcReq(self, value):
			self._ATMDgnstcReq = value if type(value) != base_types.auto else self.make_default("ATMDgnstcReq")

		@ATMDgnstcReq.deleter
		def ATMDgnstcReq(self):
			del self._ATMDgnstcReq
			self._ATMDgnstcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDgnstcReq', type=ATMDiagnosticRequestV03, min=1, max=1, mutex_group=None, array=False),
		))