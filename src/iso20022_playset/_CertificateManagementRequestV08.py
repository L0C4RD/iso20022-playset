# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificateManagementRequest4
from . import ContentInformationType38
from . import TMSHeader1

class CertificateManagementRequestV08(base_types._BaseFieldType):

	__slots__ = ["_CertMgmtReq", "_Hdr", "_SctyTrlr"]
	@property
	def CertMgmtReq(self):
		return self._CertMgmtReq

	@CertMgmtReq.setter
	def CertMgmtReq(self, value):
		self._CertMgmtReq = value if value is not None else base_types.UninitialisedField(self, 'CertMgmtReq', CertificateManagementRequest4, False)

	@CertMgmtReq.deleter
	def CertMgmtReq(self):
		del self._CertMgmtReq
		self._CertMgmtReq = base_types.UninitialisedField(self, 'CertMgmtReq', CertificateManagementRequest4, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequest4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))