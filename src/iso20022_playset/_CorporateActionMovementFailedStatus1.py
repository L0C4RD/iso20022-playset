from . import base_types
from ._FailedMovement1 import FailedMovement1
from ._Max35Text import Max35Text
from ._PartyIdentification2Choice import PartyIdentification2Choice

class CorporateActionMovementFailedStatus1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_AgtAcctId", "_ClntAcctId", "_RsrcDtls"]
	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != base_types.auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	@property
	def AgtAcctId(self):
		return self._AgtAcctId

	@AgtAcctId.setter
	def AgtAcctId(self, value):
		self._AgtAcctId = value if type(value) != base_types.auto else self.make_default("AgtAcctId")

	@AgtAcctId.deleter
	def AgtAcctId(self):
		del self._AgtAcctId
		self._AgtAcctId = None

	@property
	def ClntAcctId(self):
		return self._ClntAcctId

	@ClntAcctId.setter
	def ClntAcctId(self, value):
		self._ClntAcctId = value if type(value) != base_types.auto else self.make_default("ClntAcctId")

	@ClntAcctId.deleter
	def ClntAcctId(self):
		del self._ClntAcctId
		self._ClntAcctId = None

	@property
	def RsrcDtls(self):
		return self._RsrcDtls

	@RsrcDtls.setter
	def RsrcDtls(self, value):
		self._RsrcDtls = value if type(value) != base_types.auto else self.make_default("RsrcDtls")

	@RsrcDtls.deleter
	def RsrcDtls(self):
		del self._RsrcDtls
		self._RsrcDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtAcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcDtls', type=FailedMovement1, min=1, max=None, mutex_group=None, array=True),
	))

