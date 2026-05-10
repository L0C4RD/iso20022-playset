from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .Exact4AlphaNumericText import Exact4AlphaNumericText
from .WithdrawalReason1 import WithdrawalReason1
from .Max35Text import Max35Text

class ForeignExchangeTradeWithdrawalNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_WdrwlRsn", "_MsgId", "_MtchgSysUnqRef", "_SttlmSsnIdr"]
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
	def WdrwlRsn(self):
		return self._WdrwlRsn

	@WdrwlRsn.setter
	def WdrwlRsn(self, value):
		self._WdrwlRsn = value if type(value) != base_types.auto else self.make_default("WdrwlRsn")

	@WdrwlRsn.deleter
	def WdrwlRsn(self):
		del self._WdrwlRsn
		self._WdrwlRsn = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if type(value) != base_types.auto else self.make_default("MtchgSysUnqRef")

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = None

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != base_types.auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlRsn', type=WithdrawalReason1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

