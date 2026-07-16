# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICAPartyType1Code
from . import Exact1NumericText
from . import ISO8583MessageReasonCode
from . import Max100KBinary
from . import Max20Text
from . import Max35Text
from . import TrueFalseIndicator

class FraudulentTransactionData4(base_types._BaseFieldType):

	__slots__ = ["_AcqrrDsptCaseRef", "_AgtDsptBndlCaseRef", "_AgtDsptCaseRef", "_AltrnMsgRsn", "_Authstn", "_AuthstnNtty", "_DsptCond", "_FrdlntMsg", "_IssrDsptCaseRef", "_MsgRsn", "_PresntmntCycl"]
	@property
	def AcqrrDsptCaseRef(self):
		return self._AcqrrDsptCaseRef

	@AcqrrDsptCaseRef.setter
	def AcqrrDsptCaseRef(self, value):
		self._AcqrrDsptCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AcqrrDsptCaseRef', Max20Text, False)

	@AcqrrDsptCaseRef.deleter
	def AcqrrDsptCaseRef(self):
		del self._AcqrrDsptCaseRef
		self._AcqrrDsptCaseRef = base_types.UninitialisedField(self, 'AcqrrDsptCaseRef', Max20Text, False)

	@property
	def AgtDsptBndlCaseRef(self):
		return self._AgtDsptBndlCaseRef

	@AgtDsptBndlCaseRef.setter
	def AgtDsptBndlCaseRef(self, value):
		self._AgtDsptBndlCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AgtDsptBndlCaseRef', Max20Text, False)

	@AgtDsptBndlCaseRef.deleter
	def AgtDsptBndlCaseRef(self):
		del self._AgtDsptBndlCaseRef
		self._AgtDsptBndlCaseRef = base_types.UninitialisedField(self, 'AgtDsptBndlCaseRef', Max20Text, False)

	@property
	def AgtDsptCaseRef(self):
		return self._AgtDsptCaseRef

	@AgtDsptCaseRef.setter
	def AgtDsptCaseRef(self, value):
		self._AgtDsptCaseRef = value if value is not None else base_types.UninitialisedField(self, 'AgtDsptCaseRef', Max20Text, False)

	@AgtDsptCaseRef.deleter
	def AgtDsptCaseRef(self):
		del self._AgtDsptCaseRef
		self._AgtDsptCaseRef = base_types.UninitialisedField(self, 'AgtDsptCaseRef', Max20Text, False)

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if value is not None else base_types.UninitialisedField(self, 'AltrnMsgRsn', Max35Text, True)

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = base_types.UninitialisedField(self, 'AltrnMsgRsn', Max35Text, True)

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if value is not None else base_types.UninitialisedField(self, 'Authstn', TrueFalseIndicator, False)

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = base_types.UninitialisedField(self, 'Authstn', TrueFalseIndicator, False)

	@property
	def AuthstnNtty(self):
		return self._AuthstnNtty

	@AuthstnNtty.setter
	def AuthstnNtty(self, value):
		self._AuthstnNtty = value if value is not None else base_types.UninitialisedField(self, 'AuthstnNtty', ATICAPartyType1Code, False)

	@AuthstnNtty.deleter
	def AuthstnNtty(self):
		del self._AuthstnNtty
		self._AuthstnNtty = base_types.UninitialisedField(self, 'AuthstnNtty', ATICAPartyType1Code, False)

	@property
	def DsptCond(self):
		return self._DsptCond

	@DsptCond.setter
	def DsptCond(self, value):
		self._DsptCond = value if value is not None else base_types.UninitialisedField(self, 'DsptCond', Max35Text, False)

	@DsptCond.deleter
	def DsptCond(self):
		del self._DsptCond
		self._DsptCond = base_types.UninitialisedField(self, 'DsptCond', Max35Text, False)

	@property
	def FrdlntMsg(self):
		return self._FrdlntMsg

	@FrdlntMsg.setter
	def FrdlntMsg(self, value):
		self._FrdlntMsg = value if value is not None else base_types.UninitialisedField(self, 'FrdlntMsg', Max100KBinary, False)

	@FrdlntMsg.deleter
	def FrdlntMsg(self):
		del self._FrdlntMsg
		self._FrdlntMsg = base_types.UninitialisedField(self, 'FrdlntMsg', Max100KBinary, False)

	@property
	def IssrDsptCaseRef(self):
		return self._IssrDsptCaseRef

	@IssrDsptCaseRef.setter
	def IssrDsptCaseRef(self, value):
		self._IssrDsptCaseRef = value if value is not None else base_types.UninitialisedField(self, 'IssrDsptCaseRef', Max20Text, False)

	@IssrDsptCaseRef.deleter
	def IssrDsptCaseRef(self):
		del self._IssrDsptCaseRef
		self._IssrDsptCaseRef = base_types.UninitialisedField(self, 'IssrDsptCaseRef', Max20Text, False)

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if value is not None else base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@property
	def PresntmntCycl(self):
		return self._PresntmntCycl

	@PresntmntCycl.setter
	def PresntmntCycl(self, value):
		self._PresntmntCycl = value if value is not None else base_types.UninitialisedField(self, 'PresntmntCycl', Exact1NumericText, False)

	@PresntmntCycl.deleter
	def PresntmntCycl(self):
		del self._PresntmntCycl
		self._PresntmntCycl = base_types.UninitialisedField(self, 'PresntmntCycl', Exact1NumericText, False)

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