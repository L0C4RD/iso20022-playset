from . import base_types
from .MessageIdentification1 import MessageIdentification1
from .SupplementaryData1 import SupplementaryData1
from .BalanceTransfer5 import BalanceTransfer5
from .AmountAndDirection5 import AmountAndDirection5
from .AccountSwitchDetails1 import AccountSwitchDetails1
from .CashAccount43 import CashAccount43

class AccountSwitchBalanceTransferAcknowledgementV05(base_types._BaseFieldType):

	__slots__ = ["_OdAcct", "_MsgId", "_SplmtryData", "_BalTrf", "_OdAcctBal", "_AcctSwtchDtls"]
	@property
	def OdAcct(self):
		return self._OdAcct

	@OdAcct.setter
	def OdAcct(self, value):
		self._OdAcct = value if type(value) != auto else self.make_default("OdAcct")

	@OdAcct.deleter
	def OdAcct(self):
		del self._OdAcct
		self._OdAcct = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def BalTrf(self):
		return self._BalTrf

	@BalTrf.setter
	def BalTrf(self, value):
		self._BalTrf = value if type(value) != auto else self.make_default("BalTrf")

	@BalTrf.deleter
	def BalTrf(self):
		del self._BalTrf
		self._BalTrf = None

	@property
	def OdAcctBal(self):
		return self._OdAcctBal

	@OdAcctBal.setter
	def OdAcctBal(self, value):
		self._OdAcctBal = value if type(value) != auto else self.make_default("OdAcctBal")

	@OdAcctBal.deleter
	def OdAcctBal(self):
		del self._OdAcctBal
		self._OdAcctBal = None

	@property
	def AcctSwtchDtls(self):
		return self._AcctSwtchDtls

	@AcctSwtchDtls.setter
	def AcctSwtchDtls(self, value):
		self._AcctSwtchDtls = value if type(value) != auto else self.make_default("AcctSwtchDtls")

	@AcctSwtchDtls.deleter
	def AcctSwtchDtls(self):
		del self._AcctSwtchDtls
		self._AcctSwtchDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OdAcct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalTrf', type=BalanceTransfer5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OdAcctBal', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSwtchDtls', type=AccountSwitchDetails1, min=1, max=1, mutex_group=None, array=False),
	))

