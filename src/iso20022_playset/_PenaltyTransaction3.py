from . import base_types
from ._PartyIdentification136 import PartyIdentification136
from ._PenaltyNetMovementRecord1 import PenaltyNetMovementRecord1
from ._PenaltyTransactionRecord2 import PenaltyTransactionRecord2
from ._TransactionIdentifications55 import TransactionIdentifications55

class PenaltyTransaction3(base_types._BaseFieldType):

	__slots__ = ["_NetMvmntDtls", "_Ref", "_RefOwnr", "_TxDtls"]
	@property
	def NetMvmntDtls(self):
		return self._NetMvmntDtls

	@NetMvmntDtls.setter
	def NetMvmntDtls(self, value):
		self._NetMvmntDtls = value if type(value) != base_types.auto else self.make_default("NetMvmntDtls")

	@NetMvmntDtls.deleter
	def NetMvmntDtls(self):
		del self._NetMvmntDtls
		self._NetMvmntDtls = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RefOwnr(self):
		return self._RefOwnr

	@RefOwnr.setter
	def RefOwnr(self, value):
		self._RefOwnr = value if type(value) != base_types.auto else self.make_default("RefOwnr")

	@RefOwnr.deleter
	def RefOwnr(self):
		del self._RefOwnr
		self._RefOwnr = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetMvmntDtls', type=PenaltyNetMovementRecord1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=TransactionIdentifications55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=PenaltyTransactionRecord2, min=0, max=1, mutex_group=None, array=False),
	))

