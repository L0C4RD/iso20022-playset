# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._GenericIdentification56 import GenericIdentification56

class BalanceQuantity8Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Qty"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification56, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=1, array=False),
	))