from . import base_types
from .DisputeReference1 import DisputeReference1
from .Max35Text import Max35Text
from .TrueFalseIndicator import TrueFalseIndicator
from .PartyType26Code import PartyType26Code
from .Exact1NumericText import Exact1NumericText
from .Max100KBinary import Max100KBinary
from .ISO8583MessageReasonCode import ISO8583MessageReasonCode

class FraudulentTransactionData3(base_types._BaseFieldType):

	__slots__ = ["_DsptCond", "_AltrnMsgRsn", "_Authstn", "_OthrAuthstnNtty", "_FrdlntMsg", "_PresntmntCycl", "_DsptRef", "_AuthstnNtty", "_MsgRsn"]
	@property
	def DsptCond(self):
		return self._DsptCond

	@DsptCond.setter
	def DsptCond(self, value):
		self._DsptCond = value if type(value) != base_types.auto else self.make_default("DsptCond")

	@DsptCond.deleter
	def DsptCond(self):
		del self._DsptCond
		self._DsptCond = None

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if type(value) != base_types.auto else self.make_default("AltrnMsgRsn")

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = None

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != base_types.auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def OthrAuthstnNtty(self):
		return self._OthrAuthstnNtty

	@OthrAuthstnNtty.setter
	def OthrAuthstnNtty(self, value):
		self._OthrAuthstnNtty = value if type(value) != base_types.auto else self.make_default("OthrAuthstnNtty")

	@OthrAuthstnNtty.deleter
	def OthrAuthstnNtty(self):
		del self._OthrAuthstnNtty
		self._OthrAuthstnNtty = None

	@property
	def FrdlntMsg(self):
		return self._FrdlntMsg

	@FrdlntMsg.setter
	def FrdlntMsg(self, value):
		self._FrdlntMsg = value if type(value) != base_types.auto else self.make_default("FrdlntMsg")

	@FrdlntMsg.deleter
	def FrdlntMsg(self):
		del self._FrdlntMsg
		self._FrdlntMsg = None

	@property
	def PresntmntCycl(self):
		return self._PresntmntCycl

	@PresntmntCycl.setter
	def PresntmntCycl(self, value):
		self._PresntmntCycl = value if type(value) != base_types.auto else self.make_default("PresntmntCycl")

	@PresntmntCycl.deleter
	def PresntmntCycl(self):
		del self._PresntmntCycl
		self._PresntmntCycl = None

	@property
	def DsptRef(self):
		return self._DsptRef

	@DsptRef.setter
	def DsptRef(self, value):
		self._DsptRef = value if type(value) != base_types.auto else self.make_default("DsptRef")

	@DsptRef.deleter
	def DsptRef(self):
		del self._DsptRef
		self._DsptRef = None

	@property
	def AuthstnNtty(self):
		return self._AuthstnNtty

	@AuthstnNtty.setter
	def AuthstnNtty(self, value):
		self._AuthstnNtty = value if type(value) != base_types.auto else self.make_default("AuthstnNtty")

	@AuthstnNtty.deleter
	def AuthstnNtty(self):
		del self._AuthstnNtty
		self._AuthstnNtty = None

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if type(value) != base_types.auto else self.make_default("MsgRsn")

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptCond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAuthstnNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdlntMsg', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntCycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptRef', type=DisputeReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnNtty', type=PartyType26Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
	))

