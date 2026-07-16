# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingServiceIdentification3
from . import DecimalNumber

class BillingServiceParameters3(base_types._BaseFieldType):

	__slots__ = ["_BkSvc", "_Vol"]
	@property
	def BkSvc(self):
		return self._BkSvc

	@BkSvc.setter
	def BkSvc(self, value):
		self._BkSvc = value if value is not None else base_types.UninitialisedField(self, 'BkSvc', BillingServiceIdentification3, False)

	@BkSvc.deleter
	def BkSvc(self):
		del self._BkSvc
		self._BkSvc = base_types.UninitialisedField(self, 'BkSvc', BillingServiceIdentification3, False)

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
		base_types.FieldEntry(name='BkSvc', type=BillingServiceIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))