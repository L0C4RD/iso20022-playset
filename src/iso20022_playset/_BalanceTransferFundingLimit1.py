# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class BalanceTransferFundingLimit1(base_types._BaseFieldType):

	__slots__ = ["_CcyAmt"]
	@property
	def CcyAmt(self):
		return self._CcyAmt

	@CcyAmt.setter
	def CcyAmt(self, value):
		self._CcyAmt = value if value is not None else base_types.UninitialisedField(self, 'CcyAmt', ActiveCurrencyAndAmount, False)

	@CcyAmt.deleter
	def CcyAmt(self):
		del self._CcyAmt
		self._CcyAmt = base_types.UninitialisedField(self, 'CcyAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))