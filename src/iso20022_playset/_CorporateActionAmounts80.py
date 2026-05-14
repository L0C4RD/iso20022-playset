# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RestrictedFINImpliedCurrencyAndAmount import RestrictedFINImpliedCurrencyAndAmount

class CorporateActionAmounts80(base_types._BaseFieldType):

	__slots__ = ["_DpstryClldAmt", "_NonRfnddAmt", "_RfnddAmt"]
	@property
	def DpstryClldAmt(self):
		return self._DpstryClldAmt

	@DpstryClldAmt.setter
	def DpstryClldAmt(self, value):
		self._DpstryClldAmt = value if type(value) != base_types.auto else self.make_default("DpstryClldAmt")

	@DpstryClldAmt.deleter
	def DpstryClldAmt(self):
		del self._DpstryClldAmt
		self._DpstryClldAmt = None

	@property
	def NonRfnddAmt(self):
		return self._NonRfnddAmt

	@NonRfnddAmt.setter
	def NonRfnddAmt(self, value):
		self._NonRfnddAmt = value if type(value) != base_types.auto else self.make_default("NonRfnddAmt")

	@NonRfnddAmt.deleter
	def NonRfnddAmt(self):
		del self._NonRfnddAmt
		self._NonRfnddAmt = None

	@property
	def RfnddAmt(self):
		return self._RfnddAmt

	@RfnddAmt.setter
	def RfnddAmt(self, value):
		self._RfnddAmt = value if type(value) != base_types.auto else self.make_default("RfnddAmt")

	@RfnddAmt.deleter
	def RfnddAmt(self):
		del self._RfnddAmt
		self._RfnddAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DpstryClldAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonRfnddAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfnddAmt', type=RestrictedFINImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))