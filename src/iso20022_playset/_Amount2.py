# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ImpliedCurrencyAndAmount

class Amount2(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCcyAmt", "_RptgAmt"]
	@property
	def OrgnlCcyAmt(self):
		return self._OrgnlCcyAmt

	@OrgnlCcyAmt.setter
	def OrgnlCcyAmt(self, value):
		self._OrgnlCcyAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCcyAmt', ActiveCurrencyAndAmount, False)

	@OrgnlCcyAmt.deleter
	def OrgnlCcyAmt(self):
		del self._OrgnlCcyAmt
		self._OrgnlCcyAmt = base_types.UninitialisedField(self, 'OrgnlCcyAmt', ActiveCurrencyAndAmount, False)

	@property
	def RptgAmt(self):
		return self._RptgAmt

	@RptgAmt.setter
	def RptgAmt(self, value):
		self._RptgAmt = value if value is not None else base_types.UninitialisedField(self, 'RptgAmt', ImpliedCurrencyAndAmount, False)

	@RptgAmt.deleter
	def RptgAmt(self):
		del self._RptgAmt
		self._RptgAmt = base_types.UninitialisedField(self, 'RptgAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCcyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))