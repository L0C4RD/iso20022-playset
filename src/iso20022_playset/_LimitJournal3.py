from . import base_types
from ._LimitAmount1 import LimitAmount1
from ._LimitJournalEntry3 import LimitJournalEntry3
from ._ISODate import ISODate

class LimitJournal3(base_types._BaseFieldType):

	__slots__ = ["_Lmt", "_JrnlNtry", "_JrnlActvtyDt"]
	@property
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if type(value) != base_types.auto else self.make_default("Lmt")

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = None

	@property
	def JrnlNtry(self):
		return self._JrnlNtry

	@JrnlNtry.setter
	def JrnlNtry(self, value):
		self._JrnlNtry = value if type(value) != base_types.auto else self.make_default("JrnlNtry")

	@JrnlNtry.deleter
	def JrnlNtry(self):
		del self._JrnlNtry
		self._JrnlNtry = None

	@property
	def JrnlActvtyDt(self):
		return self._JrnlActvtyDt

	@JrnlActvtyDt.setter
	def JrnlActvtyDt(self, value):
		self._JrnlActvtyDt = value if type(value) != base_types.auto else self.make_default("JrnlActvtyDt")

	@JrnlActvtyDt.deleter
	def JrnlActvtyDt(self):
		del self._JrnlActvtyDt
		self._JrnlActvtyDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lmt', type=LimitAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnlNtry', type=LimitJournalEntry3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='JrnlActvtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

