from . import base_types
from .RequiredSubmission4 import RequiredSubmission4
from .DocumentIdentification7 import DocumentIdentification7
from .PaymentTerms5 import PaymentTerms5
from .RequiredSubmission6 import RequiredSubmission6
from .ISODate import ISODate
from .RequiredSubmission2 import RequiredSubmission2
from .LineItem13 import LineItem13
from .SettlementTerms3 import SettlementTerms3
from .DocumentIdentification1 import DocumentIdentification1
from .TradeFinanceService2Code import TradeFinanceService2Code
from .YesNoIndicator import YesNoIndicator
from .PaymentObligation2 import PaymentObligation2
from .RequiredSubmission3 import RequiredSubmission3
from .PartyIdentification26 import PartyIdentification26
from .BICIdentification1 import BICIdentification1

class Baseline5(base_types._BaseFieldType):

	__slots__ = ["_PmtTerms", "_Goods", "_BllTo", "_InsrncDataSetReqrd", "_TrnsprtDataSetReqrd", "_Buyr", "_LatstMtchDt", "_ShipTo", "_ComrclDataSetReqrd", "_BuyrBk", "_SellrBk", "_PurchsOrdrRef", "_PmtOblgtn", "_OthrCertDataSetReqrd", "_InttToPayXpctd", "_SttlmTerms", "_Sellr", "_SubmitrBaselnId", "_Consgn", "_CertDataSetReqrd", "_SvcCd", "_SellrSdSubmitgBk", "_BuyrSdSubmitgBk"]
	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if type(value) != base_types.auto else self.make_default("PmtTerms")

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = None

	@property
	def Goods(self):
		return self._Goods

	@Goods.setter
	def Goods(self, value):
		self._Goods = value if type(value) != base_types.auto else self.make_default("Goods")

	@Goods.deleter
	def Goods(self):
		del self._Goods
		self._Goods = None

	@property
	def BllTo(self):
		return self._BllTo

	@BllTo.setter
	def BllTo(self, value):
		self._BllTo = value if type(value) != base_types.auto else self.make_default("BllTo")

	@BllTo.deleter
	def BllTo(self):
		del self._BllTo
		self._BllTo = None

	@property
	def InsrncDataSetReqrd(self):
		return self._InsrncDataSetReqrd

	@InsrncDataSetReqrd.setter
	def InsrncDataSetReqrd(self, value):
		self._InsrncDataSetReqrd = value if type(value) != base_types.auto else self.make_default("InsrncDataSetReqrd")

	@InsrncDataSetReqrd.deleter
	def InsrncDataSetReqrd(self):
		del self._InsrncDataSetReqrd
		self._InsrncDataSetReqrd = None

	@property
	def TrnsprtDataSetReqrd(self):
		return self._TrnsprtDataSetReqrd

	@TrnsprtDataSetReqrd.setter
	def TrnsprtDataSetReqrd(self, value):
		self._TrnsprtDataSetReqrd = value if type(value) != base_types.auto else self.make_default("TrnsprtDataSetReqrd")

	@TrnsprtDataSetReqrd.deleter
	def TrnsprtDataSetReqrd(self):
		del self._TrnsprtDataSetReqrd
		self._TrnsprtDataSetReqrd = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def LatstMtchDt(self):
		return self._LatstMtchDt

	@LatstMtchDt.setter
	def LatstMtchDt(self, value):
		self._LatstMtchDt = value if type(value) != base_types.auto else self.make_default("LatstMtchDt")

	@LatstMtchDt.deleter
	def LatstMtchDt(self):
		del self._LatstMtchDt
		self._LatstMtchDt = None

	@property
	def ShipTo(self):
		return self._ShipTo

	@ShipTo.setter
	def ShipTo(self, value):
		self._ShipTo = value if type(value) != base_types.auto else self.make_default("ShipTo")

	@ShipTo.deleter
	def ShipTo(self):
		del self._ShipTo
		self._ShipTo = None

	@property
	def ComrclDataSetReqrd(self):
		return self._ComrclDataSetReqrd

	@ComrclDataSetReqrd.setter
	def ComrclDataSetReqrd(self, value):
		self._ComrclDataSetReqrd = value if type(value) != base_types.auto else self.make_default("ComrclDataSetReqrd")

	@ComrclDataSetReqrd.deleter
	def ComrclDataSetReqrd(self):
		del self._ComrclDataSetReqrd
		self._ComrclDataSetReqrd = None

	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if type(value) != base_types.auto else self.make_default("BuyrBk")

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = None

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if type(value) != base_types.auto else self.make_default("SellrBk")

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = None

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != base_types.auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def PmtOblgtn(self):
		return self._PmtOblgtn

	@PmtOblgtn.setter
	def PmtOblgtn(self, value):
		self._PmtOblgtn = value if type(value) != base_types.auto else self.make_default("PmtOblgtn")

	@PmtOblgtn.deleter
	def PmtOblgtn(self):
		del self._PmtOblgtn
		self._PmtOblgtn = None

	@property
	def OthrCertDataSetReqrd(self):
		return self._OthrCertDataSetReqrd

	@OthrCertDataSetReqrd.setter
	def OthrCertDataSetReqrd(self, value):
		self._OthrCertDataSetReqrd = value if type(value) != base_types.auto else self.make_default("OthrCertDataSetReqrd")

	@OthrCertDataSetReqrd.deleter
	def OthrCertDataSetReqrd(self):
		del self._OthrCertDataSetReqrd
		self._OthrCertDataSetReqrd = None

	@property
	def InttToPayXpctd(self):
		return self._InttToPayXpctd

	@InttToPayXpctd.setter
	def InttToPayXpctd(self, value):
		self._InttToPayXpctd = value if type(value) != base_types.auto else self.make_default("InttToPayXpctd")

	@InttToPayXpctd.deleter
	def InttToPayXpctd(self):
		del self._InttToPayXpctd
		self._InttToPayXpctd = None

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if type(value) != base_types.auto else self.make_default("SttlmTerms")

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != base_types.auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def SubmitrBaselnId(self):
		return self._SubmitrBaselnId

	@SubmitrBaselnId.setter
	def SubmitrBaselnId(self, value):
		self._SubmitrBaselnId = value if type(value) != base_types.auto else self.make_default("SubmitrBaselnId")

	@SubmitrBaselnId.deleter
	def SubmitrBaselnId(self):
		del self._SubmitrBaselnId
		self._SubmitrBaselnId = None

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
	def CertDataSetReqrd(self):
		return self._CertDataSetReqrd

	@CertDataSetReqrd.setter
	def CertDataSetReqrd(self, value):
		self._CertDataSetReqrd = value if type(value) != base_types.auto else self.make_default("CertDataSetReqrd")

	@CertDataSetReqrd.deleter
	def CertDataSetReqrd(self):
		del self._CertDataSetReqrd
		self._CertDataSetReqrd = None

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if type(value) != base_types.auto else self.make_default("SvcCd")

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = None

	@property
	def SellrSdSubmitgBk(self):
		return self._SellrSdSubmitgBk

	@SellrSdSubmitgBk.setter
	def SellrSdSubmitgBk(self, value):
		self._SellrSdSubmitgBk = value if type(value) != base_types.auto else self.make_default("SellrSdSubmitgBk")

	@SellrSdSubmitgBk.deleter
	def SellrSdSubmitgBk(self):
		del self._SellrSdSubmitgBk
		self._SellrSdSubmitgBk = None

	@property
	def BuyrSdSubmitgBk(self):
		return self._BuyrSdSubmitgBk

	@BuyrSdSubmitgBk.setter
	def BuyrSdSubmitgBk(self, value):
		self._BuyrSdSubmitgBk = value if type(value) != base_types.auto else self.make_default("BuyrSdSubmitgBk")

	@BuyrSdSubmitgBk.deleter
	def BuyrSdSubmitgBk(self):
		del self._BuyrSdSubmitgBk
		self._BuyrSdSubmitgBk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtTerms', type=PaymentTerms5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Goods', type=LineItem13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncDataSetReqrd', type=RequiredSubmission3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDataSetReqrd', type=RequiredSubmission2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatstMtchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipTo', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclDataSetReqrd', type=RequiredSubmission2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtOblgtn', type=PaymentObligation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCertDataSetReqrd', type=RequiredSubmission6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InttToPayXpctd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrBaselnId', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Consgn', type=PartyIdentification26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertDataSetReqrd', type=RequiredSubmission4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCd', type=TradeFinanceService2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrSdSubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrSdSubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

