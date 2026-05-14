# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMKeyDownloadRequestV05 import ATMKeyDownloadRequestV05

class CAAM_003_001_05():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='ATMKeyDwnldReq', type=ATMKeyDownloadRequestV05, min=1, max=1, mutex_group=None, array=False),
		))