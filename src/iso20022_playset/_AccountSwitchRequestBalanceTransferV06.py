# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchDetails1
from . import BalanceTransfer7
from . import CashAccount43
from . import MessageIdentification1
from . import SupplementaryData1

class AccountSwitchRequestBalanceTransferV06(base_types._BaseFieldType):

	__slots__ = ["_AcctSwtchDtls", "_BalTrf", "_MsgId", "_NewAcct", "_NmntdAcct", "_SplmtryData"]
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
	def BalTrf(self):
		return self._BalTrf

	@BalTrf.setter
	def BalTrf(self, value):
		self._BalTrf = value if value is not None else base_types.UninitialisedField(self, 'BalTrf', BalanceTransfer7, True)

	@BalTrf.deleter
	def BalTrf(self):
		del self._BalTrf
		self._BalTrf = base_types.UninitialisedField(self, 'BalTrf', BalanceTransfer7, True)

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
	def NewAcct(self):
		return self._NewAcct

	@NewAcct.setter
	def NewAcct(self, value):
		self._NewAcct = value if value is not None else base_types.UninitialisedField(self, 'NewAcct', CashAccount43, False)

	@NewAcct.deleter
	def NewAcct(self):
		del self._NewAcct
		self._NewAcct = base_types.UninitialisedField(self, 'NewAcct', CashAccount43, False)

	@property
	def NmntdAcct(self):
		return self._NmntdAcct

	@NmntdAcct.setter
	def NmntdAcct(self, value):
		self._NmntdAcct = value if value is not None else base_types.UninitialisedField(self, 'NmntdAcct', CashAccount43, False)

	@NmntdAcct.deleter
	def NmntdAcct(self):
		del self._NmntdAcct
		self._NmntdAcct = base_types.UninitialisedField(self, 'NmntdAcct', CashAccount43, False)

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
		base_types.FieldEntry(name='BalTrf', type=BalanceTransfer7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewAcct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmntdAcct', type=CashAccount43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))