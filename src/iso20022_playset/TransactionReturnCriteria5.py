from . import base_types
from .AccountCashEntryReturnCriteria3 import AccountCashEntryReturnCriteria3
from .PaymentReturnCriteria4 import PaymentReturnCriteria4
from .SystemReturnCriteria2 import SystemReturnCriteria2

class TransactionReturnCriteria5(base_types._BaseFieldType):

	__slots__ = ["_AcctCshNtryRtrCrit", "_PmtRtrCrit", "_PmtToRtrCrit", "_PmtFrRtrCrit"]
	@property
	def AcctCshNtryRtrCrit(self):
		return self._AcctCshNtryRtrCrit

	@AcctCshNtryRtrCrit.setter
	def AcctCshNtryRtrCrit(self, value):
		self._AcctCshNtryRtrCrit = value if type(value) != base_types.auto else self.make_default("AcctCshNtryRtrCrit")

	@AcctCshNtryRtrCrit.deleter
	def AcctCshNtryRtrCrit(self):
		del self._AcctCshNtryRtrCrit
		self._AcctCshNtryRtrCrit = None

	@property
	def PmtRtrCrit(self):
		return self._PmtRtrCrit

	@PmtRtrCrit.setter
	def PmtRtrCrit(self, value):
		self._PmtRtrCrit = value if type(value) != base_types.auto else self.make_default("PmtRtrCrit")

	@PmtRtrCrit.deleter
	def PmtRtrCrit(self):
		del self._PmtRtrCrit
		self._PmtRtrCrit = None

	@property
	def PmtToRtrCrit(self):
		return self._PmtToRtrCrit

	@PmtToRtrCrit.setter
	def PmtToRtrCrit(self, value):
		self._PmtToRtrCrit = value if type(value) != base_types.auto else self.make_default("PmtToRtrCrit")

	@PmtToRtrCrit.deleter
	def PmtToRtrCrit(self):
		del self._PmtToRtrCrit
		self._PmtToRtrCrit = None

	@property
	def PmtFrRtrCrit(self):
		return self._PmtFrRtrCrit

	@PmtFrRtrCrit.setter
	def PmtFrRtrCrit(self, value):
		self._PmtFrRtrCrit = value if type(value) != base_types.auto else self.make_default("PmtFrRtrCrit")

	@PmtFrRtrCrit.deleter
	def PmtFrRtrCrit(self):
		del self._PmtFrRtrCrit
		self._PmtFrRtrCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctCshNtryRtrCrit', type=AccountCashEntryReturnCriteria3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRtrCrit', type=PaymentReturnCriteria4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtToRtrCrit', type=SystemReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrRtrCrit', type=SystemReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
	))

