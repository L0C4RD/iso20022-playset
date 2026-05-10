import base_types
import Max350Text
import CashAccount204
import PercentageRate
import PartyIdentification125Choice
import CountryCode

class TaxReporting3(base_types._BaseFieldType):

	__slots__ = ["_TaxtnCtry", "_CshAcctDtls", "_TaxRate", "_TaxPyer", "_Desc", "_TaxRcpt"]
	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if type(value) != auto else self.make_default("TaxtnCtry")

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = None

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	@property
	def TaxRate(self):
		return self._TaxRate

	@TaxRate.setter
	def TaxRate(self, value):
		self._TaxRate = value if type(value) != auto else self.make_default("TaxRate")

	@TaxRate.deleter
	def TaxRate(self):
		del self._TaxRate
		self._TaxRate = None

	@property
	def TaxPyer(self):
		return self._TaxPyer

	@TaxPyer.setter
	def TaxPyer(self, value):
		self._TaxPyer = value if type(value) != auto else self.make_default("TaxPyer")

	@TaxPyer.deleter
	def TaxPyer(self):
		del self._TaxPyer
		self._TaxPyer = None

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
	def TaxRcpt(self):
		return self._TaxRcpt

	@TaxRcpt.setter
	def TaxRcpt(self, value):
		self._TaxRcpt = value if type(value) != auto else self.make_default("TaxRcpt")

	@TaxRcpt.deleter
	def TaxRcpt(self):
		del self._TaxRcpt
		self._TaxRcpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=CashAccount204, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxPyer', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRcpt', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
	))

