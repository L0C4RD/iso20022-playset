# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DisputeReference1
from . import Exact1NumericText
from . import ISO8583MessageReasonCode
from . import Max100KBinary
from . import Max35Text
from . import PartyType26Code
from . import TrueFalseIndicator

class FraudulentTransactionData3(base_types._BaseFieldType):

	__slots__ = ["_AltrnMsgRsn", "_Authstn", "_AuthstnNtty", "_DsptCond", "_DsptRef", "_FrdlntMsg", "_MsgRsn", "_OthrAuthstnNtty", "_PresntmntCycl"]
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
		self._AuthstnNtty = value if value is not None else base_types.UninitialisedField(self, 'AuthstnNtty', PartyType26Code, False)

	@AuthstnNtty.deleter
	def AuthstnNtty(self):
		del self._AuthstnNtty
		self._AuthstnNtty = base_types.UninitialisedField(self, 'AuthstnNtty', PartyType26Code, False)

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
	def DsptRef(self):
		return self._DsptRef

	@DsptRef.setter
	def DsptRef(self, value):
		self._DsptRef = value if value is not None else base_types.UninitialisedField(self, 'DsptRef', DisputeReference1, True)

	@DsptRef.deleter
	def DsptRef(self):
		del self._DsptRef
		self._DsptRef = base_types.UninitialisedField(self, 'DsptRef', DisputeReference1, True)

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
	def OthrAuthstnNtty(self):
		return self._OthrAuthstnNtty

	@OthrAuthstnNtty.setter
	def OthrAuthstnNtty(self, value):
		self._OthrAuthstnNtty = value if value is not None else base_types.UninitialisedField(self, 'OthrAuthstnNtty', Max35Text, False)

	@OthrAuthstnNtty.deleter
	def OthrAuthstnNtty(self):
		del self._OthrAuthstnNtty
		self._OthrAuthstnNtty = base_types.UninitialisedField(self, 'OthrAuthstnNtty', Max35Text, False)

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
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnNtty', type=PartyType26Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptCond', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptRef', type=DisputeReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrdlntMsg', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrAuthstnNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntCycl', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
	))