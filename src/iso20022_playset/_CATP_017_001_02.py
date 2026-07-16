# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMTransferResponseV02

class CATP_017_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.017.001.02"
		_docname = "catp.017.001.02"

		__slots__ = ["_ATMTrfRspn"]
		@property
		def ATMTrfRspn(self):
			return self._ATMTrfRspn

		@ATMTrfRspn.setter
		def ATMTrfRspn(self, value):
			self._ATMTrfRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMTrfRspn', ATMTransferResponseV02, False)

		@ATMTrfRspn.deleter
		def ATMTrfRspn(self):
			del self._ATMTrfRspn
			self._ATMTrfRspn = base_types.UninitialisedField(self, 'ATMTrfRspn', ATMTransferResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMTrfRspn', type=ATMTransferResponseV02, min=1, max=1, mutex_group=None, array=False),
		))