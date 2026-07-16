# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import DigitalTokenAmount2
from . import PriceStatus1Code

class SecuritiesTransactionPrice6(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_DgtlTkn", "_Pdg"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def DgtlTkn(self):
		return self._DgtlTkn

	@DgtlTkn.setter
	def DgtlTkn(self, value):
		self._DgtlTkn = value if value is not None else base_types.UninitialisedField(self, 'DgtlTkn', DigitalTokenAmount2, True)

	@DgtlTkn.deleter
	def DgtlTkn(self):
		del self._DgtlTkn
		self._DgtlTkn = base_types.UninitialisedField(self, 'DgtlTkn', DigitalTokenAmount2, True)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PriceStatus1Code, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PriceStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlTkn', type=DigitalTokenAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pdg', type=PriceStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))