# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._CorporateActionChangeTypeFormat7Choice import CorporateActionChangeTypeFormat7Choice
from ._CorporateActionNarrative33 import CorporateActionNarrative33
from ._CorporateActionOption43Choice import CorporateActionOption43Choice
from ._CorporateActionPrice91 import CorporateActionPrice91
from ._CorporateActionRate130 import CorporateActionRate130
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._FractionDispositionType29Choice import FractionDispositionType29Choice
from ._OptionFeaturesFormat27Choice import OptionFeaturesFormat27Choice
from ._OptionNumber1Choice import OptionNumber1Choice
from ._RestrictedFINXMax25Text import RestrictedFINXMax25Text
from ._SecuritiesQuantityOrAmount7Choice import SecuritiesQuantityOrAmount7Choice
from ._SecurityIdentification20 import SecurityIdentification20
from ._YesNoIndicator import YesNoIndicator

class CorporateActionOption243(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CcyOptn", "_CcyToBuy", "_CcyToSell", "_ChngTp", "_ElgblForCollInd", "_ExctnReqdDtTm", "_FrctnDspstn", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_PricDtls", "_RateAndAmtDtls", "_SctiesQtyOrInstdAmt", "_SctyId", "_ShrhldrNb", "_SlctnDealrFeeInd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if type(value) != base_types.auto else self.make_default("CcyOptn")

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = None

	@property
	def CcyToBuy(self):
		return self._CcyToBuy

	@CcyToBuy.setter
	def CcyToBuy(self, value):
		self._CcyToBuy = value if type(value) != base_types.auto else self.make_default("CcyToBuy")

	@CcyToBuy.deleter
	def CcyToBuy(self):
		del self._CcyToBuy
		self._CcyToBuy = None

	@property
	def CcyToSell(self):
		return self._CcyToSell

	@CcyToSell.setter
	def CcyToSell(self, value):
		self._CcyToSell = value if type(value) != base_types.auto else self.make_default("CcyToSell")

	@CcyToSell.deleter
	def CcyToSell(self):
		del self._CcyToSell
		self._CcyToSell = None

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if type(value) != base_types.auto else self.make_default("ChngTp")

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = None

	@property
	def ElgblForCollInd(self):
		return self._ElgblForCollInd

	@ElgblForCollInd.setter
	def ElgblForCollInd(self, value):
		self._ElgblForCollInd = value if type(value) != base_types.auto else self.make_default("ElgblForCollInd")

	@ElgblForCollInd.deleter
	def ElgblForCollInd(self):
		del self._ElgblForCollInd
		self._ElgblForCollInd = None

	@property
	def ExctnReqdDtTm(self):
		return self._ExctnReqdDtTm

	@ExctnReqdDtTm.setter
	def ExctnReqdDtTm(self, value):
		self._ExctnReqdDtTm = value if type(value) != base_types.auto else self.make_default("ExctnReqdDtTm")

	@ExctnReqdDtTm.deleter
	def ExctnReqdDtTm(self):
		del self._ExctnReqdDtTm
		self._ExctnReqdDtTm = None

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != base_types.auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if type(value) != base_types.auto else self.make_default("OptnFeatrs")

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != base_types.auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def SctiesQtyOrInstdAmt(self):
		return self._SctiesQtyOrInstdAmt

	@SctiesQtyOrInstdAmt.setter
	def SctiesQtyOrInstdAmt(self, value):
		self._SctiesQtyOrInstdAmt = value if type(value) != base_types.auto else self.make_default("SctiesQtyOrInstdAmt")

	@SctiesQtyOrInstdAmt.deleter
	def SctiesQtyOrInstdAmt(self):
		del self._SctiesQtyOrInstdAmt
		self._SctiesQtyOrInstdAmt = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def ShrhldrNb(self):
		return self._ShrhldrNb

	@ShrhldrNb.setter
	def ShrhldrNb(self, value):
		self._ShrhldrNb = value if type(value) != base_types.auto else self.make_default("ShrhldrNb")

	@ShrhldrNb.deleter
	def ShrhldrNb(self):
		del self._ShrhldrNb
		self._ShrhldrNb = None

	@property
	def SlctnDealrFeeInd(self):
		return self._SlctnDealrFeeInd

	@SlctnDealrFeeInd.setter
	def SlctnDealrFeeInd(self, value):
		self._SlctnDealrFeeInd = value if type(value) != base_types.auto else self.make_default("SlctnDealrFeeInd")

	@SlctnDealrFeeInd.deleter
	def SlctnDealrFeeInd(self):
		del self._SlctnDealrFeeInd
		self._SlctnDealrFeeInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToBuy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToSell', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngTp', type=CorporateActionChangeTypeFormat7Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ElgblForCollInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnReqdDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption43Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice91, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate130, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyOrInstdAmt', type=SecuritiesQuantityOrAmount7Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrNb', type=RestrictedFINXMax25Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnDealrFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))