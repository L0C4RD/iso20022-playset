# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CertificateManagementRequestV08 import CertificateManagementRequestV08

class CATM_007_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CertMgmtReq"]
		@property
		def CertMgmtReq(self):
			return self._CertMgmtReq

		@CertMgmtReq.setter
		def CertMgmtReq(self, value):
			self._CertMgmtReq = value if type(value) != base_types.auto else self.make_default("CertMgmtReq")

		@CertMgmtReq.deleter
		def CertMgmtReq(self):
			del self._CertMgmtReq
			self._CertMgmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequestV08, min=1, max=1, mutex_group=None, array=False),
		))