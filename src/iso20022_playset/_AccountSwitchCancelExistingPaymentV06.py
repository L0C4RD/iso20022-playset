# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchDetails1
from . import CashAccount43
from . import DirectDebitInstructionDetails3
from . import MessageIdentification1
from . import PaymentInstruction49
from . import SupplementaryData1

class AccountSwitchCancelExistingPaymentV06(base_types._BaseFieldType):

	__slots__ = ["_AcctSwtchDtls", "_DrctDbtInstr", "_MsgId", "_OdAcct", "_PmtInstr", "_SplmtryData"]
	@property
	def AcctSwtchDtls(self):
		return self._AcctSwtchDtls

	@AcctSwtchDtls.setter
	def AcctSwtchDtls(self, value):
		self._AcctSwtchDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchDtls', AccountSwitchDetails1, False)

	@AcctSwtchDtls.deleter
	def AcctSwtchDtls(self):
		del self._AcctSwtchDtls
		self._AcctSwtchDtls = base_types.UninitialisedField(self, 'AcctSwtchDtls', AccountSwitchDetails1, False)

	@property
	def DrctDbtInstr(self):
		return self._DrctDbtInstr

	@DrctDbtInstr.setter
	def DrctDbtInstr(self, value):
		self._DrctDbtInstr = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtInstr', DirectDebitInstructionDetails3, True)

	@DrctDbtInstr.deleter
	def DrctDbtInstr(self):
		del self._DrctDbtInstr
		self._DrctDbtInstr = base_types.UninitialisedField(self, 'DrctDbtInstr', DirectDebitInstructionDetails3, True)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def OdAcct(self):
		return self._OdAcct

	@OdAcct.setter
	def OdAcct(self, value):
		self._OdAcct = value if value is not None else base_types.UninitialisedField(self, 'OdAcct', CashAccount43, False)

	@OdAcct.deleter
	def OdAcct(self):
		del self._OdAcct
		self._OdAcct = base_types.UninitialisedField(self, 'OdAcct', CashAccount43, False)

	@property
	def PmtInstr(self):
		return self._PmtInstr

	@PmtInstr.setter
	def PmtInstr(self, value):
		self._PmtInstr = value if value is not None else base_types.UninitialisedField(self, 'PmtInstr', PaymentInstruction49, True)

	@PmtInstr.deleter
	def PmtInstr(self):
		del self._PmtInstr
		self._PmtInstr = base_types.UninitialisedField(self, 'PmtInstr', PaymentInstruction49, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSwtchDtls', type=AccountSwitchDetails1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtInstr', type=DirectDebitInstructionDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdAcct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstr', type=PaymentInstruction49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))