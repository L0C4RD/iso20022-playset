# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractModification8
from . import ISODate
from . import ISODateTime
from . import MarginCollateralReport5
from . import PostedMarginOrCollateral6
from . import ReceivedMarginOrCollateral6
from . import SupplementaryData1
from . import TechnicalAttributes6
from . import TradeCounterpartyReport20
from . import TrueFalseIndicator
from . import UniqueTransactionIdentifier2Choice

class MarginReportData10(base_types._BaseFieldType):

	__slots__ = ["_Coll", "_CtrPtyId", "_CtrPtyRatgThrshldInd", "_CtrPtyRatgTrggrInd", "_CtrctMod", "_EvtDt", "_PstdMrgnOrColl", "_RcvdMrgnOrColl", "_RptgTmStmp", "_SplmtryData", "_TechAttrbts", "_TxId"]
	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', MarginCollateralReport5, False)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', MarginCollateralReport5, False)

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', TradeCounterpartyReport20, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', TradeCounterpartyReport20, False)

	@property
	def CtrPtyRatgThrshldInd(self):
		return self._CtrPtyRatgThrshldInd

	@CtrPtyRatgThrshldInd.setter
	def CtrPtyRatgThrshldInd(self, value):
		self._CtrPtyRatgThrshldInd = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRatgThrshldInd', TrueFalseIndicator, False)

	@CtrPtyRatgThrshldInd.deleter
	def CtrPtyRatgThrshldInd(self):
		del self._CtrPtyRatgThrshldInd
		self._CtrPtyRatgThrshldInd = base_types.UninitialisedField(self, 'CtrPtyRatgThrshldInd', TrueFalseIndicator, False)

	@property
	def CtrPtyRatgTrggrInd(self):
		return self._CtrPtyRatgTrggrInd

	@CtrPtyRatgTrggrInd.setter
	def CtrPtyRatgTrggrInd(self, value):
		self._CtrPtyRatgTrggrInd = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRatgTrggrInd', TrueFalseIndicator, False)

	@CtrPtyRatgTrggrInd.deleter
	def CtrPtyRatgTrggrInd(self):
		del self._CtrPtyRatgTrggrInd
		self._CtrPtyRatgTrggrInd = base_types.UninitialisedField(self, 'CtrPtyRatgTrggrInd', TrueFalseIndicator, False)

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if value is not None else base_types.UninitialisedField(self, 'CtrctMod', ContractModification8, False)

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = base_types.UninitialisedField(self, 'CtrctMod', ContractModification8, False)

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral6, False)

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral6, False)

	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral6, False)

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral6, False)

	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if value is not None else base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TechAttrbts', TechnicalAttributes6, False)

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = base_types.UninitialisedField(self, 'TechAttrbts', TechnicalAttributes6, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', UniqueTransactionIdentifier2Choice, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', UniqueTransactionIdentifier2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coll', type=MarginCollateralReport5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=TradeCounterpartyReport20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRatgThrshldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRatgTrggrInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdMrgnOrColl', type=ReceivedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechAttrbts', type=TechnicalAttributes6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
	))