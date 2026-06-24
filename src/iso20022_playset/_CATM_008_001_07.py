# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CertificateManagementResponseV07 import CertificateManagementResponseV07

class CATM_008_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catm.008.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CertMgmtRspn"]
		@property
		def CertMgmtRspn(self):
			return self._CertMgmtRspn

		@CertMgmtRspn.setter
		def CertMgmtRspn(self, value):
			self._CertMgmtRspn = value if type(value) != base_types.auto else self.make_default("CertMgmtRspn")

		@CertMgmtRspn.deleter
		def CertMgmtRspn(self):
			del self._CertMgmtRspn
			self._CertMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CertMgmtRspn', type=CertificateManagementResponseV07, min=1, max=1, mutex_group=None, array=False),
		))