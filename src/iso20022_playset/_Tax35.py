# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CountryCode
from . import PartyIdentification139
from . import PercentageRate
from . import TaxCalculationInformation10
from . import TaxType3Choice

class Tax35(base_types._BaseFieldType):

	__slots__ = ["_ApldAmt", "_ApldRate", "_Ctry", "_RcptId", "_TaxClctnDtls", "_Tp"]
	@property
	def ApldAmt(self):
		return self._ApldAmt

	@ApldAmt.setter
	def ApldAmt(self, value):
		self._ApldAmt = value if value is not None else base_types.UninitialisedField(self, 'ApldAmt', ActiveCurrencyAndAmount, False)

	@ApldAmt.deleter
	def ApldAmt(self):
		del self._ApldAmt
		self._ApldAmt = base_types.UninitialisedField(self, 'ApldAmt', ActiveCurrencyAndAmount, False)

	@property
	def ApldRate(self):
		return self._ApldRate

	@ApldRate.setter
	def ApldRate(self, value):
		self._ApldRate = value if value is not None else base_types.UninitialisedField(self, 'ApldRate', PercentageRate, False)

	@ApldRate.deleter
	def ApldRate(self):
		del self._ApldRate
		self._ApldRate = base_types.UninitialisedField(self, 'ApldRate', PercentageRate, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if value is not None else base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation10, False)

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = base_types.UninitialisedField(self, 'TaxClctnDtls', TaxCalculationInformation10, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TaxType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TaxType3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType3Choice, min=1, max=1, mutex_group=None, array=False),
	))