# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMKeyDownloadResponseV05

class CAAM_004_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.004.001.05"
		_docname = "caam.004.001.05"

		__slots__ = ["_ATMKeyDwnldRspn"]
		@property
		def ATMKeyDwnldRspn(self):
			return self._ATMKeyDwnldRspn

		@ATMKeyDwnldRspn.setter
		def ATMKeyDwnldRspn(self, value):
			self._ATMKeyDwnldRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMKeyDwnldRspn', ATMKeyDownloadResponseV05, False)

		@ATMKeyDwnldRspn.deleter
		def ATMKeyDwnldRspn(self):
			del self._ATMKeyDwnldRspn
			self._ATMKeyDwnldRspn = base_types.UninitialisedField(self, 'ATMKeyDwnldRspn', ATMKeyDownloadResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponseV05, min=1, max=1, mutex_group=None, array=False),
		))