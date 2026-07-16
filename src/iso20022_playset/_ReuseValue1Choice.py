# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class ReuseValue1Choice(base_types._BaseFieldType):

	__slots__ = ["_Actl", "_Estmtd"]
	@property
	def Actl(self):
		return self._Actl

	@Actl.setter
	def Actl(self, value):
		self._Actl = value if value is not None else base_types.UninitialisedField(self, 'Actl', ActiveOrHistoricCurrencyAndAmount, False)

	@Actl.deleter
	def Actl(self):
		del self._Actl
		self._Actl = base_types.UninitialisedField(self, 'Actl', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Estmtd(self):
		return self._Estmtd

	@Estmtd.setter
	def Estmtd(self, value):
		self._Estmtd = value if value is not None else base_types.UninitialisedField(self, 'Estmtd', ActiveOrHistoricCurrencyAndAmount, False)

	@Estmtd.deleter
	def Estmtd(self):
		del self._Estmtd
		self._Estmtd = base_types.UninitialisedField(self, 'Estmtd', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Estmtd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))