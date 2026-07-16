# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BaseOneRate
from . import Exact3NumericText
from . import ImpliedCurrencyAndAmount

class CurrencyConversion5(base_types._BaseFieldType):

	__slots__ = ["_ClctdAmt", "_Rate", "_SrcCcy", "_SrcCcyNmrc", "_TrgtCcy", "_TrgtCcyNmrc"]
	@property
	def ClctdAmt(self):
		return self._ClctdAmt

	@ClctdAmt.setter
	def ClctdAmt(self, value):
		self._ClctdAmt = value if value is not None else base_types.UninitialisedField(self, 'ClctdAmt', ImpliedCurrencyAndAmount, False)

	@ClctdAmt.deleter
	def ClctdAmt(self):
		del self._ClctdAmt
		self._ClctdAmt = base_types.UninitialisedField(self, 'ClctdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', BaseOneRate, False)

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if value is not None else base_types.UninitialisedField(self, 'SrcCcy', ActiveCurrencyCode, False)

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = base_types.UninitialisedField(self, 'SrcCcy', ActiveCurrencyCode, False)

	@property
	def SrcCcyNmrc(self):
		return self._SrcCcyNmrc

	@SrcCcyNmrc.setter
	def SrcCcyNmrc(self, value):
		self._SrcCcyNmrc = value if value is not None else base_types.UninitialisedField(self, 'SrcCcyNmrc', ActiveCurrencyCode, False)

	@SrcCcyNmrc.deleter
	def SrcCcyNmrc(self):
		del self._SrcCcyNmrc
		self._SrcCcyNmrc = base_types.UninitialisedField(self, 'SrcCcyNmrc', ActiveCurrencyCode, False)

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcy', ActiveCurrencyCode, False)

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = base_types.UninitialisedField(self, 'TrgtCcy', ActiveCurrencyCode, False)

	@property
	def TrgtCcyNmrc(self):
		return self._TrgtCcyNmrc

	@TrgtCcyNmrc.setter
	def TrgtCcyNmrc(self, value):
		self._TrgtCcyNmrc = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcyNmrc', Exact3NumericText, False)

	@TrgtCcyNmrc.deleter
	def TrgtCcyNmrc(self):
		del self._TrgtCcyNmrc
		self._TrgtCcyNmrc = base_types.UninitialisedField(self, 'TrgtCcyNmrc', Exact3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctdAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcyNmrc', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcyNmrc', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
	))