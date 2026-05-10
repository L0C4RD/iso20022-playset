import base_types
import NovationStatus1Code
import DateAndDateTimeChoice
import PercentageRate
import SupplementaryData1
import CounterpartyIdentification3Choice
import LEIIdentifier
import Max105Text
import TransactionOperationType1Code
import ActiveCurrencyAndAmount
import ISODate
import OvernightIndexSwapType1Code

class OvernightIndexSwapTransaction4(base_types._BaseFieldType):

	__slots__ = ["_TradDt", "_UnqTxIdr", "_CtrPtyId", "_RltdPrtryTxId", "_NvtnSts", "_TxTp", "_FxdIntrstRate", "_BrnchId", "_SplmtryData", "_CtrPtyPrtryTxId", "_TxNmnlAmt", "_RptdTxSts", "_MtrtyDt", "_PrtryTxId", "_StartDt"]
	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

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

	@property
	def RltdPrtryTxId(self):
		return self._RltdPrtryTxId

	@RltdPrtryTxId.setter
	def RltdPrtryTxId(self, value):
		self._RltdPrtryTxId = value if type(value) != auto else self.make_default("RltdPrtryTxId")

	@RltdPrtryTxId.deleter
	def RltdPrtryTxId(self):
		del self._RltdPrtryTxId
		self._RltdPrtryTxId = None

	@property
	def NvtnSts(self):
		return self._NvtnSts

	@NvtnSts.setter
	def NvtnSts(self, value):
		self._NvtnSts = value if type(value) != auto else self.make_default("NvtnSts")

	@NvtnSts.deleter
	def NvtnSts(self):
		del self._NvtnSts
		self._NvtnSts = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if type(value) != auto else self.make_default("FxdIntrstRate")

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = None

	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

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
	def CtrPtyPrtryTxId(self):
		return self._CtrPtyPrtryTxId

	@CtrPtyPrtryTxId.setter
	def CtrPtyPrtryTxId(self, value):
		self._CtrPtyPrtryTxId = value if type(value) != auto else self.make_default("CtrPtyPrtryTxId")

	@CtrPtyPrtryTxId.deleter
	def CtrPtyPrtryTxId(self):
		del self._CtrPtyPrtryTxId
		self._CtrPtyPrtryTxId = None

	@property
	def TxNmnlAmt(self):
		return self._TxNmnlAmt

	@TxNmnlAmt.setter
	def TxNmnlAmt(self, value):
		self._TxNmnlAmt = value if type(value) != auto else self.make_default("TxNmnlAmt")

	@TxNmnlAmt.deleter
	def TxNmnlAmt(self):
		del self._TxNmnlAmt
		self._TxNmnlAmt = None

	@property
	def RptdTxSts(self):
		return self._RptdTxSts

	@RptdTxSts.setter
	def RptdTxSts(self, value):
		self._RptdTxSts = value if type(value) != auto else self.make_default("RptdTxSts")

	@RptdTxSts.deleter
	def RptdTxSts(self):
		del self._RptdTxSts
		self._RptdTxSts = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def PrtryTxId(self):
		return self._PrtryTxId

	@PrtryTxId.setter
	def PrtryTxId(self, value):
		self._PrtryTxId = value if type(value) != auto else self.make_default("PrtryTxId")

	@PrtryTxId.deleter
	def PrtryTxId(self):
		del self._PrtryTxId
		self._PrtryTxId = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradDt', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvtnSts', type=NovationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=OvernightIndexSwapType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdIntrstRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrnchId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxNmnlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdTxSts', type=TransactionOperationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryTxId', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

