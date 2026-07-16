# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaType4Code
from . import ActiveCurrencyCode
from . import Number
from . import TrueFalseIndicator

class ATMTransactionAmounts10(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_DispFlg", "_MaxNb", "_MdiaTp", "_MinNb"]
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
	def DispFlg(self):
		return self._DispFlg

	@DispFlg.setter
	def DispFlg(self, value):
		self._DispFlg = value if value is not None else base_types.UninitialisedField(self, 'DispFlg', TrueFalseIndicator, False)

	@DispFlg.deleter
	def DispFlg(self):
		del self._DispFlg
		self._DispFlg = base_types.UninitialisedField(self, 'DispFlg', TrueFalseIndicator, False)

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if value is not None else base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if value is not None else base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@property
	def MinNb(self):
		return self._MinNb

	@MinNb.setter
	def MinNb(self, value):
		self._MinNb = value if value is not None else base_types.UninitialisedField(self, 'MinNb', Number, False)

	@MinNb.deleter
	def MinNb(self):
		del self._MinNb
		self._MinNb = base_types.UninitialisedField(self, 'MinNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))