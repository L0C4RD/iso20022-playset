# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CertificateManagementRequestV07 import CertificateManagementRequestV07

class CATM_007_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.007.001.07"
		_docname = "catm.007.001.07"

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
			base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequestV07, min=1, max=1, mutex_group=None, array=False),
		))