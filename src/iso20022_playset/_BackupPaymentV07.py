# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import MessageHeader1
from . import PaymentInstruction13
from . import SupplementaryData1
from . import SystemMember3

class BackupPaymentV07(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_DbtrAgt", "_InstrInf", "_MsgHdr", "_OrgnlMsgId", "_SplmtryData", "_TrfdAmt"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', SystemMember3, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', SystemMember3, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', SystemMember3, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', SystemMember3, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', SystemMember3, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', SystemMember3, False)

	@property
	def InstrInf(self):
		return self._InstrInf

	@InstrInf.setter
	def InstrInf(self, value):
		self._InstrInf = value if value is not None else base_types.UninitialisedField(self, 'InstrInf', PaymentInstruction13, False)

	@InstrInf.deleter
	def InstrInf(self):
		del self._InstrInf
		self._InstrInf = base_types.UninitialisedField(self, 'InstrInf', PaymentInstruction13, False)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', MessageHeader1, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', MessageHeader1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TrfdAmt(self):
		return self._TrfdAmt

	@TrfdAmt.setter
	def TrfdAmt(self, value):
		self._TrfdAmt = value if value is not None else base_types.UninitialisedField(self, 'TrfdAmt', Amount2Choice, False)

	@TrfdAmt.deleter
	def TrfdAmt(self):
		del self._TrfdAmt
		self._TrfdAmt = base_types.UninitialisedField(self, 'TrfdAmt', Amount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=SystemMember3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=SystemMember3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=SystemMember3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrInf', type=PaymentInstruction13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfdAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))