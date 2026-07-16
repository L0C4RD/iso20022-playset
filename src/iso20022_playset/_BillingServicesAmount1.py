# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34

class BillingServicesAmount1(base_types._BaseFieldType):

	__slots__ = ["_HstAmt", "_PricgAmt"]
	@property
	def HstAmt(self):
		return self._HstAmt

	@HstAmt.setter
	def HstAmt(self, value):
		self._HstAmt = value if value is not None else base_types.UninitialisedField(self, 'HstAmt', AmountAndDirection34, False)

	@HstAmt.deleter
	def HstAmt(self):
		del self._HstAmt
		self._HstAmt = base_types.UninitialisedField(self, 'HstAmt', AmountAndDirection34, False)

	@property
	def PricgAmt(self):
		return self._PricgAmt

	@PricgAmt.setter
	def PricgAmt(self, value):
		self._PricgAmt = value if value is not None else base_types.UninitialisedField(self, 'PricgAmt', AmountAndDirection34, False)

	@PricgAmt.deleter
	def PricgAmt(self):
		del self._PricgAmt
		self._PricgAmt = base_types.UninitialisedField(self, 'PricgAmt', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))