# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import EquivalentAmount2

class AmountType4Choice(base_types._BaseFieldType):

	__slots__ = ["_EqvtAmt", "_InstdAmt"]
	@property
	def EqvtAmt(self):
		return self._EqvtAmt

	@EqvtAmt.setter
	def EqvtAmt(self, value):
		self._EqvtAmt = value if value is not None else base_types.UninitialisedField(self, 'EqvtAmt', EquivalentAmount2, False)

	@EqvtAmt.deleter
	def EqvtAmt(self):
		del self._EqvtAmt
		self._EqvtAmt = base_types.UninitialisedField(self, 'EqvtAmt', EquivalentAmount2, False)

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if value is not None else base_types.UninitialisedField(self, 'InstdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = base_types.UninitialisedField(self, 'InstdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EqvtAmt', type=EquivalentAmount2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))