from . import base_types
from .LoanMatchingCriteria9 import LoanMatchingCriteria9
from .CollateralMatchingCriteria6 import CollateralMatchingCriteria6
from .CounterpartyMatchingCriteria4 import CounterpartyMatchingCriteria4

class MatchingCriteria10(base_types._BaseFieldType):

	__slots__ = ["_LnMtchgCrit", "_CtrPtyMtchgCrit", "_CollMtchgCrit"]
	@property
	def LnMtchgCrit(self):
		return self._LnMtchgCrit

	@LnMtchgCrit.setter
	def LnMtchgCrit(self, value):
		self._LnMtchgCrit = value if type(value) != base_types.auto else self.make_default("LnMtchgCrit")

	@LnMtchgCrit.deleter
	def LnMtchgCrit(self):
		del self._LnMtchgCrit
		self._LnMtchgCrit = None

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
	def CollMtchgCrit(self):
		return self._CollMtchgCrit

	@CollMtchgCrit.setter
	def CollMtchgCrit(self, value):
		self._CollMtchgCrit = value if type(value) != base_types.auto else self.make_default("CollMtchgCrit")

	@CollMtchgCrit.deleter
	def CollMtchgCrit(self):
		del self._CollMtchgCrit
		self._CollMtchgCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LnMtchgCrit', type=LoanMatchingCriteria9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMtchgCrit', type=CounterpartyMatchingCriteria4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMtchgCrit', type=CollateralMatchingCriteria6, min=0, max=1, mutex_group=None, array=False),
	))

