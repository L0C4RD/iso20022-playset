from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Number import Number
from .FinancingDateDetails1 import FinancingDateDetails1
from .CashAccount7 import CashAccount7
from .PercentageRate import PercentageRate

class FinancingAllowedSummary1(base_types._BaseFieldType):

	__slots__ = ["_TtlAccptdItmsAmt", "_TtlFincdAmt", "_FincgAcct", "_ApldPctg", "_FincdItmNb", "_CdtAcct", "_FincgDtDtls"]
	@property
	def TtlAccptdItmsAmt(self):
		return self._TtlAccptdItmsAmt

	@TtlAccptdItmsAmt.setter
	def TtlAccptdItmsAmt(self, value):
		self._TtlAccptdItmsAmt = value if type(value) != base_types.auto else self.make_default("TtlAccptdItmsAmt")

	@TtlAccptdItmsAmt.deleter
	def TtlAccptdItmsAmt(self):
		del self._TtlAccptdItmsAmt
		self._TtlAccptdItmsAmt = None

	@property
	def TtlFincdAmt(self):
		return self._TtlFincdAmt

	@TtlFincdAmt.setter
	def TtlFincdAmt(self, value):
		self._TtlFincdAmt = value if type(value) != base_types.auto else self.make_default("TtlFincdAmt")

	@TtlFincdAmt.deleter
	def TtlFincdAmt(self):
		del self._TtlFincdAmt
		self._TtlFincdAmt = None

	@property
	def FincgAcct(self):
		return self._FincgAcct

	@FincgAcct.setter
	def FincgAcct(self, value):
		self._FincgAcct = value if type(value) != base_types.auto else self.make_default("FincgAcct")

	@FincgAcct.deleter
	def FincgAcct(self):
		del self._FincgAcct
		self._FincgAcct = None

	@property
	def ApldPctg(self):
		return self._ApldPctg

	@ApldPctg.setter
	def ApldPctg(self, value):
		self._ApldPctg = value if type(value) != base_types.auto else self.make_default("ApldPctg")

	@ApldPctg.deleter
	def ApldPctg(self):
		del self._ApldPctg
		self._ApldPctg = None

	@property
	def FincdItmNb(self):
		return self._FincdItmNb

	@FincdItmNb.setter
	def FincdItmNb(self, value):
		self._FincdItmNb = value if type(value) != base_types.auto else self.make_default("FincdItmNb")

	@FincdItmNb.deleter
	def FincdItmNb(self):
		del self._FincdItmNb
		self._FincdItmNb = None

	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if type(value) != base_types.auto else self.make_default("CdtAcct")

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = None

	@property
	def FincgDtDtls(self):
		return self._FincgDtDtls

	@FincgDtDtls.setter
	def FincgDtDtls(self, value):
		self._FincgDtDtls = value if type(value) != base_types.auto else self.make_default("FincgDtDtls")

	@FincgDtDtls.deleter
	def FincgDtDtls(self):
		del self._FincgDtDtls
		self._FincgDtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlAccptdItmsAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFincdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincdItmNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgDtDtls', type=FinancingDateDetails1, min=0, max=1, mutex_group=None, array=False),
	))

