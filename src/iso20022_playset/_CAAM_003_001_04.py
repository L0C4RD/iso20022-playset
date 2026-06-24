# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMKeyDownloadRequestV04 import ATMKeyDownloadRequestV04

class CAAM_003_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caam.003.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ATMKeyDwnldReq"]
		@property
		def ATMKeyDwnldReq(self):
			return self._ATMKeyDwnldReq

		@ATMKeyDwnldReq.setter
		def ATMKeyDwnldReq(self, value):
			self._ATMKeyDwnldReq = value if type(value) != base_types.auto else self.make_default("ATMKeyDwnldReq")

		@ATMKeyDwnldReq.deleter
		def ATMKeyDwnldReq(self):
			del self._ATMKeyDwnldReq
			self._ATMKeyDwnldReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequestV04, min=1, max=1, mutex_group=None, array=False),
		))