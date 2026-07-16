# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINImpliedCurrencyAndAmount

class CorporateActionBalanceDetails48(base_types._BaseFieldType):

	__slots__ = ["_SctyClldAmt", "_TtlAmtOutsdng"]
	@property
	def SctyClldAmt(self):
		return self._SctyClldAmt

	@SctyClldAmt.setter
	def SctyClldAmt(self, value):
		self._SctyClldAmt = value if value is not None else base_types.UninitialisedField(self, 'SctyClldAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@SctyClldAmt.deleter
	def SctyClldAmt(self):
		del self._SctyClldAmt
		self._SctyClldAmt = base_types.UninitialisedField(self, 'SctyClldAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@property
	def TtlAmtOutsdng(self):
		return self._TtlAmtOutsdng

	@TtlAmtOutsdng.setter
	def TtlAmtOutsdng(self, value):
		self._TtlAmtOutsdng = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtOutsdng', RestrictedFINImpliedCurrencyAndAmount, False)

	@TtlAmtOutsdng.deleter
	def TtlAmtOutsdng(self):
		del self._TtlAmtOutsdng
		self._TtlAmtOutsdng = base_types.UninitialisedField(self, 'TtlAmtOutsdng', RestrictedFINImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyClldAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtOutsdng', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))