# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import ISODate
from . import Max70Text
from . import PlusOrMinusIndicator

class AmountAndDirection111(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Dt", "_Labl", "_Sgn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', CurrencyAndAmount, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if value is not None else base_types.UninitialisedField(self, 'Labl', Max70Text, False)

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = base_types.UninitialisedField(self, 'Labl', Max70Text, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Labl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))