# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account23
from . import AccountManagementType3Code
from . import InvestmentAccount77
from . import LinkedMessage5Choice
from . import Max35Text

class AccountManagementMessageReference5(base_types._BaseFieldType):

	__slots__ = ["_AcctApplId", "_ExstgAcctId", "_InvstmtAcct", "_LkdRef", "_StsReqTp"]
	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if value is not None else base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if value is not None else base_types.UninitialisedField(self, 'ExstgAcctId', Account23, False)

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = base_types.UninitialisedField(self, 'ExstgAcctId', Account23, False)

	@property
	def InvstmtAcct(self):
		return self._InvstmtAcct

	@InvstmtAcct.setter
	def InvstmtAcct(self, value):
		self._InvstmtAcct = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcct', InvestmentAccount77, False)

	@InvstmtAcct.deleter
	def InvstmtAcct(self):
		del self._InvstmtAcct
		self._InvstmtAcct = base_types.UninitialisedField(self, 'InvstmtAcct', InvestmentAccount77, False)

	@property
	def LkdRef(self):
		return self._LkdRef

	@LkdRef.setter
	def LkdRef(self, value):
		self._LkdRef = value if value is not None else base_types.UninitialisedField(self, 'LkdRef', LinkedMessage5Choice, False)

	@LkdRef.deleter
	def LkdRef(self):
		del self._LkdRef
		self._LkdRef = base_types.UninitialisedField(self, 'LkdRef', LinkedMessage5Choice, False)

	@property
	def StsReqTp(self):
		return self._StsReqTp

	@StsReqTp.setter
	def StsReqTp(self, value):
		self._StsReqTp = value if value is not None else base_types.UninitialisedField(self, 'StsReqTp', AccountManagementType3Code, False)

	@StsReqTp.deleter
	def StsReqTp(self):
		del self._StsReqTp
		self._StsReqTp = base_types.UninitialisedField(self, 'StsReqTp', AccountManagementType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcct', type=InvestmentAccount77, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkdRef', type=LinkedMessage5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsReqTp', type=AccountManagementType3Code, min=1, max=1, mutex_group=None, array=False),
	))