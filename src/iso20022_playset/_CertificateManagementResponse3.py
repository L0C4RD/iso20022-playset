# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentServiceType10Code import CardPaymentServiceType10Code
from ._GenericIdentification176 import GenericIdentification176
from ._ISODateTime import ISODateTime
from ._Max10KBinary import Max10KBinary
from ._Max140Binary import Max140Binary
from ._Max3000Binary import Max3000Binary
from ._Max35Text import Max35Text
from ._ResponseType6 import ResponseType6

class CertificateManagementResponse3(base_types._BaseFieldType):

	__slots__ = ["_CertSvc", "_ClntCert", "_ClntCertPth", "_POIChllngVal", "_POIId", "_Rslt", "_SctyPrfl", "_SvrCertPth", "_TMId", "_TMSDtTm"]
	@property
	def CertSvc(self):
		return self._CertSvc

	@CertSvc.setter
	def CertSvc(self, value):
		self._CertSvc = value if type(value) != base_types.auto else self.make_default("CertSvc")

	@CertSvc.deleter
	def CertSvc(self):
		del self._CertSvc
		self._CertSvc = None

	@property
	def ClntCert(self):
		return self._ClntCert

	@ClntCert.setter
	def ClntCert(self, value):
		self._ClntCert = value if type(value) != base_types.auto else self.make_default("ClntCert")

	@ClntCert.deleter
	def ClntCert(self):
		del self._ClntCert
		self._ClntCert = None

	@property
	def ClntCertPth(self):
		return self._ClntCertPth

	@ClntCertPth.setter
	def ClntCertPth(self, value):
		self._ClntCertPth = value if type(value) != base_types.auto else self.make_default("ClntCertPth")

	@ClntCertPth.deleter
	def ClntCertPth(self):
		del self._ClntCertPth
		self._ClntCertPth = None

	@property
	def POIChllngVal(self):
		return self._POIChllngVal

	@POIChllngVal.setter
	def POIChllngVal(self, value):
		self._POIChllngVal = value if type(value) != base_types.auto else self.make_default("POIChllngVal")

	@POIChllngVal.deleter
	def POIChllngVal(self):
		del self._POIChllngVal
		self._POIChllngVal = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if type(value) != base_types.auto else self.make_default("SctyPrfl")

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = None

	@property
	def SvrCertPth(self):
		return self._SvrCertPth

	@SvrCertPth.setter
	def SvrCertPth(self, value):
		self._SvrCertPth = value if type(value) != base_types.auto else self.make_default("SvrCertPth")

	@SvrCertPth.deleter
	def SvrCertPth(self):
		del self._SvrCertPth
		self._SvrCertPth = None

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if type(value) != base_types.auto else self.make_default("TMId")

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = None

	@property
	def TMSDtTm(self):
		return self._TMSDtTm

	@TMSDtTm.setter
	def TMSDtTm(self, value):
		self._TMSDtTm = value if type(value) != base_types.auto else self.make_default("TMSDtTm")

	@TMSDtTm.deleter
	def TMSDtTm(self):
		del self._TMSDtTm
		self._TMSDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertSvc', type=CardPaymentServiceType10Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCert', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCertPth', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=ResponseType6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrCertPth', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))