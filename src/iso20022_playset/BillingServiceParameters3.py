import base_types
import DecimalNumber
import BillingServiceIdentification3

class BillingServiceParameters3(base_types._BaseFieldType):

	__slots__ = ["_BkSvc", "_Vol"]
	@property
	def BkSvc(self):
		return self._BkSvc

	@BkSvc.setter
	def BkSvc(self, value):
		self._BkSvc = value if type(value) != auto else self.make_default("BkSvc")

	@BkSvc.deleter
	def BkSvc(self):
		del self._BkSvc
		self._BkSvc = None

	@property
	def Vol(self):
		return self._Vol

	@Vol.setter
	def Vol(self, value):
		self._Vol = value if type(value) != auto else self.make_default("Vol")

	@Vol.deleter
	def Vol(self):
		del self._Vol
		self._Vol = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkSvc', type=BillingServiceIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

