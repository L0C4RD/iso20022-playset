# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import ApplicableRules1Choice
from . import BeneficiaryDrawdown2
from . import Capped1
from . import DrawdownType2Choice
from . import ISODate
from . import Max140Text
from . import PercentageRate
from . import TaxReference2
from . import YesNoIndicator

class Drawdown04(base_types._BaseFieldType):

	__slots__ = ["_AddtlFndsDsgntd", "_AddtlInf", "_AplblRules", "_BnfcryDtls", "_CapdLmts", "_FlxblDrwdwnTrggrdDt", "_Id", "_InvstrTaxRef", "_LftmAllwnc", "_MltplPnsnCmcmntLumpSums", "_PctgOfTtlTrfVal", "_PnsnCmcmntLumpSumDt", "_PnsnCmcmntLumpSumRmng", "_RcptOfDrwdwnInd", "_TrchDt", "_TrchTp", "_TtlAmtNetDrwdwn"]
	@property
	def AddtlFndsDsgntd(self):
		return self._AddtlFndsDsgntd

	@AddtlFndsDsgntd.setter
	def AddtlFndsDsgntd(self, value):
		self._AddtlFndsDsgntd = value if value is not None else base_types.UninitialisedField(self, 'AddtlFndsDsgntd', YesNoIndicator, False)

	@AddtlFndsDsgntd.deleter
	def AddtlFndsDsgntd(self):
		del self._AddtlFndsDsgntd
		self._AddtlFndsDsgntd = base_types.UninitialisedField(self, 'AddtlFndsDsgntd', YesNoIndicator, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def AplblRules(self):
		return self._AplblRules

	@AplblRules.setter
	def AplblRules(self, value):
		self._AplblRules = value if value is not None else base_types.UninitialisedField(self, 'AplblRules', ApplicableRules1Choice, False)

	@AplblRules.deleter
	def AplblRules(self):
		del self._AplblRules
		self._AplblRules = base_types.UninitialisedField(self, 'AplblRules', ApplicableRules1Choice, False)

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfcryDtls', BeneficiaryDrawdown2, False)

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = base_types.UninitialisedField(self, 'BnfcryDtls', BeneficiaryDrawdown2, False)

	@property
	def CapdLmts(self):
		return self._CapdLmts

	@CapdLmts.setter
	def CapdLmts(self, value):
		self._CapdLmts = value if value is not None else base_types.UninitialisedField(self, 'CapdLmts', Capped1, False)

	@CapdLmts.deleter
	def CapdLmts(self):
		del self._CapdLmts
		self._CapdLmts = base_types.UninitialisedField(self, 'CapdLmts', Capped1, False)

	@property
	def FlxblDrwdwnTrggrdDt(self):
		return self._FlxblDrwdwnTrggrdDt

	@FlxblDrwdwnTrggrdDt.setter
	def FlxblDrwdwnTrggrdDt(self, value):
		self._FlxblDrwdwnTrggrdDt = value if value is not None else base_types.UninitialisedField(self, 'FlxblDrwdwnTrggrdDt', ISODate, False)

	@FlxblDrwdwnTrggrdDt.deleter
	def FlxblDrwdwnTrggrdDt(self):
		del self._FlxblDrwdwnTrggrdDt
		self._FlxblDrwdwnTrggrdDt = base_types.UninitialisedField(self, 'FlxblDrwdwnTrggrdDt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max140Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max140Text, False)

	@property
	def InvstrTaxRef(self):
		return self._InvstrTaxRef

	@InvstrTaxRef.setter
	def InvstrTaxRef(self, value):
		self._InvstrTaxRef = value if value is not None else base_types.UninitialisedField(self, 'InvstrTaxRef', TaxReference2, False)

	@InvstrTaxRef.deleter
	def InvstrTaxRef(self):
		del self._InvstrTaxRef
		self._InvstrTaxRef = base_types.UninitialisedField(self, 'InvstrTaxRef', TaxReference2, False)

	@property
	def LftmAllwnc(self):
		return self._LftmAllwnc

	@LftmAllwnc.setter
	def LftmAllwnc(self, value):
		self._LftmAllwnc = value if value is not None else base_types.UninitialisedField(self, 'LftmAllwnc', PercentageRate, False)

	@LftmAllwnc.deleter
	def LftmAllwnc(self):
		del self._LftmAllwnc
		self._LftmAllwnc = base_types.UninitialisedField(self, 'LftmAllwnc', PercentageRate, False)

	@property
	def MltplPnsnCmcmntLumpSums(self):
		return self._MltplPnsnCmcmntLumpSums

	@MltplPnsnCmcmntLumpSums.setter
	def MltplPnsnCmcmntLumpSums(self, value):
		self._MltplPnsnCmcmntLumpSums = value if value is not None else base_types.UninitialisedField(self, 'MltplPnsnCmcmntLumpSums', YesNoIndicator, False)

	@MltplPnsnCmcmntLumpSums.deleter
	def MltplPnsnCmcmntLumpSums(self):
		del self._MltplPnsnCmcmntLumpSums
		self._MltplPnsnCmcmntLumpSums = base_types.UninitialisedField(self, 'MltplPnsnCmcmntLumpSums', YesNoIndicator, False)

	@property
	def PctgOfTtlTrfVal(self):
		return self._PctgOfTtlTrfVal

	@PctgOfTtlTrfVal.setter
	def PctgOfTtlTrfVal(self, value):
		self._PctgOfTtlTrfVal = value if value is not None else base_types.UninitialisedField(self, 'PctgOfTtlTrfVal', PercentageRate, False)

	@PctgOfTtlTrfVal.deleter
	def PctgOfTtlTrfVal(self):
		del self._PctgOfTtlTrfVal
		self._PctgOfTtlTrfVal = base_types.UninitialisedField(self, 'PctgOfTtlTrfVal', PercentageRate, False)

	@property
	def PnsnCmcmntLumpSumDt(self):
		return self._PnsnCmcmntLumpSumDt

	@PnsnCmcmntLumpSumDt.setter
	def PnsnCmcmntLumpSumDt(self, value):
		self._PnsnCmcmntLumpSumDt = value if value is not None else base_types.UninitialisedField(self, 'PnsnCmcmntLumpSumDt', ISODate, False)

	@PnsnCmcmntLumpSumDt.deleter
	def PnsnCmcmntLumpSumDt(self):
		del self._PnsnCmcmntLumpSumDt
		self._PnsnCmcmntLumpSumDt = base_types.UninitialisedField(self, 'PnsnCmcmntLumpSumDt', ISODate, False)

	@property
	def PnsnCmcmntLumpSumRmng(self):
		return self._PnsnCmcmntLumpSumRmng

	@PnsnCmcmntLumpSumRmng.setter
	def PnsnCmcmntLumpSumRmng(self, value):
		self._PnsnCmcmntLumpSumRmng = value if value is not None else base_types.UninitialisedField(self, 'PnsnCmcmntLumpSumRmng', ActiveCurrencyAnd13DecimalAmount, False)

	@PnsnCmcmntLumpSumRmng.deleter
	def PnsnCmcmntLumpSumRmng(self):
		del self._PnsnCmcmntLumpSumRmng
		self._PnsnCmcmntLumpSumRmng = base_types.UninitialisedField(self, 'PnsnCmcmntLumpSumRmng', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def RcptOfDrwdwnInd(self):
		return self._RcptOfDrwdwnInd

	@RcptOfDrwdwnInd.setter
	def RcptOfDrwdwnInd(self, value):
		self._RcptOfDrwdwnInd = value if value is not None else base_types.UninitialisedField(self, 'RcptOfDrwdwnInd', YesNoIndicator, False)

	@RcptOfDrwdwnInd.deleter
	def RcptOfDrwdwnInd(self):
		del self._RcptOfDrwdwnInd
		self._RcptOfDrwdwnInd = base_types.UninitialisedField(self, 'RcptOfDrwdwnInd', YesNoIndicator, False)

	@property
	def TrchDt(self):
		return self._TrchDt

	@TrchDt.setter
	def TrchDt(self, value):
		self._TrchDt = value if value is not None else base_types.UninitialisedField(self, 'TrchDt', ISODate, False)

	@TrchDt.deleter
	def TrchDt(self):
		del self._TrchDt
		self._TrchDt = base_types.UninitialisedField(self, 'TrchDt', ISODate, False)

	@property
	def TrchTp(self):
		return self._TrchTp

	@TrchTp.setter
	def TrchTp(self, value):
		self._TrchTp = value if value is not None else base_types.UninitialisedField(self, 'TrchTp', DrawdownType2Choice, False)

	@TrchTp.deleter
	def TrchTp(self):
		del self._TrchTp
		self._TrchTp = base_types.UninitialisedField(self, 'TrchTp', DrawdownType2Choice, False)

	@property
	def TtlAmtNetDrwdwn(self):
		return self._TtlAmtNetDrwdwn

	@TtlAmtNetDrwdwn.setter
	def TtlAmtNetDrwdwn(self, value):
		self._TtlAmtNetDrwdwn = value if value is not None else base_types.UninitialisedField(self, 'TtlAmtNetDrwdwn', ActiveCurrencyAnd13DecimalAmount, False)

	@TtlAmtNetDrwdwn.deleter
	def TtlAmtNetDrwdwn(self):
		del self._TtlAmtNetDrwdwn
		self._TtlAmtNetDrwdwn = base_types.UninitialisedField(self, 'TtlAmtNetDrwdwn', ActiveCurrencyAnd13DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlFndsDsgntd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AplblRules', type=ApplicableRules1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=BeneficiaryDrawdown2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CapdLmts', type=Capped1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlxblDrwdwnTrggrdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTaxRef', type=TaxReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LftmAllwnc', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplPnsnCmcmntLumpSums', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfTtlTrfVal', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnCmcmntLumpSumDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnCmcmntLumpSumRmng', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptOfDrwdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchTp', type=DrawdownType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtNetDrwdwn', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))