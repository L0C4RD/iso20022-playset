# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import DocumentIdentification1
from . import DocumentIdentification7
from . import ISODate
from . import LineItem13
from . import PartyIdentification26
from . import PaymentObligation2
from . import PaymentTerms5
from . import RequiredSubmission2
from . import RequiredSubmission3
from . import RequiredSubmission4
from . import RequiredSubmission6
from . import SettlementTerms3
from . import TradeFinanceService2Code
from . import YesNoIndicator

class Baseline5(base_types._BaseFieldType):

	__slots__ = ["_BllTo", "_Buyr", "_BuyrBk", "_BuyrSdSubmitgBk", "_CertDataSetReqrd", "_ComrclDataSetReqrd", "_Consgn", "_Goods", "_InsrncDataSetReqrd", "_InttToPayXpctd", "_LatstMtchDt", "_OthrCertDataSetReqrd", "_PmtOblgtn", "_PmtTerms", "_PurchsOrdrRef", "_Sellr", "_SellrBk", "_SellrSdSubmitgBk", "_ShipTo", "_SttlmTerms", "_SubmitrBaselnId", "_SvcCd", "_TrnsprtDataSetReqrd"]
	@property
	def BllTo(self):
		return self._BllTo

	@BllTo.setter
	def BllTo(self, value):
		self._BllTo = value if value is not None else base_types.UninitialisedField(self, 'BllTo', PartyIdentification26, False)

	@BllTo.deleter
	def BllTo(self):
		del self._BllTo
		self._BllTo = base_types.UninitialisedField(self, 'BllTo', PartyIdentification26, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if value is not None else base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

	@property
	def BuyrSdSubmitgBk(self):
		return self._BuyrSdSubmitgBk

	@BuyrSdSubmitgBk.setter
	def BuyrSdSubmitgBk(self, value):
		self._BuyrSdSubmitgBk = value if value is not None else base_types.UninitialisedField(self, 'BuyrSdSubmitgBk', BICIdentification1, True)

	@BuyrSdSubmitgBk.deleter
	def BuyrSdSubmitgBk(self):
		del self._BuyrSdSubmitgBk
		self._BuyrSdSubmitgBk = base_types.UninitialisedField(self, 'BuyrSdSubmitgBk', BICIdentification1, True)

	@property
	def CertDataSetReqrd(self):
		return self._CertDataSetReqrd

	@CertDataSetReqrd.setter
	def CertDataSetReqrd(self, value):
		self._CertDataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'CertDataSetReqrd', RequiredSubmission4, True)

	@CertDataSetReqrd.deleter
	def CertDataSetReqrd(self):
		del self._CertDataSetReqrd
		self._CertDataSetReqrd = base_types.UninitialisedField(self, 'CertDataSetReqrd', RequiredSubmission4, True)

	@property
	def ComrclDataSetReqrd(self):
		return self._ComrclDataSetReqrd

	@ComrclDataSetReqrd.setter
	def ComrclDataSetReqrd(self, value):
		self._ComrclDataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'ComrclDataSetReqrd', RequiredSubmission2, False)

	@ComrclDataSetReqrd.deleter
	def ComrclDataSetReqrd(self):
		del self._ComrclDataSetReqrd
		self._ComrclDataSetReqrd = base_types.UninitialisedField(self, 'ComrclDataSetReqrd', RequiredSubmission2, False)

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
	def Goods(self):
		return self._Goods

	@Goods.setter
	def Goods(self, value):
		self._Goods = value if value is not None else base_types.UninitialisedField(self, 'Goods', LineItem13, False)

	@Goods.deleter
	def Goods(self):
		del self._Goods
		self._Goods = base_types.UninitialisedField(self, 'Goods', LineItem13, False)

	@property
	def InsrncDataSetReqrd(self):
		return self._InsrncDataSetReqrd

	@InsrncDataSetReqrd.setter
	def InsrncDataSetReqrd(self, value):
		self._InsrncDataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'InsrncDataSetReqrd', RequiredSubmission3, False)

	@InsrncDataSetReqrd.deleter
	def InsrncDataSetReqrd(self):
		del self._InsrncDataSetReqrd
		self._InsrncDataSetReqrd = base_types.UninitialisedField(self, 'InsrncDataSetReqrd', RequiredSubmission3, False)

	@property
	def InttToPayXpctd(self):
		return self._InttToPayXpctd

	@InttToPayXpctd.setter
	def InttToPayXpctd(self, value):
		self._InttToPayXpctd = value if value is not None else base_types.UninitialisedField(self, 'InttToPayXpctd', YesNoIndicator, False)

	@InttToPayXpctd.deleter
	def InttToPayXpctd(self):
		del self._InttToPayXpctd
		self._InttToPayXpctd = base_types.UninitialisedField(self, 'InttToPayXpctd', YesNoIndicator, False)

	@property
	def LatstMtchDt(self):
		return self._LatstMtchDt

	@LatstMtchDt.setter
	def LatstMtchDt(self, value):
		self._LatstMtchDt = value if value is not None else base_types.UninitialisedField(self, 'LatstMtchDt', ISODate, False)

	@LatstMtchDt.deleter
	def LatstMtchDt(self):
		del self._LatstMtchDt
		self._LatstMtchDt = base_types.UninitialisedField(self, 'LatstMtchDt', ISODate, False)

	@property
	def OthrCertDataSetReqrd(self):
		return self._OthrCertDataSetReqrd

	@OthrCertDataSetReqrd.setter
	def OthrCertDataSetReqrd(self, value):
		self._OthrCertDataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'OthrCertDataSetReqrd', RequiredSubmission6, True)

	@OthrCertDataSetReqrd.deleter
	def OthrCertDataSetReqrd(self):
		del self._OthrCertDataSetReqrd
		self._OthrCertDataSetReqrd = base_types.UninitialisedField(self, 'OthrCertDataSetReqrd', RequiredSubmission6, True)

	@property
	def PmtOblgtn(self):
		return self._PmtOblgtn

	@PmtOblgtn.setter
	def PmtOblgtn(self, value):
		self._PmtOblgtn = value if value is not None else base_types.UninitialisedField(self, 'PmtOblgtn', PaymentObligation2, True)

	@PmtOblgtn.deleter
	def PmtOblgtn(self):
		del self._PmtOblgtn
		self._PmtOblgtn = base_types.UninitialisedField(self, 'PmtOblgtn', PaymentObligation2, True)

	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if value is not None else base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms5, True)

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = base_types.UninitialisedField(self, 'PmtTerms', PaymentTerms5, True)

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if value is not None else base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

	@property
	def SellrSdSubmitgBk(self):
		return self._SellrSdSubmitgBk

	@SellrSdSubmitgBk.setter
	def SellrSdSubmitgBk(self, value):
		self._SellrSdSubmitgBk = value if value is not None else base_types.UninitialisedField(self, 'SellrSdSubmitgBk', BICIdentification1, True)

	@SellrSdSubmitgBk.deleter
	def SellrSdSubmitgBk(self):
		del self._SellrSdSubmitgBk
		self._SellrSdSubmitgBk = base_types.UninitialisedField(self, 'SellrSdSubmitgBk', BICIdentification1, True)

	@property
	def ShipTo(self):
		return self._ShipTo

	@ShipTo.setter
	def ShipTo(self, value):
		self._ShipTo = value if value is not None else base_types.UninitialisedField(self, 'ShipTo', PartyIdentification26, False)

	@ShipTo.deleter
	def ShipTo(self):
		del self._ShipTo
		self._ShipTo = base_types.UninitialisedField(self, 'ShipTo', PartyIdentification26, False)

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if value is not None else base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@property
	def SubmitrBaselnId(self):
		return self._SubmitrBaselnId

	@SubmitrBaselnId.setter
	def SubmitrBaselnId(self, value):
		self._SubmitrBaselnId = value if value is not None else base_types.UninitialisedField(self, 'SubmitrBaselnId', DocumentIdentification1, False)

	@SubmitrBaselnId.deleter
	def SubmitrBaselnId(self):
		del self._SubmitrBaselnId
		self._SubmitrBaselnId = base_types.UninitialisedField(self, 'SubmitrBaselnId', DocumentIdentification1, False)

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if value is not None else base_types.UninitialisedField(self, 'SvcCd', TradeFinanceService2Code, False)

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = base_types.UninitialisedField(self, 'SvcCd', TradeFinanceService2Code, False)

	@property
	def TrnsprtDataSetReqrd(self):
		return self._TrnsprtDataSetReqrd

	@TrnsprtDataSetReqrd.setter
	def TrnsprtDataSetReqrd(self, value):
		self._TrnsprtDataSetReqrd = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtDataSetReqrd', RequiredSubmission2, False)

	@TrnsprtDataSetReqrd.deleter
	def TrnsprtDataSetReqrd(self):
		del self._TrnsprtDataSetReqrd
		self._TrnsprtDataSetReqrd = base_types.UninitialisedField(self, 'TrnsprtDataSetReqrd', RequiredSubmission2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrSdSubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertDataSetReqrd', type=RequiredSubmission4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclDataSetReqrd', type=RequiredSubmission2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgn', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Goods', type=LineItem13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncDataSetReqrd', type=RequiredSubmission3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InttToPayXpctd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstMtchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCertDataSetReqrd', type=RequiredSubmission6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtOblgtn', type=PaymentObligation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrSdSubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShipTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrBaselnId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=TradeFinanceService2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDataSetReqrd', type=RequiredSubmission2, min=0, max=1, mutex_group=None, array=False),
	))