import base_types
import Max35Text
import AmountAndDirection34
import Max40Text
import DecimalNumber

class BillingServicesTax3(base_types._BaseFieldType):

	__slots__ = ["_TtlTaxAmt", "_Nb", "_Desc", "_Rate"]
	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if type(value) != auto else self.make_default("TtlTaxAmt")

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlTaxAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

