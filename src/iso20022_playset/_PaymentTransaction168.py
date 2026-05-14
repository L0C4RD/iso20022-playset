from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._Charges16 import Charges16
from ._CurrencyExchange26 import CurrencyExchange26
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._OriginalGroupInformation33 import OriginalGroupInformation33
from ._OriginalTransactionReference45 import OriginalTransactionReference45
from ._PaymentReturnReason7 import PaymentReturnReason7
from ._PaymentTypeInformation28 import PaymentTypeInformation28
from ._Priority3Code import Priority3Code
from ._SettlementDateTimeIndication1 import SettlementDateTimeIndication1
from ._SettlementTimeRequest2 import SettlementTimeRequest2
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionParties11 import TransactionParties11
from ._UUIDv4Identifier import UUIDv4Identifier

class PaymentTransaction168(base_types._BaseFieldType):

	__slots__ = ["_AgrdRate", "_ChrgBr", "_ChrgsInf", "_ClrSysRef", "_CompstnAmt", "_InstdAgt", "_InstgAgt", "_IntrBkSttlmDt", "_OrgnlClrSysRef", "_OrgnlEndToEndId", "_OrgnlGrpInf", "_OrgnlInstrId", "_OrgnlIntrBkSttlmAmt", "_OrgnlIntrBkSttlmDt", "_OrgnlTxId", "_OrgnlTxRef", "_OrgnlUETR", "_PmtTpInf", "_RtrChain", "_RtrId", "_RtrRsnInf", "_RtrdInstdAmt", "_RtrdIntrBkSttlmAmt", "_SplmtryData", "_SttlmPrty", "_SttlmTmIndctn", "_SttlmTmReq", "_XchgRate"]
	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if type(value) != base_types.auto else self.make_default("AgrdRate")

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if type(value) != base_types.auto else self.make_default("ChrgsInf")

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = None

	@property
	def ClrSysRef(self):
		return self._ClrSysRef

	@ClrSysRef.setter
	def ClrSysRef(self, value):
		self._ClrSysRef = value if type(value) != base_types.auto else self.make_default("ClrSysRef")

	@ClrSysRef.deleter
	def ClrSysRef(self):
		del self._ClrSysRef
		self._ClrSysRef = None

	@property
	def CompstnAmt(self):
		return self._CompstnAmt

	@CompstnAmt.setter
	def CompstnAmt(self, value):
		self._CompstnAmt = value if type(value) != base_types.auto else self.make_default("CompstnAmt")

	@CompstnAmt.deleter
	def CompstnAmt(self):
		del self._CompstnAmt
		self._CompstnAmt = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != base_types.auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != base_types.auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def OrgnlClrSysRef(self):
		return self._OrgnlClrSysRef

	@OrgnlClrSysRef.setter
	def OrgnlClrSysRef(self, value):
		self._OrgnlClrSysRef = value if type(value) != base_types.auto else self.make_default("OrgnlClrSysRef")

	@OrgnlClrSysRef.deleter
	def OrgnlClrSysRef(self):
		del self._OrgnlClrSysRef
		self._OrgnlClrSysRef = None

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != base_types.auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != base_types.auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def OrgnlIntrBkSttlmAmt(self):
		return self._OrgnlIntrBkSttlmAmt

	@OrgnlIntrBkSttlmAmt.setter
	def OrgnlIntrBkSttlmAmt(self, value):
		self._OrgnlIntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("OrgnlIntrBkSttlmAmt")

	@OrgnlIntrBkSttlmAmt.deleter
	def OrgnlIntrBkSttlmAmt(self):
		del self._OrgnlIntrBkSttlmAmt
		self._OrgnlIntrBkSttlmAmt = None

	@property
	def OrgnlIntrBkSttlmDt(self):
		return self._OrgnlIntrBkSttlmDt

	@OrgnlIntrBkSttlmDt.setter
	def OrgnlIntrBkSttlmDt(self, value):
		self._OrgnlIntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("OrgnlIntrBkSttlmDt")

	@OrgnlIntrBkSttlmDt.deleter
	def OrgnlIntrBkSttlmDt(self):
		del self._OrgnlIntrBkSttlmDt
		self._OrgnlIntrBkSttlmDt = None

	@property
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if type(value) != base_types.auto else self.make_default("OrgnlTxId")

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != base_types.auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != base_types.auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def RtrChain(self):
		return self._RtrChain

	@RtrChain.setter
	def RtrChain(self, value):
		self._RtrChain = value if type(value) != base_types.auto else self.make_default("RtrChain")

	@RtrChain.deleter
	def RtrChain(self):
		del self._RtrChain
		self._RtrChain = None

	@property
	def RtrId(self):
		return self._RtrId

	@RtrId.setter
	def RtrId(self, value):
		self._RtrId = value if type(value) != base_types.auto else self.make_default("RtrId")

	@RtrId.deleter
	def RtrId(self):
		del self._RtrId
		self._RtrId = None

	@property
	def RtrRsnInf(self):
		return self._RtrRsnInf

	@RtrRsnInf.setter
	def RtrRsnInf(self, value):
		self._RtrRsnInf = value if type(value) != base_types.auto else self.make_default("RtrRsnInf")

	@RtrRsnInf.deleter
	def RtrRsnInf(self):
		del self._RtrRsnInf
		self._RtrRsnInf = None

	@property
	def RtrdInstdAmt(self):
		return self._RtrdInstdAmt

	@RtrdInstdAmt.setter
	def RtrdInstdAmt(self, value):
		self._RtrdInstdAmt = value if type(value) != base_types.auto else self.make_default("RtrdInstdAmt")

	@RtrdInstdAmt.deleter
	def RtrdInstdAmt(self):
		del self._RtrdInstdAmt
		self._RtrdInstdAmt = None

	@property
	def RtrdIntrBkSttlmAmt(self):
		return self._RtrdIntrBkSttlmAmt

	@RtrdIntrBkSttlmAmt.setter
	def RtrdIntrBkSttlmAmt(self, value):
		self._RtrdIntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("RtrdIntrBkSttlmAmt")

	@RtrdIntrBkSttlmAmt.deleter
	def RtrdIntrBkSttlmAmt(self):
		del self._RtrdIntrBkSttlmAmt
		self._RtrdIntrBkSttlmAmt = None

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
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != base_types.auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != base_types.auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	@property
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if type(value) != base_types.auto else self.make_default("SttlmTmReq")

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdRate', type=CurrencyExchange26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrChain', type=TransactionParties11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrRsnInf', type=PaymentReturnReason7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtrdInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrdIntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

