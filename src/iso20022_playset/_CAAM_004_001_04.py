# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMKeyDownloadResponseV04 import ATMKeyDownloadResponseV04

class CAAM_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.004.001.04"
		_docname = "caam.004.001.04"

		__slots__ = ["_ATMKeyDwnldRspn"]
		@property
		def ATMKeyDwnldRspn(self):
			return self._ATMKeyDwnldRspn

		@ATMKeyDwnldRspn.setter
		def ATMKeyDwnldRspn(self, value):
			self._ATMKeyDwnldRspn = value if type(value) != base_types.auto else self.make_default("ATMKeyDwnldRspn")

		@ATMKeyDwnldRspn.deleter
		def ATMKeyDwnldRspn(self):
			del self._ATMKeyDwnldRspn
			self._ATMKeyDwnldRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldRspn', type=ATMKeyDownloadResponseV04, min=1, max=1, mutex_group=None, array=False),
		))