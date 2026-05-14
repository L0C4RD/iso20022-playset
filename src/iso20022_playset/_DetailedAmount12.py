# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._DetailedAmount13 import DetailedAmount13
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class DetailedAmount12(base_types._BaseFieldType):

	__slots__ = ["_AmtToDspns", "_Ccy", "_Dontn", "_Fees"]
	@property
	def AmtToDspns(self):
		return self._AmtToDspns

	@AmtToDspns.setter
	def AmtToDspns(self, value):
		self._AmtToDspns = value if type(value) != base_types.auto else self.make_default("AmtToDspns")

	@AmtToDspns.deleter
	def AmtToDspns(self):
		del self._AmtToDspns
		self._AmtToDspns = None

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
	def Dontn(self):
		return self._Dontn

	@Dontn.setter
	def Dontn(self, value):
		self._Dontn = value if type(value) != base_types.auto else self.make_default("Dontn")

	@Dontn.deleter
	def Dontn(self):
		del self._Dontn
		self._Dontn = None

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != base_types.auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToDspns', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dontn', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fees', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
	))