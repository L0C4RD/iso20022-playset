# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CertificateManagementRequest3 import CertificateManagementRequest3
from ._ContentInformationType38 import ContentInformationType38
from ._TMSHeader1 import TMSHeader1

class CertificateManagementRequestV07(base_types._BaseFieldType):

	__slots__ = ["_CertMgmtReq", "_Hdr", "_SctyTrlr"]
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

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertMgmtReq', type=CertificateManagementRequest3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))