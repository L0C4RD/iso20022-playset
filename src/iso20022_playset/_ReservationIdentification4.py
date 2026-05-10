from . import base_types
from .Max35Text import Max35Text
from .ReservationType2Choice import ReservationType2Choice
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .AccountIdentification4Choice import AccountIdentification4Choice
from .SystemIdentification2Choice import SystemIdentification2Choice

class ReservationIdentification4(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_Tp", "_SysId", "_RsvatnId", "_AcctId"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def RsvatnId(self):
		return self._RsvatnId

	@RsvatnId.setter
	def RsvatnId(self, value):
		self._RsvatnId = value if type(value) != base_types.auto else self.make_default("RsvatnId")

	@RsvatnId.deleter
	def RsvatnId(self):
		del self._RsvatnId
		self._RsvatnId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReservationType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
	))

