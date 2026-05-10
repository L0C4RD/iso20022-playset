from . import base_types
from .AmountAndDirection34 import AmountAndDirection34
from .DecimalNumber import DecimalNumber
from .BillingServiceIdentification2 import BillingServiceIdentification2

class BillingServiceParameters2(base_types._BaseFieldType):

	__slots__ = ["_BkSvc", "_Vol", "_SvcChrgAmt", "_UnitPric"]
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

	@property
	def SvcChrgAmt(self):
		return self._SvcChrgAmt

	@SvcChrgAmt.setter
	def SvcChrgAmt(self, value):
		self._SvcChrgAmt = value if type(value) != auto else self.make_default("SvcChrgAmt")

	@SvcChrgAmt.deleter
	def SvcChrgAmt(self):
		del self._SvcChrgAmt
		self._SvcChrgAmt = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkSvc', type=BillingServiceIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcChrgAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))

