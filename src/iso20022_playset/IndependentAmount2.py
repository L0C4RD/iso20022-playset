from . import base_types
import IndependentAmountConventionType1Code
import Max140Text
import ActiveCurrencyAndAmount

class IndependentAmount2(base_types._BaseFieldType):

	__slots__ = ["_Cnvntn", "_Amt", "_Desc"]
	@property
	def Cnvntn(self):
		return self._Cnvntn

	@Cnvntn.setter
	def Cnvntn(self, value):
		self._Cnvntn = value if type(value) != auto else self.make_default("Cnvntn")

	@Cnvntn.deleter
	def Cnvntn(self):
		del self._Cnvntn
		self._Cnvntn = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnvntn', type=IndependentAmountConventionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

