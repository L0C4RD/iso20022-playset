# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentServiceType10Code
from . import GenericIdentification176
from . import ISODateTime
from . import Max10KBinary
from . import Max140Binary
from . import Max3000Binary
from . import Max35Text
from . import ResponseType6

class CertificateManagementResponse3(base_types._BaseFieldType):

	__slots__ = ["_CertSvc", "_ClntCert", "_ClntCertPth", "_POIChllngVal", "_POIId", "_Rslt", "_SctyPrfl", "_SvrCertPth", "_TMId", "_TMSDtTm"]
	@property
	def CertSvc(self):
		return self._CertSvc

	@CertSvc.setter
	def CertSvc(self, value):
		self._CertSvc = value if value is not None else base_types.UninitialisedField(self, 'CertSvc', CardPaymentServiceType10Code, False)

	@CertSvc.deleter
	def CertSvc(self):
		del self._CertSvc
		self._CertSvc = base_types.UninitialisedField(self, 'CertSvc', CardPaymentServiceType10Code, False)

	@property
	def ClntCert(self):
		return self._ClntCert

	@ClntCert.setter
	def ClntCert(self, value):
		self._ClntCert = value if value is not None else base_types.UninitialisedField(self, 'ClntCert', Max3000Binary, False)

	@ClntCert.deleter
	def ClntCert(self):
		del self._ClntCert
		self._ClntCert = base_types.UninitialisedField(self, 'ClntCert', Max3000Binary, False)

	@property
	def ClntCertPth(self):
		return self._ClntCertPth

	@ClntCertPth.setter
	def ClntCertPth(self, value):
		self._ClntCertPth = value if value is not None else base_types.UninitialisedField(self, 'ClntCertPth', Max10KBinary, True)

	@ClntCertPth.deleter
	def ClntCertPth(self):
		del self._ClntCertPth
		self._ClntCertPth = base_types.UninitialisedField(self, 'ClntCertPth', Max10KBinary, True)

	@property
	def POIChllngVal(self):
		return self._POIChllngVal

	@POIChllngVal.setter
	def POIChllngVal(self, value):
		self._POIChllngVal = value if value is not None else base_types.UninitialisedField(self, 'POIChllngVal', Max140Binary, False)

	@POIChllngVal.deleter
	def POIChllngVal(self):
		del self._POIChllngVal
		self._POIChllngVal = base_types.UninitialisedField(self, 'POIChllngVal', Max140Binary, False)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', GenericIdentification176, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', GenericIdentification176, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', ResponseType6, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', ResponseType6, False)

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if value is not None else base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@property
	def SvrCertPth(self):
		return self._SvrCertPth

	@SvrCertPth.setter
	def SvrCertPth(self, value):
		self._SvrCertPth = value if value is not None else base_types.UninitialisedField(self, 'SvrCertPth', Max10KBinary, True)

	@SvrCertPth.deleter
	def SvrCertPth(self):
		del self._SvrCertPth
		self._SvrCertPth = base_types.UninitialisedField(self, 'SvrCertPth', Max10KBinary, True)

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if value is not None else base_types.UninitialisedField(self, 'TMId', GenericIdentification176, False)

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = base_types.UninitialisedField(self, 'TMId', GenericIdentification176, False)

	@property
	def TMSDtTm(self):
		return self._TMSDtTm

	@TMSDtTm.setter
	def TMSDtTm(self, value):
		self._TMSDtTm = value if value is not None else base_types.UninitialisedField(self, 'TMSDtTm', ISODateTime, False)

	@TMSDtTm.deleter
	def TMSDtTm(self):
		del self._TMSDtTm
		self._TMSDtTm = base_types.UninitialisedField(self, 'TMSDtTm', ISODateTime, False)

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