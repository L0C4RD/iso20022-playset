import base_types
import ServicePaymentMethod1Code
import ServiceTaxDesignation1
import AmountAndDirection34
import BillingServiceParameters3
import BillingMethod1Choice
import BillingPrice1

class BillingService2(base_types._BaseFieldType):

	__slots__ = ["_SvcDtl", "_Pric", "_TaxClctn", "_OrgnlChrgSttlmAmt", "_OrgnlChrgPric", "_PmtMtd", "_TaxDsgnt", "_BalReqrdAcctAmt"]
	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if type(value) != auto else self.make_default("SvcDtl")

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def TaxClctn(self):
		return self._TaxClctn

	@TaxClctn.setter
	def TaxClctn(self, value):
		self._TaxClctn = value if type(value) != auto else self.make_default("TaxClctn")

	@TaxClctn.deleter
	def TaxClctn(self):
		del self._TaxClctn
		self._TaxClctn = None

	@property
	def OrgnlChrgSttlmAmt(self):
		return self._OrgnlChrgSttlmAmt

	@OrgnlChrgSttlmAmt.setter
	def OrgnlChrgSttlmAmt(self, value):
		self._OrgnlChrgSttlmAmt = value if type(value) != auto else self.make_default("OrgnlChrgSttlmAmt")

	@OrgnlChrgSttlmAmt.deleter
	def OrgnlChrgSttlmAmt(self):
		del self._OrgnlChrgSttlmAmt
		self._OrgnlChrgSttlmAmt = None

	@property
	def OrgnlChrgPric(self):
		return self._OrgnlChrgPric

	@OrgnlChrgPric.setter
	def OrgnlChrgPric(self, value):
		self._OrgnlChrgPric = value if type(value) != auto else self.make_default("OrgnlChrgPric")

	@OrgnlChrgPric.deleter
	def OrgnlChrgPric(self):
		del self._OrgnlChrgPric
		self._OrgnlChrgPric = None

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	@property
	def TaxDsgnt(self):
		return self._TaxDsgnt

	@TaxDsgnt.setter
	def TaxDsgnt(self, value):
		self._TaxDsgnt = value if type(value) != auto else self.make_default("TaxDsgnt")

	@TaxDsgnt.deleter
	def TaxDsgnt(self):
		del self._TaxDsgnt
		self._TaxDsgnt = None

	@property
	def BalReqrdAcctAmt(self):
		return self._BalReqrdAcctAmt

	@BalReqrdAcctAmt.setter
	def BalReqrdAcctAmt(self, value):
		self._BalReqrdAcctAmt = value if type(value) != auto else self.make_default("BalReqrdAcctAmt")

	@BalReqrdAcctAmt.deleter
	def BalReqrdAcctAmt(self):
		del self._BalReqrdAcctAmt
		self._BalReqrdAcctAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcDtl', type=BillingServiceParameters3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=BillingPrice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctn', type=BillingMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgSttlmAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgPric', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=ServicePaymentMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDsgnt', type=ServiceTaxDesignation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalReqrdAcctAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))

