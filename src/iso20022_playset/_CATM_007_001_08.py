# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificateManagementRequestV08

class CATM_007_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.007.001.08"
		_docname = "catm.007.001.08"

		__slots__ = ["_CertMgmtReq"]
		@property
		def CertMgmtReq(self):
			return self._CertMgmtReq

		@CertMgmtReq.setter
		def CertMgmtReq(self, value):
			self._CertMgmtReq = value if value is not None else base_types.UninitialisedField(self, 'CertMgmtReq', CertificateManagementRequestV08, False)

		@CertMgmtReq.deleter
		def CertMgmtReq(self):
			del self._CertMgmtReq
			self._CertMgmtReq = base_types.UninitialisedField(self, 'CertMgmtReq', CertificateManagementRequestV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequestV08, min=1, max=1, mutex_group=None, array=False),
		))