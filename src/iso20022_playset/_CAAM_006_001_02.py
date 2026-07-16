# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDiagnosticResponseV02

class CAAM_006_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.006.001.02"
		_docname = "caam.006.001.02"

		__slots__ = ["_ATMDgnstcRspn"]
		@property
		def ATMDgnstcRspn(self):
			return self._ATMDgnstcRspn

		@ATMDgnstcRspn.setter
		def ATMDgnstcRspn(self, value):
			self._ATMDgnstcRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMDgnstcRspn', ATMDiagnosticResponseV02, False)

		@ATMDgnstcRspn.deleter
		def ATMDgnstcRspn(self):
			del self._ATMDgnstcRspn
			self._ATMDgnstcRspn = base_types.UninitialisedField(self, 'ATMDgnstcRspn', ATMDiagnosticResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDgnstcRspn', type=ATMDiagnosticResponseV02, min=1, max=1, mutex_group=None, array=False),
		))