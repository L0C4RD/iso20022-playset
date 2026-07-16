# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingServiceIdentification2
from . import DecimalNumber

class BillingServiceParameters2(base_types._BaseFieldType):

	__slots__ = ["_BkSvc", "_SvcChrgAmt", "_UnitPric", "_Vol"]
	@property
	def BkSvc(self):
		return self._BkSvc

	@BkSvc.setter
	def BkSvc(self, value):
		self._BkSvc = value if value is not None else base_types.UninitialisedField(self, 'BkSvc', BillingServiceIdentification2, False)

	@BkSvc.deleter
	def BkSvc(self):
		del self._BkSvc
		self._BkSvc = base_types.UninitialisedField(self, 'BkSvc', BillingServiceIdentification2, False)

	@property
	def SvcChrgAmt(self):
		return self._SvcChrgAmt

	@SvcChrgAmt.setter
	def SvcChrgAmt(self, value):
		self._SvcChrgAmt = value if value is not None else base_types.UninitialisedField(self, 'SvcChrgAmt', AmountAndDirection34, False)

	@SvcChrgAmt.deleter
	def SvcChrgAmt(self):
		del self._SvcChrgAmt
		self._SvcChrgAmt = base_types.UninitialisedField(self, 'SvcChrgAmt', AmountAndDirection34, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', AmountAndDirection34, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', AmountAndDirection34, False)

	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if value is not None else base_types.UninitialisedField(self, 'Vol', DecimalNumber, False)

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = base_types.UninitialisedField(self, 'Vol', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkSvc', type=BillingServiceIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcChrgAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))