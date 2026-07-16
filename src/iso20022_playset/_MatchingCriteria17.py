# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractMatchingCriteria3
from . import CounterpartyMatchingCriteria6
from . import TransactionMatchingCriteria7
from . import ValuationMatchingCriteria1

class MatchingCriteria17(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyMtchgCrit", "_CtrctMtchgCrit", "_TxMtchgCrit", "_ValtnMtchgCrit"]
	@property
	def CtrPtyMtchgCrit(self):
		return self._CtrPtyMtchgCrit

	@CtrPtyMtchgCrit.setter
	def CtrPtyMtchgCrit(self, value):
		self._CtrPtyMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMtchgCrit', CounterpartyMatchingCriteria6, False)

	@CtrPtyMtchgCrit.deleter
	def CtrPtyMtchgCrit(self):
		del self._CtrPtyMtchgCrit
		self._CtrPtyMtchgCrit = base_types.UninitialisedField(self, 'CtrPtyMtchgCrit', CounterpartyMatchingCriteria6, False)

	@property
	def CtrctMtchgCrit(self):
		return self._CtrctMtchgCrit

	@CtrctMtchgCrit.setter
	def CtrctMtchgCrit(self, value):
		self._CtrctMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'CtrctMtchgCrit', ContractMatchingCriteria3, False)

	@CtrctMtchgCrit.deleter
	def CtrctMtchgCrit(self):
		del self._CtrctMtchgCrit
		self._CtrctMtchgCrit = base_types.UninitialisedField(self, 'CtrctMtchgCrit', ContractMatchingCriteria3, False)

	@property
	def TxMtchgCrit(self):
		return self._TxMtchgCrit

	@TxMtchgCrit.setter
	def TxMtchgCrit(self, value):
		self._TxMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'TxMtchgCrit', TransactionMatchingCriteria7, False)

	@TxMtchgCrit.deleter
	def TxMtchgCrit(self):
		del self._TxMtchgCrit
		self._TxMtchgCrit = base_types.UninitialisedField(self, 'TxMtchgCrit', TransactionMatchingCriteria7, False)

	@property
	def ValtnMtchgCrit(self):
		return self._ValtnMtchgCrit

	@ValtnMtchgCrit.setter
	def ValtnMtchgCrit(self, value):
		self._ValtnMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'ValtnMtchgCrit', ValuationMatchingCriteria1, False)

	@ValtnMtchgCrit.deleter
	def ValtnMtchgCrit(self):
		del self._ValtnMtchgCrit
		self._ValtnMtchgCrit = base_types.UninitialisedField(self, 'ValtnMtchgCrit', ValuationMatchingCriteria1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyMtchgCrit', type=CounterpartyMatchingCriteria6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMtchgCrit', type=ContractMatchingCriteria3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxMtchgCrit', type=TransactionMatchingCriteria7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnMtchgCrit', type=ValuationMatchingCriteria1, min=0, max=1, mutex_group=None, array=False),
	))