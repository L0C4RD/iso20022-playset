import base_types
import ISODate
import Max15PlusSignedNumericText

class CashAvailabilityDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_ActlDt", "_NbOfDays"]
	@property
	def ActlDt(self):
		return self._ActlDt

	@ActlDt.setter
	def ActlDt(self, value):
		self._ActlDt = value if type(value) != auto else self.make_default("ActlDt")

	@ActlDt.deleter
	def ActlDt(self):
		del self._ActlDt
		self._ActlDt = None

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if type(value) != auto else self.make_default("NbOfDays")

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Max15PlusSignedNumericText, min=0, max=1, mutex_group=1, array=False),
	))

