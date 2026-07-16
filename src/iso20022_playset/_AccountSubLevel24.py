# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSubLevel25
from . import FinancialInstrumentQuantity18Choice

class AccountSubLevel24(base_types._BaseFieldType):

	__slots__ = ["_BlwThrshldShrhldgQty", "_Dsclsr", "_NonDscldShrhldgQty"]
	@property
	def BlwThrshldShrhldgQty(self):
		return self._BlwThrshldShrhldgQty

	@BlwThrshldShrhldgQty.setter
	def BlwThrshldShrhldgQty(self, value):
		self._BlwThrshldShrhldgQty = value if value is not None else base_types.UninitialisedField(self, 'BlwThrshldShrhldgQty', FinancialInstrumentQuantity18Choice, False)

	@BlwThrshldShrhldgQty.deleter
	def BlwThrshldShrhldgQty(self):
		del self._BlwThrshldShrhldgQty
		self._BlwThrshldShrhldgQty = base_types.UninitialisedField(self, 'BlwThrshldShrhldgQty', FinancialInstrumentQuantity18Choice, False)

	@property
	def Dsclsr(self):
		return self._Dsclsr

	@Dsclsr.setter
	def Dsclsr(self, value):
		self._Dsclsr = value if value is not None else base_types.UninitialisedField(self, 'Dsclsr', AccountSubLevel25, True)

	@Dsclsr.deleter
	def Dsclsr(self):
		del self._Dsclsr
		self._Dsclsr = base_types.UninitialisedField(self, 'Dsclsr', AccountSubLevel25, True)

	@property
	def NonDscldShrhldgQty(self):
		return self._NonDscldShrhldgQty

	@NonDscldShrhldgQty.setter
	def NonDscldShrhldgQty(self, value):
		self._NonDscldShrhldgQty = value if value is not None else base_types.UninitialisedField(self, 'NonDscldShrhldgQty', FinancialInstrumentQuantity18Choice, False)

	@NonDscldShrhldgQty.deleter
	def NonDscldShrhldgQty(self):
		del self._NonDscldShrhldgQty
		self._NonDscldShrhldgQty = base_types.UninitialisedField(self, 'NonDscldShrhldgQty', FinancialInstrumentQuantity18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlwThrshldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclsr', type=AccountSubLevel25, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonDscldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
	))