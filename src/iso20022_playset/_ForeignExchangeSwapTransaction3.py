# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CounterpartyIdentification3Choice
from . import DateAndDateTimeChoice
from . import ForeignExchange1
from . import ISODate
from . import LEIIdentifier
from . import Max105Text
from . import NovationStatus1Code
from . import SecuritiesTransactionType15Code
from . import SupplementaryData1
from . import TransactionOperationType1Code

class ForeignExchangeSwapTransaction3(base_types._BaseFieldType):

	__slots__ = ["_BrnchId", "_CtrPtyId", "_CtrPtyPrtryTxId", "_FX", "_MtrtyDt", "_NvtnSts", "_PrtryTxId", "_RltdPrtryTxId", "_RptdTxSts", "_SplmtryData", "_SpotValDt", "_TradDt", "_TxNmnlAmt", "_TxTp", "_UnqTxIdr"]
	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if value is not None else base_types.UninitialisedField(self, 'BrnchId', LEIIdentifier, False)

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = base_types.UninitialisedField(self, 'BrnchId', LEIIdentifier, False)

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyIdentification3Choice, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyIdentification3Choice, False)

	@property
	def CtrPtyPrtryTxId(self):
		return self._CtrPtyPrtryTxId

	@CtrPtyPrtryTxId.setter
	def CtrPtyPrtryTxId(self, value):
		self._CtrPtyPrtryTxId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyPrtryTxId', Max105Text, False)

	@CtrPtyPrtryTxId.deleter
	def CtrPtyPrtryTxId(self):
		del self._CtrPtyPrtryTxId
		self._CtrPtyPrtryTxId = base_types.UninitialisedField(self, 'CtrPtyPrtryTxId', Max105Text, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', ForeignExchange1, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', ForeignExchange1, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def NvtnSts(self):
		return self._NvtnSts

	@NvtnSts.setter
	def NvtnSts(self, value):
		self._NvtnSts = value if value is not None else base_types.UninitialisedField(self, 'NvtnSts', NovationStatus1Code, False)

	@NvtnSts.deleter
	def NvtnSts(self):
		del self._NvtnSts
		self._NvtnSts = base_types.UninitialisedField(self, 'NvtnSts', NovationStatus1Code, False)

	@property
	def PrtryTxId(self):
		return self._PrtryTxId

	@PrtryTxId.setter
	def PrtryTxId(self, value):
		self._PrtryTxId = value if value is not None else base_types.UninitialisedField(self, 'PrtryTxId', Max105Text, False)

	@PrtryTxId.deleter
	def PrtryTxId(self):
		del self._PrtryTxId
		self._PrtryTxId = base_types.UninitialisedField(self, 'PrtryTxId', Max105Text, False)

	@property
	def RltdPrtryTxId(self):
		return self._RltdPrtryTxId

	@RltdPrtryTxId.setter
	def RltdPrtryTxId(self, value):
		self._RltdPrtryTxId = value if value is not None else base_types.UninitialisedField(self, 'RltdPrtryTxId', Max105Text, False)

	@RltdPrtryTxId.deleter
	def RltdPrtryTxId(self):
		del self._RltdPrtryTxId
		self._RltdPrtryTxId = base_types.UninitialisedField(self, 'RltdPrtryTxId', Max105Text, False)

	@property
	def RptdTxSts(self):
		return self._RptdTxSts

	@RptdTxSts.setter
	def RptdTxSts(self, value):
		self._RptdTxSts = value if value is not None else base_types.UninitialisedField(self, 'RptdTxSts', TransactionOperationType1Code, False)

	@RptdTxSts.deleter
	def RptdTxSts(self):
		del self._RptdTxSts
		self._RptdTxSts = base_types.UninitialisedField(self, 'RptdTxSts', TransactionOperationType1Code, False)

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
	def SpotValDt(self):
		return self._SpotValDt

	@SpotValDt.setter
	def SpotValDt(self, value):
		self._SpotValDt = value if value is not None else base_types.UninitialisedField(self, 'SpotValDt', ISODate, False)

	@SpotValDt.deleter
	def SpotValDt(self):
		del self._SpotValDt
		self._SpotValDt = base_types.UninitialisedField(self, 'SpotValDt', ISODate, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', DateAndDateTimeChoice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', DateAndDateTimeChoice, False)

	@property
	def TxNmnlAmt(self):
		return self._TxNmnlAmt

	@TxNmnlAmt.setter
	def TxNmnlAmt(self, value):
		self._TxNmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'TxNmnlAmt', ActiveCurrencyAndAmount, False)

	@TxNmnlAmt.deleter
	def TxNmnlAmt(self):
		del self._TxNmnlAmt
		self._TxNmnlAmt = base_types.UninitialisedField(self, 'TxNmnlAmt', ActiveCurrencyAndAmount, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', SecuritiesTransactionType15Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', SecuritiesTransactionType15Code, False)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', Max105Text, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', Max105Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrnchId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvtnSts', type=NovationStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryTxId', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPrtryTxId', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdTxSts', type=TransactionOperationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpotValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxNmnlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=SecuritiesTransactionType15Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
	))