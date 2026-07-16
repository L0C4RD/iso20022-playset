# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CashAccount7
from . import FinancingDateDetails1
from . import Number
from . import PercentageRate

class FinancingAllowedSummary1(base_types._BaseFieldType):

	__slots__ = ["_ApldPctg", "_CdtAcct", "_FincdItmNb", "_FincgAcct", "_FincgDtDtls", "_TtlAccptdItmsAmt", "_TtlFincdAmt"]
	@property
	def ApldPctg(self):
		return self._ApldPctg

	@ApldPctg.setter
	def ApldPctg(self, value):
		self._ApldPctg = value if value is not None else base_types.UninitialisedField(self, 'ApldPctg', PercentageRate, False)

	@ApldPctg.deleter
	def ApldPctg(self):
		del self._ApldPctg
		self._ApldPctg = base_types.UninitialisedField(self, 'ApldPctg', PercentageRate, False)

	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtAcct', CashAccount7, False)

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = base_types.UninitialisedField(self, 'CdtAcct', CashAccount7, False)

	@property
	def FincdItmNb(self):
		return self._FincdItmNb

	@FincdItmNb.setter
	def FincdItmNb(self, value):
		self._FincdItmNb = value if value is not None else base_types.UninitialisedField(self, 'FincdItmNb', Number, False)

	@FincdItmNb.deleter
	def FincdItmNb(self):
		del self._FincdItmNb
		self._FincdItmNb = base_types.UninitialisedField(self, 'FincdItmNb', Number, False)

	@property
	def FincgAcct(self):
		return self._FincgAcct

	@FincgAcct.setter
	def FincgAcct(self, value):
		self._FincgAcct = value if value is not None else base_types.UninitialisedField(self, 'FincgAcct', CashAccount7, False)

	@FincgAcct.deleter
	def FincgAcct(self):
		del self._FincgAcct
		self._FincgAcct = base_types.UninitialisedField(self, 'FincgAcct', CashAccount7, False)

	@property
	def FincgDtDtls(self):
		return self._FincgDtDtls

	@FincgDtDtls.setter
	def FincgDtDtls(self, value):
		self._FincgDtDtls = value if value is not None else base_types.UninitialisedField(self, 'FincgDtDtls', FinancingDateDetails1, False)

	@FincgDtDtls.deleter
	def FincgDtDtls(self):
		del self._FincgDtDtls
		self._FincgDtDtls = base_types.UninitialisedField(self, 'FincgDtDtls', FinancingDateDetails1, False)

	@property
	def TtlAccptdItmsAmt(self):
		return self._TtlAccptdItmsAmt

	@TtlAccptdItmsAmt.setter
	def TtlAccptdItmsAmt(self, value):
		self._TtlAccptdItmsAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAccptdItmsAmt', ActiveCurrencyAndAmount, False)

	@TtlAccptdItmsAmt.deleter
	def TtlAccptdItmsAmt(self):
		del self._TtlAccptdItmsAmt
		self._TtlAccptdItmsAmt = base_types.UninitialisedField(self, 'TtlAccptdItmsAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlFincdAmt(self):
		return self._TtlFincdAmt

	@TtlFincdAmt.setter
	def TtlFincdAmt(self, value):
		self._TtlFincdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlFincdAmt', ActiveCurrencyAndAmount, False)

	@TtlFincdAmt.deleter
	def TtlFincdAmt(self):
		del self._TtlFincdAmt
		self._TtlFincdAmt = base_types.UninitialisedField(self, 'TtlFincdAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincdItmNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgDtDtls', type=FinancingDateDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAccptdItmsAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFincdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))