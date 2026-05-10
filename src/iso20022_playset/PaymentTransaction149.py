import base_types
import SupplementaryData1
import Charges16
import UUIDv4Identifier
import ISODate
import OriginalGroupInformation29
import Priority3Code
import ActiveCurrencyAndAmount
import BaseOneRate
import Max35Text
import OriginalTransactionReference42
import ActiveOrHistoricCurrencyAndAmount
import PaymentReversalReason10
import SettlementDateTimeIndication1
import ChargeBearerType1Code
import BranchAndFinancialInstitutionIdentification8

class PaymentTransaction149(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlUETR", "_SttlmPrty", "_OrgnlGrpInf", "_XchgRate", "_InstgAgt", "_OrgnlClrSysRef", "_IntrBkSttlmDt", "_OrgnlEndToEndId", "_OrgnlIntrBkSttlmAmt", "_InstdAgt", "_ChrgBr", "_ChrgsInf", "_OrgnlInstrId", "_RvsdIntrBkSttlmAmt", "_SttlmTmIndctn", "_OrgnlTxRef", "_RvslId", "_CompstnAmt", "_RvslRsnInf", "_OrgnlTxId", "_RvsdInstdAmt"]
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
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def OrgnlClrSysRef(self):
		return self._OrgnlClrSysRef

	@OrgnlClrSysRef.setter
	def OrgnlClrSysRef(self, value):
		self._OrgnlClrSysRef = value if type(value) != auto else self.make_default("OrgnlClrSysRef")

	@OrgnlClrSysRef.deleter
	def OrgnlClrSysRef(self):
		del self._OrgnlClrSysRef
		self._OrgnlClrSysRef = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def OrgnlIntrBkSttlmAmt(self):
		return self._OrgnlIntrBkSttlmAmt

	@OrgnlIntrBkSttlmAmt.setter
	def OrgnlIntrBkSttlmAmt(self, value):
		self._OrgnlIntrBkSttlmAmt = value if type(value) != auto else self.make_default("OrgnlIntrBkSttlmAmt")

	@OrgnlIntrBkSttlmAmt.deleter
	def OrgnlIntrBkSttlmAmt(self):
		del self._OrgnlIntrBkSttlmAmt
		self._OrgnlIntrBkSttlmAmt = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if type(value) != auto else self.make_default("ChrgsInf")

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def RvsdIntrBkSttlmAmt(self):
		return self._RvsdIntrBkSttlmAmt

	@RvsdIntrBkSttlmAmt.setter
	def RvsdIntrBkSttlmAmt(self, value):
		self._RvsdIntrBkSttlmAmt = value if type(value) != auto else self.make_default("RvsdIntrBkSttlmAmt")

	@RvsdIntrBkSttlmAmt.deleter
	def RvsdIntrBkSttlmAmt(self):
		del self._RvsdIntrBkSttlmAmt
		self._RvsdIntrBkSttlmAmt = None

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def RvslId(self):
		return self._RvslId

	@RvslId.setter
	def RvslId(self, value):
		self._RvslId = value if type(value) != auto else self.make_default("RvslId")

	@RvslId.deleter
	def RvslId(self):
		del self._RvslId
		self._RvslId = None

	@property
	def CompstnAmt(self):
		return self._CompstnAmt

	@CompstnAmt.setter
	def CompstnAmt(self, value):
		self._CompstnAmt = value if type(value) != auto else self.make_default("CompstnAmt")

	@CompstnAmt.deleter
	def CompstnAmt(self):
		del self._CompstnAmt
		self._CompstnAmt = None

	@property
	def RvslRsnInf(self):
		return self._RvslRsnInf

	@RvslRsnInf.setter
	def RvslRsnInf(self, value):
		self._RvslRsnInf = value if type(value) != auto else self.make_default("RvslRsnInf")

	@RvslRsnInf.deleter
	def RvslRsnInf(self):
		del self._RvslRsnInf
		self._RvslRsnInf = None

	@property
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if type(value) != auto else self.make_default("OrgnlTxId")

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = None

	@property
	def RvsdInstdAmt(self):
		return self._RvsdInstdAmt

	@RvsdInstdAmt.setter
	def RvsdInstdAmt(self, value):
		self._RvsdInstdAmt = value if type(value) != auto else self.make_default("RvsdInstdAmt")

	@RvsdInstdAmt.deleter
	def RvsdInstdAmt(self):
		del self._RvsdInstdAmt
		self._RvsdInstdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsdIntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CompstnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsnInf', type=PaymentReversalReason10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsdInstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

