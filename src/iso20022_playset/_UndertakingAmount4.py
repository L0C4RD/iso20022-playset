# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class UndertakingAmount4(base_types._BaseFieldType):

	__slots__ = ["_BalAmt", "_VartnAmt"]
	@property
	def BalAmt(self):
		return self._BalAmt

	@BalAmt.setter
	def BalAmt(self, value):
		self._BalAmt = value if value is not None else base_types.UninitialisedField(self, 'BalAmt', ActiveCurrencyAndAmount, False)

	@BalAmt.deleter
	def BalAmt(self):
		del self._BalAmt
		self._BalAmt = base_types.UninitialisedField(self, 'BalAmt', ActiveCurrencyAndAmount, False)

	@property
	def VartnAmt(self):
		return self._VartnAmt

	@VartnAmt.setter
	def VartnAmt(self, value):
		self._VartnAmt = value if value is not None else base_types.UninitialisedField(self, 'VartnAmt', ActiveCurrencyAndAmount, False)

	@VartnAmt.deleter
	def VartnAmt(self):
		del self._VartnAmt
		self._VartnAmt = base_types.UninitialisedField(self, 'VartnAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))