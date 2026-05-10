from . import base_types
from .FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from .AccountSubLevel25 import AccountSubLevel25

class AccountSubLevel24(base_types._BaseFieldType):

	__slots__ = ["_NonDscldShrhldgQty", "_BlwThrshldShrhldgQty", "_Dsclsr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonDscldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlwThrshldShrhldgQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsclsr', type=AccountSubLevel25, min=0, max=None, mutex_group=None, array=True),
	))

