# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class CashEntitlement1(base_types._BaseFieldType):

	__slots__ = ["_CshAmt"]
	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if type(value) != base_types.auto else self.make_default("CshAmt")

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))