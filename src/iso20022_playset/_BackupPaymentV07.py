from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader1 import MessageHeader1
from .SystemMember3 import SystemMember3
from .PaymentInstruction13 import PaymentInstruction13
from .Amount2Choice import Amount2Choice

class BackupPaymentV07(base_types._BaseFieldType):

	__slots__ = ["_InstrInf", "_DbtrAgt", "_SplmtryData", "_Cdtr", "_CdtrAgt", "_OrgnlMsgId", "_MsgHdr", "_TrfdAmt"]
	@property
	def InstrInf(self):
		return self._InstrInf

	@InstrInf.setter
	def InstrInf(self, value):
		self._InstrInf = value if type(value) != base_types.auto else self.make_default("InstrInf")

	@InstrInf.deleter
	def InstrInf(self):
		del self._InstrInf
		self._InstrInf = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

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
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != base_types.auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def TrfdAmt(self):
		return self._TrfdAmt

	@TrfdAmt.setter
	def TrfdAmt(self, value):
		self._TrfdAmt = value if type(value) != base_types.auto else self.make_default("TrfdAmt")

	@TrfdAmt.deleter
	def TrfdAmt(self):
		del self._TrfdAmt
		self._TrfdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrInf', type=PaymentInstruction13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=SystemMember3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cdtr', type=SystemMember3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=SystemMember3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfdAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))

