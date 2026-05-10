from . import base_types
from ._CardPaymentServiceType10Code import CardPaymentServiceType10Code
from ._KeyUsage1Code import KeyUsage1Code
from ._Max20000Text import Max20000Text
from ._PointOfInteraction6 import PointOfInteraction6
from ._Max140Binary import Max140Binary
from ._Max70Text import Max70Text
from ._CertificationRequest1 import CertificationRequest1
from ._Max10KBinary import Max10KBinary
from ._ISODateTime import ISODateTime
from ._GenericIdentification176 import GenericIdentification176

class CertificateManagementRequest3(base_types._BaseFieldType):

	__slots__ = ["_POIChllngVal", "_WhtListId", "_KeyFctn", "_SctyDomn", "_BinryCertfctnReq", "_ClntCert", "_TMId", "_CertSvc", "_CertfctnReq", "_POIId", "_POIDtTm"]
	@property
	def BinryCertfctnReq(self):
		return self._BinryCertfctnReq

	@BinryCertfctnReq.setter
	def BinryCertfctnReq(self, value):
		self._BinryCertfctnReq = value if type(value) != base_types.auto else self.make_default("BinryCertfctnReq")

	@BinryCertfctnReq.deleter
	def BinryCertfctnReq(self):
		del self._BinryCertfctnReq
		self._BinryCertfctnReq = None

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
	def CertfctnReq(self):
		return self._CertfctnReq

	@CertfctnReq.setter
	def CertfctnReq(self, value):
		self._CertfctnReq = value if type(value) != base_types.auto else self.make_default("CertfctnReq")

	@CertfctnReq.deleter
	def CertfctnReq(self):
		del self._CertfctnReq
		self._CertfctnReq = None

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
	def KeyFctn(self):
		return self._KeyFctn

	@KeyFctn.setter
	def KeyFctn(self, value):
		self._KeyFctn = value if type(value) != base_types.auto else self.make_default("KeyFctn")

	@KeyFctn.deleter
	def KeyFctn(self):
		del self._KeyFctn
		self._KeyFctn = None

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
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if type(value) != base_types.auto else self.make_default("POIDtTm")

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = None

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
	def SctyDomn(self):
		return self._SctyDomn

	@SctyDomn.setter
	def SctyDomn(self, value):
		self._SctyDomn = value if type(value) != base_types.auto else self.make_default("SctyDomn")

	@SctyDomn.deleter
	def SctyDomn(self):
		del self._SctyDomn
		self._SctyDomn = None

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
	def WhtListId(self):
		return self._WhtListId

	@WhtListId.setter
	def WhtListId(self, value):
		self._WhtListId = value if type(value) != base_types.auto else self.make_default("WhtListId")

	@WhtListId.deleter
	def WhtListId(self):
		del self._WhtListId
		self._WhtListId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BinryCertfctnReq', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertSvc', type=CardPaymentServiceType10Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnReq', type=CertificationRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCert', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyFctn', type=KeyUsage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDomn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhtListId', type=PointOfInteraction6, min=0, max=1, mutex_group=None, array=False),
	))

