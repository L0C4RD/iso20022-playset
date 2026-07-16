# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODateTime

class PayInScheduleItems1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ddln"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Ddln(self):
		return self._Ddln

	@Ddln.setter
	def Ddln(self, value):
		self._Ddln = value if value is not None else base_types.UninitialisedField(self, 'Ddln', ISODateTime, False)

	@Ddln.deleter
	def Ddln(self):
		del self._Ddln
		self._Ddln = base_types.UninitialisedField(self, 'Ddln', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ddln', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))