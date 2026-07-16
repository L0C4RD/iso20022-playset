# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMKeyDownloadRequestV05

class CAAM_003_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.003.001.05"
		_docname = "caam.003.001.05"

		__slots__ = ["_ATMKeyDwnldReq"]
		@property
		def ATMKeyDwnldReq(self):
			return self._ATMKeyDwnldReq

		@ATMKeyDwnldReq.setter
		def ATMKeyDwnldReq(self, value):
			self._ATMKeyDwnldReq = value if value is not None else base_types.UninitialisedField(self, 'ATMKeyDwnldReq', ATMKeyDownloadRequestV05, False)

		@ATMKeyDwnldReq.deleter
		def ATMKeyDwnldReq(self):
			del self._ATMKeyDwnldReq
			self._ATMKeyDwnldReq = base_types.UninitialisedField(self, 'ATMKeyDwnldReq', ATMKeyDownloadRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequestV05, min=1, max=1, mutex_group=None, array=False),
		))