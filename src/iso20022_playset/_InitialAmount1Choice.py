# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Number

class InitialAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_InitlNbOfInstlmts"]
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
	def InitlNbOfInstlmts(self):
		return self._InitlNbOfInstlmts

	@InitlNbOfInstlmts.setter
	def InitlNbOfInstlmts(self, value):
		self._InitlNbOfInstlmts = value if value is not None else base_types.UninitialisedField(self, 'InitlNbOfInstlmts', Number, False)

	@InitlNbOfInstlmts.deleter
	def InitlNbOfInstlmts(self):
		del self._InitlNbOfInstlmts
		self._InitlNbOfInstlmts = base_types.UninitialisedField(self, 'InitlNbOfInstlmts', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InitlNbOfInstlmts', type=Number, min=0, max=1, mutex_group=1, array=False),
	))