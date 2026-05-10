from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .BalanceTransfer5 import BalanceTransfer5
from .MessageIdentification1 import MessageIdentification1
from .CashAccount43 import CashAccount43
from .AccountSwitchDetails1 import AccountSwitchDetails1

class AccountSwitchRequestBalanceTransferV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_NewAcct", "_NmntdAcct", "_AcctSwtchDtls", "_BalTrf", "_MsgId"]
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
	def NewAcct(self):
		return self._NewAcct

	@NewAcct.setter
	def NewAcct(self, value):
		self._NewAcct = value if type(value) != base_types.auto else self.make_default("NewAcct")

	@NewAcct.deleter
	def NewAcct(self):
		del self._NewAcct
		self._NewAcct = None

	@property
	def NmntdAcct(self):
		return self._NmntdAcct

	@NmntdAcct.setter
	def NmntdAcct(self, value):
		self._NmntdAcct = value if type(value) != base_types.auto else self.make_default("NmntdAcct")

	@NmntdAcct.deleter
	def NmntdAcct(self):
		del self._NmntdAcct
		self._NmntdAcct = None

	@property
	def AcctSwtchDtls(self):
		return self._AcctSwtchDtls

	@AcctSwtchDtls.setter
	def AcctSwtchDtls(self, value):
		self._AcctSwtchDtls = value if type(value) != base_types.auto else self.make_default("AcctSwtchDtls")

	@AcctSwtchDtls.deleter
	def AcctSwtchDtls(self):
		del self._AcctSwtchDtls
		self._AcctSwtchDtls = None

	@property
	def BalTrf(self):
		return self._BalTrf

	@BalTrf.setter
	def BalTrf(self, value):
		self._BalTrf = value if type(value) != base_types.auto else self.make_default("BalTrf")

	@BalTrf.deleter
	def BalTrf(self):
		del self._BalTrf
		self._BalTrf = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAcct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmntdAcct', type=CashAccount43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSwtchDtls', type=AccountSwitchDetails1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrf', type=BalanceTransfer5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

