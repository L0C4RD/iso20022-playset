# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import ISINOct2015Identifier
from . import ImpliedCurrencyAndAmount
from . import Max35Text

class VolumeCapReport2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Id", "_TechRcrdId", "_TtlNgtdTxsTradgVol", "_TtlRefPricTradgVol", "_TtlTradgVol"]
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
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TtlNgtdTxsTradgVol(self):
		return self._TtlNgtdTxsTradgVol

	@TtlNgtdTxsTradgVol.setter
	def TtlNgtdTxsTradgVol(self, value):
		self._TtlNgtdTxsTradgVol = value if value is not None else base_types.UninitialisedField(self, 'TtlNgtdTxsTradgVol', ImpliedCurrencyAndAmount, False)

	@TtlNgtdTxsTradgVol.deleter
	def TtlNgtdTxsTradgVol(self):
		del self._TtlNgtdTxsTradgVol
		self._TtlNgtdTxsTradgVol = base_types.UninitialisedField(self, 'TtlNgtdTxsTradgVol', ImpliedCurrencyAndAmount, False)

	@property
	def TtlRefPricTradgVol(self):
		return self._TtlRefPricTradgVol

	@TtlRefPricTradgVol.setter
	def TtlRefPricTradgVol(self, value):
		self._TtlRefPricTradgVol = value if value is not None else base_types.UninitialisedField(self, 'TtlRefPricTradgVol', ImpliedCurrencyAndAmount, False)

	@TtlRefPricTradgVol.deleter
	def TtlRefPricTradgVol(self):
		del self._TtlRefPricTradgVol
		self._TtlRefPricTradgVol = base_types.UninitialisedField(self, 'TtlRefPricTradgVol', ImpliedCurrencyAndAmount, False)

	@property
	def TtlTradgVol(self):
		return self._TtlTradgVol

	@TtlTradgVol.setter
	def TtlTradgVol(self, value):
		self._TtlTradgVol = value if value is not None else base_types.UninitialisedField(self, 'TtlTradgVol', ImpliedCurrencyAndAmount, False)

	@TtlTradgVol.deleter
	def TtlTradgVol(self):
		del self._TtlTradgVol
		self._TtlTradgVol = base_types.UninitialisedField(self, 'TtlTradgVol', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNgtdTxsTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRefPricTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))