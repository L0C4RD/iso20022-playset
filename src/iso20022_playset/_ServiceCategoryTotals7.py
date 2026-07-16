# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndForeignExchange1
from . import BillingTaxRecord2
from . import PartyIdentification136
from . import ServiceCategory1Choice
from . import ServiceItemTotals10
from . import ServiceItemTotals11

class ServiceCategoryTotals7(base_types._BaseFieldType):

	__slots__ = ["_BlldCstmrId", "_SvcCtgy", "_SvcItmCrrctn", "_SvcItmTtls", "_Tax", "_TtlInvcAmt"]
	@property
	def BlldCstmrId(self):
		return self._BlldCstmrId

	@BlldCstmrId.setter
	def BlldCstmrId(self, value):
		self._BlldCstmrId = value if value is not None else base_types.UninitialisedField(self, 'BlldCstmrId', PartyIdentification136, False)

	@BlldCstmrId.deleter
	def BlldCstmrId(self):
		del self._BlldCstmrId
		self._BlldCstmrId = base_types.UninitialisedField(self, 'BlldCstmrId', PartyIdentification136, False)

	@property
	def SvcCtgy(self):
		return self._SvcCtgy

	@SvcCtgy.setter
	def SvcCtgy(self, value):
		self._SvcCtgy = value if value is not None else base_types.UninitialisedField(self, 'SvcCtgy', ServiceCategory1Choice, False)

	@SvcCtgy.deleter
	def SvcCtgy(self):
		del self._SvcCtgy
		self._SvcCtgy = base_types.UninitialisedField(self, 'SvcCtgy', ServiceCategory1Choice, False)

	@property
	def SvcItmCrrctn(self):
		return self._SvcItmCrrctn

	@SvcItmCrrctn.setter
	def SvcItmCrrctn(self, value):
		self._SvcItmCrrctn = value if value is not None else base_types.UninitialisedField(self, 'SvcItmCrrctn', ServiceItemTotals11, True)

	@SvcItmCrrctn.deleter
	def SvcItmCrrctn(self):
		del self._SvcItmCrrctn
		self._SvcItmCrrctn = base_types.UninitialisedField(self, 'SvcItmCrrctn', ServiceItemTotals11, True)

	@property
	def SvcItmTtls(self):
		return self._SvcItmTtls

	@SvcItmTtls.setter
	def SvcItmTtls(self, value):
		self._SvcItmTtls = value if value is not None else base_types.UninitialisedField(self, 'SvcItmTtls', ServiceItemTotals10, True)

	@SvcItmTtls.deleter
	def SvcItmTtls(self):
		del self._SvcItmTtls
		self._SvcItmTtls = base_types.UninitialisedField(self, 'SvcItmTtls', ServiceItemTotals10, True)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', BillingTaxRecord2, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', BillingTaxRecord2, True)

	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlInvcAmt', AmountAndForeignExchange1, False)

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = base_types.UninitialisedField(self, 'TtlInvcAmt', AmountAndForeignExchange1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlldCstmrId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCtgy', type=ServiceCategory1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcItmCrrctn', type=ServiceItemTotals11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcItmTtls', type=ServiceItemTotals10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tax', type=BillingTaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInvcAmt', type=AmountAndForeignExchange1, min=1, max=1, mutex_group=None, array=False),
	))