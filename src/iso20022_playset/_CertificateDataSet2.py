from . import base_types
from ._CertifiedCharacteristics2Choice import CertifiedCharacteristics2Choice
from ._DatePeriodDetails import DatePeriodDetails
from ._DocumentIdentification1 import DocumentIdentification1
from ._ISODate import ISODate
from ._LineItemAndPOIdentification1 import LineItemAndPOIdentification1
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._PartyIdentification26 import PartyIdentification26
from ._PostalAddress5 import PostalAddress5
from ._SingleTransport3 import SingleTransport3
from ._TradeCertificateType1Code import TradeCertificateType1Code
from ._YesNoIndicator import YesNoIndicator

class CertificateDataSet2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AuthrsdInspctrInd", "_CertId", "_CertTp", "_CertfdChrtcs", "_Consgn", "_Consgnr", "_DataSetId", "_GoodsDesc", "_InspctnDt", "_IsseDt", "_Issr", "_LineItm", "_Manfctr", "_PlcOfIsse", "_Trnsprt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AuthrsdInspctrInd(self):
		return self._AuthrsdInspctrInd

	@AuthrsdInspctrInd.setter
	def AuthrsdInspctrInd(self, value):
		self._AuthrsdInspctrInd = value if type(value) != base_types.auto else self.make_default("AuthrsdInspctrInd")

	@AuthrsdInspctrInd.deleter
	def AuthrsdInspctrInd(self):
		del self._AuthrsdInspctrInd
		self._AuthrsdInspctrInd = None

	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if type(value) != base_types.auto else self.make_default("CertId")

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = None

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if type(value) != base_types.auto else self.make_default("CertTp")

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = None

	@property
	def CertfdChrtcs(self):
		return self._CertfdChrtcs

	@CertfdChrtcs.setter
	def CertfdChrtcs(self, value):
		self._CertfdChrtcs = value if type(value) != base_types.auto else self.make_default("CertfdChrtcs")

	@CertfdChrtcs.deleter
	def CertfdChrtcs(self):
		del self._CertfdChrtcs
		self._CertfdChrtcs = None

	@property
	def Consgn(self):
		return self._Consgn

	@Consgn.setter
	def Consgn(self, value):
		self._Consgn = value if type(value) != base_types.auto else self.make_default("Consgn")

	@Consgn.deleter
	def Consgn(self):
		del self._Consgn
		self._Consgn = None

	@property
	def Consgnr(self):
		return self._Consgnr

	@Consgnr.setter
	def Consgnr(self, value):
		self._Consgnr = value if type(value) != base_types.auto else self.make_default("Consgnr")

	@Consgnr.deleter
	def Consgnr(self):
		del self._Consgnr
		self._Consgnr = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != base_types.auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def GoodsDesc(self):
		return self._GoodsDesc

	@GoodsDesc.setter
	def GoodsDesc(self, value):
		self._GoodsDesc = value if type(value) != base_types.auto else self.make_default("GoodsDesc")

	@GoodsDesc.deleter
	def GoodsDesc(self):
		del self._GoodsDesc
		self._GoodsDesc = None

	@property
	def InspctnDt(self):
		return self._InspctnDt

	@InspctnDt.setter
	def InspctnDt(self, value):
		self._InspctnDt = value if type(value) != base_types.auto else self.make_default("InspctnDt")

	@InspctnDt.deleter
	def InspctnDt(self):
		del self._InspctnDt
		self._InspctnDt = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != base_types.auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if type(value) != base_types.auto else self.make_default("Manfctr")

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = None

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if type(value) != base_types.auto else self.make_default("PlcOfIsse")

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = None

	@property
	def Trnsprt(self):
		return self._Trnsprt

	@Trnsprt.setter
	def Trnsprt(self, value):
		self._Trnsprt = value if type(value) != base_types.auto else self.make_default("Trnsprt")

	@Trnsprt.deleter
	def Trnsprt(self):
		del self._Trnsprt
		self._Trnsprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthrsdInspctrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTp', type=TradeCertificateType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfdChrtcs', type=CertifiedCharacteristics2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgn', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgnr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataSetId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoodsDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InspctnDt', type=DatePeriodDetails, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=LineItemAndPOIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Manfctr', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfIsse', type=PostalAddress5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trnsprt', type=SingleTransport3, min=0, max=1, mutex_group=None, array=False),
	))

