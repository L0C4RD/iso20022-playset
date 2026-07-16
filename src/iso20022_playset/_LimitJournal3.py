# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import LimitAmount1
from . import LimitJournalEntry3

class LimitJournal3(base_types._BaseFieldType):

	__slots__ = ["_JrnlActvtyDt", "_JrnlNtry", "_Lmt"]
	@property
	def JrnlActvtyDt(self):
		return self._JrnlActvtyDt

	@JrnlActvtyDt.setter
	def JrnlActvtyDt(self, value):
		self._JrnlActvtyDt = value if value is not None else base_types.UninitialisedField(self, 'JrnlActvtyDt', ISODate, False)

	@JrnlActvtyDt.deleter
	def JrnlActvtyDt(self):
		del self._JrnlActvtyDt
		self._JrnlActvtyDt = base_types.UninitialisedField(self, 'JrnlActvtyDt', ISODate, False)

	@property
	def JrnlNtry(self):
		return self._JrnlNtry

	@JrnlNtry.setter
	def JrnlNtry(self, value):
		self._JrnlNtry = value if value is not None else base_types.UninitialisedField(self, 'JrnlNtry', LimitJournalEntry3, True)

	@JrnlNtry.deleter
	def JrnlNtry(self):
		del self._JrnlNtry
		self._JrnlNtry = base_types.UninitialisedField(self, 'JrnlNtry', LimitJournalEntry3, True)

	@property
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if value is not None else base_types.UninitialisedField(self, 'Lmt', LimitAmount1, False)

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = base_types.UninitialisedField(self, 'Lmt', LimitAmount1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='JrnlActvtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnlNtry', type=LimitJournalEntry3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lmt', type=LimitAmount1, min=1, max=1, mutex_group=None, array=False),
	))