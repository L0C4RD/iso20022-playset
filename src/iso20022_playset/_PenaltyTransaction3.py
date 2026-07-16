# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification136
from . import PenaltyNetMovementRecord1
from . import PenaltyTransactionRecord2
from . import TransactionIdentifications55

class PenaltyTransaction3(base_types._BaseFieldType):

	__slots__ = ["_NetMvmntDtls", "_Ref", "_RefOwnr", "_TxDtls"]
	@property
	def NetMvmntDtls(self):
		return self._NetMvmntDtls

	@NetMvmntDtls.setter
	def NetMvmntDtls(self, value):
		self._NetMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'NetMvmntDtls', PenaltyNetMovementRecord1, False)

	@NetMvmntDtls.deleter
	def NetMvmntDtls(self):
		del self._NetMvmntDtls
		self._NetMvmntDtls = base_types.UninitialisedField(self, 'NetMvmntDtls', PenaltyNetMovementRecord1, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', TransactionIdentifications55, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', TransactionIdentifications55, False)

	@property
	def RefOwnr(self):
		return self._RefOwnr

	@RefOwnr.setter
	def RefOwnr(self, value):
		self._RefOwnr = value if value is not None else base_types.UninitialisedField(self, 'RefOwnr', PartyIdentification136, False)

	@RefOwnr.deleter
	def RefOwnr(self):
		del self._RefOwnr
		self._RefOwnr = base_types.UninitialisedField(self, 'RefOwnr', PartyIdentification136, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', PenaltyTransactionRecord2, False)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', PenaltyTransactionRecord2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetMvmntDtls', type=PenaltyNetMovementRecord1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=TransactionIdentifications55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=PenaltyTransactionRecord2, min=0, max=1, mutex_group=None, array=False),
	))