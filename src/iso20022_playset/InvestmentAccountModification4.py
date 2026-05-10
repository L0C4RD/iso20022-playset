from . import base_types
from .Max350Text import Max350Text
from .AdditionalReference13 import AdditionalReference13
from .Account23 import Account23
from .Max35Text import Max35Text

class InvestmentAccountModification4(base_types._BaseFieldType):

	__slots__ = ["_ModRsn", "_AcctApplId", "_ClntRef", "_CtrPtyRef", "_ExstgAcctId"]
	@property
	def ModRsn(self):
		return self._ModRsn

	@ModRsn.setter
	def ModRsn(self, value):
		self._ModRsn = value if type(value) != base_types.auto else self.make_default("ModRsn")

	@ModRsn.deleter
	def ModRsn(self):
		del self._ModRsn
		self._ModRsn = None

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
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != base_types.auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=None, mutex_group=None, array=True),
	))

