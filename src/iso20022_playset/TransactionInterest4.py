import base_types
import ActiveOrHistoricCurrencyAndAmount
import InterestRecord2

class TransactionInterest4(base_types._BaseFieldType):

	__slots__ = ["_TtlIntrstAndTaxAmt", "_Rcrd"]
	@property
	def TtlIntrstAndTaxAmt(self):
		return self._TtlIntrstAndTaxAmt

	@TtlIntrstAndTaxAmt.setter
	def TtlIntrstAndTaxAmt(self, value):
		self._TtlIntrstAndTaxAmt = value if type(value) != auto else self.make_default("TtlIntrstAndTaxAmt")

	@TtlIntrstAndTaxAmt.deleter
	def TtlIntrstAndTaxAmt(self):
		del self._TtlIntrstAndTaxAmt
		self._TtlIntrstAndTaxAmt = None

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlIntrstAndTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=InterestRecord2, min=0, max=None, mutex_group=None, array=True),
	))

