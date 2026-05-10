from . import base_types
from .CertificateManagementRequestV07 import CertificateManagementRequestV07

class CATM_007_001_07():

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
			base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

