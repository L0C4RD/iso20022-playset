# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import BatchManagementInformation1
from . import ExternalMessageFunction1Code
from . import GenericIdentification183
from . import ISODateTime
from . import Max2048Text
from . import Max35Text
from . import Max3NumericText
from . import Traceability10

class Header71(base_types._BaseFieldType):

	__slots__ = ["_BtchMgmtInf", "_CreDtTm", "_InitgPty", "_MsgFctn", "_PrtcolVrsn", "_RcptPty", "_ReTrnsmssnCntr", "_TracData", "_Tracblt", "_XchgId"]
	@property
	def BtchMgmtInf(self):
		return self._BtchMgmtInf

	@BtchMgmtInf.setter
	def BtchMgmtInf(self, value):
		self._BtchMgmtInf = value if value is not None else base_types.UninitialisedField(self, 'BtchMgmtInf', BatchManagementInformation1, False)

	@BtchMgmtInf.deleter
	def BtchMgmtInf(self):
		del self._BtchMgmtInf
		self._BtchMgmtInf = base_types.UninitialisedField(self, 'BtchMgmtInf', BatchManagementInformation1, False)

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
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', GenericIdentification183, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', GenericIdentification183, False)

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
	def RcptPty(self):
		return self._RcptPty

	@RcptPty.setter
	def RcptPty(self, value):
		self._RcptPty = value if value is not None else base_types.UninitialisedField(self, 'RcptPty', GenericIdentification183, False)

	@RcptPty.deleter
	def RcptPty(self):
		del self._RcptPty
		self._RcptPty = base_types.UninitialisedField(self, 'RcptPty', GenericIdentification183, False)

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
		self._TracData = value if value is not None else base_types.UninitialisedField(self, 'TracData', AdditionalData1, True)

	@TracData.deleter
	def TracData(self):
		del self._TracData
		self._TracData = base_types.UninitialisedField(self, 'TracData', AdditionalData1, True)

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if value is not None else base_types.UninitialisedField(self, 'Tracblt', Traceability10, True)

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = base_types.UninitialisedField(self, 'Tracblt', Traceability10, True)

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
		base_types.FieldEntry(name='BtchMgmtInf', type=BatchManagementInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification183, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=ExternalMessageFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPty', type=GenericIdentification183, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTrnsmssnCntr', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tracblt', type=Traceability10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))