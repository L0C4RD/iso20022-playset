import base_types
import Frequency3Code
import ISODate
import Number

class RecurringTransaction3(base_types._BaseFieldType):

	__slots__ = ["_IntrvlDay", "_EndDt", "_PrdUnit", "_NbOfOcrncs", "_StartDt"]
	@property
	def IntrvlDay(self):
		return self._IntrvlDay

	@IntrvlDay.setter
	def IntrvlDay(self, value):
		self._IntrvlDay = value if type(value) != auto else self.make_default("IntrvlDay")

	@IntrvlDay.deleter
	def IntrvlDay(self):
		del self._IntrvlDay
		self._IntrvlDay = None

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if type(value) != auto else self.make_default("PrdUnit")

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = None

	@property
	def NbOfOcrncs(self):
		return self._NbOfOcrncs

	@NbOfOcrncs.setter
	def NbOfOcrncs(self, value):
		self._NbOfOcrncs = value if type(value) != auto else self.make_default("NbOfOcrncs")

	@NbOfOcrncs.deleter
	def NbOfOcrncs(self):
		del self._NbOfOcrncs
		self._NbOfOcrncs = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrvlDay', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOcrncs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

