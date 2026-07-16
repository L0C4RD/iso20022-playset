# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaMix2
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import TrueFalseIndicator

class ATMTransaction8(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_BalPrtFlg", "_Ccy", "_Mix", "_MixTp", "_RctFlg"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def BalPrtFlg(self):
		return self._BalPrtFlg

	@BalPrtFlg.setter
	def BalPrtFlg(self, value):
		self._BalPrtFlg = value if value is not None else base_types.UninitialisedField(self, 'BalPrtFlg', TrueFalseIndicator, False)

	@BalPrtFlg.deleter
	def BalPrtFlg(self):
		del self._BalPrtFlg
		self._BalPrtFlg = base_types.UninitialisedField(self, 'BalPrtFlg', TrueFalseIndicator, False)

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
	def Mix(self):
		return self._Mix

	@Mix.setter
	def Mix(self, value):
		self._Mix = value if value is not None else base_types.UninitialisedField(self, 'Mix', ATMMediaMix2, True)

	@Mix.deleter
	def Mix(self):
		del self._Mix
		self._Mix = base_types.UninitialisedField(self, 'Mix', ATMMediaMix2, True)

	@property
	def MixTp(self):
		return self._MixTp

	@MixTp.setter
	def MixTp(self, value):
		self._MixTp = value if value is not None else base_types.UninitialisedField(self, 'MixTp', Max35Text, False)

	@MixTp.deleter
	def MixTp(self):
		del self._MixTp
		self._MixTp = base_types.UninitialisedField(self, 'MixTp', Max35Text, False)

	@property
	def RctFlg(self):
		return self._RctFlg

	@RctFlg.setter
	def RctFlg(self, value):
		self._RctFlg = value if value is not None else base_types.UninitialisedField(self, 'RctFlg', TrueFalseIndicator, False)

	@RctFlg.deleter
	def RctFlg(self):
		del self._RctFlg
		self._RctFlg = base_types.UninitialisedField(self, 'RctFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalPrtFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mix', type=ATMMediaMix2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MixTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))