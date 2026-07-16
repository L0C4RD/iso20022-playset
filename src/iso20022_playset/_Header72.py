# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalMessageFunction1Code
from . import ISODateTime
from . import Max140Binary
from . import Max15NumericText
from . import Max2048Text
from . import Max35Text
from . import Max3NumericText
from . import Max70Text

class Header72(base_types._BaseFieldType):

	__slots__ = ["_BtchId", "_ColltnId", "_CreDtTm", "_InitgPtyId", "_MsgChcksmInptVal", "_MsgFctn", "_MsgSeqNb", "_PrtcolVrsn", "_RcptPtyId", "_ReTrnsmssnCntr", "_TracData", "_XchgId"]
	@property
	def BtchId(self):
		return self._BtchId

	@BtchId.setter
	def BtchId(self, value):
		self._BtchId = value if value is not None else base_types.UninitialisedField(self, 'BtchId', Max35Text, False)

	@BtchId.deleter
	def BtchId(self):
		del self._BtchId
		self._BtchId = base_types.UninitialisedField(self, 'BtchId', Max35Text, False)

	@property
	def ColltnId(self):
		return self._ColltnId

	@ColltnId.setter
	def ColltnId(self, value):
		self._ColltnId = value if value is not None else base_types.UninitialisedField(self, 'ColltnId', Max35Text, False)

	@ColltnId.deleter
	def ColltnId(self):
		del self._ColltnId
		self._ColltnId = base_types.UninitialisedField(self, 'ColltnId', Max35Text, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def InitgPtyId(self):
		return self._InitgPtyId

	@InitgPtyId.setter
	def InitgPtyId(self, value):
		self._InitgPtyId = value if value is not None else base_types.UninitialisedField(self, 'InitgPtyId', Max35Text, False)

	@InitgPtyId.deleter
	def InitgPtyId(self):
		del self._InitgPtyId
		self._InitgPtyId = base_types.UninitialisedField(self, 'InitgPtyId', Max35Text, False)

	@property
	def MsgChcksmInptVal(self):
		return self._MsgChcksmInptVal

	@MsgChcksmInptVal.setter
	def MsgChcksmInptVal(self, value):
		self._MsgChcksmInptVal = value if value is not None else base_types.UninitialisedField(self, 'MsgChcksmInptVal', Max140Binary, False)

	@MsgChcksmInptVal.deleter
	def MsgChcksmInptVal(self):
		del self._MsgChcksmInptVal
		self._MsgChcksmInptVal = base_types.UninitialisedField(self, 'MsgChcksmInptVal', Max140Binary, False)

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if value is not None else base_types.UninitialisedField(self, 'MsgFctn', ExternalMessageFunction1Code, False)

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = base_types.UninitialisedField(self, 'MsgFctn', ExternalMessageFunction1Code, False)

	@property
	def MsgSeqNb(self):
		return self._MsgSeqNb

	@MsgSeqNb.setter
	def MsgSeqNb(self, value):
		self._MsgSeqNb = value if value is not None else base_types.UninitialisedField(self, 'MsgSeqNb', Max15NumericText, False)

	@MsgSeqNb.deleter
	def MsgSeqNb(self):
		del self._MsgSeqNb
		self._MsgSeqNb = base_types.UninitialisedField(self, 'MsgSeqNb', Max15NumericText, False)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max2048Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max2048Text, False)

	@property
	def RcptPtyId(self):
		return self._RcptPtyId

	@RcptPtyId.setter
	def RcptPtyId(self, value):
		self._RcptPtyId = value if value is not None else base_types.UninitialisedField(self, 'RcptPtyId', Max35Text, False)

	@RcptPtyId.deleter
	def RcptPtyId(self):
		del self._RcptPtyId
		self._RcptPtyId = base_types.UninitialisedField(self, 'RcptPtyId', Max35Text, False)

	@property
	def ReTrnsmssnCntr(self):
		return self._ReTrnsmssnCntr

	@ReTrnsmssnCntr.setter
	def ReTrnsmssnCntr(self, value):
		self._ReTrnsmssnCntr = value if value is not None else base_types.UninitialisedField(self, 'ReTrnsmssnCntr', Max3NumericText, False)

	@ReTrnsmssnCntr.deleter
	def ReTrnsmssnCntr(self):
		del self._ReTrnsmssnCntr
		self._ReTrnsmssnCntr = base_types.UninitialisedField(self, 'ReTrnsmssnCntr', Max3NumericText, False)

	@property
	def TracData(self):
		return self._TracData

	@TracData.setter
	def TracData(self, value):
		self._TracData = value if value is not None else base_types.UninitialisedField(self, 'TracData', Max70Text, False)

	@TracData.deleter
	def TracData(self):
		del self._TracData
		self._TracData = base_types.UninitialisedField(self, 'TracData', Max70Text, False)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

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