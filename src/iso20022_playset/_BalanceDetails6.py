# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection31
from . import BalanceType7Choice
from . import FinancialAssetTypeCategory1Code
from . import Unrealised1Code

class BalanceDetails6(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ctgy", "_Tp", "_Urlsd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountAndDirection31, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountAndDirection31, False)

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', FinancialAssetTypeCategory1Code, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', FinancialAssetTypeCategory1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BalanceType7Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BalanceType7Choice, False)

	@property
	def Urlsd(self):
		return self._Urlsd

	@Urlsd.setter
	def Urlsd(self, value):
		self._Urlsd = value if value is not None else base_types.UninitialisedField(self, 'Urlsd', Unrealised1Code, False)

	@Urlsd.deleter
	def Urlsd(self):
		del self._Urlsd
		self._Urlsd = base_types.UninitialisedField(self, 'Urlsd', Unrealised1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=FinancialAssetTypeCategory1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Urlsd', type=Unrealised1Code, min=0, max=1, mutex_group=None, array=False),
	))