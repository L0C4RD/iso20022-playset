import base_types
import RegulatoryTradingCapacity1Code
import LEIIdentifier
import TrueFalseIndicator
import OrderClassification2
import OrderPriceData2
import OrderInstructionData2
import ExecutingParty2Choice
import TransactionData3
import PersonOrOrganisation4Choice

class OrderData4(base_types._BaseFieldType):

	__slots__ = ["_ClntId", "_InvstmtDcsnPrsn", "_InstrData", "_ExctgPrsn", "_LqdtyPrvsnActvty", "_TxData", "_DrctElctrncAccs", "_OrdrPrics", "_SubmitgNtty", "_TradgCpcty", "_OrdrClssfctn", "_NonExctgBrkr"]
	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if type(value) != auto else self.make_default("ClntId")

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = None

	@property
	def InvstmtDcsnPrsn(self):
		return self._InvstmtDcsnPrsn

	@InvstmtDcsnPrsn.setter
	def InvstmtDcsnPrsn(self, value):
		self._InvstmtDcsnPrsn = value if type(value) != auto else self.make_default("InvstmtDcsnPrsn")

	@InvstmtDcsnPrsn.deleter
	def InvstmtDcsnPrsn(self):
		del self._InvstmtDcsnPrsn
		self._InvstmtDcsnPrsn = None

	@property
	def InstrData(self):
		return self._InstrData

	@InstrData.setter
	def InstrData(self, value):
		self._InstrData = value if type(value) != auto else self.make_default("InstrData")

	@InstrData.deleter
	def InstrData(self):
		del self._InstrData
		self._InstrData = None

	@property
	def ExctgPrsn(self):
		return self._ExctgPrsn

	@ExctgPrsn.setter
	def ExctgPrsn(self, value):
		self._ExctgPrsn = value if type(value) != auto else self.make_default("ExctgPrsn")

	@ExctgPrsn.deleter
	def ExctgPrsn(self):
		del self._ExctgPrsn
		self._ExctgPrsn = None

	@property
	def LqdtyPrvsnActvty(self):
		return self._LqdtyPrvsnActvty

	@LqdtyPrvsnActvty.setter
	def LqdtyPrvsnActvty(self, value):
		self._LqdtyPrvsnActvty = value if type(value) != auto else self.make_default("LqdtyPrvsnActvty")

	@LqdtyPrvsnActvty.deleter
	def LqdtyPrvsnActvty(self):
		del self._LqdtyPrvsnActvty
		self._LqdtyPrvsnActvty = None

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if type(value) != auto else self.make_default("TxData")

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = None

	@property
	def DrctElctrncAccs(self):
		return self._DrctElctrncAccs

	@DrctElctrncAccs.setter
	def DrctElctrncAccs(self, value):
		self._DrctElctrncAccs = value if type(value) != auto else self.make_default("DrctElctrncAccs")

	@DrctElctrncAccs.deleter
	def DrctElctrncAccs(self):
		del self._DrctElctrncAccs
		self._DrctElctrncAccs = None

	@property
	def OrdrPrics(self):
		return self._OrdrPrics

	@OrdrPrics.setter
	def OrdrPrics(self, value):
		self._OrdrPrics = value if type(value) != auto else self.make_default("OrdrPrics")

	@OrdrPrics.deleter
	def OrdrPrics(self):
		del self._OrdrPrics
		self._OrdrPrics = None

	@property
	def SubmitgNtty(self):
		return self._SubmitgNtty

	@SubmitgNtty.setter
	def SubmitgNtty(self, value):
		self._SubmitgNtty = value if type(value) != auto else self.make_default("SubmitgNtty")

	@SubmitgNtty.deleter
	def SubmitgNtty(self):
		del self._SubmitgNtty
		self._SubmitgNtty = None

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	@property
	def OrdrClssfctn(self):
		return self._OrdrClssfctn

	@OrdrClssfctn.setter
	def OrdrClssfctn(self, value):
		self._OrdrClssfctn = value if type(value) != auto else self.make_default("OrdrClssfctn")

	@OrdrClssfctn.deleter
	def OrdrClssfctn(self):
		del self._OrdrClssfctn
		self._OrdrClssfctn = None

	@property
	def NonExctgBrkr(self):
		return self._NonExctgBrkr

	@NonExctgBrkr.setter
	def NonExctgBrkr(self, value):
		self._NonExctgBrkr = value if type(value) != auto else self.make_default("NonExctgBrkr")

	@NonExctgBrkr.deleter
	def NonExctgBrkr(self):
		del self._NonExctgBrkr
		self._NonExctgBrkr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntId', type=PersonOrOrganisation4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtDcsnPrsn', type=ExecutingParty2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrData', type=OrderInstructionData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPrsn', type=ExecutingParty2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyPrvsnActvty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxData', type=TransactionData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctElctrncAccs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrPrics', type=OrderPriceData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgNtty', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=RegulatoryTradingCapacity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrClssfctn', type=OrderClassification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonExctgBrkr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

