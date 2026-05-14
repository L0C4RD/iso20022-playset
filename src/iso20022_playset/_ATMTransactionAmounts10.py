# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMMediaType4Code import ATMMediaType4Code
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._Number import Number
from ._TrueFalseIndicator import TrueFalseIndicator

class ATMTransactionAmounts10(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_DispFlg", "_MaxNb", "_MdiaTp", "_MinNb"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def DispFlg(self):
		return self._DispFlg

	@DispFlg.setter
	def DispFlg(self, value):
		self._DispFlg = value if type(value) != base_types.auto else self.make_default("DispFlg")

	@DispFlg.deleter
	def DispFlg(self):
		del self._DispFlg
		self._DispFlg = None

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if type(value) != base_types.auto else self.make_default("MaxNb")

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = None

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if type(value) != base_types.auto else self.make_default("MdiaTp")

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = None

	@property
	def MinNb(self):
		return self._MinNb

	@MinNb.setter
	def MinNb(self, value):
		self._MinNb = value if type(value) != base_types.auto else self.make_default("MinNb")

	@MinNb.deleter
	def MinNb(self):
		del self._MinNb
		self._MinNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNb', type=Number, min=0, max=1, mutex_group=None, array=False),
	))