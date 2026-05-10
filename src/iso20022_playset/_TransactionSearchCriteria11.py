from . import base_types
from ._CashAccountEntrySearch8 import CashAccountEntrySearch8
from ._PaymentSearch10 import PaymentSearch10
from ._SystemSearch5 import SystemSearch5

class TransactionSearchCriteria11(base_types._BaseFieldType):

	__slots__ = ["_PmtTo", "_AcctNtrySch", "_PmtSch", "_PmtFr"]
	@property
	def AcctNtrySch(self):
		return self._AcctNtrySch

	@AcctNtrySch.setter
	def AcctNtrySch(self, value):
		self._AcctNtrySch = value if type(value) != base_types.auto else self.make_default("AcctNtrySch")

	@AcctNtrySch.deleter
	def AcctNtrySch(self):
		del self._AcctNtrySch
		self._AcctNtrySch = None

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if type(value) != base_types.auto else self.make_default("PmtFr")

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = None

	@property
	def PmtSch(self):
		return self._PmtSch

	@PmtSch.setter
	def PmtSch(self, value):
		self._PmtSch = value if type(value) != base_types.auto else self.make_default("PmtSch")

	@PmtSch.deleter
	def PmtSch(self):
		del self._PmtSch
		self._PmtSch = None

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if type(value) != base_types.auto else self.make_default("PmtTo")

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNtrySch', type=CashAccountEntrySearch8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=SystemSearch5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSch', type=PaymentSearch10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=SystemSearch5, min=0, max=None, mutex_group=None, array=True),
	))

