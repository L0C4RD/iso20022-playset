# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ReinvestmentType1Code

class ReinvestedCashTypeAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_RinvstdCshAmt", "_Tp"]
	@property
	def RinvstdCshAmt(self):
		return self._RinvstdCshAmt

	@RinvstdCshAmt.setter
	def RinvstdCshAmt(self, value):
		self._RinvstdCshAmt = value if value is not None else base_types.UninitialisedField(self, 'RinvstdCshAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@RinvstdCshAmt.deleter
	def RinvstdCshAmt(self):
		del self._RinvstdCshAmt
		self._RinvstdCshAmt = base_types.UninitialisedField(self, 'RinvstdCshAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ReinvestmentType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ReinvestmentType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RinvstdCshAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReinvestmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))