# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DebtIssuerType1Code
from . import Max350Text
from . import ProductType6Code

class ReportingAssetBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DebtIssrTp", "_Id", "_RptgAsstTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max350Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max350Text, False)

	@property
	def RptgAsstTp(self):
		return self._RptgAsstTp

	@RptgAsstTp.setter
	def RptgAsstTp(self, value):
		self._RptgAsstTp = value if value is not None else base_types.UninitialisedField(self, 'RptgAsstTp', ProductType6Code, False)

	@RptgAsstTp.deleter
	def RptgAsstTp(self):
		del self._RptgAsstTp
		self._RptgAsstTp = base_types.UninitialisedField(self, 'RptgAsstTp', ProductType6Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DebtIssrTp', type=DebtIssuerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAsstTp', type=ProductType6Code, min=1, max=1, mutex_group=None, array=False),
	))