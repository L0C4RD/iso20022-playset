# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountEntrySearch8
from . import PaymentSearch10
from . import SystemSearch5

class TransactionSearchCriteria11(base_types._BaseFieldType):

	__slots__ = ["_AcctNtrySch", "_PmtFr", "_PmtSch", "_PmtTo"]
	@property
	def AcctNtrySch(self):
		return self._AcctNtrySch

	@AcctNtrySch.setter
	def AcctNtrySch(self, value):
		self._AcctNtrySch = value if value is not None else base_types.UninitialisedField(self, 'AcctNtrySch', CashAccountEntrySearch8, False)

	@AcctNtrySch.deleter
	def AcctNtrySch(self):
		del self._AcctNtrySch
		self._AcctNtrySch = base_types.UninitialisedField(self, 'AcctNtrySch', CashAccountEntrySearch8, False)

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if value is not None else base_types.UninitialisedField(self, 'PmtFr', SystemSearch5, True)

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = base_types.UninitialisedField(self, 'PmtFr', SystemSearch5, True)

	@property
	def PmtSch(self):
		return self._PmtSch

	@PmtSch.setter
	def PmtSch(self, value):
		self._PmtSch = value if value is not None else base_types.UninitialisedField(self, 'PmtSch', PaymentSearch10, False)

	@PmtSch.deleter
	def PmtSch(self):
		del self._PmtSch
		self._PmtSch = base_types.UninitialisedField(self, 'PmtSch', PaymentSearch10, False)

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if value is not None else base_types.UninitialisedField(self, 'PmtTo', SystemSearch5, True)

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = base_types.UninitialisedField(self, 'PmtTo', SystemSearch5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNtrySch', type=CashAccountEntrySearch8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=SystemSearch5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSch', type=PaymentSearch10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=SystemSearch5, min=0, max=None, mutex_group=None, array=True),
	))