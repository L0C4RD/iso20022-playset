import base_types
import ChargesRecord8
import ActiveOrHistoricCurrencyAndAmount

class Charges15(base_types._BaseFieldType):

	__slots__ = ["_TtlChrgsAndTaxAmt", "_Rcrd"]
	@property
	def TtlChrgsAndTaxAmt(self):
		return self._TtlChrgsAndTaxAmt

	@TtlChrgsAndTaxAmt.setter
	def TtlChrgsAndTaxAmt(self, value):
		self._TtlChrgsAndTaxAmt = value if type(value) != auto else self.make_default("TtlChrgsAndTaxAmt")

	@TtlChrgsAndTaxAmt.deleter
	def TtlChrgsAndTaxAmt(self):
		del self._TtlChrgsAndTaxAmt
		self._TtlChrgsAndTaxAmt = None

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
		base_types.FieldEntry(name='TtlChrgsAndTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=ChargesRecord8, min=0, max=None, mutex_group=None, array=True),
	))

