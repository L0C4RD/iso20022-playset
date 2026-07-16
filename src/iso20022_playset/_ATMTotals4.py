# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaType4Code
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Number

class ATMTotals4(base_types._BaseFieldType):

	__slots__ = ["_ATMBal", "_ATMBalNb", "_ATMCur", "_ATMCurNb", "_Ccy", "_MdiaTp"]
	@property
	def ATMBal(self):
		return self._ATMBal

	@ATMBal.setter
	def ATMBal(self, value):
		self._ATMBal = value if value is not None else base_types.UninitialisedField(self, 'ATMBal', ImpliedCurrencyAndAmount, False)

	@ATMBal.deleter
	def ATMBal(self):
		del self._ATMBal
		self._ATMBal = base_types.UninitialisedField(self, 'ATMBal', ImpliedCurrencyAndAmount, False)

	@property
	def ATMBalNb(self):
		return self._ATMBalNb

	@ATMBalNb.setter
	def ATMBalNb(self, value):
		self._ATMBalNb = value if value is not None else base_types.UninitialisedField(self, 'ATMBalNb', Number, False)

	@ATMBalNb.deleter
	def ATMBalNb(self):
		del self._ATMBalNb
		self._ATMBalNb = base_types.UninitialisedField(self, 'ATMBalNb', Number, False)

	@property
	def ATMCur(self):
		return self._ATMCur

	@ATMCur.setter
	def ATMCur(self, value):
		self._ATMCur = value if value is not None else base_types.UninitialisedField(self, 'ATMCur', ImpliedCurrencyAndAmount, False)

	@ATMCur.deleter
	def ATMCur(self):
		del self._ATMCur
		self._ATMCur = base_types.UninitialisedField(self, 'ATMCur', ImpliedCurrencyAndAmount, False)

	@property
	def ATMCurNb(self):
		return self._ATMCurNb

	@ATMCurNb.setter
	def ATMCurNb(self, value):
		self._ATMCurNb = value if value is not None else base_types.UninitialisedField(self, 'ATMCurNb', Number, False)

	@ATMCurNb.deleter
	def ATMCurNb(self):
		del self._ATMCurNb
		self._ATMCurNb = base_types.UninitialisedField(self, 'ATMCurNb', Number, False)

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
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if value is not None else base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMBal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMBalNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCur', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMCurNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=0, max=1, mutex_group=None, array=False),
	))