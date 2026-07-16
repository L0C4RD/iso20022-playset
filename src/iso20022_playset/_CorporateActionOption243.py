# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import CorporateActionChangeTypeFormat7Choice
from . import CorporateActionNarrative33
from . import CorporateActionOption43Choice
from . import CorporateActionPrice91
from . import CorporateActionRate130
from . import DateAndDateTime2Choice
from . import FractionDispositionType29Choice
from . import OptionFeaturesFormat27Choice
from . import OptionNumber1Choice
from . import RestrictedFINXMax25Text
from . import SecuritiesQuantityOrAmount7Choice
from . import SecurityIdentification20
from . import YesNoIndicator

class CorporateActionOption243(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CcyOptn", "_CcyToBuy", "_CcyToSell", "_ChngTp", "_ElgblForCollInd", "_ExctnReqdDtTm", "_FrctnDspstn", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_PricDtls", "_RateAndAmtDtls", "_SctiesQtyOrInstdAmt", "_SctyId", "_ShrhldrNb", "_SlctnDealrFeeInd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative33, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative33, False)

	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if value is not None else base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

	@property
	def CcyToBuy(self):
		return self._CcyToBuy

	@CcyToBuy.setter
	def CcyToBuy(self, value):
		self._CcyToBuy = value if value is not None else base_types.UninitialisedField(self, 'CcyToBuy', ActiveCurrencyCode, False)

	@CcyToBuy.deleter
	def CcyToBuy(self):
		del self._CcyToBuy
		self._CcyToBuy = base_types.UninitialisedField(self, 'CcyToBuy', ActiveCurrencyCode, False)

	@property
	def CcyToSell(self):
		return self._CcyToSell

	@CcyToSell.setter
	def CcyToSell(self, value):
		self._CcyToSell = value if value is not None else base_types.UninitialisedField(self, 'CcyToSell', ActiveCurrencyCode, False)

	@CcyToSell.deleter
	def CcyToSell(self):
		del self._CcyToSell
		self._CcyToSell = base_types.UninitialisedField(self, 'CcyToSell', ActiveCurrencyCode, False)

	@property
	def ChngTp(self):
		return self._ChngTp

	@ChngTp.setter
	def ChngTp(self, value):
		self._ChngTp = value if value is not None else base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat7Choice, True)

	@ChngTp.deleter
	def ChngTp(self):
		del self._ChngTp
		self._ChngTp = base_types.UninitialisedField(self, 'ChngTp', CorporateActionChangeTypeFormat7Choice, True)

	@property
	def ElgblForCollInd(self):
		return self._ElgblForCollInd

	@ElgblForCollInd.setter
	def ElgblForCollInd(self, value):
		self._ElgblForCollInd = value if value is not None else base_types.UninitialisedField(self, 'ElgblForCollInd', YesNoIndicator, False)

	@ElgblForCollInd.deleter
	def ElgblForCollInd(self):
		del self._ElgblForCollInd
		self._ElgblForCollInd = base_types.UninitialisedField(self, 'ElgblForCollInd', YesNoIndicator, False)

	@property
	def ExctnReqdDtTm(self):
		return self._ExctnReqdDtTm

	@ExctnReqdDtTm.setter
	def ExctnReqdDtTm(self, value):
		self._ExctnReqdDtTm = value if value is not None else base_types.UninitialisedField(self, 'ExctnReqdDtTm', DateAndDateTime2Choice, False)

	@ExctnReqdDtTm.deleter
	def ExctnReqdDtTm(self):
		del self._ExctnReqdDtTm
		self._ExctnReqdDtTm = base_types.UninitialisedField(self, 'ExctnReqdDtTm', DateAndDateTime2Choice, False)

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType29Choice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType29Choice, False)

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat27Choice, False)

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat27Choice, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption43Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption43Choice, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice91, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice91, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate130, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate130, False)

	@property
	def SctiesQtyOrInstdAmt(self):
		return self._SctiesQtyOrInstdAmt

	@SctiesQtyOrInstdAmt.setter
	def SctiesQtyOrInstdAmt(self, value):
		self._SctiesQtyOrInstdAmt = value if value is not None else base_types.UninitialisedField(self, 'SctiesQtyOrInstdAmt', SecuritiesQuantityOrAmount7Choice, False)

	@SctiesQtyOrInstdAmt.deleter
	def SctiesQtyOrInstdAmt(self):
		del self._SctiesQtyOrInstdAmt
		self._SctiesQtyOrInstdAmt = base_types.UninitialisedField(self, 'SctiesQtyOrInstdAmt', SecuritiesQuantityOrAmount7Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification20, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification20, False)

	@property
	def ShrhldrNb(self):
		return self._ShrhldrNb

	@ShrhldrNb.setter
	def ShrhldrNb(self, value):
		self._ShrhldrNb = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrNb', RestrictedFINXMax25Text, False)

	@ShrhldrNb.deleter
	def ShrhldrNb(self):
		del self._ShrhldrNb
		self._ShrhldrNb = base_types.UninitialisedField(self, 'ShrhldrNb', RestrictedFINXMax25Text, False)

	@property
	def SlctnDealrFeeInd(self):
		return self._SlctnDealrFeeInd

	@SlctnDealrFeeInd.setter
	def SlctnDealrFeeInd(self, value):
		self._SlctnDealrFeeInd = value if value is not None else base_types.UninitialisedField(self, 'SlctnDealrFeeInd', YesNoIndicator, False)

	@SlctnDealrFeeInd.deleter
	def SlctnDealrFeeInd(self):
		del self._SlctnDealrFeeInd
		self._SlctnDealrFeeInd = base_types.UninitialisedField(self, 'SlctnDealrFeeInd', YesNoIndicator, False)

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