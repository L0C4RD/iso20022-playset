# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import DebtIssuerType1Code
from . import ISINOct2015Identifier
from . import ProductType6Code

class SecurityIdentificationAndAmount2(base_types._BaseFieldType):

	__slots__ = ["_DebtIssrTp", "_FinInstrmTp", "_Id", "_MktVal"]
	@property
	def DebtIssrTp(self):
		return self._DebtIssrTp

	@DebtIssrTp.setter
	def DebtIssrTp(self, value):
		self._DebtIssrTp = value if value is not None else base_types.UninitialisedField(self, 'DebtIssrTp', DebtIssuerType1Code, False)

	@DebtIssrTp.deleter
	def DebtIssrTp(self):
		del self._DebtIssrTp
		self._DebtIssrTp = base_types.UninitialisedField(self, 'DebtIssrTp', DebtIssuerType1Code, False)

	@property
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmTp', ProductType6Code, False)

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = base_types.UninitialisedField(self, 'FinInstrmTp', ProductType6Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAnd24Amount, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAnd24Amount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtIssrTp', type=DebtIssuerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmTp', type=ProductType6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))