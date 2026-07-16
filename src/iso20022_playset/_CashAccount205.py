# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import CashAccount206

class CashAccount205(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_PmryAcct", "_ScndryAcct"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def PmryAcct(self):
		return self._PmryAcct

	@PmryAcct.setter
	def PmryAcct(self, value):
		self._PmryAcct = value if value is not None else base_types.UninitialisedField(self, 'PmryAcct', CashAccount206, False)

	@PmryAcct.deleter
	def PmryAcct(self):
		del self._PmryAcct
		self._PmryAcct = base_types.UninitialisedField(self, 'PmryAcct', CashAccount206, False)

	@property
	def ScndryAcct(self):
		return self._ScndryAcct

	@ScndryAcct.setter
	def ScndryAcct(self, value):
		self._ScndryAcct = value if value is not None else base_types.UninitialisedField(self, 'ScndryAcct', CashAccount206, False)

	@ScndryAcct.deleter
	def ScndryAcct(self):
		del self._ScndryAcct
		self._ScndryAcct = base_types.UninitialisedField(self, 'ScndryAcct', CashAccount206, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryAcct', type=CashAccount206, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryAcct', type=CashAccount206, min=0, max=1, mutex_group=None, array=False),
	))