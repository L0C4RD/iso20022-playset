from . import base_types
from ._ExternalMessageFunction1Code import ExternalMessageFunction1Code
from ._ISODateTime import ISODateTime
from ._Max140Binary import Max140Binary
from ._Max15NumericText import Max15NumericText
from ._Max2048Text import Max2048Text
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._Max70Text import Max70Text

class Header72(base_types._BaseFieldType):

	__slots__ = ["_BtchId", "_ColltnId", "_CreDtTm", "_InitgPtyId", "_MsgChcksmInptVal", "_MsgFctn", "_MsgSeqNb", "_PrtcolVrsn", "_RcptPtyId", "_ReTrnsmssnCntr", "_TracData", "_XchgId"]
	@property
	def BtchId(self):
		return self._BtchId

	@BtchId.setter
	def BtchId(self, value):
		self._BtchId = value if type(value) != base_types.auto else self.make_default("BtchId")

	@BtchId.deleter
	def BtchId(self):
		del self._BtchId
		self._BtchId = None

	@property
	def ColltnId(self):
		return self._ColltnId

	@ColltnId.setter
	def ColltnId(self, value):
		self._ColltnId = value if type(value) != base_types.auto else self.make_default("ColltnId")

	@ColltnId.deleter
	def ColltnId(self):
		del self._ColltnId
		self._ColltnId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def InitgPtyId(self):
		return self._InitgPtyId

	@InitgPtyId.setter
	def InitgPtyId(self, value):
		self._InitgPtyId = value if type(value) != base_types.auto else self.make_default("InitgPtyId")

	@InitgPtyId.deleter
	def InitgPtyId(self):
		del self._InitgPtyId
		self._InitgPtyId = None

	@property
	def MsgChcksmInptVal(self):
		return self._MsgChcksmInptVal

	@MsgChcksmInptVal.setter
	def MsgChcksmInptVal(self, value):
		self._MsgChcksmInptVal = value if type(value) != base_types.auto else self.make_default("MsgChcksmInptVal")

	@MsgChcksmInptVal.deleter
	def MsgChcksmInptVal(self):
		del self._MsgChcksmInptVal
		self._MsgChcksmInptVal = None

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if type(value) != base_types.auto else self.make_default("MsgFctn")

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = None

	@property
	def MsgSeqNb(self):
		return self._MsgSeqNb

	@MsgSeqNb.setter
	def MsgSeqNb(self, value):
		self._MsgSeqNb = value if type(value) != base_types.auto else self.make_default("MsgSeqNb")

	@MsgSeqNb.deleter
	def MsgSeqNb(self):
		del self._MsgSeqNb
		self._MsgSeqNb = None

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if type(value) != base_types.auto else self.make_default("PrtcolVrsn")

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = None

	@property
	def RcptPtyId(self):
		return self._RcptPtyId

	@RcptPtyId.setter
	def RcptPtyId(self, value):
		self._RcptPtyId = value if type(value) != base_types.auto else self.make_default("RcptPtyId")

	@RcptPtyId.deleter
	def RcptPtyId(self):
		del self._RcptPtyId
		self._RcptPtyId = None

	@property
	def ReTrnsmssnCntr(self):
		return self._ReTrnsmssnCntr

	@ReTrnsmssnCntr.setter
	def ReTrnsmssnCntr(self, value):
		self._ReTrnsmssnCntr = value if type(value) != base_types.auto else self.make_default("ReTrnsmssnCntr")

	@ReTrnsmssnCntr.deleter
	def ReTrnsmssnCntr(self):
		del self._ReTrnsmssnCntr
		self._ReTrnsmssnCntr = None

	@property
	def TracData(self):
		return self._TracData

	@TracData.setter
	def TracData(self, value):
		self._TracData = value if type(value) != base_types.auto else self.make_default("TracData")

	@TracData.deleter
	def TracData(self):
		del self._TracData
		self._TracData = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgChcksmInptVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=ExternalMessageFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSeqNb', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTrnsmssnCntr', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

