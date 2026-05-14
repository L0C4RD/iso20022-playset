# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CertificateManagementResponse3 import CertificateManagementResponse3
from ._ContentInformationType38 import ContentInformationType38
from ._TMSHeader1 import TMSHeader1

class CertificateManagementResponseV07(base_types._BaseFieldType):

	__slots__ = ["_CertMgmtRspn", "_Hdr", "_SctyTrlr"]
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
		base_types.FieldEntry(name='CertMgmtRspn', type=CertificateManagementResponse3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))