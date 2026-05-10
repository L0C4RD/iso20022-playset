from . import base_types
import CashAccount43
import MessageIdentification1
import AccountSwitchDetails1
import NewAccount4
import SupplementaryData1
import BalanceTransfer5

class AccountSwitchInformationRequestV05(base_types._BaseFieldType):

	__slots__ = ["_AcctSwtchDtls", "_SplmtryData", "_MsgId", "_OdAcct", "_BalTrf", "_NewAcct"]
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
	def NewAcct(self):
		return self._NewAcct

	@NewAcct.setter
	def NewAcct(self, value):
		self._NewAcct = value if type(value) != auto else self.make_default("NewAcct")

	@NewAcct.deleter
	def NewAcct(self):
		del self._NewAcct
		self._NewAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSwtchDtls', type=AccountSwitchDetails1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdAcct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrf', type=BalanceTransfer5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAcct', type=NewAccount4, min=1, max=1, mutex_group=None, array=False),
	))

