# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertifiedCharacteristics2Choice
from . import DatePeriodDetails
from . import DocumentIdentification1
from . import ISODate
from . import LineItemAndPOIdentification1
from . import Max350Text
from . import Max35Text
from . import Max70Text
from . import PartyIdentification26
from . import PostalAddress5
from . import SingleTransport3
from . import TradeCertificateType1Code
from . import YesNoIndicator

class CertificateDataSet2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AuthrsdInspctrInd", "_CertId", "_CertTp", "_CertfdChrtcs", "_Consgn", "_Consgnr", "_DataSetId", "_GoodsDesc", "_InspctnDt", "_IsseDt", "_Issr", "_LineItm", "_Manfctr", "_PlcOfIsse", "_Trnsprt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, True)

	@property
	def AuthrsdInspctrInd(self):
		return self._AuthrsdInspctrInd

	@AuthrsdInspctrInd.setter
	def AuthrsdInspctrInd(self, value):
		self._AuthrsdInspctrInd = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdInspctrInd', YesNoIndicator, False)

	@AuthrsdInspctrInd.deleter
	def AuthrsdInspctrInd(self):
		del self._AuthrsdInspctrInd
		self._AuthrsdInspctrInd = base_types.UninitialisedField(self, 'AuthrsdInspctrInd', YesNoIndicator, False)

	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if value is not None else base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if value is not None else base_types.UninitialisedField(self, 'CertTp', TradeCertificateType1Code, False)

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = base_types.UninitialisedField(self, 'CertTp', TradeCertificateType1Code, False)

	@property
	def CertfdChrtcs(self):
		return self._CertfdChrtcs

	@CertfdChrtcs.setter
	def CertfdChrtcs(self, value):
		self._CertfdChrtcs = value if value is not None else base_types.UninitialisedField(self, 'CertfdChrtcs', CertifiedCharacteristics2Choice, False)

	@CertfdChrtcs.deleter
	def CertfdChrtcs(self):
		del self._CertfdChrtcs
		self._CertfdChrtcs = base_types.UninitialisedField(self, 'CertfdChrtcs', CertifiedCharacteristics2Choice, False)

	@property
	def Consgn(self):
		return self._Consgn

	@Consgn.setter
	def Consgn(self, value):
		self._Consgn = value if value is not None else base_types.UninitialisedField(self, 'Consgn', PartyIdentification26, False)

	@Consgn.deleter
	def Consgn(self):
		del self._Consgn
		self._Consgn = base_types.UninitialisedField(self, 'Consgn', PartyIdentification26, False)

	@property
	def Consgnr(self):
		return self._Consgnr

	@Consgnr.setter
	def Consgnr(self, value):
		self._Consgnr = value if value is not None else base_types.UninitialisedField(self, 'Consgnr', PartyIdentification26, False)

	@Consgnr.deleter
	def Consgnr(self):
		del self._Consgnr
		self._Consgnr = base_types.UninitialisedField(self, 'Consgnr', PartyIdentification26, False)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DocumentIdentification1, False)

	@property
	def GoodsDesc(self):
		return self._GoodsDesc

	@GoodsDesc.setter
	def GoodsDesc(self, value):
		self._GoodsDesc = value if value is not None else base_types.UninitialisedField(self, 'GoodsDesc', Max70Text, False)

	@GoodsDesc.deleter
	def GoodsDesc(self):
		del self._GoodsDesc
		self._GoodsDesc = base_types.UninitialisedField(self, 'GoodsDesc', Max70Text, False)

	@property
	def InspctnDt(self):
		return self._InspctnDt

	@InspctnDt.setter
	def InspctnDt(self, value):
		self._InspctnDt = value if value is not None else base_types.UninitialisedField(self, 'InspctnDt', DatePeriodDetails, False)

	@InspctnDt.deleter
	def InspctnDt(self):
		del self._InspctnDt
		self._InspctnDt = base_types.UninitialisedField(self, 'InspctnDt', DatePeriodDetails, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification26, False)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', LineItemAndPOIdentification1, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', LineItemAndPOIdentification1, True)

	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if value is not None else base_types.UninitialisedField(self, 'Manfctr', PartyIdentification26, False)

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = base_types.UninitialisedField(self, 'Manfctr', PartyIdentification26, False)

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if value is not None else base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress5, False)

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress5, False)

	@property
	def Trnsprt(self):
		return self._Trnsprt

	@Trnsprt.setter
	def Trnsprt(self, value):
		self._Trnsprt = value if value is not None else base_types.UninitialisedField(self, 'Trnsprt', SingleTransport3, False)

	@Trnsprt.deleter
	def Trnsprt(self):
		del self._Trnsprt
		self._Trnsprt = base_types.UninitialisedField(self, 'Trnsprt', SingleTransport3, False)

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