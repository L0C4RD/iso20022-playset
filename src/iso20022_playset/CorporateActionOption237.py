import base_types
import CorporateActionOption40Choice
import DateAndDateTime2Choice
import CorporateActionChangeTypeFormat6Choice
import ActiveCurrencyCode
import SecuritiesQuantityOrAmount6Choice
import CorporateActionNarrative32
import OptionFeaturesFormat25Choice
import OptionNumber1Choice
import YesNoIndicator
import Max25Text
import CorporateActionPrice88
import CorporateActionRate127
import SecurityIdentification19
import FractionDispositionType28Choice

class CorporateActionOption237(base_types._BaseFieldType):

	__slots__ = ["_FrctnDspstn", "_ChngTp", "_CcyToSell", "_PricDtls", "_OptnNb", "_AddtlInf", "_SctyId", "_CcyOptn", "_ElgblForCollInd", "_SlctnDealrFeeInd", "_ShrhldrNb", "_CcyToBuy", "_SctiesQtyOrInstdAmt", "_RateAndAmtDtls", "_OptnTp", "_OptnFeatrs", "_ExctnReqdDtTm"]
	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if type(value) != auto else self.make_default("ChngTp")

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = None

	@property
	def CcyToSell(self):
		return self._CcyToSell

	@CcyToSell.setter
	def CcyToSell(self, value):
		self._CcyToSell = value if type(value) != auto else self.make_default("CcyToSell")

	@CcyToSell.deleter
	def CcyToSell(self):
		del self._CcyToSell
		self._CcyToSell = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if type(value) != auto else self.make_default("CcyOptn")

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = None

	@property
	def ElgblForCollInd(self):
		return self._ElgblForCollInd

	@ElgblForCollInd.setter
	def ElgblForCollInd(self, value):
		self._ElgblForCollInd = value if type(value) != auto else self.make_default("ElgblForCollInd")

	@ElgblForCollInd.deleter
	def ElgblForCollInd(self):
		del self._ElgblForCollInd
		self._ElgblForCollInd = None

	@property
	def SlctnDealrFeeInd(self):
		return self._SlctnDealrFeeInd

	@SlctnDealrFeeInd.setter
	def SlctnDealrFeeInd(self, value):
		self._SlctnDealrFeeInd = value if type(value) != auto else self.make_default("SlctnDealrFeeInd")

	@SlctnDealrFeeInd.deleter
	def SlctnDealrFeeInd(self):
		del self._SlctnDealrFeeInd
		self._SlctnDealrFeeInd = None

	@property
	def ShrhldrNb(self):
		return self._ShrhldrNb

	@ShrhldrNb.setter
	def ShrhldrNb(self, value):
		self._ShrhldrNb = value if type(value) != auto else self.make_default("ShrhldrNb")

	@ShrhldrNb.deleter
	def ShrhldrNb(self):
		del self._ShrhldrNb
		self._ShrhldrNb = None

	@property
	def CcyToBuy(self):
		return self._CcyToBuy

	@CcyToBuy.setter
	def CcyToBuy(self, value):
		self._CcyToBuy = value if type(value) != auto else self.make_default("CcyToBuy")

	@CcyToBuy.deleter
	def CcyToBuy(self):
		del self._CcyToBuy
		self._CcyToBuy = None

	@property
	def SctiesQtyOrInstdAmt(self):
		return self._SctiesQtyOrInstdAmt

	@SctiesQtyOrInstdAmt.setter
	def SctiesQtyOrInstdAmt(self, value):
		self._SctiesQtyOrInstdAmt = value if type(value) != auto else self.make_default("SctiesQtyOrInstdAmt")

	@SctiesQtyOrInstdAmt.deleter
	def SctiesQtyOrInstdAmt(self):
		del self._SctiesQtyOrInstdAmt
		self._SctiesQtyOrInstdAmt = None

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if type(value) != auto else self.make_default("OptnFeatrs")

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = None

	@property
	def ExctnReqdDtTm(self):
		return self._ExctnReqdDtTm

	@ExctnReqdDtTm.setter
	def ExctnReqdDtTm(self, value):
		self._ExctnReqdDtTm = value if type(value) != auto else self.make_default("ExctnReqdDtTm")

	@ExctnReqdDtTm.deleter
	def ExctnReqdDtTm(self):
		del self._ExctnReqdDtTm
		self._ExctnReqdDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyToSell', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice88, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForCollInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnDealrFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrNb', type=Max25Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToBuy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyOrInstdAmt', type=SecuritiesQuantityOrAmount6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption40Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnReqdDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

