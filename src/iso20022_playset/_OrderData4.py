# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExecutingParty2Choice
from . import LEIIdentifier
from . import OrderClassification2
from . import OrderInstructionData2
from . import OrderPriceData2
from . import PersonOrOrganisation4Choice
from . import RegulatoryTradingCapacity1Code
from . import TransactionData3
from . import TrueFalseIndicator

class OrderData4(base_types._BaseFieldType):

	__slots__ = ["_ClntId", "_DrctElctrncAccs", "_ExctgPrsn", "_InstrData", "_InvstmtDcsnPrsn", "_LqdtyPrvsnActvty", "_NonExctgBrkr", "_OrdrClssfctn", "_OrdrPrics", "_SubmitgNtty", "_TradgCpcty", "_TxData"]
	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if value is not None else base_types.UninitialisedField(self, 'ClntId', PersonOrOrganisation4Choice, False)

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = base_types.UninitialisedField(self, 'ClntId', PersonOrOrganisation4Choice, False)

	@property
	def DrctElctrncAccs(self):
		return self._DrctElctrncAccs

	@DrctElctrncAccs.setter
	def DrctElctrncAccs(self, value):
		self._DrctElctrncAccs = value if value is not None else base_types.UninitialisedField(self, 'DrctElctrncAccs', TrueFalseIndicator, False)

	@DrctElctrncAccs.deleter
	def DrctElctrncAccs(self):
		del self._DrctElctrncAccs
		self._DrctElctrncAccs = base_types.UninitialisedField(self, 'DrctElctrncAccs', TrueFalseIndicator, False)

	@property
	def ExctgPrsn(self):
		return self._ExctgPrsn

	@ExctgPrsn.setter
	def ExctgPrsn(self, value):
		self._ExctgPrsn = value if value is not None else base_types.UninitialisedField(self, 'ExctgPrsn', ExecutingParty2Choice, False)

	@ExctgPrsn.deleter
	def ExctgPrsn(self):
		del self._ExctgPrsn
		self._ExctgPrsn = base_types.UninitialisedField(self, 'ExctgPrsn', ExecutingParty2Choice, False)

	@property
	def InstrData(self):
		return self._InstrData

	@InstrData.setter
	def InstrData(self, value):
		self._InstrData = value if value is not None else base_types.UninitialisedField(self, 'InstrData', OrderInstructionData2, False)

	@InstrData.deleter
	def InstrData(self):
		del self._InstrData
		self._InstrData = base_types.UninitialisedField(self, 'InstrData', OrderInstructionData2, False)

	@property
	def InvstmtDcsnPrsn(self):
		return self._InvstmtDcsnPrsn

	@InvstmtDcsnPrsn.setter
	def InvstmtDcsnPrsn(self, value):
		self._InvstmtDcsnPrsn = value if value is not None else base_types.UninitialisedField(self, 'InvstmtDcsnPrsn', ExecutingParty2Choice, False)

	@InvstmtDcsnPrsn.deleter
	def InvstmtDcsnPrsn(self):
		del self._InvstmtDcsnPrsn
		self._InvstmtDcsnPrsn = base_types.UninitialisedField(self, 'InvstmtDcsnPrsn', ExecutingParty2Choice, False)

	@property
	def LqdtyPrvsnActvty(self):
		return self._LqdtyPrvsnActvty

	@LqdtyPrvsnActvty.setter
	def LqdtyPrvsnActvty(self, value):
		self._LqdtyPrvsnActvty = value if value is not None else base_types.UninitialisedField(self, 'LqdtyPrvsnActvty', TrueFalseIndicator, False)

	@LqdtyPrvsnActvty.deleter
	def LqdtyPrvsnActvty(self):
		del self._LqdtyPrvsnActvty
		self._LqdtyPrvsnActvty = base_types.UninitialisedField(self, 'LqdtyPrvsnActvty', TrueFalseIndicator, False)

	@property
	def NonExctgBrkr(self):
		return self._NonExctgBrkr

	@NonExctgBrkr.setter
	def NonExctgBrkr(self, value):
		self._NonExctgBrkr = value if value is not None else base_types.UninitialisedField(self, 'NonExctgBrkr', LEIIdentifier, False)

	@NonExctgBrkr.deleter
	def NonExctgBrkr(self):
		del self._NonExctgBrkr
		self._NonExctgBrkr = base_types.UninitialisedField(self, 'NonExctgBrkr', LEIIdentifier, False)

	@property
	def OrdrClssfctn(self):
		return self._OrdrClssfctn

	@OrdrClssfctn.setter
	def OrdrClssfctn(self, value):
		self._OrdrClssfctn = value if value is not None else base_types.UninitialisedField(self, 'OrdrClssfctn', OrderClassification2, False)

	@OrdrClssfctn.deleter
	def OrdrClssfctn(self):
		del self._OrdrClssfctn
		self._OrdrClssfctn = base_types.UninitialisedField(self, 'OrdrClssfctn', OrderClassification2, False)

	@property
	def OrdrPrics(self):
		return self._OrdrPrics

	@OrdrPrics.setter
	def OrdrPrics(self, value):
		self._OrdrPrics = value if value is not None else base_types.UninitialisedField(self, 'OrdrPrics', OrderPriceData2, False)

	@OrdrPrics.deleter
	def OrdrPrics(self):
		del self._OrdrPrics
		self._OrdrPrics = base_types.UninitialisedField(self, 'OrdrPrics', OrderPriceData2, False)

	@property
	def SubmitgNtty(self):
		return self._SubmitgNtty

	@SubmitgNtty.setter
	def SubmitgNtty(self, value):
		self._SubmitgNtty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgNtty', LEIIdentifier, False)

	@SubmitgNtty.deleter
	def SubmitgNtty(self):
		del self._SubmitgNtty
		self._SubmitgNtty = base_types.UninitialisedField(self, 'SubmitgNtty', LEIIdentifier, False)

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgCpcty', RegulatoryTradingCapacity1Code, False)

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = base_types.UninitialisedField(self, 'TradgCpcty', RegulatoryTradingCapacity1Code, False)

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if value is not None else base_types.UninitialisedField(self, 'TxData', TransactionData3, False)

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = base_types.UninitialisedField(self, 'TxData', TransactionData3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntId', type=PersonOrOrganisation4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctElctrncAccs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgPrsn', type=ExecutingParty2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrData', type=OrderInstructionData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtDcsnPrsn', type=ExecutingParty2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyPrvsnActvty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonExctgBrkr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrClssfctn', type=OrderClassification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrPrics', type=OrderPriceData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgNtty', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=RegulatoryTradingCapacity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxData', type=TransactionData3, min=0, max=1, mutex_group=None, array=False),
	))