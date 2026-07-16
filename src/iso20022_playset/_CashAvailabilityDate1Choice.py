# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max15PlusSignedNumericText

class CashAvailabilityDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_ActlDt", "_NbOfDays"]
	@property
	def ActlDt(self):
		return self._ActlDt

	@ActlDt.setter
	def ActlDt(self, value):
		self._ActlDt = value if value is not None else base_types.UninitialisedField(self, 'ActlDt', ISODate, False)

	@ActlDt.deleter
	def ActlDt(self):
		del self._ActlDt
		self._ActlDt = base_types.UninitialisedField(self, 'ActlDt', ISODate, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Max15PlusSignedNumericText, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Max15PlusSignedNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Max15PlusSignedNumericText, min=0, max=1, mutex_group=1, array=False),
	))