# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34

class BillingServicesAmount3(base_types._BaseFieldType):

	__slots__ = ["_HstAmt", "_SrcAmt"]
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
	def SrcAmt(self):
		return self._SrcAmt

	@SrcAmt.setter
	def SrcAmt(self, value):
		self._SrcAmt = value if value is not None else base_types.UninitialisedField(self, 'SrcAmt', AmountAndDirection34, False)

	@SrcAmt.deleter
	def SrcAmt(self):
		del self._SrcAmt
		self._SrcAmt = base_types.UninitialisedField(self, 'SrcAmt', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))