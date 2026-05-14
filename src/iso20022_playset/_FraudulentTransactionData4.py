# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._Exact1NumericText import Exact1NumericText
from ._ISO8583MessageReasonCode import ISO8583MessageReasonCode
from ._Max100KBinary import Max100KBinary
from ._Max20Text import Max20Text
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class FraudulentTransactionData4(base_types._BaseFieldType):

	__slots__ = ["_AcqrrDsptCaseRef", "_AgtDsptBndlCaseRef", "_AgtDsptCaseRef", "_AltrnMsgRsn", "_Authstn", "_AuthstnNtty", "_DsptCond", "_FrdlntMsg", "_IssrDsptCaseRef", "_MsgRsn", "_PresntmntCycl"]
	@property
	def AcqrrDsptCaseRef(self):
		return self._AcqrrDsptCaseRef

	@AcqrrDsptCaseRef.setter
	def AcqrrDsptCaseRef(self, value):
		self._AcqrrDsptCaseRef = value if type(value) != base_types.auto else self.make_default("AcqrrDsptCaseRef")

	@AcqrrDsptCaseRef.deleter
	def AcqrrDsptCaseRef(self):
		del self._AcqrrDsptCaseRef
		self._AcqrrDsptCaseRef = None

	@property
	def AgtDsptBndlCaseRef(self):
		return self._AgtDsptBndlCaseRef

	@AgtDsptBndlCaseRef.setter
	def AgtDsptBndlCaseRef(self, value):
		self._AgtDsptBndlCaseRef = value if type(value) != base_types.auto else self.make_default("AgtDsptBndlCaseRef")

	@AgtDsptBndlCaseRef.deleter
	def AgtDsptBndlCaseRef(self):
		del self._AgtDsptBndlCaseRef
		self._AgtDsptBndlCaseRef = None

	@property
	def AgtDsptCaseRef(self):
		return self._AgtDsptCaseRef

	@AgtDsptCaseRef.setter
	def AgtDsptCaseRef(self, value):
		self._AgtDsptCaseRef = value if type(value) != base_types.auto else self.make_default("AgtDsptCaseRef")

	@AgtDsptCaseRef.deleter
	def AgtDsptCaseRef(self):
		del self._AgtDsptCaseRef
		self._AgtDsptCaseRef = None

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
	def IssrDsptCaseRef(self):
		return self._IssrDsptCaseRef

	@IssrDsptCaseRef.setter
	def IssrDsptCaseRef(self, value):
		self._IssrDsptCaseRef = value if type(value) != base_types.auto else self.make_default("IssrDsptCaseRef")

	@IssrDsptCaseRef.deleter
	def IssrDsptCaseRef(self):
		del self._IssrDsptCaseRef
		self._IssrDsptCaseRef = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrDsptCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtDsptBndlCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtDsptCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnNtty', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptCond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrdlntMsg', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsptCaseRef', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PresntmntCycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
	))