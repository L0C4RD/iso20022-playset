# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountCashEntryReturnCriteria3
from . import PaymentReturnCriteria4
from . import SystemReturnCriteria2

class TransactionReturnCriteria5(base_types._BaseFieldType):

	__slots__ = ["_AcctCshNtryRtrCrit", "_PmtFrRtrCrit", "_PmtRtrCrit", "_PmtToRtrCrit"]
	@property
	def AcctCshNtryRtrCrit(self):
		return self._AcctCshNtryRtrCrit

	@AcctCshNtryRtrCrit.setter
	def AcctCshNtryRtrCrit(self, value):
		self._AcctCshNtryRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'AcctCshNtryRtrCrit', AccountCashEntryReturnCriteria3, False)

	@AcctCshNtryRtrCrit.deleter
	def AcctCshNtryRtrCrit(self):
		del self._AcctCshNtryRtrCrit
		self._AcctCshNtryRtrCrit = base_types.UninitialisedField(self, 'AcctCshNtryRtrCrit', AccountCashEntryReturnCriteria3, False)

	@property
	def PmtFrRtrCrit(self):
		return self._PmtFrRtrCrit

	@PmtFrRtrCrit.setter
	def PmtFrRtrCrit(self, value):
		self._PmtFrRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'PmtFrRtrCrit', SystemReturnCriteria2, False)

	@PmtFrRtrCrit.deleter
	def PmtFrRtrCrit(self):
		del self._PmtFrRtrCrit
		self._PmtFrRtrCrit = base_types.UninitialisedField(self, 'PmtFrRtrCrit', SystemReturnCriteria2, False)

	@property
	def PmtRtrCrit(self):
		return self._PmtRtrCrit

	@PmtRtrCrit.setter
	def PmtRtrCrit(self, value):
		self._PmtRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'PmtRtrCrit', PaymentReturnCriteria4, False)

	@PmtRtrCrit.deleter
	def PmtRtrCrit(self):
		del self._PmtRtrCrit
		self._PmtRtrCrit = base_types.UninitialisedField(self, 'PmtRtrCrit', PaymentReturnCriteria4, False)

	@property
	def PmtToRtrCrit(self):
		return self._PmtToRtrCrit

	@PmtToRtrCrit.setter
	def PmtToRtrCrit(self, value):
		self._PmtToRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'PmtToRtrCrit', SystemReturnCriteria2, False)

	@PmtToRtrCrit.deleter
	def PmtToRtrCrit(self):
		del self._PmtToRtrCrit
		self._PmtToRtrCrit = base_types.UninitialisedField(self, 'PmtToRtrCrit', SystemReturnCriteria2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctCshNtryRtrCrit', type=AccountCashEntryReturnCriteria3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrRtrCrit', type=SystemReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRtrCrit', type=PaymentReturnCriteria4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtToRtrCrit', type=SystemReturnCriteria2, min=0, max=1, mutex_group=None, array=False),
	))