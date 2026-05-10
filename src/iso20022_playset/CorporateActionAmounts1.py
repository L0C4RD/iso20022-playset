from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class CorporateActionAmounts1(base_types._BaseFieldType):

	__slots__ = ["_TrfTaxAmt", "_FullyFrnkdAmt", "_ShppgFeesAmt", "_CptlGn", "_WhldgTaxAmt", "_StmpDtyAmt", "_UfrnkdAmt", "_PstgFeeAmt", "_EURtntnTaxAmt", "_SpclCncssnAmt", "_TaxCdtAmt", "_RgltryFeesAmt", "_IsseDscntAmt", "_AddtlTaxAmt", "_RinvstmtAmt", "_PrncplOrCrps", "_GrmnLclTax3Amt", "_SlctnFees", "_MktClmAmt", "_SndryOrOthrAmt", "_CshIncntiv", "_CshInLieuOfShr", "_ManfctrdDvddAmt", "_IntrstAmt", "_LclBrkrComssnAmt", "_LclTaxAmt", "_RedPrmAmt", "_StockXchgTaxAmt", "_AddtlSbcptCost", "_PmtLevyTaxAmt", "_CtryNtlFdrlTaxAmt", "_NetCshAmt", "_WhldgOfLclTaxAmt", "_ExctgBrkrAmt", "_EntitldAmt", "_ChrgsAmt", "_WhldgOfFrgnTaxAmt", "_TaxRclmAmt", "_GrmnLclTax4Amt", "_ValAddedTaxAmt", "_PngAgtComssnAmt", "_GrmnLclTax1Amt", "_TaxDfrrdAmt", "_FsclStmpAmt", "_GrmnLclTax2Amt", "_IndmntyAmt", "_GrssCshAmt", "_TxTaxAmt", "_TaxFreeAmt", "_OrgnlAmt"]
	@property
	def TrfTaxAmt(self):
		return self._TrfTaxAmt

	@TrfTaxAmt.setter
	def TrfTaxAmt(self, value):
		self._TrfTaxAmt = value if type(value) != base_types.auto else self.make_default("TrfTaxAmt")

	@TrfTaxAmt.deleter
	def TrfTaxAmt(self):
		del self._TrfTaxAmt
		self._TrfTaxAmt = None

	@property
	def FullyFrnkdAmt(self):
		return self._FullyFrnkdAmt

	@FullyFrnkdAmt.setter
	def FullyFrnkdAmt(self, value):
		self._FullyFrnkdAmt = value if type(value) != base_types.auto else self.make_default("FullyFrnkdAmt")

	@FullyFrnkdAmt.deleter
	def FullyFrnkdAmt(self):
		del self._FullyFrnkdAmt
		self._FullyFrnkdAmt = None

	@property
	def ShppgFeesAmt(self):
		return self._ShppgFeesAmt

	@ShppgFeesAmt.setter
	def ShppgFeesAmt(self, value):
		self._ShppgFeesAmt = value if type(value) != base_types.auto else self.make_default("ShppgFeesAmt")

	@ShppgFeesAmt.deleter
	def ShppgFeesAmt(self):
		del self._ShppgFeesAmt
		self._ShppgFeesAmt = None

	@property
	def CptlGn(self):
		return self._CptlGn

	@CptlGn.setter
	def CptlGn(self, value):
		self._CptlGn = value if type(value) != base_types.auto else self.make_default("CptlGn")

	@CptlGn.deleter
	def CptlGn(self):
		del self._CptlGn
		self._CptlGn = None

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if type(value) != base_types.auto else self.make_default("WhldgTaxAmt")

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = None

	@property
	def StmpDtyAmt(self):
		return self._StmpDtyAmt

	@StmpDtyAmt.setter
	def StmpDtyAmt(self, value):
		self._StmpDtyAmt = value if type(value) != base_types.auto else self.make_default("StmpDtyAmt")

	@StmpDtyAmt.deleter
	def StmpDtyAmt(self):
		del self._StmpDtyAmt
		self._StmpDtyAmt = None

	@property
	def UfrnkdAmt(self):
		return self._UfrnkdAmt

	@UfrnkdAmt.setter
	def UfrnkdAmt(self, value):
		self._UfrnkdAmt = value if type(value) != base_types.auto else self.make_default("UfrnkdAmt")

	@UfrnkdAmt.deleter
	def UfrnkdAmt(self):
		del self._UfrnkdAmt
		self._UfrnkdAmt = None

	@property
	def PstgFeeAmt(self):
		return self._PstgFeeAmt

	@PstgFeeAmt.setter
	def PstgFeeAmt(self, value):
		self._PstgFeeAmt = value if type(value) != base_types.auto else self.make_default("PstgFeeAmt")

	@PstgFeeAmt.deleter
	def PstgFeeAmt(self):
		del self._PstgFeeAmt
		self._PstgFeeAmt = None

	@property
	def EURtntnTaxAmt(self):
		return self._EURtntnTaxAmt

	@EURtntnTaxAmt.setter
	def EURtntnTaxAmt(self, value):
		self._EURtntnTaxAmt = value if type(value) != base_types.auto else self.make_default("EURtntnTaxAmt")

	@EURtntnTaxAmt.deleter
	def EURtntnTaxAmt(self):
		del self._EURtntnTaxAmt
		self._EURtntnTaxAmt = None

	@property
	def SpclCncssnAmt(self):
		return self._SpclCncssnAmt

	@SpclCncssnAmt.setter
	def SpclCncssnAmt(self, value):
		self._SpclCncssnAmt = value if type(value) != base_types.auto else self.make_default("SpclCncssnAmt")

	@SpclCncssnAmt.deleter
	def SpclCncssnAmt(self):
		del self._SpclCncssnAmt
		self._SpclCncssnAmt = None

	@property
	def TaxCdtAmt(self):
		return self._TaxCdtAmt

	@TaxCdtAmt.setter
	def TaxCdtAmt(self, value):
		self._TaxCdtAmt = value if type(value) != base_types.auto else self.make_default("TaxCdtAmt")

	@TaxCdtAmt.deleter
	def TaxCdtAmt(self):
		del self._TaxCdtAmt
		self._TaxCdtAmt = None

	@property
	def RgltryFeesAmt(self):
		return self._RgltryFeesAmt

	@RgltryFeesAmt.setter
	def RgltryFeesAmt(self, value):
		self._RgltryFeesAmt = value if type(value) != base_types.auto else self.make_default("RgltryFeesAmt")

	@RgltryFeesAmt.deleter
	def RgltryFeesAmt(self):
		del self._RgltryFeesAmt
		self._RgltryFeesAmt = None

	@property
	def IsseDscntAmt(self):
		return self._IsseDscntAmt

	@IsseDscntAmt.setter
	def IsseDscntAmt(self, value):
		self._IsseDscntAmt = value if type(value) != base_types.auto else self.make_default("IsseDscntAmt")

	@IsseDscntAmt.deleter
	def IsseDscntAmt(self):
		del self._IsseDscntAmt
		self._IsseDscntAmt = None

	@property
	def AddtlTaxAmt(self):
		return self._AddtlTaxAmt

	@AddtlTaxAmt.setter
	def AddtlTaxAmt(self, value):
		self._AddtlTaxAmt = value if type(value) != base_types.auto else self.make_default("AddtlTaxAmt")

	@AddtlTaxAmt.deleter
	def AddtlTaxAmt(self):
		del self._AddtlTaxAmt
		self._AddtlTaxAmt = None

	@property
	def RinvstmtAmt(self):
		return self._RinvstmtAmt

	@RinvstmtAmt.setter
	def RinvstmtAmt(self, value):
		self._RinvstmtAmt = value if type(value) != base_types.auto else self.make_default("RinvstmtAmt")

	@RinvstmtAmt.deleter
	def RinvstmtAmt(self):
		del self._RinvstmtAmt
		self._RinvstmtAmt = None

	@property
	def PrncplOrCrps(self):
		return self._PrncplOrCrps

	@PrncplOrCrps.setter
	def PrncplOrCrps(self, value):
		self._PrncplOrCrps = value if type(value) != base_types.auto else self.make_default("PrncplOrCrps")

	@PrncplOrCrps.deleter
	def PrncplOrCrps(self):
		del self._PrncplOrCrps
		self._PrncplOrCrps = None

	@property
	def GrmnLclTax3Amt(self):
		return self._GrmnLclTax3Amt

	@GrmnLclTax3Amt.setter
	def GrmnLclTax3Amt(self, value):
		self._GrmnLclTax3Amt = value if type(value) != base_types.auto else self.make_default("GrmnLclTax3Amt")

	@GrmnLclTax3Amt.deleter
	def GrmnLclTax3Amt(self):
		del self._GrmnLclTax3Amt
		self._GrmnLclTax3Amt = None

	@property
	def SlctnFees(self):
		return self._SlctnFees

	@SlctnFees.setter
	def SlctnFees(self, value):
		self._SlctnFees = value if type(value) != base_types.auto else self.make_default("SlctnFees")

	@SlctnFees.deleter
	def SlctnFees(self):
		del self._SlctnFees
		self._SlctnFees = None

	@property
	def MktClmAmt(self):
		return self._MktClmAmt

	@MktClmAmt.setter
	def MktClmAmt(self, value):
		self._MktClmAmt = value if type(value) != base_types.auto else self.make_default("MktClmAmt")

	@MktClmAmt.deleter
	def MktClmAmt(self):
		del self._MktClmAmt
		self._MktClmAmt = None

	@property
	def SndryOrOthrAmt(self):
		return self._SndryOrOthrAmt

	@SndryOrOthrAmt.setter
	def SndryOrOthrAmt(self, value):
		self._SndryOrOthrAmt = value if type(value) != base_types.auto else self.make_default("SndryOrOthrAmt")

	@SndryOrOthrAmt.deleter
	def SndryOrOthrAmt(self):
		del self._SndryOrOthrAmt
		self._SndryOrOthrAmt = None

	@property
	def CshIncntiv(self):
		return self._CshIncntiv

	@CshIncntiv.setter
	def CshIncntiv(self, value):
		self._CshIncntiv = value if type(value) != base_types.auto else self.make_default("CshIncntiv")

	@CshIncntiv.deleter
	def CshIncntiv(self):
		del self._CshIncntiv
		self._CshIncntiv = None

	@property
	def CshInLieuOfShr(self):
		return self._CshInLieuOfShr

	@CshInLieuOfShr.setter
	def CshInLieuOfShr(self, value):
		self._CshInLieuOfShr = value if type(value) != base_types.auto else self.make_default("CshInLieuOfShr")

	@CshInLieuOfShr.deleter
	def CshInLieuOfShr(self):
		del self._CshInLieuOfShr
		self._CshInLieuOfShr = None

	@property
	def ManfctrdDvddAmt(self):
		return self._ManfctrdDvddAmt

	@ManfctrdDvddAmt.setter
	def ManfctrdDvddAmt(self, value):
		self._ManfctrdDvddAmt = value if type(value) != base_types.auto else self.make_default("ManfctrdDvddAmt")

	@ManfctrdDvddAmt.deleter
	def ManfctrdDvddAmt(self):
		del self._ManfctrdDvddAmt
		self._ManfctrdDvddAmt = None

	@property
	def IntrstAmt(self):
		return self._IntrstAmt

	@IntrstAmt.setter
	def IntrstAmt(self, value):
		self._IntrstAmt = value if type(value) != base_types.auto else self.make_default("IntrstAmt")

	@IntrstAmt.deleter
	def IntrstAmt(self):
		del self._IntrstAmt
		self._IntrstAmt = None

	@property
	def LclBrkrComssnAmt(self):
		return self._LclBrkrComssnAmt

	@LclBrkrComssnAmt.setter
	def LclBrkrComssnAmt(self, value):
		self._LclBrkrComssnAmt = value if type(value) != base_types.auto else self.make_default("LclBrkrComssnAmt")

	@LclBrkrComssnAmt.deleter
	def LclBrkrComssnAmt(self):
		del self._LclBrkrComssnAmt
		self._LclBrkrComssnAmt = None

	@property
	def LclTaxAmt(self):
		return self._LclTaxAmt

	@LclTaxAmt.setter
	def LclTaxAmt(self, value):
		self._LclTaxAmt = value if type(value) != base_types.auto else self.make_default("LclTaxAmt")

	@LclTaxAmt.deleter
	def LclTaxAmt(self):
		del self._LclTaxAmt
		self._LclTaxAmt = None

	@property
	def RedPrmAmt(self):
		return self._RedPrmAmt

	@RedPrmAmt.setter
	def RedPrmAmt(self, value):
		self._RedPrmAmt = value if type(value) != base_types.auto else self.make_default("RedPrmAmt")

	@RedPrmAmt.deleter
	def RedPrmAmt(self):
		del self._RedPrmAmt
		self._RedPrmAmt = None

	@property
	def StockXchgTaxAmt(self):
		return self._StockXchgTaxAmt

	@StockXchgTaxAmt.setter
	def StockXchgTaxAmt(self, value):
		self._StockXchgTaxAmt = value if type(value) != base_types.auto else self.make_default("StockXchgTaxAmt")

	@StockXchgTaxAmt.deleter
	def StockXchgTaxAmt(self):
		del self._StockXchgTaxAmt
		self._StockXchgTaxAmt = None

	@property
	def AddtlSbcptCost(self):
		return self._AddtlSbcptCost

	@AddtlSbcptCost.setter
	def AddtlSbcptCost(self, value):
		self._AddtlSbcptCost = value if type(value) != base_types.auto else self.make_default("AddtlSbcptCost")

	@AddtlSbcptCost.deleter
	def AddtlSbcptCost(self):
		del self._AddtlSbcptCost
		self._AddtlSbcptCost = None

	@property
	def PmtLevyTaxAmt(self):
		return self._PmtLevyTaxAmt

	@PmtLevyTaxAmt.setter
	def PmtLevyTaxAmt(self, value):
		self._PmtLevyTaxAmt = value if type(value) != base_types.auto else self.make_default("PmtLevyTaxAmt")

	@PmtLevyTaxAmt.deleter
	def PmtLevyTaxAmt(self):
		del self._PmtLevyTaxAmt
		self._PmtLevyTaxAmt = None

	@property
	def CtryNtlFdrlTaxAmt(self):
		return self._CtryNtlFdrlTaxAmt

	@CtryNtlFdrlTaxAmt.setter
	def CtryNtlFdrlTaxAmt(self, value):
		self._CtryNtlFdrlTaxAmt = value if type(value) != base_types.auto else self.make_default("CtryNtlFdrlTaxAmt")

	@CtryNtlFdrlTaxAmt.deleter
	def CtryNtlFdrlTaxAmt(self):
		del self._CtryNtlFdrlTaxAmt
		self._CtryNtlFdrlTaxAmt = None

	@property
	def NetCshAmt(self):
		return self._NetCshAmt

	@NetCshAmt.setter
	def NetCshAmt(self, value):
		self._NetCshAmt = value if type(value) != base_types.auto else self.make_default("NetCshAmt")

	@NetCshAmt.deleter
	def NetCshAmt(self):
		del self._NetCshAmt
		self._NetCshAmt = None

	@property
	def WhldgOfLclTaxAmt(self):
		return self._WhldgOfLclTaxAmt

	@WhldgOfLclTaxAmt.setter
	def WhldgOfLclTaxAmt(self, value):
		self._WhldgOfLclTaxAmt = value if type(value) != base_types.auto else self.make_default("WhldgOfLclTaxAmt")

	@WhldgOfLclTaxAmt.deleter
	def WhldgOfLclTaxAmt(self):
		del self._WhldgOfLclTaxAmt
		self._WhldgOfLclTaxAmt = None

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if type(value) != base_types.auto else self.make_default("ExctgBrkrAmt")

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = None

	@property
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if type(value) != base_types.auto else self.make_default("EntitldAmt")

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = None

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if type(value) != base_types.auto else self.make_default("ChrgsAmt")

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = None

	@property
	def WhldgOfFrgnTaxAmt(self):
		return self._WhldgOfFrgnTaxAmt

	@WhldgOfFrgnTaxAmt.setter
	def WhldgOfFrgnTaxAmt(self, value):
		self._WhldgOfFrgnTaxAmt = value if type(value) != base_types.auto else self.make_default("WhldgOfFrgnTaxAmt")

	@WhldgOfFrgnTaxAmt.deleter
	def WhldgOfFrgnTaxAmt(self):
		del self._WhldgOfFrgnTaxAmt
		self._WhldgOfFrgnTaxAmt = None

	@property
	def TaxRclmAmt(self):
		return self._TaxRclmAmt

	@TaxRclmAmt.setter
	def TaxRclmAmt(self, value):
		self._TaxRclmAmt = value if type(value) != base_types.auto else self.make_default("TaxRclmAmt")

	@TaxRclmAmt.deleter
	def TaxRclmAmt(self):
		del self._TaxRclmAmt
		self._TaxRclmAmt = None

	@property
	def GrmnLclTax4Amt(self):
		return self._GrmnLclTax4Amt

	@GrmnLclTax4Amt.setter
	def GrmnLclTax4Amt(self, value):
		self._GrmnLclTax4Amt = value if type(value) != base_types.auto else self.make_default("GrmnLclTax4Amt")

	@GrmnLclTax4Amt.deleter
	def GrmnLclTax4Amt(self):
		del self._GrmnLclTax4Amt
		self._GrmnLclTax4Amt = None

	@property
	def ValAddedTaxAmt(self):
		return self._ValAddedTaxAmt

	@ValAddedTaxAmt.setter
	def ValAddedTaxAmt(self, value):
		self._ValAddedTaxAmt = value if type(value) != base_types.auto else self.make_default("ValAddedTaxAmt")

	@ValAddedTaxAmt.deleter
	def ValAddedTaxAmt(self):
		del self._ValAddedTaxAmt
		self._ValAddedTaxAmt = None

	@property
	def PngAgtComssnAmt(self):
		return self._PngAgtComssnAmt

	@PngAgtComssnAmt.setter
	def PngAgtComssnAmt(self, value):
		self._PngAgtComssnAmt = value if type(value) != base_types.auto else self.make_default("PngAgtComssnAmt")

	@PngAgtComssnAmt.deleter
	def PngAgtComssnAmt(self):
		del self._PngAgtComssnAmt
		self._PngAgtComssnAmt = None

	@property
	def GrmnLclTax1Amt(self):
		return self._GrmnLclTax1Amt

	@GrmnLclTax1Amt.setter
	def GrmnLclTax1Amt(self, value):
		self._GrmnLclTax1Amt = value if type(value) != base_types.auto else self.make_default("GrmnLclTax1Amt")

	@GrmnLclTax1Amt.deleter
	def GrmnLclTax1Amt(self):
		del self._GrmnLclTax1Amt
		self._GrmnLclTax1Amt = None

	@property
	def TaxDfrrdAmt(self):
		return self._TaxDfrrdAmt

	@TaxDfrrdAmt.setter
	def TaxDfrrdAmt(self, value):
		self._TaxDfrrdAmt = value if type(value) != base_types.auto else self.make_default("TaxDfrrdAmt")

	@TaxDfrrdAmt.deleter
	def TaxDfrrdAmt(self):
		del self._TaxDfrrdAmt
		self._TaxDfrrdAmt = None

	@property
	def FsclStmpAmt(self):
		return self._FsclStmpAmt

	@FsclStmpAmt.setter
	def FsclStmpAmt(self, value):
		self._FsclStmpAmt = value if type(value) != base_types.auto else self.make_default("FsclStmpAmt")

	@FsclStmpAmt.deleter
	def FsclStmpAmt(self):
		del self._FsclStmpAmt
		self._FsclStmpAmt = None

	@property
	def GrmnLclTax2Amt(self):
		return self._GrmnLclTax2Amt

	@GrmnLclTax2Amt.setter
	def GrmnLclTax2Amt(self, value):
		self._GrmnLclTax2Amt = value if type(value) != base_types.auto else self.make_default("GrmnLclTax2Amt")

	@GrmnLclTax2Amt.deleter
	def GrmnLclTax2Amt(self):
		del self._GrmnLclTax2Amt
		self._GrmnLclTax2Amt = None

	@property
	def IndmntyAmt(self):
		return self._IndmntyAmt

	@IndmntyAmt.setter
	def IndmntyAmt(self, value):
		self._IndmntyAmt = value if type(value) != base_types.auto else self.make_default("IndmntyAmt")

	@IndmntyAmt.deleter
	def IndmntyAmt(self):
		del self._IndmntyAmt
		self._IndmntyAmt = None

	@property
	def GrssCshAmt(self):
		return self._GrssCshAmt

	@GrssCshAmt.setter
	def GrssCshAmt(self, value):
		self._GrssCshAmt = value if type(value) != base_types.auto else self.make_default("GrssCshAmt")

	@GrssCshAmt.deleter
	def GrssCshAmt(self):
		del self._GrssCshAmt
		self._GrssCshAmt = None

	@property
	def TxTaxAmt(self):
		return self._TxTaxAmt

	@TxTaxAmt.setter
	def TxTaxAmt(self, value):
		self._TxTaxAmt = value if type(value) != base_types.auto else self.make_default("TxTaxAmt")

	@TxTaxAmt.deleter
	def TxTaxAmt(self):
		del self._TxTaxAmt
		self._TxTaxAmt = None

	@property
	def TaxFreeAmt(self):
		return self._TaxFreeAmt

	@TaxFreeAmt.setter
	def TaxFreeAmt(self, value):
		self._TaxFreeAmt = value if type(value) != base_types.auto else self.make_default("TaxFreeAmt")

	@TaxFreeAmt.deleter
	def TaxFreeAmt(self):
		del self._TaxFreeAmt
		self._TaxFreeAmt = None

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if type(value) != base_types.auto else self.make_default("OrgnlAmt")

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrfTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgFeesAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfrnkdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstgFeeAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EURtntnTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryFeesAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplOrCrps', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax3Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndryOrOthrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshIncntiv', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShr', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrdDvddAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPrmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSbcptCost', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfLclTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfFrgnTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax4Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgtComssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax1Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDfrrdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmpAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax2Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndmntyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssCshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

