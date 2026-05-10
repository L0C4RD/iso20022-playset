import base_types
import TaxReference2
import PercentageRate
import Capped1
import Max140Text
import ActiveCurrencyAnd13DecimalAmount
import YesNoIndicator
import DrawdownType2Choice
import AdditionalInformation15
import ISODate
import BeneficiaryDrawdown1
import ApplicableRules1Choice

class Drawdown2(base_types._BaseFieldType):

	__slots__ = ["_RcptOfDrwdwnInd", "_PnsnCmcmntLumpSumDt", "_Id", "_AddtlFndsDsgntd", "_AplblRules", "_InvstrTaxRef", "_LftmAllwnc", "_FlxblDrwdwnTrggrdDt", "_MltplPnsnCmcmntLumpSums", "_AddtlInf", "_TrchTp", "_PnsnCmcmntLumpSumRmng", "_CapdLmts", "_TtlAmtNetDrwdwn", "_BnfcryDtls", "_PctgOfTtlTrfVal"]
	@property
	def RcptOfDrwdwnInd(self):
		return self._RcptOfDrwdwnInd

	@RcptOfDrwdwnInd.setter
	def RcptOfDrwdwnInd(self, value):
		self._RcptOfDrwdwnInd = value if type(value) != auto else self.make_default("RcptOfDrwdwnInd")

	@RcptOfDrwdwnInd.deleter
	def RcptOfDrwdwnInd(self):
		del self._RcptOfDrwdwnInd
		self._RcptOfDrwdwnInd = None

	@property
	def PnsnCmcmntLumpSumDt(self):
		return self._PnsnCmcmntLumpSumDt

	@PnsnCmcmntLumpSumDt.setter
	def PnsnCmcmntLumpSumDt(self, value):
		self._PnsnCmcmntLumpSumDt = value if type(value) != auto else self.make_default("PnsnCmcmntLumpSumDt")

	@PnsnCmcmntLumpSumDt.deleter
	def PnsnCmcmntLumpSumDt(self):
		del self._PnsnCmcmntLumpSumDt
		self._PnsnCmcmntLumpSumDt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AddtlFndsDsgntd(self):
		return self._AddtlFndsDsgntd

	@AddtlFndsDsgntd.setter
	def AddtlFndsDsgntd(self, value):
		self._AddtlFndsDsgntd = value if type(value) != auto else self.make_default("AddtlFndsDsgntd")

	@AddtlFndsDsgntd.deleter
	def AddtlFndsDsgntd(self):
		del self._AddtlFndsDsgntd
		self._AddtlFndsDsgntd = None

	@property
	def AplblRules(self):
		return self._AplblRules

	@AplblRules.setter
	def AplblRules(self, value):
		self._AplblRules = value if type(value) != auto else self.make_default("AplblRules")

	@AplblRules.deleter
	def AplblRules(self):
		del self._AplblRules
		self._AplblRules = None

	@property
	def InvstrTaxRef(self):
		return self._InvstrTaxRef

	@InvstrTaxRef.setter
	def InvstrTaxRef(self, value):
		self._InvstrTaxRef = value if type(value) != auto else self.make_default("InvstrTaxRef")

	@InvstrTaxRef.deleter
	def InvstrTaxRef(self):
		del self._InvstrTaxRef
		self._InvstrTaxRef = None

	@property
	def LftmAllwnc(self):
		return self._LftmAllwnc

	@LftmAllwnc.setter
	def LftmAllwnc(self, value):
		self._LftmAllwnc = value if type(value) != auto else self.make_default("LftmAllwnc")

	@LftmAllwnc.deleter
	def LftmAllwnc(self):
		del self._LftmAllwnc
		self._LftmAllwnc = None

	@property
	def FlxblDrwdwnTrggrdDt(self):
		return self._FlxblDrwdwnTrggrdDt

	@FlxblDrwdwnTrggrdDt.setter
	def FlxblDrwdwnTrggrdDt(self, value):
		self._FlxblDrwdwnTrggrdDt = value if type(value) != auto else self.make_default("FlxblDrwdwnTrggrdDt")

	@FlxblDrwdwnTrggrdDt.deleter
	def FlxblDrwdwnTrggrdDt(self):
		del self._FlxblDrwdwnTrggrdDt
		self._FlxblDrwdwnTrggrdDt = None

	@property
	def MltplPnsnCmcmntLumpSums(self):
		return self._MltplPnsnCmcmntLumpSums

	@MltplPnsnCmcmntLumpSums.setter
	def MltplPnsnCmcmntLumpSums(self, value):
		self._MltplPnsnCmcmntLumpSums = value if type(value) != auto else self.make_default("MltplPnsnCmcmntLumpSums")

	@MltplPnsnCmcmntLumpSums.deleter
	def MltplPnsnCmcmntLumpSums(self):
		del self._MltplPnsnCmcmntLumpSums
		self._MltplPnsnCmcmntLumpSums = None

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
	def TrchTp(self):
		return self._TrchTp

	@TrchTp.setter
	def TrchTp(self, value):
		self._TrchTp = value if type(value) != auto else self.make_default("TrchTp")

	@TrchTp.deleter
	def TrchTp(self):
		del self._TrchTp
		self._TrchTp = None

	@property
	def PnsnCmcmntLumpSumRmng(self):
		return self._PnsnCmcmntLumpSumRmng

	@PnsnCmcmntLumpSumRmng.setter
	def PnsnCmcmntLumpSumRmng(self, value):
		self._PnsnCmcmntLumpSumRmng = value if type(value) != auto else self.make_default("PnsnCmcmntLumpSumRmng")

	@PnsnCmcmntLumpSumRmng.deleter
	def PnsnCmcmntLumpSumRmng(self):
		del self._PnsnCmcmntLumpSumRmng
		self._PnsnCmcmntLumpSumRmng = None

	@property
	def CapdLmts(self):
		return self._CapdLmts

	@CapdLmts.setter
	def CapdLmts(self, value):
		self._CapdLmts = value if type(value) != auto else self.make_default("CapdLmts")

	@CapdLmts.deleter
	def CapdLmts(self):
		del self._CapdLmts
		self._CapdLmts = None

	@property
	def TtlAmtNetDrwdwn(self):
		return self._TtlAmtNetDrwdwn

	@TtlAmtNetDrwdwn.setter
	def TtlAmtNetDrwdwn(self, value):
		self._TtlAmtNetDrwdwn = value if type(value) != auto else self.make_default("TtlAmtNetDrwdwn")

	@TtlAmtNetDrwdwn.deleter
	def TtlAmtNetDrwdwn(self):
		del self._TtlAmtNetDrwdwn
		self._TtlAmtNetDrwdwn = None

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if type(value) != auto else self.make_default("BnfcryDtls")

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = None

	@property
	def PctgOfTtlTrfVal(self):
		return self._PctgOfTtlTrfVal

	@PctgOfTtlTrfVal.setter
	def PctgOfTtlTrfVal(self, value):
		self._PctgOfTtlTrfVal = value if type(value) != auto else self.make_default("PctgOfTtlTrfVal")

	@PctgOfTtlTrfVal.deleter
	def PctgOfTtlTrfVal(self):
		del self._PctgOfTtlTrfVal
		self._PctgOfTtlTrfVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcptOfDrwdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnCmcmntLumpSumDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFndsDsgntd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRules', type=ApplicableRules1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTaxRef', type=TaxReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LftmAllwnc', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlxblDrwdwnTrggrdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplPnsnCmcmntLumpSums', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrchTp', type=DrawdownType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnCmcmntLumpSumRmng', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CapdLmts', type=Capped1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmtNetDrwdwn', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=BeneficiaryDrawdown1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfTtlTrfVal', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

