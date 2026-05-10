import base_types
import Max35Text
import ConfirmationType1Choice
import AdditionalReference13
import Account23

class AccountManagementConfirmation5(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_ExstgAcctId", "_AcctApplId", "_CtrPtyRef", "_ConfTp"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if type(value) != auto else self.make_default("ExstgAcctId")

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = None

	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if type(value) != auto else self.make_default("AcctApplId")

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = None

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

	@property
	def ConfTp(self):
		return self._ConfTp

	@ConfTp.setter
	def ConfTp(self, value):
		self._ConfTp = value if type(value) != auto else self.make_default("ConfTp")

	@ConfTp.deleter
	def ConfTp(self):
		del self._ConfTp
		self._ConfTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfTp', type=ConfirmationType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

