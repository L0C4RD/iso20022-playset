# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingMethod1Choice
from . import BillingPrice1
from . import BillingServiceParameters3
from . import ServicePaymentMethod1Code
from . import ServiceTaxDesignation1

class BillingService2(base_types._BaseFieldType):

	__slots__ = ["_BalReqrdAcctAmt", "_OrgnlChrgPric", "_OrgnlChrgSttlmAmt", "_PmtMtd", "_Pric", "_SvcDtl", "_TaxClctn", "_TaxDsgnt"]
	@property
	def BalReqrdAcctAmt(self):
		return self._BalReqrdAcctAmt

	@BalReqrdAcctAmt.setter
	def BalReqrdAcctAmt(self, value):
		self._BalReqrdAcctAmt = value if value is not None else base_types.UninitialisedField(self, 'BalReqrdAcctAmt', AmountAndDirection34, False)

	@BalReqrdAcctAmt.deleter
	def BalReqrdAcctAmt(self):
		del self._BalReqrdAcctAmt
		self._BalReqrdAcctAmt = base_types.UninitialisedField(self, 'BalReqrdAcctAmt', AmountAndDirection34, False)

	@property
	def OrgnlChrgPric(self):
		return self._OrgnlChrgPric

	@OrgnlChrgPric.setter
	def OrgnlChrgPric(self, value):
		self._OrgnlChrgPric = value if value is not None else base_types.UninitialisedField(self, 'OrgnlChrgPric', AmountAndDirection34, False)

	@OrgnlChrgPric.deleter
	def OrgnlChrgPric(self):
		del self._OrgnlChrgPric
		self._OrgnlChrgPric = base_types.UninitialisedField(self, 'OrgnlChrgPric', AmountAndDirection34, False)

	@property
	def OrgnlChrgSttlmAmt(self):
		return self._OrgnlChrgSttlmAmt

	@OrgnlChrgSttlmAmt.setter
	def OrgnlChrgSttlmAmt(self, value):
		self._OrgnlChrgSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlChrgSttlmAmt', AmountAndDirection34, False)

	@OrgnlChrgSttlmAmt.deleter
	def OrgnlChrgSttlmAmt(self):
		del self._OrgnlChrgSttlmAmt
		self._OrgnlChrgSttlmAmt = base_types.UninitialisedField(self, 'OrgnlChrgSttlmAmt', AmountAndDirection34, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', ServicePaymentMethod1Code, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', ServicePaymentMethod1Code, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', BillingPrice1, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', BillingPrice1, False)

	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if value is not None else base_types.UninitialisedField(self, 'SvcDtl', BillingServiceParameters3, False)

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = base_types.UninitialisedField(self, 'SvcDtl', BillingServiceParameters3, False)

	@property
	def TaxClctn(self):
		return self._TaxClctn

	@TaxClctn.setter
	def TaxClctn(self, value):
		self._TaxClctn = value if value is not None else base_types.UninitialisedField(self, 'TaxClctn', BillingMethod1Choice, False)

	@TaxClctn.deleter
	def TaxClctn(self):
		del self._TaxClctn
		self._TaxClctn = base_types.UninitialisedField(self, 'TaxClctn', BillingMethod1Choice, False)

	@property
	def TaxDsgnt(self):
		return self._TaxDsgnt

	@TaxDsgnt.setter
	def TaxDsgnt(self, value):
		self._TaxDsgnt = value if value is not None else base_types.UninitialisedField(self, 'TaxDsgnt', ServiceTaxDesignation1, False)

	@TaxDsgnt.deleter
	def TaxDsgnt(self):
		del self._TaxDsgnt
		self._TaxDsgnt = base_types.UninitialisedField(self, 'TaxDsgnt', ServiceTaxDesignation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalReqrdAcctAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgPric', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgSttlmAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=ServicePaymentMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=BillingPrice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDtl', type=BillingServiceParameters3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctn', type=BillingMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDsgnt', type=ServiceTaxDesignation1, min=1, max=1, mutex_group=None, array=False),
	))