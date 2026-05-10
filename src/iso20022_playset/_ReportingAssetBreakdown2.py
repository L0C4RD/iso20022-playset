from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._DebtIssuerType1Code import DebtIssuerType1Code
from ._Max350Text import Max350Text
from ._ProductType6Code import ProductType6Code

class ReportingAssetBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DebtIssrTp", "_Id", "_RptgAsstTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def DebtIssrTp(self):
		return self._DebtIssrTp

	@DebtIssrTp.setter
	def DebtIssrTp(self, value):
		self._DebtIssrTp = value if type(value) != base_types.auto else self.make_default("DebtIssrTp")

	@DebtIssrTp.deleter
	def DebtIssrTp(self):
		del self._DebtIssrTp
		self._DebtIssrTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RptgAsstTp(self):
		return self._RptgAsstTp

	@RptgAsstTp.setter
	def RptgAsstTp(self, value):
		self._RptgAsstTp = value if type(value) != base_types.auto else self.make_default("RptgAsstTp")

	@RptgAsstTp.deleter
	def RptgAsstTp(self):
		del self._RptgAsstTp
		self._RptgAsstTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DebtIssrTp', type=DebtIssuerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAsstTp', type=ProductType6Code, min=1, max=1, mutex_group=None, array=False),
	))

