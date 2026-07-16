# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Frequency3Code
from . import ISODate
from . import Number

class RecurringTransaction3(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_IntrvlDay", "_NbOfOcrncs", "_PrdUnit", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@property
	def IntrvlDay(self):
		return self._IntrvlDay

	@IntrvlDay.setter
	def IntrvlDay(self, value):
		self._IntrvlDay = value if value is not None else base_types.UninitialisedField(self, 'IntrvlDay', Number, False)

	@IntrvlDay.deleter
	def IntrvlDay(self):
		del self._IntrvlDay
		self._IntrvlDay = base_types.UninitialisedField(self, 'IntrvlDay', Number, False)

	@property
	def NbOfOcrncs(self):
		return self._NbOfOcrncs

	@NbOfOcrncs.setter
	def NbOfOcrncs(self, value):
		self._NbOfOcrncs = value if value is not None else base_types.UninitialisedField(self, 'NbOfOcrncs', Number, False)

	@NbOfOcrncs.deleter
	def NbOfOcrncs(self):
		del self._NbOfOcrncs
		self._NbOfOcrncs = base_types.UninitialisedField(self, 'NbOfOcrncs', Number, False)

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if value is not None else base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrvlDay', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOcrncs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))