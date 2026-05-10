from . import base_types
from ._ContractMatchingCriteria3 import ContractMatchingCriteria3
from ._CounterpartyMatchingCriteria6 import CounterpartyMatchingCriteria6
from ._TransactionMatchingCriteria7 import TransactionMatchingCriteria7
from ._ValuationMatchingCriteria1 import ValuationMatchingCriteria1

class MatchingCriteria17(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyMtchgCrit", "_CtrctMtchgCrit", "_TxMtchgCrit", "_ValtnMtchgCrit"]
	@property
	def CtrPtyMtchgCrit(self):
		return self._CtrPtyMtchgCrit

	@CtrPtyMtchgCrit.setter
	def CtrPtyMtchgCrit(self, value):
		self._CtrPtyMtchgCrit = value if type(value) != base_types.auto else self.make_default("CtrPtyMtchgCrit")

	@CtrPtyMtchgCrit.deleter
	def CtrPtyMtchgCrit(self):
		del self._CtrPtyMtchgCrit
		self._CtrPtyMtchgCrit = None

	@property
	def CtrctMtchgCrit(self):
		return self._CtrctMtchgCrit

	@CtrctMtchgCrit.setter
	def CtrctMtchgCrit(self, value):
		self._CtrctMtchgCrit = value if type(value) != base_types.auto else self.make_default("CtrctMtchgCrit")

	@CtrctMtchgCrit.deleter
	def CtrctMtchgCrit(self):
		del self._CtrctMtchgCrit
		self._CtrctMtchgCrit = None

	@property
	def TxMtchgCrit(self):
		return self._TxMtchgCrit

	@TxMtchgCrit.setter
	def TxMtchgCrit(self, value):
		self._TxMtchgCrit = value if type(value) != base_types.auto else self.make_default("TxMtchgCrit")

	@TxMtchgCrit.deleter
	def TxMtchgCrit(self):
		del self._TxMtchgCrit
		self._TxMtchgCrit = None

	@property
	def ValtnMtchgCrit(self):
		return self._ValtnMtchgCrit

	@ValtnMtchgCrit.setter
	def ValtnMtchgCrit(self, value):
		self._ValtnMtchgCrit = value if type(value) != base_types.auto else self.make_default("ValtnMtchgCrit")

	@ValtnMtchgCrit.deleter
	def ValtnMtchgCrit(self):
		del self._ValtnMtchgCrit
		self._ValtnMtchgCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyMtchgCrit', type=CounterpartyMatchingCriteria6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMtchgCrit', type=ContractMatchingCriteria3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxMtchgCrit', type=TransactionMatchingCriteria7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnMtchgCrit', type=ValuationMatchingCriteria1, min=0, max=1, mutex_group=None, array=False),
	))

