# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class CorporateActionAmounts1(base_types._BaseFieldType):

	__slots__ = ["_AddtlSbcptCost", "_AddtlTaxAmt", "_ChrgsAmt", "_CptlGn", "_CshInLieuOfShr", "_CshIncntiv", "_CtryNtlFdrlTaxAmt", "_EURtntnTaxAmt", "_EntitldAmt", "_ExctgBrkrAmt", "_FsclStmpAmt", "_FullyFrnkdAmt", "_GrmnLclTax1Amt", "_GrmnLclTax2Amt", "_GrmnLclTax3Amt", "_GrmnLclTax4Amt", "_GrssCshAmt", "_IndmntyAmt", "_IntrstAmt", "_IsseDscntAmt", "_LclBrkrComssnAmt", "_LclTaxAmt", "_ManfctrdDvddAmt", "_MktClmAmt", "_NetCshAmt", "_OrgnlAmt", "_PmtLevyTaxAmt", "_PngAgtComssnAmt", "_PrncplOrCrps", "_PstgFeeAmt", "_RedPrmAmt", "_RgltryFeesAmt", "_RinvstmtAmt", "_ShppgFeesAmt", "_SlctnFees", "_SndryOrOthrAmt", "_SpclCncssnAmt", "_StmpDtyAmt", "_StockXchgTaxAmt", "_TaxCdtAmt", "_TaxDfrrdAmt", "_TaxFreeAmt", "_TaxRclmAmt", "_TrfTaxAmt", "_TxTaxAmt", "_UfrnkdAmt", "_ValAddedTaxAmt", "_WhldgOfFrgnTaxAmt", "_WhldgOfLclTaxAmt", "_WhldgTaxAmt"]
	@property
	def AddtlSbcptCost(self):
		return self._AddtlSbcptCost

	@AddtlSbcptCost.setter
	def AddtlSbcptCost(self, value):
		self._AddtlSbcptCost = value if value is not None else base_types.UninitialisedField(self, 'AddtlSbcptCost', ActiveCurrencyAndAmount, False)

	@AddtlSbcptCost.deleter
	def AddtlSbcptCost(self):
		del self._AddtlSbcptCost
		self._AddtlSbcptCost = base_types.UninitialisedField(self, 'AddtlSbcptCost', ActiveCurrencyAndAmount, False)

	@property
	def AddtlTaxAmt(self):
		return self._AddtlTaxAmt

	@AddtlTaxAmt.setter
	def AddtlTaxAmt(self, value):
		self._AddtlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTaxAmt', ActiveCurrencyAndAmount, False)

	@AddtlTaxAmt.deleter
	def AddtlTaxAmt(self):
		del self._AddtlTaxAmt
		self._AddtlTaxAmt = base_types.UninitialisedField(self, 'AddtlTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAmt', ActiveCurrencyAndAmount, False)

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = base_types.UninitialisedField(self, 'ChrgsAmt', ActiveCurrencyAndAmount, False)

	@property
	def CptlGn(self):
		return self._CptlGn

	@CptlGn.setter
	def CptlGn(self, value):
		self._CptlGn = value if value is not None else base_types.UninitialisedField(self, 'CptlGn', ActiveCurrencyAndAmount, False)

	@CptlGn.deleter
	def CptlGn(self):
		del self._CptlGn
		self._CptlGn = base_types.UninitialisedField(self, 'CptlGn', ActiveCurrencyAndAmount, False)

	@property
	def CshInLieuOfShr(self):
		return self._CshInLieuOfShr

	@CshInLieuOfShr.setter
	def CshInLieuOfShr(self, value):
		self._CshInLieuOfShr = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShr', ActiveCurrencyAndAmount, False)

	@CshInLieuOfShr.deleter
	def CshInLieuOfShr(self):
		del self._CshInLieuOfShr
		self._CshInLieuOfShr = base_types.UninitialisedField(self, 'CshInLieuOfShr', ActiveCurrencyAndAmount, False)

	@property
	def CshIncntiv(self):
		return self._CshIncntiv

	@CshIncntiv.setter
	def CshIncntiv(self, value):
		self._CshIncntiv = value if value is not None else base_types.UninitialisedField(self, 'CshIncntiv', ActiveCurrencyAndAmount, False)

	@CshIncntiv.deleter
	def CshIncntiv(self):
		del self._CshIncntiv
		self._CshIncntiv = base_types.UninitialisedField(self, 'CshIncntiv', ActiveCurrencyAndAmount, False)

	@property
	def CtryNtlFdrlTaxAmt(self):
		return self._CtryNtlFdrlTaxAmt

	@CtryNtlFdrlTaxAmt.setter
	def CtryNtlFdrlTaxAmt(self, value):
		self._CtryNtlFdrlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'CtryNtlFdrlTaxAmt', ActiveCurrencyAndAmount, False)

	@CtryNtlFdrlTaxAmt.deleter
	def CtryNtlFdrlTaxAmt(self):
		del self._CtryNtlFdrlTaxAmt
		self._CtryNtlFdrlTaxAmt = base_types.UninitialisedField(self, 'CtryNtlFdrlTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def EURtntnTaxAmt(self):
		return self._EURtntnTaxAmt

	@EURtntnTaxAmt.setter
	def EURtntnTaxAmt(self, value):
		self._EURtntnTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'EURtntnTaxAmt', ActiveCurrencyAndAmount, False)

	@EURtntnTaxAmt.deleter
	def EURtntnTaxAmt(self):
		del self._EURtntnTaxAmt
		self._EURtntnTaxAmt = base_types.UninitialisedField(self, 'EURtntnTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if value is not None else base_types.UninitialisedField(self, 'EntitldAmt', ActiveCurrencyAndAmount, False)

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = base_types.UninitialisedField(self, 'EntitldAmt', ActiveCurrencyAndAmount, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', ActiveCurrencyAndAmount, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', ActiveCurrencyAndAmount, False)

	@property
	def FsclStmpAmt(self):
		return self._FsclStmpAmt

	@FsclStmpAmt.setter
	def FsclStmpAmt(self, value):
		self._FsclStmpAmt = value if value is not None else base_types.UninitialisedField(self, 'FsclStmpAmt', ActiveCurrencyAndAmount, False)

	@FsclStmpAmt.deleter
	def FsclStmpAmt(self):
		del self._FsclStmpAmt
		self._FsclStmpAmt = base_types.UninitialisedField(self, 'FsclStmpAmt', ActiveCurrencyAndAmount, False)

	@property
	def FullyFrnkdAmt(self):
		return self._FullyFrnkdAmt

	@FullyFrnkdAmt.setter
	def FullyFrnkdAmt(self, value):
		self._FullyFrnkdAmt = value if value is not None else base_types.UninitialisedField(self, 'FullyFrnkdAmt', ActiveCurrencyAndAmount, False)

	@FullyFrnkdAmt.deleter
	def FullyFrnkdAmt(self):
		del self._FullyFrnkdAmt
		self._FullyFrnkdAmt = base_types.UninitialisedField(self, 'FullyFrnkdAmt', ActiveCurrencyAndAmount, False)

	@property
	def GrmnLclTax1Amt(self):
		return self._GrmnLclTax1Amt

	@GrmnLclTax1Amt.setter
	def GrmnLclTax1Amt(self, value):
		self._GrmnLclTax1Amt = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax1Amt', ActiveCurrencyAndAmount, False)

	@GrmnLclTax1Amt.deleter
	def GrmnLclTax1Amt(self):
		del self._GrmnLclTax1Amt
		self._GrmnLclTax1Amt = base_types.UninitialisedField(self, 'GrmnLclTax1Amt', ActiveCurrencyAndAmount, False)

	@property
	def GrmnLclTax2Amt(self):
		return self._GrmnLclTax2Amt

	@GrmnLclTax2Amt.setter
	def GrmnLclTax2Amt(self, value):
		self._GrmnLclTax2Amt = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax2Amt', ActiveCurrencyAndAmount, False)

	@GrmnLclTax2Amt.deleter
	def GrmnLclTax2Amt(self):
		del self._GrmnLclTax2Amt
		self._GrmnLclTax2Amt = base_types.UninitialisedField(self, 'GrmnLclTax2Amt', ActiveCurrencyAndAmount, False)

	@property
	def GrmnLclTax3Amt(self):
		return self._GrmnLclTax3Amt

	@GrmnLclTax3Amt.setter
	def GrmnLclTax3Amt(self, value):
		self._GrmnLclTax3Amt = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax3Amt', ActiveCurrencyAndAmount, False)

	@GrmnLclTax3Amt.deleter
	def GrmnLclTax3Amt(self):
		del self._GrmnLclTax3Amt
		self._GrmnLclTax3Amt = base_types.UninitialisedField(self, 'GrmnLclTax3Amt', ActiveCurrencyAndAmount, False)

	@property
	def GrmnLclTax4Amt(self):
		return self._GrmnLclTax4Amt

	@GrmnLclTax4Amt.setter
	def GrmnLclTax4Amt(self, value):
		self._GrmnLclTax4Amt = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax4Amt', ActiveCurrencyAndAmount, False)

	@GrmnLclTax4Amt.deleter
	def GrmnLclTax4Amt(self):
		del self._GrmnLclTax4Amt
		self._GrmnLclTax4Amt = base_types.UninitialisedField(self, 'GrmnLclTax4Amt', ActiveCurrencyAndAmount, False)

	@property
	def GrssCshAmt(self):
		return self._GrssCshAmt

	@GrssCshAmt.setter
	def GrssCshAmt(self, value):
		self._GrssCshAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssCshAmt', ActiveCurrencyAndAmount, False)

	@GrssCshAmt.deleter
	def GrssCshAmt(self):
		del self._GrssCshAmt
		self._GrssCshAmt = base_types.UninitialisedField(self, 'GrssCshAmt', ActiveCurrencyAndAmount, False)

	@property
	def IndmntyAmt(self):
		return self._IndmntyAmt

	@IndmntyAmt.setter
	def IndmntyAmt(self, value):
		self._IndmntyAmt = value if value is not None else base_types.UninitialisedField(self, 'IndmntyAmt', ActiveCurrencyAndAmount, False)

	@IndmntyAmt.deleter
	def IndmntyAmt(self):
		del self._IndmntyAmt
		self._IndmntyAmt = base_types.UninitialisedField(self, 'IndmntyAmt', ActiveCurrencyAndAmount, False)

	@property
	def IntrstAmt(self):
		return self._IntrstAmt

	@IntrstAmt.setter
	def IntrstAmt(self, value):
		self._IntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstAmt', ActiveCurrencyAndAmount, False)

	@IntrstAmt.deleter
	def IntrstAmt(self):
		del self._IntrstAmt
		self._IntrstAmt = base_types.UninitialisedField(self, 'IntrstAmt', ActiveCurrencyAndAmount, False)

	@property
	def IsseDscntAmt(self):
		return self._IsseDscntAmt

	@IsseDscntAmt.setter
	def IsseDscntAmt(self, value):
		self._IsseDscntAmt = value if value is not None else base_types.UninitialisedField(self, 'IsseDscntAmt', ActiveCurrencyAndAmount, False)

	@IsseDscntAmt.deleter
	def IsseDscntAmt(self):
		del self._IsseDscntAmt
		self._IsseDscntAmt = base_types.UninitialisedField(self, 'IsseDscntAmt', ActiveCurrencyAndAmount, False)

	@property
	def LclBrkrComssnAmt(self):
		return self._LclBrkrComssnAmt

	@LclBrkrComssnAmt.setter
	def LclBrkrComssnAmt(self, value):
		self._LclBrkrComssnAmt = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssnAmt', ActiveCurrencyAndAmount, False)

	@LclBrkrComssnAmt.deleter
	def LclBrkrComssnAmt(self):
		del self._LclBrkrComssnAmt
		self._LclBrkrComssnAmt = base_types.UninitialisedField(self, 'LclBrkrComssnAmt', ActiveCurrencyAndAmount, False)

	@property
	def LclTaxAmt(self):
		return self._LclTaxAmt

	@LclTaxAmt.setter
	def LclTaxAmt(self, value):
		self._LclTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'LclTaxAmt', ActiveCurrencyAndAmount, False)

	@LclTaxAmt.deleter
	def LclTaxAmt(self):
		del self._LclTaxAmt
		self._LclTaxAmt = base_types.UninitialisedField(self, 'LclTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def ManfctrdDvddAmt(self):
		return self._ManfctrdDvddAmt

	@ManfctrdDvddAmt.setter
	def ManfctrdDvddAmt(self, value):
		self._ManfctrdDvddAmt = value if value is not None else base_types.UninitialisedField(self, 'ManfctrdDvddAmt', ActiveCurrencyAndAmount, False)

	@ManfctrdDvddAmt.deleter
	def ManfctrdDvddAmt(self):
		del self._ManfctrdDvddAmt
		self._ManfctrdDvddAmt = base_types.UninitialisedField(self, 'ManfctrdDvddAmt', ActiveCurrencyAndAmount, False)

	@property
	def MktClmAmt(self):
		return self._MktClmAmt

	@MktClmAmt.setter
	def MktClmAmt(self, value):
		self._MktClmAmt = value if value is not None else base_types.UninitialisedField(self, 'MktClmAmt', ActiveCurrencyAndAmount, False)

	@MktClmAmt.deleter
	def MktClmAmt(self):
		del self._MktClmAmt
		self._MktClmAmt = base_types.UninitialisedField(self, 'MktClmAmt', ActiveCurrencyAndAmount, False)

	@property
	def NetCshAmt(self):
		return self._NetCshAmt

	@NetCshAmt.setter
	def NetCshAmt(self, value):
		self._NetCshAmt = value if value is not None else base_types.UninitialisedField(self, 'NetCshAmt', ActiveCurrencyAndAmount, False)

	@NetCshAmt.deleter
	def NetCshAmt(self):
		del self._NetCshAmt
		self._NetCshAmt = base_types.UninitialisedField(self, 'NetCshAmt', ActiveCurrencyAndAmount, False)

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@property
	def PmtLevyTaxAmt(self):
		return self._PmtLevyTaxAmt

	@PmtLevyTaxAmt.setter
	def PmtLevyTaxAmt(self, value):
		self._PmtLevyTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'PmtLevyTaxAmt', ActiveCurrencyAndAmount, False)

	@PmtLevyTaxAmt.deleter
	def PmtLevyTaxAmt(self):
		del self._PmtLevyTaxAmt
		self._PmtLevyTaxAmt = base_types.UninitialisedField(self, 'PmtLevyTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def PngAgtComssnAmt(self):
		return self._PngAgtComssnAmt

	@PngAgtComssnAmt.setter
	def PngAgtComssnAmt(self, value):
		self._PngAgtComssnAmt = value if value is not None else base_types.UninitialisedField(self, 'PngAgtComssnAmt', ActiveCurrencyAndAmount, False)

	@PngAgtComssnAmt.deleter
	def PngAgtComssnAmt(self):
		del self._PngAgtComssnAmt
		self._PngAgtComssnAmt = base_types.UninitialisedField(self, 'PngAgtComssnAmt', ActiveCurrencyAndAmount, False)

	@property
	def PrncplOrCrps(self):
		return self._PrncplOrCrps

	@PrncplOrCrps.setter
	def PrncplOrCrps(self, value):
		self._PrncplOrCrps = value if value is not None else base_types.UninitialisedField(self, 'PrncplOrCrps', ActiveCurrencyAndAmount, False)

	@PrncplOrCrps.deleter
	def PrncplOrCrps(self):
		del self._PrncplOrCrps
		self._PrncplOrCrps = base_types.UninitialisedField(self, 'PrncplOrCrps', ActiveCurrencyAndAmount, False)

	@property
	def PstgFeeAmt(self):
		return self._PstgFeeAmt

	@PstgFeeAmt.setter
	def PstgFeeAmt(self, value):
		self._PstgFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'PstgFeeAmt', ActiveCurrencyAndAmount, False)

	@PstgFeeAmt.deleter
	def PstgFeeAmt(self):
		del self._PstgFeeAmt
		self._PstgFeeAmt = base_types.UninitialisedField(self, 'PstgFeeAmt', ActiveCurrencyAndAmount, False)

	@property
	def RedPrmAmt(self):
		return self._RedPrmAmt

	@RedPrmAmt.setter
	def RedPrmAmt(self, value):
		self._RedPrmAmt = value if value is not None else base_types.UninitialisedField(self, 'RedPrmAmt', ActiveCurrencyAndAmount, False)

	@RedPrmAmt.deleter
	def RedPrmAmt(self):
		del self._RedPrmAmt
		self._RedPrmAmt = base_types.UninitialisedField(self, 'RedPrmAmt', ActiveCurrencyAndAmount, False)

	@property
	def RgltryFeesAmt(self):
		return self._RgltryFeesAmt

	@RgltryFeesAmt.setter
	def RgltryFeesAmt(self, value):
		self._RgltryFeesAmt = value if value is not None else base_types.UninitialisedField(self, 'RgltryFeesAmt', ActiveCurrencyAndAmount, False)

	@RgltryFeesAmt.deleter
	def RgltryFeesAmt(self):
		del self._RgltryFeesAmt
		self._RgltryFeesAmt = base_types.UninitialisedField(self, 'RgltryFeesAmt', ActiveCurrencyAndAmount, False)

	@property
	def RinvstmtAmt(self):
		return self._RinvstmtAmt

	@RinvstmtAmt.setter
	def RinvstmtAmt(self, value):
		self._RinvstmtAmt = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtAmt', ActiveCurrencyAndAmount, False)

	@RinvstmtAmt.deleter
	def RinvstmtAmt(self):
		del self._RinvstmtAmt
		self._RinvstmtAmt = base_types.UninitialisedField(self, 'RinvstmtAmt', ActiveCurrencyAndAmount, False)

	@property
	def ShppgFeesAmt(self):
		return self._ShppgFeesAmt

	@ShppgFeesAmt.setter
	def ShppgFeesAmt(self, value):
		self._ShppgFeesAmt = value if value is not None else base_types.UninitialisedField(self, 'ShppgFeesAmt', ActiveCurrencyAndAmount, False)

	@ShppgFeesAmt.deleter
	def ShppgFeesAmt(self):
		del self._ShppgFeesAmt
		self._ShppgFeesAmt = base_types.UninitialisedField(self, 'ShppgFeesAmt', ActiveCurrencyAndAmount, False)

	@property
	def SlctnFees(self):
		return self._SlctnFees

	@SlctnFees.setter
	def SlctnFees(self, value):
		self._SlctnFees = value if value is not None else base_types.UninitialisedField(self, 'SlctnFees', ActiveCurrencyAndAmount, False)

	@SlctnFees.deleter
	def SlctnFees(self):
		del self._SlctnFees
		self._SlctnFees = base_types.UninitialisedField(self, 'SlctnFees', ActiveCurrencyAndAmount, False)

	@property
	def SndryOrOthrAmt(self):
		return self._SndryOrOthrAmt

	@SndryOrOthrAmt.setter
	def SndryOrOthrAmt(self, value):
		self._SndryOrOthrAmt = value if value is not None else base_types.UninitialisedField(self, 'SndryOrOthrAmt', ActiveCurrencyAndAmount, False)

	@SndryOrOthrAmt.deleter
	def SndryOrOthrAmt(self):
		del self._SndryOrOthrAmt
		self._SndryOrOthrAmt = base_types.UninitialisedField(self, 'SndryOrOthrAmt', ActiveCurrencyAndAmount, False)

	@property
	def SpclCncssnAmt(self):
		return self._SpclCncssnAmt

	@SpclCncssnAmt.setter
	def SpclCncssnAmt(self, value):
		self._SpclCncssnAmt = value if value is not None else base_types.UninitialisedField(self, 'SpclCncssnAmt', ActiveCurrencyAndAmount, False)

	@SpclCncssnAmt.deleter
	def SpclCncssnAmt(self):
		del self._SpclCncssnAmt
		self._SpclCncssnAmt = base_types.UninitialisedField(self, 'SpclCncssnAmt', ActiveCurrencyAndAmount, False)

	@property
	def StmpDtyAmt(self):
		return self._StmpDtyAmt

	@StmpDtyAmt.setter
	def StmpDtyAmt(self, value):
		self._StmpDtyAmt = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyAmt', ActiveCurrencyAndAmount, False)

	@StmpDtyAmt.deleter
	def StmpDtyAmt(self):
		del self._StmpDtyAmt
		self._StmpDtyAmt = base_types.UninitialisedField(self, 'StmpDtyAmt', ActiveCurrencyAndAmount, False)

	@property
	def StockXchgTaxAmt(self):
		return self._StockXchgTaxAmt

	@StockXchgTaxAmt.setter
	def StockXchgTaxAmt(self, value):
		self._StockXchgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'StockXchgTaxAmt', ActiveCurrencyAndAmount, False)

	@StockXchgTaxAmt.deleter
	def StockXchgTaxAmt(self):
		del self._StockXchgTaxAmt
		self._StockXchgTaxAmt = base_types.UninitialisedField(self, 'StockXchgTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def TaxCdtAmt(self):
		return self._TaxCdtAmt

	@TaxCdtAmt.setter
	def TaxCdtAmt(self, value):
		self._TaxCdtAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtAmt', ActiveCurrencyAndAmount, False)

	@TaxCdtAmt.deleter
	def TaxCdtAmt(self):
		del self._TaxCdtAmt
		self._TaxCdtAmt = base_types.UninitialisedField(self, 'TaxCdtAmt', ActiveCurrencyAndAmount, False)

	@property
	def TaxDfrrdAmt(self):
		return self._TaxDfrrdAmt

	@TaxDfrrdAmt.setter
	def TaxDfrrdAmt(self, value):
		self._TaxDfrrdAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxDfrrdAmt', ActiveCurrencyAndAmount, False)

	@TaxDfrrdAmt.deleter
	def TaxDfrrdAmt(self):
		del self._TaxDfrrdAmt
		self._TaxDfrrdAmt = base_types.UninitialisedField(self, 'TaxDfrrdAmt', ActiveCurrencyAndAmount, False)

	@property
	def TaxFreeAmt(self):
		return self._TaxFreeAmt

	@TaxFreeAmt.setter
	def TaxFreeAmt(self, value):
		self._TaxFreeAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxFreeAmt', ActiveCurrencyAndAmount, False)

	@TaxFreeAmt.deleter
	def TaxFreeAmt(self):
		del self._TaxFreeAmt
		self._TaxFreeAmt = base_types.UninitialisedField(self, 'TaxFreeAmt', ActiveCurrencyAndAmount, False)

	@property
	def TaxRclmAmt(self):
		return self._TaxRclmAmt

	@TaxRclmAmt.setter
	def TaxRclmAmt(self, value):
		self._TaxRclmAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmAmt', ActiveCurrencyAndAmount, False)

	@TaxRclmAmt.deleter
	def TaxRclmAmt(self):
		del self._TaxRclmAmt
		self._TaxRclmAmt = base_types.UninitialisedField(self, 'TaxRclmAmt', ActiveCurrencyAndAmount, False)

	@property
	def TrfTaxAmt(self):
		return self._TrfTaxAmt

	@TrfTaxAmt.setter
	def TrfTaxAmt(self, value):
		self._TrfTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TrfTaxAmt', ActiveCurrencyAndAmount, False)

	@TrfTaxAmt.deleter
	def TrfTaxAmt(self):
		del self._TrfTaxAmt
		self._TrfTaxAmt = base_types.UninitialisedField(self, 'TrfTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def TxTaxAmt(self):
		return self._TxTaxAmt

	@TxTaxAmt.setter
	def TxTaxAmt(self, value):
		self._TxTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TxTaxAmt', ActiveCurrencyAndAmount, False)

	@TxTaxAmt.deleter
	def TxTaxAmt(self):
		del self._TxTaxAmt
		self._TxTaxAmt = base_types.UninitialisedField(self, 'TxTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def UfrnkdAmt(self):
		return self._UfrnkdAmt

	@UfrnkdAmt.setter
	def UfrnkdAmt(self, value):
		self._UfrnkdAmt = value if value is not None else base_types.UninitialisedField(self, 'UfrnkdAmt', ActiveCurrencyAndAmount, False)

	@UfrnkdAmt.deleter
	def UfrnkdAmt(self):
		del self._UfrnkdAmt
		self._UfrnkdAmt = base_types.UninitialisedField(self, 'UfrnkdAmt', ActiveCurrencyAndAmount, False)

	@property
	def ValAddedTaxAmt(self):
		return self._ValAddedTaxAmt

	@ValAddedTaxAmt.setter
	def ValAddedTaxAmt(self, value):
		self._ValAddedTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTaxAmt', ActiveCurrencyAndAmount, False)

	@ValAddedTaxAmt.deleter
	def ValAddedTaxAmt(self):
		del self._ValAddedTaxAmt
		self._ValAddedTaxAmt = base_types.UninitialisedField(self, 'ValAddedTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def WhldgOfFrgnTaxAmt(self):
		return self._WhldgOfFrgnTaxAmt

	@WhldgOfFrgnTaxAmt.setter
	def WhldgOfFrgnTaxAmt(self, value):
		self._WhldgOfFrgnTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgOfFrgnTaxAmt', ActiveCurrencyAndAmount, False)

	@WhldgOfFrgnTaxAmt.deleter
	def WhldgOfFrgnTaxAmt(self):
		del self._WhldgOfFrgnTaxAmt
		self._WhldgOfFrgnTaxAmt = base_types.UninitialisedField(self, 'WhldgOfFrgnTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def WhldgOfLclTaxAmt(self):
		return self._WhldgOfLclTaxAmt

	@WhldgOfLclTaxAmt.setter
	def WhldgOfLclTaxAmt(self, value):
		self._WhldgOfLclTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgOfLclTaxAmt', ActiveCurrencyAndAmount, False)

	@WhldgOfLclTaxAmt.deleter
	def WhldgOfLclTaxAmt(self):
		del self._WhldgOfLclTaxAmt
		self._WhldgOfLclTaxAmt = base_types.UninitialisedField(self, 'WhldgOfLclTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSbcptCost', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShr', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshIncntiv', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EURtntnTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmpAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax1Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax2Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax3Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax4Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndmntyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrdDvddAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgtComssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplOrCrps', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstgFeeAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPrmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryFeesAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgFeesAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndryOrOthrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDfrrdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfrnkdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfFrgnTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfLclTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))