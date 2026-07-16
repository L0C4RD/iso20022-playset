# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DetailedAmount18
from . import ImpliedCurrencyAndAmount

class DetailedAmount17(base_types._BaseFieldType):

	__slots__ = ["_AmtToTrf", "_Ccy", "_Dontn", "_Fees"]
	@property
	def AmtToTrf(self):
		return self._AmtToTrf

	@AmtToTrf.setter
	def AmtToTrf(self, value):
		self._AmtToTrf = value if value is not None else base_types.UninitialisedField(self, 'AmtToTrf', ImpliedCurrencyAndAmount, False)

	@AmtToTrf.deleter
	def AmtToTrf(self):
		del self._AmtToTrf
		self._AmtToTrf = base_types.UninitialisedField(self, 'AmtToTrf', ImpliedCurrencyAndAmount, False)

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
	def Dontn(self):
		return self._Dontn

	@Dontn.setter
	def Dontn(self, value):
		self._Dontn = value if value is not None else base_types.UninitialisedField(self, 'Dontn', DetailedAmount18, True)

	@Dontn.deleter
	def Dontn(self):
		del self._Dontn
		self._Dontn = base_types.UninitialisedField(self, 'Dontn', DetailedAmount18, True)

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if value is not None else base_types.UninitialisedField(self, 'Fees', DetailedAmount18, True)

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = base_types.UninitialisedField(self, 'Fees', DetailedAmount18, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToTrf', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dontn', type=DetailedAmount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fees', type=DetailedAmount18, min=0, max=None, mutex_group=None, array=True),
	))