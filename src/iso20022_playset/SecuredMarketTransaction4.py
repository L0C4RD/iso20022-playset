from . import base_types
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .TransactionOperationType1Code import TransactionOperationType1Code
from .InterestRateType1Code import InterestRateType1Code
from .SupplementaryData1 import SupplementaryData1
from .PercentageRate import PercentageRate
from .BrokeredDeal1Code import BrokeredDeal1Code
from .CounterpartyIdentification3Choice import CounterpartyIdentification3Choice
from .MoneyMarketTransactionType1Code import MoneyMarketTransactionType1Code
from .LEIIdentifier import LEIIdentifier
from .Collateral18 import Collateral18
from .ISODate import ISODate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Max105Text import Max105Text
from .FloatingRateNote2 import FloatingRateNote2
from .NovationStatus1Code import NovationStatus1Code

class SecuredMarketTransaction4(base_types._BaseFieldType):

	__slots__ = ["_TxNmnlAmt", "_BrnchId", "_Coll", "_TxTp", "_CtrPtyPrtryTxId", "_NvtnSts", "_MtrtyDt", "_DealRate", "_SttlmDt", "_FltgRateRpAgrmt", "_PrtryTxId", "_RltdPrtryTxId", "_SplmtryData", "_UnqTxIdr", "_TrptyAgtId", "_TradDt", "_CtrPtyId", "_RptdTxSts", "_BrkrdDeal", "_RateTp"]
	@property
	def TxNmnlAmt(self):
		return self._TxNmnlAmt

	@TxNmnlAmt.setter
	def TxNmnlAmt(self, value):
		self._TxNmnlAmt = value if type(value) != base_types.auto else self.make_default("TxNmnlAmt")

	@TxNmnlAmt.deleter
	def TxNmnlAmt(self):
		del self._TxNmnlAmt
		self._TxNmnlAmt = None

	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != base_types.auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != base_types.auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def CtrPtyPrtryTxId(self):
		return self._CtrPtyPrtryTxId

	@CtrPtyPrtryTxId.setter
	def CtrPtyPrtryTxId(self, value):
		self._CtrPtyPrtryTxId = value if type(value) != base_types.auto else self.make_default("CtrPtyPrtryTxId")

	@CtrPtyPrtryTxId.deleter
	def CtrPtyPrtryTxId(self):
		del self._CtrPtyPrtryTxId
		self._CtrPtyPrtryTxId = None

	@property
	def NvtnSts(self):
		return self._NvtnSts

	@NvtnSts.setter
	def NvtnSts(self, value):
		self._NvtnSts = value if type(value) != base_types.auto else self.make_default("NvtnSts")

	@NvtnSts.deleter
	def NvtnSts(self):
		del self._NvtnSts
		self._NvtnSts = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def DealRate(self):
		return self._DealRate

	@DealRate.setter
	def DealRate(self, value):
		self._DealRate = value if type(value) != base_types.auto else self.make_default("DealRate")

	@DealRate.deleter
	def DealRate(self):
		del self._DealRate
		self._DealRate = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def FltgRateRpAgrmt(self):
		return self._FltgRateRpAgrmt

	@FltgRateRpAgrmt.setter
	def FltgRateRpAgrmt(self, value):
		self._FltgRateRpAgrmt = value if type(value) != base_types.auto else self.make_default("FltgRateRpAgrmt")

	@FltgRateRpAgrmt.deleter
	def FltgRateRpAgrmt(self):
		del self._FltgRateRpAgrmt
		self._FltgRateRpAgrmt = None

	@property
	def PrtryTxId(self):
		return self._PrtryTxId

	@PrtryTxId.setter
	def PrtryTxId(self, value):
		self._PrtryTxId = value if type(value) != base_types.auto else self.make_default("PrtryTxId")

	@PrtryTxId.deleter
	def PrtryTxId(self):
		del self._PrtryTxId
		self._PrtryTxId = None

	@property
	def RltdPrtryTxId(self):
		return self._RltdPrtryTxId

	@RltdPrtryTxId.setter
	def RltdPrtryTxId(self, value):
		self._RltdPrtryTxId = value if type(value) != base_types.auto else self.make_default("RltdPrtryTxId")

	@RltdPrtryTxId.deleter
	def RltdPrtryTxId(self):
		del self._RltdPrtryTxId
		self._RltdPrtryTxId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def TrptyAgtId(self):
		return self._TrptyAgtId

	@TrptyAgtId.setter
	def TrptyAgtId(self, value):
		self._TrptyAgtId = value if type(value) != base_types.auto else self.make_default("TrptyAgtId")

	@TrptyAgtId.deleter
	def TrptyAgtId(self):
		del self._TrptyAgtId
		self._TrptyAgtId = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != base_types.auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def RptdTxSts(self):
		return self._RptdTxSts

	@RptdTxSts.setter
	def RptdTxSts(self, value):
		self._RptdTxSts = value if type(value) != base_types.auto else self.make_default("RptdTxSts")

	@RptdTxSts.deleter
	def RptdTxSts(self):
		del self._RptdTxSts
		self._RptdTxSts = None

	@property
	def BrkrdDeal(self):
		return self._BrkrdDeal

	@BrkrdDeal.setter
	def BrkrdDeal(self, value):
		self._BrkrdDeal = value if type(value) != base_types.auto else self.make_default("BrkrdDeal")

	@BrkrdDeal.deleter
	def BrkrdDeal(self):
		del self._BrkrdDeal
		self._BrkrdDeal = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxNmnlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrnchId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=Collateral18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=MoneyMarketTransactionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvtnSts', type=NovationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgRateRpAgrmt', type=FloatingRateNote2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryTxId', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqTxIdr', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdTxSts', type=TransactionOperationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrdDeal', type=BrokeredDeal1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=InterestRateType1Code, min=1, max=1, mutex_group=None, array=False),
	))

