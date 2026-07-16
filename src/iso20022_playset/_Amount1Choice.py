# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class Amount1Choice(base_types._BaseFieldType):

	__slots__ = ["_DcrAmt", "_IncrAmt"]
	@property
	def DcrAmt(self):
		return self._DcrAmt

	@DcrAmt.setter
	def DcrAmt(self, value):
		self._DcrAmt = value if value is not None else base_types.UninitialisedField(self, 'DcrAmt', ActiveCurrencyAndAmount, False)

	@DcrAmt.deleter
	def DcrAmt(self):
		del self._DcrAmt
		self._DcrAmt = base_types.UninitialisedField(self, 'DcrAmt', ActiveCurrencyAndAmount, False)

	@property
	def IncrAmt(self):
		return self._IncrAmt

	@IncrAmt.setter
	def IncrAmt(self, value):
		self._IncrAmt = value if value is not None else base_types.UninitialisedField(self, 'IncrAmt', ActiveCurrencyAndAmount, False)

	@IncrAmt.deleter
	def IncrAmt(self):
		del self._IncrAmt
		self._IncrAmt = base_types.UninitialisedField(self, 'IncrAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DcrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IncrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))