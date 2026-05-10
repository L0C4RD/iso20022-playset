from . import base_types
from .RestrictedFINActiveCurrencyAndAmount import RestrictedFINActiveCurrencyAndAmount

class CorporateActionAmounts76(base_types._BaseFieldType):

	__slots__ = ["_FsclStmpAmt", "_TaxOnIncmAmt", "_PngAgtComssnAmt", "_IncmPrtn", "_ExctgBrkrAmt", "_LclBrkrComssnAmt", "_DmdRyltsAmt", "_WhldgTaxAmt", "_GrssAmt", "_TaxFreeAmt", "_EqulstnAmt", "_TxTax", "_ManfctrdDvddPmtAmt", "_RinvstmtAmt", "_RgltryFeesAmt", "_ShppgFeesAmt", "_TaxRclmAmt", "_IntrstAmt", "_DmdFndAmt", "_BuyUpAmt", "_TaxDfrrdAmt", "_IndmntyAmt", "_FrgnIncmAmt", "_DmdDvddAmt", "_ScndLvlTaxAmt", "_DmdIntrstAmt", "_SlctnFees", "_CptlGn", "_DmdAmt", "_PrncplOrCrps", "_SndryOrOthrAmt", "_OrgnlAmt", "_FullyFrnkdAmt", "_FATCATaxAmt", "_NetAmt", "_ChrgsAmt", "_RedPrmAmt", "_AcrdIntrstAmt", "_UfrnkdAmt", "_CshInLieuOfShr", "_AddtlTaxAmt", "_EUTaxRtntnAmt", "_TaxCdtAmt", "_StockXchgTax", "_ValAddedTaxAmt", "_BckUpWhldgTaxAmt", "_NRATaxAmt", "_StmpDtyAmt", "_EntitldAmt"]
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
	def TaxOnIncmAmt(self):
		return self._TaxOnIncmAmt

	@TaxOnIncmAmt.setter
	def TaxOnIncmAmt(self, value):
		self._TaxOnIncmAmt = value if type(value) != base_types.auto else self.make_default("TaxOnIncmAmt")

	@TaxOnIncmAmt.deleter
	def TaxOnIncmAmt(self):
		del self._TaxOnIncmAmt
		self._TaxOnIncmAmt = None

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
	def IncmPrtn(self):
		return self._IncmPrtn

	@IncmPrtn.setter
	def IncmPrtn(self, value):
		self._IncmPrtn = value if type(value) != base_types.auto else self.make_default("IncmPrtn")

	@IncmPrtn.deleter
	def IncmPrtn(self):
		del self._IncmPrtn
		self._IncmPrtn = None

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
	def DmdRyltsAmt(self):
		return self._DmdRyltsAmt

	@DmdRyltsAmt.setter
	def DmdRyltsAmt(self, value):
		self._DmdRyltsAmt = value if type(value) != base_types.auto else self.make_default("DmdRyltsAmt")

	@DmdRyltsAmt.deleter
	def DmdRyltsAmt(self):
		del self._DmdRyltsAmt
		self._DmdRyltsAmt = None

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
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

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
	def EqulstnAmt(self):
		return self._EqulstnAmt

	@EqulstnAmt.setter
	def EqulstnAmt(self, value):
		self._EqulstnAmt = value if type(value) != base_types.auto else self.make_default("EqulstnAmt")

	@EqulstnAmt.deleter
	def EqulstnAmt(self):
		del self._EqulstnAmt
		self._EqulstnAmt = None

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if type(value) != base_types.auto else self.make_default("TxTax")

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = None

	@property
	def ManfctrdDvddPmtAmt(self):
		return self._ManfctrdDvddPmtAmt

	@ManfctrdDvddPmtAmt.setter
	def ManfctrdDvddPmtAmt(self, value):
		self._ManfctrdDvddPmtAmt = value if type(value) != base_types.auto else self.make_default("ManfctrdDvddPmtAmt")

	@ManfctrdDvddPmtAmt.deleter
	def ManfctrdDvddPmtAmt(self):
		del self._ManfctrdDvddPmtAmt
		self._ManfctrdDvddPmtAmt = None

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
	def DmdFndAmt(self):
		return self._DmdFndAmt

	@DmdFndAmt.setter
	def DmdFndAmt(self, value):
		self._DmdFndAmt = value if type(value) != base_types.auto else self.make_default("DmdFndAmt")

	@DmdFndAmt.deleter
	def DmdFndAmt(self):
		del self._DmdFndAmt
		self._DmdFndAmt = None

	@property
	def BuyUpAmt(self):
		return self._BuyUpAmt

	@BuyUpAmt.setter
	def BuyUpAmt(self, value):
		self._BuyUpAmt = value if type(value) != base_types.auto else self.make_default("BuyUpAmt")

	@BuyUpAmt.deleter
	def BuyUpAmt(self):
		del self._BuyUpAmt
		self._BuyUpAmt = None

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
	def FrgnIncmAmt(self):
		return self._FrgnIncmAmt

	@FrgnIncmAmt.setter
	def FrgnIncmAmt(self, value):
		self._FrgnIncmAmt = value if type(value) != base_types.auto else self.make_default("FrgnIncmAmt")

	@FrgnIncmAmt.deleter
	def FrgnIncmAmt(self):
		del self._FrgnIncmAmt
		self._FrgnIncmAmt = None

	@property
	def DmdDvddAmt(self):
		return self._DmdDvddAmt

	@DmdDvddAmt.setter
	def DmdDvddAmt(self, value):
		self._DmdDvddAmt = value if type(value) != base_types.auto else self.make_default("DmdDvddAmt")

	@DmdDvddAmt.deleter
	def DmdDvddAmt(self):
		del self._DmdDvddAmt
		self._DmdDvddAmt = None

	@property
	def ScndLvlTaxAmt(self):
		return self._ScndLvlTaxAmt

	@ScndLvlTaxAmt.setter
	def ScndLvlTaxAmt(self, value):
		self._ScndLvlTaxAmt = value if type(value) != base_types.auto else self.make_default("ScndLvlTaxAmt")

	@ScndLvlTaxAmt.deleter
	def ScndLvlTaxAmt(self):
		del self._ScndLvlTaxAmt
		self._ScndLvlTaxAmt = None

	@property
	def DmdIntrstAmt(self):
		return self._DmdIntrstAmt

	@DmdIntrstAmt.setter
	def DmdIntrstAmt(self, value):
		self._DmdIntrstAmt = value if type(value) != base_types.auto else self.make_default("DmdIntrstAmt")

	@DmdIntrstAmt.deleter
	def DmdIntrstAmt(self):
		del self._DmdIntrstAmt
		self._DmdIntrstAmt = None

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
	def DmdAmt(self):
		return self._DmdAmt

	@DmdAmt.setter
	def DmdAmt(self, value):
		self._DmdAmt = value if type(value) != base_types.auto else self.make_default("DmdAmt")

	@DmdAmt.deleter
	def DmdAmt(self):
		del self._DmdAmt
		self._DmdAmt = None

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
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if type(value) != base_types.auto else self.make_default("OrgnlAmt")

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = None

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
	def FATCATaxAmt(self):
		return self._FATCATaxAmt

	@FATCATaxAmt.setter
	def FATCATaxAmt(self, value):
		self._FATCATaxAmt = value if type(value) != base_types.auto else self.make_default("FATCATaxAmt")

	@FATCATaxAmt.deleter
	def FATCATaxAmt(self):
		del self._FATCATaxAmt
		self._FATCATaxAmt = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

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
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

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
	def EUTaxRtntnAmt(self):
		return self._EUTaxRtntnAmt

	@EUTaxRtntnAmt.setter
	def EUTaxRtntnAmt(self, value):
		self._EUTaxRtntnAmt = value if type(value) != base_types.auto else self.make_default("EUTaxRtntnAmt")

	@EUTaxRtntnAmt.deleter
	def EUTaxRtntnAmt(self):
		del self._EUTaxRtntnAmt
		self._EUTaxRtntnAmt = None

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
	def StockXchgTax(self):
		return self._StockXchgTax

	@StockXchgTax.setter
	def StockXchgTax(self, value):
		self._StockXchgTax = value if type(value) != base_types.auto else self.make_default("StockXchgTax")

	@StockXchgTax.deleter
	def StockXchgTax(self):
		del self._StockXchgTax
		self._StockXchgTax = None

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
	def BckUpWhldgTaxAmt(self):
		return self._BckUpWhldgTaxAmt

	@BckUpWhldgTaxAmt.setter
	def BckUpWhldgTaxAmt(self, value):
		self._BckUpWhldgTaxAmt = value if type(value) != base_types.auto else self.make_default("BckUpWhldgTaxAmt")

	@BckUpWhldgTaxAmt.deleter
	def BckUpWhldgTaxAmt(self):
		del self._BckUpWhldgTaxAmt
		self._BckUpWhldgTaxAmt = None

	@property
	def NRATaxAmt(self):
		return self._NRATaxAmt

	@NRATaxAmt.setter
	def NRATaxAmt(self, value):
		self._NRATaxAmt = value if type(value) != base_types.auto else self.make_default("NRATaxAmt")

	@NRATaxAmt.deleter
	def NRATaxAmt(self):
		del self._NRATaxAmt
		self._NRATaxAmt = None

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
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if type(value) != base_types.auto else self.make_default("EntitldAmt")

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FsclStmpAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgtComssnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPrtn', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdRyltsAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrdDvddPmtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryFeesAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgFeesAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdFndAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyUpAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDfrrdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndmntyAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrgnIncmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdDvddAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdIntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFees', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGn', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplOrCrps', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndryOrOthrAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FATCATaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPrmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfrnkdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShr', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EUTaxRtntnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckUpWhldgTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NRATaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

