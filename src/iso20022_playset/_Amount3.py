# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class Amount3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAmt", "_RptgAmt"]
	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@property
	def RptgAmt(self):
		return self._RptgAmt

	@RptgAmt.setter
	def RptgAmt(self, value):
		self._RptgAmt = value if value is not None else base_types.UninitialisedField(self, 'RptgAmt', ActiveCurrencyAndAmount, False)

	@RptgAmt.deleter
	def RptgAmt(self):
		del self._RptgAmt
		self._RptgAmt = base_types.UninitialisedField(self, 'RptgAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))