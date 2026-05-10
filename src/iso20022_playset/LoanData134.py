import base_types
import ContractTerm6Choice
import ISODate
import ExternalAgreementType1Code
import SpecialCollateral1Code
import ActiveOrHistoricCurrencyCode
import Security49
import ExposureType10Code
import TrueFalseIndicator
import Rates1Choice
import Max52Text
import TradingVenueType1Choice

class LoanData134(base_types._BaseFieldType):

	__slots__ = ["_OutsdngMrgnLnCcy", "_Term", "_PrtflCd", "_CtrctTp", "_PrncplAmtCcy", "_PricCcy", "_Rates", "_TradgVn", "_GnlColl", "_Scty", "_MtrtyDt", "_Clrd", "_MstrAgrmtTp"]
	@property
	def OutsdngMrgnLnCcy(self):
		return self._OutsdngMrgnLnCcy

	@OutsdngMrgnLnCcy.setter
	def OutsdngMrgnLnCcy(self, value):
		self._OutsdngMrgnLnCcy = value if type(value) != auto else self.make_default("OutsdngMrgnLnCcy")

	@OutsdngMrgnLnCcy.deleter
	def OutsdngMrgnLnCcy(self):
		del self._OutsdngMrgnLnCcy
		self._OutsdngMrgnLnCcy = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	@property
	def PrtflCd(self):
		return self._PrtflCd

	@PrtflCd.setter
	def PrtflCd(self, value):
		self._PrtflCd = value if type(value) != auto else self.make_default("PrtflCd")

	@PrtflCd.deleter
	def PrtflCd(self):
		del self._PrtflCd
		self._PrtflCd = None

	@property
	def CtrctTp(self):
		return self._CtrctTp

	@CtrctTp.setter
	def CtrctTp(self, value):
		self._CtrctTp = value if type(value) != auto else self.make_default("CtrctTp")

	@CtrctTp.deleter
	def CtrctTp(self):
		del self._CtrctTp
		self._CtrctTp = None

	@property
	def PrncplAmtCcy(self):
		return self._PrncplAmtCcy

	@PrncplAmtCcy.setter
	def PrncplAmtCcy(self, value):
		self._PrncplAmtCcy = value if type(value) != auto else self.make_default("PrncplAmtCcy")

	@PrncplAmtCcy.deleter
	def PrncplAmtCcy(self):
		del self._PrncplAmtCcy
		self._PrncplAmtCcy = None

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if type(value) != auto else self.make_default("PricCcy")

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = None

	@property
	def Rates(self):
		return self._Rates

	@Rates.setter
	def Rates(self, value):
		self._Rates = value if type(value) != auto else self.make_default("Rates")

	@Rates.deleter
	def Rates(self):
		del self._Rates
		self._Rates = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if type(value) != auto else self.make_default("Clrd")

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = None

	@property
	def MstrAgrmtTp(self):
		return self._MstrAgrmtTp

	@MstrAgrmtTp.setter
	def MstrAgrmtTp(self, value):
		self._MstrAgrmtTp = value if type(value) != auto else self.make_default("MstrAgrmtTp")

	@MstrAgrmtTp.deleter
	def MstrAgrmtTp(self):
		del self._MstrAgrmtTp
		self._MstrAgrmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutsdngMrgnLnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=ContractTerm6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCd', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctTp', type=ExposureType10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rates', type=Rates1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=TradingVenueType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=SpecialCollateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=Security49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmtTp', type=ExternalAgreementType1Code, min=0, max=1, mutex_group=None, array=False),
	))

