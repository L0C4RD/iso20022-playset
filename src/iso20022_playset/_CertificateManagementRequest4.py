# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentServiceType10Code
from . import GenericIdentification176
from . import ISODateTime
from . import KeyUsage1Code
from . import Max10KBinary
from . import Max140Binary
from . import Max20000Text
from . import Max70Text
from . import PointOfInteraction6
from . import SignedData9

class CertificateManagementRequest4(base_types._BaseFieldType):

	__slots__ = ["_BinryCertfctnReq", "_CertSvc", "_CertfctnReq", "_ClntCert", "_KeyFctn", "_POIChllngVal", "_POIDtTm", "_POIId", "_SctyDomn", "_TMId", "_WhtListId"]
	@property
	def BinryCertfctnReq(self):
		return self._BinryCertfctnReq

	@BinryCertfctnReq.setter
	def BinryCertfctnReq(self, value):
		self._BinryCertfctnReq = value if value is not None else base_types.UninitialisedField(self, 'BinryCertfctnReq', Max20000Text, False)

	@BinryCertfctnReq.deleter
	def BinryCertfctnReq(self):
		del self._BinryCertfctnReq
		self._BinryCertfctnReq = base_types.UninitialisedField(self, 'BinryCertfctnReq', Max20000Text, False)

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
	def CertfctnReq(self):
		return self._CertfctnReq

	@CertfctnReq.setter
	def CertfctnReq(self, value):
		self._CertfctnReq = value if value is not None else base_types.UninitialisedField(self, 'CertfctnReq', SignedData9, False)

	@CertfctnReq.deleter
	def CertfctnReq(self):
		del self._CertfctnReq
		self._CertfctnReq = base_types.UninitialisedField(self, 'CertfctnReq', SignedData9, False)

	@property
	def ClntCert(self):
		return self._ClntCert

	@ClntCert.setter
	def ClntCert(self, value):
		self._ClntCert = value if value is not None else base_types.UninitialisedField(self, 'ClntCert', Max10KBinary, False)

	@ClntCert.deleter
	def ClntCert(self):
		del self._ClntCert
		self._ClntCert = base_types.UninitialisedField(self, 'ClntCert', Max10KBinary, False)

	@property
	def KeyFctn(self):
		return self._KeyFctn

	@KeyFctn.setter
	def KeyFctn(self, value):
		self._KeyFctn = value if value is not None else base_types.UninitialisedField(self, 'KeyFctn', KeyUsage1Code, True)

	@KeyFctn.deleter
	def KeyFctn(self):
		del self._KeyFctn
		self._KeyFctn = base_types.UninitialisedField(self, 'KeyFctn', KeyUsage1Code, True)

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
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if value is not None else base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = base_types.UninitialisedField(self, 'POIDtTm', ISODateTime, False)

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
	def SctyDomn(self):
		return self._SctyDomn

	@SctyDomn.setter
	def SctyDomn(self, value):
		self._SctyDomn = value if value is not None else base_types.UninitialisedField(self, 'SctyDomn', Max70Text, False)

	@SctyDomn.deleter
	def SctyDomn(self):
		del self._SctyDomn
		self._SctyDomn = base_types.UninitialisedField(self, 'SctyDomn', Max70Text, False)

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
	def WhtListId(self):
		return self._WhtListId

	@WhtListId.setter
	def WhtListId(self, value):
		self._WhtListId = value if value is not None else base_types.UninitialisedField(self, 'WhtListId', PointOfInteraction6, False)

	@WhtListId.deleter
	def WhtListId(self):
		del self._WhtListId
		self._WhtListId = base_types.UninitialisedField(self, 'WhtListId', PointOfInteraction6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BinryCertfctnReq', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertSvc', type=CardPaymentServiceType10Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnReq', type=SignedData9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCert', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyFctn', type=KeyUsage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIChllngVal', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDomn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhtListId', type=PointOfInteraction6, min=0, max=1, mutex_group=None, array=False),
	))