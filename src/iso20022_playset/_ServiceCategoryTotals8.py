from . import base_types
from ._AccountIdentification38Choice import AccountIdentification38Choice
from ._AmountAndForeignExchange1 import AmountAndForeignExchange1
from ._BillingTaxRecord2 import BillingTaxRecord2
from ._PartyIdentification136 import PartyIdentification136
from ._ServiceCategory1Choice import ServiceCategory1Choice
from ._ServiceItemTotals12 import ServiceItemTotals12
from ._ServiceItemTotals13 import ServiceItemTotals13

class ServiceCategoryTotals8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BlldCstmrId", "_PrntAcctId", "_SvcCtgy", "_SvcItmCrrctn", "_SvcItmTtls", "_Tax", "_TtlInvcAmt"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def BlldCstmrId(self):
		return self._BlldCstmrId

	@BlldCstmrId.setter
	def BlldCstmrId(self, value):
		self._BlldCstmrId = value if type(value) != base_types.auto else self.make_default("BlldCstmrId")

	@BlldCstmrId.deleter
	def BlldCstmrId(self):
		del self._BlldCstmrId
		self._BlldCstmrId = None

	@property
	def PrntAcctId(self):
		return self._PrntAcctId

	@PrntAcctId.setter
	def PrntAcctId(self, value):
		self._PrntAcctId = value if type(value) != base_types.auto else self.make_default("PrntAcctId")

	@PrntAcctId.deleter
	def PrntAcctId(self):
		del self._PrntAcctId
		self._PrntAcctId = None

	@property
	def SvcCtgy(self):
		return self._SvcCtgy

	@SvcCtgy.setter
	def SvcCtgy(self, value):
		self._SvcCtgy = value if type(value) != base_types.auto else self.make_default("SvcCtgy")

	@SvcCtgy.deleter
	def SvcCtgy(self):
		del self._SvcCtgy
		self._SvcCtgy = None

	@property
	def SvcItmCrrctn(self):
		return self._SvcItmCrrctn

	@SvcItmCrrctn.setter
	def SvcItmCrrctn(self, value):
		self._SvcItmCrrctn = value if type(value) != base_types.auto else self.make_default("SvcItmCrrctn")

	@SvcItmCrrctn.deleter
	def SvcItmCrrctn(self):
		del self._SvcItmCrrctn
		self._SvcItmCrrctn = None

	@property
	def SvcItmTtls(self):
		return self._SvcItmTtls

	@SvcItmTtls.setter
	def SvcItmTtls(self, value):
		self._SvcItmTtls = value if type(value) != base_types.auto else self.make_default("SvcItmTtls")

	@SvcItmTtls.deleter
	def SvcItmTtls(self):
		del self._SvcItmTtls
		self._SvcItmTtls = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if type(value) != base_types.auto else self.make_default("TtlInvcAmt")

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlldCstmrId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrntAcctId', type=AccountIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgy', type=ServiceCategory1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcItmCrrctn', type=ServiceItemTotals13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcItmTtls', type=ServiceItemTotals12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tax', type=BillingTaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInvcAmt', type=AmountAndForeignExchange1, min=1, max=1, mutex_group=None, array=False),
	))

