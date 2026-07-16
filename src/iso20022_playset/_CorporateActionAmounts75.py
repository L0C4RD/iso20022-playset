# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINActiveCurrencyAndAmount

class CorporateActionAmounts75(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AddtlTaxAmt", "_BckUpWhldgTaxAmt", "_BuyUpAmt", "_ChrgsAmt", "_CptlGn", "_CshInLieuOfShr", "_DmdAmt", "_DmdDvddAmt", "_DmdFndAmt", "_DmdIntrstAmt", "_DmdRyltsAmt", "_EntitldAmt", "_EqulstnAmt", "_ExctgBrkrAmt", "_FATCATaxAmt", "_FrgnIncmAmt", "_FsclStmpAmt", "_FullyFrnkdAmt", "_GrssAmt", "_IncmPrtn", "_IndmntyAmt", "_IntrstAmt", "_LclBrkrComssnAmt", "_ManfctrdDvddPmtAmt", "_MktClmAmt", "_NRATaxAmt", "_NetAmt", "_OrgnlAmt", "_PngAgtComssnAmt", "_RgltryFeesAmt", "_RinvstmtAmt", "_ScndLvlTaxAmt", "_ShppgFeesAmt", "_SlctnFees", "_SndryOrOthrAmt", "_StmpDtyAmt", "_TaxCdtAmt", "_TaxDfrrdAmt", "_TaxFreeAmt", "_TaxOnIncmAmt", "_TaxRclmAmt", "_TxTax", "_UfrnkdAmt", "_ValAddedTaxAmt", "_WhldgTaxAmt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def AddtlTaxAmt(self):
		return self._AddtlTaxAmt

	@AddtlTaxAmt.setter
	def AddtlTaxAmt(self, value):
		self._AddtlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@AddtlTaxAmt.deleter
	def AddtlTaxAmt(self):
		del self._AddtlTaxAmt
		self._AddtlTaxAmt = base_types.UninitialisedField(self, 'AddtlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def BckUpWhldgTaxAmt(self):
		return self._BckUpWhldgTaxAmt

	@BckUpWhldgTaxAmt.setter
	def BckUpWhldgTaxAmt(self, value):
		self._BckUpWhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'BckUpWhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@BckUpWhldgTaxAmt.deleter
	def BckUpWhldgTaxAmt(self):
		del self._BckUpWhldgTaxAmt
		self._BckUpWhldgTaxAmt = base_types.UninitialisedField(self, 'BckUpWhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def BuyUpAmt(self):
		return self._BuyUpAmt

	@BuyUpAmt.setter
	def BuyUpAmt(self, value):
		self._BuyUpAmt = value if value is not None else base_types.UninitialisedField(self, 'BuyUpAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@BuyUpAmt.deleter
	def BuyUpAmt(self):
		del self._BuyUpAmt
		self._BuyUpAmt = base_types.UninitialisedField(self, 'BuyUpAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = base_types.UninitialisedField(self, 'ChrgsAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def CptlGn(self):
		return self._CptlGn

	@CptlGn.setter
	def CptlGn(self, value):
		self._CptlGn = value if value is not None else base_types.UninitialisedField(self, 'CptlGn', RestrictedFINActiveCurrencyAndAmount, False)

	@CptlGn.deleter
	def CptlGn(self):
		del self._CptlGn
		self._CptlGn = base_types.UninitialisedField(self, 'CptlGn', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def CshInLieuOfShr(self):
		return self._CshInLieuOfShr

	@CshInLieuOfShr.setter
	def CshInLieuOfShr(self, value):
		self._CshInLieuOfShr = value if value is not None else base_types.UninitialisedField(self, 'CshInLieuOfShr', RestrictedFINActiveCurrencyAndAmount, False)

	@CshInLieuOfShr.deleter
	def CshInLieuOfShr(self):
		del self._CshInLieuOfShr
		self._CshInLieuOfShr = base_types.UninitialisedField(self, 'CshInLieuOfShr', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def DmdAmt(self):
		return self._DmdAmt

	@DmdAmt.setter
	def DmdAmt(self, value):
		self._DmdAmt = value if value is not None else base_types.UninitialisedField(self, 'DmdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@DmdAmt.deleter
	def DmdAmt(self):
		del self._DmdAmt
		self._DmdAmt = base_types.UninitialisedField(self, 'DmdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def DmdDvddAmt(self):
		return self._DmdDvddAmt

	@DmdDvddAmt.setter
	def DmdDvddAmt(self, value):
		self._DmdDvddAmt = value if value is not None else base_types.UninitialisedField(self, 'DmdDvddAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@DmdDvddAmt.deleter
	def DmdDvddAmt(self):
		del self._DmdDvddAmt
		self._DmdDvddAmt = base_types.UninitialisedField(self, 'DmdDvddAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def DmdFndAmt(self):
		return self._DmdFndAmt

	@DmdFndAmt.setter
	def DmdFndAmt(self, value):
		self._DmdFndAmt = value if value is not None else base_types.UninitialisedField(self, 'DmdFndAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@DmdFndAmt.deleter
	def DmdFndAmt(self):
		del self._DmdFndAmt
		self._DmdFndAmt = base_types.UninitialisedField(self, 'DmdFndAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def DmdIntrstAmt(self):
		return self._DmdIntrstAmt

	@DmdIntrstAmt.setter
	def DmdIntrstAmt(self, value):
		self._DmdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'DmdIntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@DmdIntrstAmt.deleter
	def DmdIntrstAmt(self):
		del self._DmdIntrstAmt
		self._DmdIntrstAmt = base_types.UninitialisedField(self, 'DmdIntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def DmdRyltsAmt(self):
		return self._DmdRyltsAmt

	@DmdRyltsAmt.setter
	def DmdRyltsAmt(self, value):
		self._DmdRyltsAmt = value if value is not None else base_types.UninitialisedField(self, 'DmdRyltsAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@DmdRyltsAmt.deleter
	def DmdRyltsAmt(self):
		del self._DmdRyltsAmt
		self._DmdRyltsAmt = base_types.UninitialisedField(self, 'DmdRyltsAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def EntitldAmt(self):
		return self._EntitldAmt

	@EntitldAmt.setter
	def EntitldAmt(self, value):
		self._EntitldAmt = value if value is not None else base_types.UninitialisedField(self, 'EntitldAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@EntitldAmt.deleter
	def EntitldAmt(self):
		del self._EntitldAmt
		self._EntitldAmt = base_types.UninitialisedField(self, 'EntitldAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def EqulstnAmt(self):
		return self._EqulstnAmt

	@EqulstnAmt.setter
	def EqulstnAmt(self, value):
		self._EqulstnAmt = value if value is not None else base_types.UninitialisedField(self, 'EqulstnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@EqulstnAmt.deleter
	def EqulstnAmt(self):
		del self._EqulstnAmt
		self._EqulstnAmt = base_types.UninitialisedField(self, 'EqulstnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def FATCATaxAmt(self):
		return self._FATCATaxAmt

	@FATCATaxAmt.setter
	def FATCATaxAmt(self, value):
		self._FATCATaxAmt = value if value is not None else base_types.UninitialisedField(self, 'FATCATaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@FATCATaxAmt.deleter
	def FATCATaxAmt(self):
		del self._FATCATaxAmt
		self._FATCATaxAmt = base_types.UninitialisedField(self, 'FATCATaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def FrgnIncmAmt(self):
		return self._FrgnIncmAmt

	@FrgnIncmAmt.setter
	def FrgnIncmAmt(self, value):
		self._FrgnIncmAmt = value if value is not None else base_types.UninitialisedField(self, 'FrgnIncmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@FrgnIncmAmt.deleter
	def FrgnIncmAmt(self):
		del self._FrgnIncmAmt
		self._FrgnIncmAmt = base_types.UninitialisedField(self, 'FrgnIncmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def FsclStmpAmt(self):
		return self._FsclStmpAmt

	@FsclStmpAmt.setter
	def FsclStmpAmt(self, value):
		self._FsclStmpAmt = value if value is not None else base_types.UninitialisedField(self, 'FsclStmpAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@FsclStmpAmt.deleter
	def FsclStmpAmt(self):
		del self._FsclStmpAmt
		self._FsclStmpAmt = base_types.UninitialisedField(self, 'FsclStmpAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def FullyFrnkdAmt(self):
		return self._FullyFrnkdAmt

	@FullyFrnkdAmt.setter
	def FullyFrnkdAmt(self, value):
		self._FullyFrnkdAmt = value if value is not None else base_types.UninitialisedField(self, 'FullyFrnkdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@FullyFrnkdAmt.deleter
	def FullyFrnkdAmt(self):
		del self._FullyFrnkdAmt
		self._FullyFrnkdAmt = base_types.UninitialisedField(self, 'FullyFrnkdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = base_types.UninitialisedField(self, 'GrssAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def IncmPrtn(self):
		return self._IncmPrtn

	@IncmPrtn.setter
	def IncmPrtn(self, value):
		self._IncmPrtn = value if value is not None else base_types.UninitialisedField(self, 'IncmPrtn', RestrictedFINActiveCurrencyAndAmount, False)

	@IncmPrtn.deleter
	def IncmPrtn(self):
		del self._IncmPrtn
		self._IncmPrtn = base_types.UninitialisedField(self, 'IncmPrtn', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def IndmntyAmt(self):
		return self._IndmntyAmt

	@IndmntyAmt.setter
	def IndmntyAmt(self, value):
		self._IndmntyAmt = value if value is not None else base_types.UninitialisedField(self, 'IndmntyAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@IndmntyAmt.deleter
	def IndmntyAmt(self):
		del self._IndmntyAmt
		self._IndmntyAmt = base_types.UninitialisedField(self, 'IndmntyAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def IntrstAmt(self):
		return self._IntrstAmt

	@IntrstAmt.setter
	def IntrstAmt(self, value):
		self._IntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@IntrstAmt.deleter
	def IntrstAmt(self):
		del self._IntrstAmt
		self._IntrstAmt = base_types.UninitialisedField(self, 'IntrstAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def LclBrkrComssnAmt(self):
		return self._LclBrkrComssnAmt

	@LclBrkrComssnAmt.setter
	def LclBrkrComssnAmt(self, value):
		self._LclBrkrComssnAmt = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@LclBrkrComssnAmt.deleter
	def LclBrkrComssnAmt(self):
		del self._LclBrkrComssnAmt
		self._LclBrkrComssnAmt = base_types.UninitialisedField(self, 'LclBrkrComssnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ManfctrdDvddPmtAmt(self):
		return self._ManfctrdDvddPmtAmt

	@ManfctrdDvddPmtAmt.setter
	def ManfctrdDvddPmtAmt(self, value):
		self._ManfctrdDvddPmtAmt = value if value is not None else base_types.UninitialisedField(self, 'ManfctrdDvddPmtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ManfctrdDvddPmtAmt.deleter
	def ManfctrdDvddPmtAmt(self):
		del self._ManfctrdDvddPmtAmt
		self._ManfctrdDvddPmtAmt = base_types.UninitialisedField(self, 'ManfctrdDvddPmtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def MktClmAmt(self):
		return self._MktClmAmt

	@MktClmAmt.setter
	def MktClmAmt(self, value):
		self._MktClmAmt = value if value is not None else base_types.UninitialisedField(self, 'MktClmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@MktClmAmt.deleter
	def MktClmAmt(self):
		del self._MktClmAmt
		self._MktClmAmt = base_types.UninitialisedField(self, 'MktClmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def NRATaxAmt(self):
		return self._NRATaxAmt

	@NRATaxAmt.setter
	def NRATaxAmt(self, value):
		self._NRATaxAmt = value if value is not None else base_types.UninitialisedField(self, 'NRATaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@NRATaxAmt.deleter
	def NRATaxAmt(self):
		del self._NRATaxAmt
		self._NRATaxAmt = base_types.UninitialisedField(self, 'NRATaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = base_types.UninitialisedField(self, 'OrgnlAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def PngAgtComssnAmt(self):
		return self._PngAgtComssnAmt

	@PngAgtComssnAmt.setter
	def PngAgtComssnAmt(self, value):
		self._PngAgtComssnAmt = value if value is not None else base_types.UninitialisedField(self, 'PngAgtComssnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@PngAgtComssnAmt.deleter
	def PngAgtComssnAmt(self):
		del self._PngAgtComssnAmt
		self._PngAgtComssnAmt = base_types.UninitialisedField(self, 'PngAgtComssnAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def RgltryFeesAmt(self):
		return self._RgltryFeesAmt

	@RgltryFeesAmt.setter
	def RgltryFeesAmt(self, value):
		self._RgltryFeesAmt = value if value is not None else base_types.UninitialisedField(self, 'RgltryFeesAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@RgltryFeesAmt.deleter
	def RgltryFeesAmt(self):
		del self._RgltryFeesAmt
		self._RgltryFeesAmt = base_types.UninitialisedField(self, 'RgltryFeesAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def RinvstmtAmt(self):
		return self._RinvstmtAmt

	@RinvstmtAmt.setter
	def RinvstmtAmt(self, value):
		self._RinvstmtAmt = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@RinvstmtAmt.deleter
	def RinvstmtAmt(self):
		del self._RinvstmtAmt
		self._RinvstmtAmt = base_types.UninitialisedField(self, 'RinvstmtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ScndLvlTaxAmt(self):
		return self._ScndLvlTaxAmt

	@ScndLvlTaxAmt.setter
	def ScndLvlTaxAmt(self, value):
		self._ScndLvlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ScndLvlTaxAmt.deleter
	def ScndLvlTaxAmt(self):
		del self._ScndLvlTaxAmt
		self._ScndLvlTaxAmt = base_types.UninitialisedField(self, 'ScndLvlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ShppgFeesAmt(self):
		return self._ShppgFeesAmt

	@ShppgFeesAmt.setter
	def ShppgFeesAmt(self, value):
		self._ShppgFeesAmt = value if value is not None else base_types.UninitialisedField(self, 'ShppgFeesAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ShppgFeesAmt.deleter
	def ShppgFeesAmt(self):
		del self._ShppgFeesAmt
		self._ShppgFeesAmt = base_types.UninitialisedField(self, 'ShppgFeesAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def SlctnFees(self):
		return self._SlctnFees

	@SlctnFees.setter
	def SlctnFees(self, value):
		self._SlctnFees = value if value is not None else base_types.UninitialisedField(self, 'SlctnFees', RestrictedFINActiveCurrencyAndAmount, False)

	@SlctnFees.deleter
	def SlctnFees(self):
		del self._SlctnFees
		self._SlctnFees = base_types.UninitialisedField(self, 'SlctnFees', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def SndryOrOthrAmt(self):
		return self._SndryOrOthrAmt

	@SndryOrOthrAmt.setter
	def SndryOrOthrAmt(self, value):
		self._SndryOrOthrAmt = value if value is not None else base_types.UninitialisedField(self, 'SndryOrOthrAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@SndryOrOthrAmt.deleter
	def SndryOrOthrAmt(self):
		del self._SndryOrOthrAmt
		self._SndryOrOthrAmt = base_types.UninitialisedField(self, 'SndryOrOthrAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def StmpDtyAmt(self):
		return self._StmpDtyAmt

	@StmpDtyAmt.setter
	def StmpDtyAmt(self, value):
		self._StmpDtyAmt = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@StmpDtyAmt.deleter
	def StmpDtyAmt(self):
		del self._StmpDtyAmt
		self._StmpDtyAmt = base_types.UninitialisedField(self, 'StmpDtyAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TaxCdtAmt(self):
		return self._TaxCdtAmt

	@TaxCdtAmt.setter
	def TaxCdtAmt(self, value):
		self._TaxCdtAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@TaxCdtAmt.deleter
	def TaxCdtAmt(self):
		del self._TaxCdtAmt
		self._TaxCdtAmt = base_types.UninitialisedField(self, 'TaxCdtAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TaxDfrrdAmt(self):
		return self._TaxDfrrdAmt

	@TaxDfrrdAmt.setter
	def TaxDfrrdAmt(self, value):
		self._TaxDfrrdAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxDfrrdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@TaxDfrrdAmt.deleter
	def TaxDfrrdAmt(self):
		del self._TaxDfrrdAmt
		self._TaxDfrrdAmt = base_types.UninitialisedField(self, 'TaxDfrrdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TaxFreeAmt(self):
		return self._TaxFreeAmt

	@TaxFreeAmt.setter
	def TaxFreeAmt(self, value):
		self._TaxFreeAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxFreeAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@TaxFreeAmt.deleter
	def TaxFreeAmt(self):
		del self._TaxFreeAmt
		self._TaxFreeAmt = base_types.UninitialisedField(self, 'TaxFreeAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TaxOnIncmAmt(self):
		return self._TaxOnIncmAmt

	@TaxOnIncmAmt.setter
	def TaxOnIncmAmt(self, value):
		self._TaxOnIncmAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxOnIncmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@TaxOnIncmAmt.deleter
	def TaxOnIncmAmt(self):
		del self._TaxOnIncmAmt
		self._TaxOnIncmAmt = base_types.UninitialisedField(self, 'TaxOnIncmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TaxRclmAmt(self):
		return self._TaxRclmAmt

	@TaxRclmAmt.setter
	def TaxRclmAmt(self, value):
		self._TaxRclmAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@TaxRclmAmt.deleter
	def TaxRclmAmt(self):
		del self._TaxRclmAmt
		self._TaxRclmAmt = base_types.UninitialisedField(self, 'TaxRclmAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if value is not None else base_types.UninitialisedField(self, 'TxTax', RestrictedFINActiveCurrencyAndAmount, False)

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = base_types.UninitialisedField(self, 'TxTax', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def UfrnkdAmt(self):
		return self._UfrnkdAmt

	@UfrnkdAmt.setter
	def UfrnkdAmt(self, value):
		self._UfrnkdAmt = value if value is not None else base_types.UninitialisedField(self, 'UfrnkdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@UfrnkdAmt.deleter
	def UfrnkdAmt(self):
		del self._UfrnkdAmt
		self._UfrnkdAmt = base_types.UninitialisedField(self, 'UfrnkdAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def ValAddedTaxAmt(self):
		return self._ValAddedTaxAmt

	@ValAddedTaxAmt.setter
	def ValAddedTaxAmt(self, value):
		self._ValAddedTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ValAddedTaxAmt.deleter
	def ValAddedTaxAmt(self):
		del self._ValAddedTaxAmt
		self._ValAddedTaxAmt = base_types.UninitialisedField(self, 'ValAddedTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = base_types.UninitialisedField(self, 'WhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BckUpWhldgTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyUpAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlGn', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInLieuOfShr', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdDvddAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdFndAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdIntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdRyltsAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FATCATaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrgnIncmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmpAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPrtn', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndmntyAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrdDvddPmtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NRATaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgtComssnAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryFeesAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgFeesAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFees', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndryOrOthrAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDfrrdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfrnkdAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))