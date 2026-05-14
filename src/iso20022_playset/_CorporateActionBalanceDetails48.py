# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RestrictedFINImpliedCurrencyAndAmount import RestrictedFINImpliedCurrencyAndAmount

class CorporateActionBalanceDetails48(base_types._BaseFieldType):

	__slots__ = ["_SctyClldAmt", "_TtlAmtOutsdng"]
	@property
	def SctyClldAmt(self):
		return self._SctyClldAmt

	@SctyClldAmt.setter
	def SctyClldAmt(self, value):
		self._SctyClldAmt = value if type(value) != base_types.auto else self.make_default("SctyClldAmt")

	@SctyClldAmt.deleter
	def SctyClldAmt(self):
		del self._SctyClldAmt
		self._SctyClldAmt = None

	@property
	def TtlAmtOutsdng(self):
		return self._TtlAmtOutsdng

	@TtlAmtOutsdng.setter
	def TtlAmtOutsdng(self, value):
		self._TtlAmtOutsdng = value if type(value) != base_types.auto else self.make_default("TtlAmtOutsdng")

	@TtlAmtOutsdng.deleter
	def TtlAmtOutsdng(self):
		del self._TtlAmtOutsdng
		self._TtlAmtOutsdng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyClldAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtOutsdng', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))