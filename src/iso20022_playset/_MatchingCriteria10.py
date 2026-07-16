# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralMatchingCriteria6
from . import CounterpartyMatchingCriteria4
from . import LoanMatchingCriteria9

class MatchingCriteria10(base_types._BaseFieldType):

	__slots__ = ["_CollMtchgCrit", "_CtrPtyMtchgCrit", "_LnMtchgCrit"]
	@property
	def CollMtchgCrit(self):
		return self._CollMtchgCrit

	@CollMtchgCrit.setter
	def CollMtchgCrit(self, value):
		self._CollMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'CollMtchgCrit', CollateralMatchingCriteria6, False)

	@CollMtchgCrit.deleter
	def CollMtchgCrit(self):
		del self._CollMtchgCrit
		self._CollMtchgCrit = base_types.UninitialisedField(self, 'CollMtchgCrit', CollateralMatchingCriteria6, False)

	@property
	def CtrPtyMtchgCrit(self):
		return self._CtrPtyMtchgCrit

	@CtrPtyMtchgCrit.setter
	def CtrPtyMtchgCrit(self, value):
		self._CtrPtyMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMtchgCrit', CounterpartyMatchingCriteria4, False)

	@CtrPtyMtchgCrit.deleter
	def CtrPtyMtchgCrit(self):
		del self._CtrPtyMtchgCrit
		self._CtrPtyMtchgCrit = base_types.UninitialisedField(self, 'CtrPtyMtchgCrit', CounterpartyMatchingCriteria4, False)

	@property
	def LnMtchgCrit(self):
		return self._LnMtchgCrit

	@LnMtchgCrit.setter
	def LnMtchgCrit(self, value):
		self._LnMtchgCrit = value if value is not None else base_types.UninitialisedField(self, 'LnMtchgCrit', LoanMatchingCriteria9, False)

	@LnMtchgCrit.deleter
	def LnMtchgCrit(self):
		del self._LnMtchgCrit
		self._LnMtchgCrit = base_types.UninitialisedField(self, 'LnMtchgCrit', LoanMatchingCriteria9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMtchgCrit', type=CollateralMatchingCriteria6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMtchgCrit', type=CounterpartyMatchingCriteria4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnMtchgCrit', type=LoanMatchingCriteria9, min=0, max=1, mutex_group=None, array=False),
	))