# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificateManagementResponseV07

class CATM_008_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.008.001.07"
		_docname = "catm.008.001.07"

		__slots__ = ["_CertMgmtRspn"]
		@property
		def CertMgmtRspn(self):
			return self._CertMgmtRspn

		@CertMgmtRspn.setter
		def CertMgmtRspn(self, value):
			self._CertMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'CertMgmtRspn', CertificateManagementResponseV07, False)

		@CertMgmtRspn.deleter
		def CertMgmtRspn(self):
			del self._CertMgmtRspn
			self._CertMgmtRspn = base_types.UninitialisedField(self, 'CertMgmtRspn', CertificateManagementResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CertMgmtRspn', type=CertificateManagementResponseV07, min=1, max=1, mutex_group=None, array=False),
		))