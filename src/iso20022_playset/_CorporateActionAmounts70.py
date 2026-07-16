# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINImpliedCurrencyAndAmount

class CorporateActionAmounts70(base_types._BaseFieldType):

	__slots__ = ["_NonRfnddAmt", "_RfnddAmt"]
	@property
	def NonRfnddAmt(self):
		return self._NonRfnddAmt

	@NonRfnddAmt.setter
	def NonRfnddAmt(self, value):
		self._NonRfnddAmt = value if value is not None else base_types.UninitialisedField(self, 'NonRfnddAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@NonRfnddAmt.deleter
	def NonRfnddAmt(self):
		del self._NonRfnddAmt
		self._NonRfnddAmt = base_types.UninitialisedField(self, 'NonRfnddAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@property
	def RfnddAmt(self):
		return self._RfnddAmt

	@RfnddAmt.setter
	def RfnddAmt(self, value):
		self._RfnddAmt = value if value is not None else base_types.UninitialisedField(self, 'RfnddAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	@RfnddAmt.deleter
	def RfnddAmt(self):
		del self._RfnddAmt
		self._RfnddAmt = base_types.UninitialisedField(self, 'RfnddAmt', RestrictedFINImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonRfnddAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfnddAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))