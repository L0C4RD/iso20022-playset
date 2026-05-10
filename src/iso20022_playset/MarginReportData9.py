from . import base_types
from .ISODate import ISODate
from .TechnicalAttributes6 import TechnicalAttributes6
from .PostedMarginOrCollateral6 import PostedMarginOrCollateral6
from .UniqueTransactionIdentifier2Choice import UniqueTransactionIdentifier2Choice
from .SupplementaryData1 import SupplementaryData1
from .MarginCollateralReport5 import MarginCollateralReport5
from .TrueFalseIndicator import TrueFalseIndicator
from .ReceivedMarginOrCollateral6 import ReceivedMarginOrCollateral6
from .TradeCounterpartyReport20 import TradeCounterpartyReport20
from .ISODateTime import ISODateTime

class MarginReportData9(base_types._BaseFieldType):

	__slots__ = ["_RptgTmStmp", "_TechAttrbts", "_TxId", "_SplmtryData", "_RcvdMrgnOrColl", "_CtrPtyRatgTrggrInd", "_Coll", "_CtrPtyRatgThrshldInd", "_EvtDt", "_PstdMrgnOrColl", "_CtrPtyId"]
	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if type(value) != auto else self.make_default("RptgTmStmp")

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = None

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if type(value) != auto else self.make_default("TechAttrbts")

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if type(value) != auto else self.make_default("RcvdMrgnOrColl")

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = None

	@property
	def CtrPtyRatgTrggrInd(self):
		return self._CtrPtyRatgTrggrInd

	@CtrPtyRatgTrggrInd.setter
	def CtrPtyRatgTrggrInd(self, value):
		self._CtrPtyRatgTrggrInd = value if type(value) != auto else self.make_default("CtrPtyRatgTrggrInd")

	@CtrPtyRatgTrggrInd.deleter
	def CtrPtyRatgTrggrInd(self):
		del self._CtrPtyRatgTrggrInd
		self._CtrPtyRatgTrggrInd = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	@property
	def CtrPtyRatgThrshldInd(self):
		return self._CtrPtyRatgThrshldInd

	@CtrPtyRatgThrshldInd.setter
	def CtrPtyRatgThrshldInd(self, value):
		self._CtrPtyRatgThrshldInd = value if type(value) != auto else self.make_default("CtrPtyRatgThrshldInd")

	@CtrPtyRatgThrshldInd.deleter
	def CtrPtyRatgThrshldInd(self):
		del self._CtrPtyRatgThrshldInd
		self._CtrPtyRatgThrshldInd = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if type(value) != auto else self.make_default("PstdMrgnOrColl")

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=TechnicalAttributes6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvdMrgnOrColl', type=ReceivedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRatgTrggrInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=MarginCollateralReport5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRatgThrshldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=TradeCounterpartyReport20, min=1, max=1, mutex_group=None, array=False),
	))

