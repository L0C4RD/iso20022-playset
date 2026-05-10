from . import base_types
from .CertificateManagementResponseV07 import CertificateManagementResponseV07

class CATM_008_001_07():

	class Document(base_types._BaseFieldType):

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

