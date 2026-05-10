from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .AccountSwitchDetails1 import AccountSwitchDetails1
from .MessageIdentification1 import MessageIdentification1

class AccountSwitchTerminationSwitchV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgId", "_AcctSwtchDtls"]
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
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSwtchDtls', type=AccountSwitchDetails1, min=1, max=1, mutex_group=None, array=False),
	))

