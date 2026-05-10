from . import base_types
from ._Account23 import Account23
from ._AccountManagementType3Code import AccountManagementType3Code
from ._Max35Text import Max35Text
from ._InvestmentAccount77 import InvestmentAccount77
from ._LinkedMessage5Choice import LinkedMessage5Choice

class AccountManagementMessageReference5(base_types._BaseFieldType):

	__slots__ = ["_ExstgAcctId", "_InvstmtAcct", "_AcctApplId", "_StsReqTp", "_LkdRef"]
	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if type(value) != base_types.auto else self.make_default("AcctApplId")

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = None

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if type(value) != base_types.auto else self.make_default("ExstgAcctId")

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = None

	@property
	def InvstmtAcct(self):
		return self._InvstmtAcct

	@InvstmtAcct.setter
	def InvstmtAcct(self, value):
		self._InvstmtAcct = value if type(value) != base_types.auto else self.make_default("InvstmtAcct")

	@InvstmtAcct.deleter
	def InvstmtAcct(self):
		del self._InvstmtAcct
		self._InvstmtAcct = None

	@property
	def LkdRef(self):
		return self._LkdRef

	@LkdRef.setter
	def LkdRef(self, value):
		self._LkdRef = value if type(value) != base_types.auto else self.make_default("LkdRef")

	@LkdRef.deleter
	def LkdRef(self):
		del self._LkdRef
		self._LkdRef = None

	@property
	def StsReqTp(self):
		return self._StsReqTp

	@StsReqTp.setter
	def StsReqTp(self, value):
		self._StsReqTp = value if type(value) != base_types.auto else self.make_default("StsReqTp")

	@StsReqTp.deleter
	def StsReqTp(self):
		del self._StsReqTp
		self._StsReqTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcct', type=InvestmentAccount77, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkdRef', type=LinkedMessage5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsReqTp', type=AccountManagementType3Code, min=1, max=1, mutex_group=None, array=False),
	))

