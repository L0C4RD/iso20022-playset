# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSubLevel25 import AccountSubLevel25
from ._FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice

class AccountSubLevel24(base_types._BaseFieldType):

	__slots__ = ["_BlwThrshldShrhldgQty", "_Dsclsr", "_NonDscldShrhldgQty"]
	@property
	def BlwThrshldShrhldgQty(self):
		return self._BlwThrshldShrhldgQty

	@BlwThrshldShrhldgQty.setter
	def BlwThrshldShrhldgQty(self, value):
		self._BlwThrshldShrhldgQty = value if type(value) != base_types.auto else self.make_default("BlwThrshldShrhldgQty")

	@BlwThrshldShrhldgQty.deleter
	def BlwThrshldShrhldgQty(self):
		del self._BlwThrshldShrhldgQty
		self._BlwThrshldShrhldgQty = None

	@property
	def Dsclsr(self):
		return self._Dsclsr

	@Dsclsr.setter
	def Dsclsr(self, value):
		self._Dsclsr = value if type(value) != base_types.auto else self.make_default("Dsclsr")

	@Dsclsr.deleter
	def Dsclsr(self):
		del self._Dsclsr
		self._Dsclsr = None

	@property
	def NonDscldShrhldgQty(self):
		return self._NonDscldShrhldgQty

	@NonDscldShrhldgQty.setter
	def NonDscldShrhldgQty(self, value):
		self._NonDscldShrhldgQty = value if type(value) != base_types.auto else self.make_default("NonDscldShrhldgQty")

	@NonDscldShrhldgQty.deleter
	def NonDscldShrhldgQty(self):
		del self._NonDscldShrhldgQty
		self._NonDscldShrhldgQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlwThrshldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclsr', type=AccountSubLevel25, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonDscldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
	))