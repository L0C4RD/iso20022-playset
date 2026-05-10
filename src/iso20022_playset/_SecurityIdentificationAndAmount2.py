from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._ProductType6Code import ProductType6Code
from ._DebtIssuerType1Code import DebtIssuerType1Code

class SecurityIdentificationAndAmount2(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmTp", "_Id", "_DebtIssrTp", "_MktVal"]
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
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if type(value) != base_types.auto else self.make_default("FinInstrmTp")

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = None

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
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtIssrTp', type=DebtIssuerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmTp', type=ProductType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))

