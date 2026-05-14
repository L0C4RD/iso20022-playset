# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData1 import AdditionalData1
from ._BatchManagementInformation1 import BatchManagementInformation1
from ._ExternalMessageFunction1Code import ExternalMessageFunction1Code
from ._GenericIdentification183 import GenericIdentification183
from ._ISODateTime import ISODateTime
from ._Max2048Text import Max2048Text
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._Traceability10 import Traceability10

class Header71(base_types._BaseFieldType):

	__slots__ = ["_BtchMgmtInf", "_CreDtTm", "_InitgPty", "_MsgFctn", "_PrtcolVrsn", "_RcptPty", "_ReTrnsmssnCntr", "_TracData", "_Tracblt", "_XchgId"]
	@property
	def BtchMgmtInf(self):
		return self._BtchMgmtInf

	@BtchMgmtInf.setter
	def BtchMgmtInf(self, value):
		self._BtchMgmtInf = value if type(value) != base_types.auto else self.make_default("BtchMgmtInf")

	@BtchMgmtInf.deleter
	def BtchMgmtInf(self):
		del self._BtchMgmtInf
		self._BtchMgmtInf = None

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
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

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
	def RcptPty(self):
		return self._RcptPty

	@RcptPty.setter
	def RcptPty(self, value):
		self._RcptPty = value if type(value) != base_types.auto else self.make_default("RcptPty")

	@RcptPty.deleter
	def RcptPty(self):
		del self._RcptPty
		self._RcptPty = None

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
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if type(value) != base_types.auto else self.make_default("Tracblt")

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = None

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