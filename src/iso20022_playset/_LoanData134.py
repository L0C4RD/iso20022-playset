# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import ContractTerm6Choice
from . import ExposureType10Code
from . import ExternalAgreementType1Code
from . import ISODate
from . import Max52Text
from . import Rates1Choice
from . import Security49
from . import SpecialCollateral1Code
from . import TradingVenueType1Choice
from . import TrueFalseIndicator

class LoanData134(base_types._BaseFieldType):

	__slots__ = ["_Clrd", "_CtrctTp", "_GnlColl", "_MstrAgrmtTp", "_MtrtyDt", "_OutsdngMrgnLnCcy", "_PricCcy", "_PrncplAmtCcy", "_PrtflCd", "_Rates", "_Scty", "_Term", "_TradgVn"]
	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if value is not None else base_types.UninitialisedField(self, 'Clrd', TrueFalseIndicator, False)

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = base_types.UninitialisedField(self, 'Clrd', TrueFalseIndicator, False)

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctTp', ExposureType10Code, False)

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = base_types.UninitialisedField(self, 'CtrctTp', ExposureType10Code, False)

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if value is not None else base_types.UninitialisedField(self, 'GnlColl', SpecialCollateral1Code, False)

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = base_types.UninitialisedField(self, 'GnlColl', SpecialCollateral1Code, False)

	@property
	def MstrAgrmtTp(self):
		return self._MstrAgrmtTp

	@MstrAgrmtTp.setter
	def MstrAgrmtTp(self, value):
		self._MstrAgrmtTp = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmtTp', ExternalAgreementType1Code, False)

	@MstrAgrmtTp.deleter
	def MstrAgrmtTp(self):
		del self._MstrAgrmtTp
		self._MstrAgrmtTp = base_types.UninitialisedField(self, 'MstrAgrmtTp', ExternalAgreementType1Code, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def OutsdngMrgnLnCcy(self):
		return self._OutsdngMrgnLnCcy

	@OutsdngMrgnLnCcy.setter
	def OutsdngMrgnLnCcy(self, value):
		self._OutsdngMrgnLnCcy = value if value is not None else base_types.UninitialisedField(self, 'OutsdngMrgnLnCcy', ActiveOrHistoricCurrencyCode, False)

	@OutsdngMrgnLnCcy.deleter
	def OutsdngMrgnLnCcy(self):
		del self._OutsdngMrgnLnCcy
		self._OutsdngMrgnLnCcy = base_types.UninitialisedField(self, 'OutsdngMrgnLnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if value is not None else base_types.UninitialisedField(self, 'PricCcy', ActiveOrHistoricCurrencyCode, False)

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = base_types.UninitialisedField(self, 'PricCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def PrncplAmtCcy(self):
		return self._PrncplAmtCcy

	@PrncplAmtCcy.setter
	def PrncplAmtCcy(self, value):
		self._PrncplAmtCcy = value if value is not None else base_types.UninitialisedField(self, 'PrncplAmtCcy', ActiveOrHistoricCurrencyCode, False)

	@PrncplAmtCcy.deleter
	def PrncplAmtCcy(self):
		del self._PrncplAmtCcy
		self._PrncplAmtCcy = base_types.UninitialisedField(self, 'PrncplAmtCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def PrtflCd(self):
		return self._PrtflCd

	@PrtflCd.setter
	def PrtflCd(self, value):
		self._PrtflCd = value if value is not None else base_types.UninitialisedField(self, 'PrtflCd', Max52Text, False)

	@PrtflCd.deleter
	def PrtflCd(self):
		del self._PrtflCd
		self._PrtflCd = base_types.UninitialisedField(self, 'PrtflCd', Max52Text, False)

	@property
	def Rates(self):
		return self._Rates

	@Rates.setter
	def Rates(self, value):
		self._Rates = value if value is not None else base_types.UninitialisedField(self, 'Rates', Rates1Choice, False)

	@Rates.deleter
	def Rates(self):
		del self._Rates
		self._Rates = base_types.UninitialisedField(self, 'Rates', Rates1Choice, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', Security49, False)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', Security49, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', ContractTerm6Choice, False)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', ContractTerm6Choice, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', TradingVenueType1Choice, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', TradingVenueType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=ExposureType10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=SpecialCollateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtTp', type=ExternalAgreementType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngMrgnLnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCd', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rates', type=Rates1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=Security49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=ContractTerm6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=TradingVenueType1Choice, min=0, max=1, mutex_group=None, array=False),
	))