# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import ReinvestmentType1Code

class ReinvestedCashTypeAndAmount2(base_types._BaseFieldType):

	__slots__ = ["_RinvstdCshCcy", "_Tp"]
	@property
	def RinvstdCshCcy(self):
		return self._RinvstdCshCcy

	@RinvstdCshCcy.setter
	def RinvstdCshCcy(self, value):
		self._RinvstdCshCcy = value if value is not None else base_types.UninitialisedField(self, 'RinvstdCshCcy', ActiveOrHistoricCurrencyCode, False)

	@RinvstdCshCcy.deleter
	def RinvstdCshCcy(self):
		del self._RinvstdCshCcy
		self._RinvstdCshCcy = base_types.UninitialisedField(self, 'RinvstdCshCcy', ActiveOrHistoricCurrencyCode, False)

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
		base_types.FieldEntry(name='RinvstdCshCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReinvestmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))