# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount204
from . import CountryCode
from . import Max350Text
from . import PartyIdentification125Choice
from . import PercentageRate

class TaxReporting3(base_types._BaseFieldType):

	__slots__ = ["_CshAcctDtls", "_Desc", "_TaxPyer", "_TaxRate", "_TaxRcpt", "_TaxtnCtry"]
	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'CshAcctDtls', CashAccount204, False)

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = base_types.UninitialisedField(self, 'CshAcctDtls', CashAccount204, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def TaxPyer(self):
		return self._TaxPyer

	@TaxPyer.setter
	def TaxPyer(self, value):
		self._TaxPyer = value if value is not None else base_types.UninitialisedField(self, 'TaxPyer', PartyIdentification125Choice, False)

	@TaxPyer.deleter
	def TaxPyer(self):
		del self._TaxPyer
		self._TaxPyer = base_types.UninitialisedField(self, 'TaxPyer', PartyIdentification125Choice, False)

	@property
	def TaxRate(self):
		return self._TaxRate

	@TaxRate.setter
	def TaxRate(self, value):
		self._TaxRate = value if value is not None else base_types.UninitialisedField(self, 'TaxRate', PercentageRate, False)

	@TaxRate.deleter
	def TaxRate(self):
		del self._TaxRate
		self._TaxRate = base_types.UninitialisedField(self, 'TaxRate', PercentageRate, False)

	@property
	def TaxRcpt(self):
		return self._TaxRcpt

	@TaxRcpt.setter
	def TaxRcpt(self, value):
		self._TaxRcpt = value if value is not None else base_types.UninitialisedField(self, 'TaxRcpt', PartyIdentification125Choice, False)

	@TaxRcpt.deleter
	def TaxRcpt(self):
		del self._TaxRcpt
		self._TaxRcpt = base_types.UninitialisedField(self, 'TaxRcpt', PartyIdentification125Choice, False)

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if value is not None else base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctDtls', type=CashAccount204, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxPyer', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRcpt', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))