from . import base_types
import AmountAndDirection44
import AmountAndDirection58

class OtherAmounts44(base_types._BaseFieldType):

	__slots__ = ["_ShppgAmt", "_TradAmt", "_SpclCncssn", "_ExctgBrkrAmt", "_AcrdCptlstnAmt", "_TrfTax", "_CsmptnTax", "_IsseDscntAllwnc", "_CtryNtlFdrlTax", "_ValAddedTax", "_BookVal", "_AcrdIntrstAmt", "_RgltryAmt", "_PmtLevyTax", "_Mrgn", "_RsrchFee", "_CollMntrAmt", "_StmpDty", "_WhldgTax", "_NetGnLoss", "_LclTaxCtrySpcfc", "_Othr", "_LclBrkrComssn", "_StockXchgTax", "_ChrgsFees", "_LclTax", "_TxTax"]
	@property
	def ShppgAmt(self):
		return self._ShppgAmt

	@ShppgAmt.setter
	def ShppgAmt(self, value):
		self._ShppgAmt = value if type(value) != auto else self.make_default("ShppgAmt")

	@ShppgAmt.deleter
	def ShppgAmt(self):
		del self._ShppgAmt
		self._ShppgAmt = None

	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if type(value) != auto else self.make_default("TradAmt")

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = None

	@property
	def SpclCncssn(self):
		return self._SpclCncssn

	@SpclCncssn.setter
	def SpclCncssn(self, value):
		self._SpclCncssn = value if type(value) != auto else self.make_default("SpclCncssn")

	@SpclCncssn.deleter
	def SpclCncssn(self):
		del self._SpclCncssn
		self._SpclCncssn = None

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if type(value) != auto else self.make_default("ExctgBrkrAmt")

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = None

	@property
	def AcrdCptlstnAmt(self):
		return self._AcrdCptlstnAmt

	@AcrdCptlstnAmt.setter
	def AcrdCptlstnAmt(self, value):
		self._AcrdCptlstnAmt = value if type(value) != auto else self.make_default("AcrdCptlstnAmt")

	@AcrdCptlstnAmt.deleter
	def AcrdCptlstnAmt(self):
		del self._AcrdCptlstnAmt
		self._AcrdCptlstnAmt = None

	@property
	def TrfTax(self):
		return self._TrfTax

	@TrfTax.setter
	def TrfTax(self, value):
		self._TrfTax = value if type(value) != auto else self.make_default("TrfTax")

	@TrfTax.deleter
	def TrfTax(self):
		del self._TrfTax
		self._TrfTax = None

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if type(value) != auto else self.make_default("CsmptnTax")

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = None

	@property
	def IsseDscntAllwnc(self):
		return self._IsseDscntAllwnc

	@IsseDscntAllwnc.setter
	def IsseDscntAllwnc(self, value):
		self._IsseDscntAllwnc = value if type(value) != auto else self.make_default("IsseDscntAllwnc")

	@IsseDscntAllwnc.deleter
	def IsseDscntAllwnc(self):
		del self._IsseDscntAllwnc
		self._IsseDscntAllwnc = None

	@property
	def CtryNtlFdrlTax(self):
		return self._CtryNtlFdrlTax

	@CtryNtlFdrlTax.setter
	def CtryNtlFdrlTax(self, value):
		self._CtryNtlFdrlTax = value if type(value) != auto else self.make_default("CtryNtlFdrlTax")

	@CtryNtlFdrlTax.deleter
	def CtryNtlFdrlTax(self):
		del self._CtryNtlFdrlTax
		self._CtryNtlFdrlTax = None

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if type(value) != auto else self.make_default("ValAddedTax")

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = None

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if type(value) != auto else self.make_default("BookVal")

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if type(value) != auto else self.make_default("RgltryAmt")

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = None

	@property
	def PmtLevyTax(self):
		return self._PmtLevyTax

	@PmtLevyTax.setter
	def PmtLevyTax(self, value):
		self._PmtLevyTax = value if type(value) != auto else self.make_default("PmtLevyTax")

	@PmtLevyTax.deleter
	def PmtLevyTax(self):
		del self._PmtLevyTax
		self._PmtLevyTax = None

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if type(value) != auto else self.make_default("Mrgn")

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = None

	@property
	def RsrchFee(self):
		return self._RsrchFee

	@RsrchFee.setter
	def RsrchFee(self, value):
		self._RsrchFee = value if type(value) != auto else self.make_default("RsrchFee")

	@RsrchFee.deleter
	def RsrchFee(self):
		del self._RsrchFee
		self._RsrchFee = None

	@property
	def CollMntrAmt(self):
		return self._CollMntrAmt

	@CollMntrAmt.setter
	def CollMntrAmt(self, value):
		self._CollMntrAmt = value if type(value) != auto else self.make_default("CollMntrAmt")

	@CollMntrAmt.deleter
	def CollMntrAmt(self):
		del self._CollMntrAmt
		self._CollMntrAmt = None

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if type(value) != auto else self.make_default("StmpDty")

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = None

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if type(value) != auto else self.make_default("WhldgTax")

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = None

	@property
	def NetGnLoss(self):
		return self._NetGnLoss

	@NetGnLoss.setter
	def NetGnLoss(self, value):
		self._NetGnLoss = value if type(value) != auto else self.make_default("NetGnLoss")

	@NetGnLoss.deleter
	def NetGnLoss(self):
		del self._NetGnLoss
		self._NetGnLoss = None

	@property
	def LclTaxCtrySpcfc(self):
		return self._LclTaxCtrySpcfc

	@LclTaxCtrySpcfc.setter
	def LclTaxCtrySpcfc(self, value):
		self._LclTaxCtrySpcfc = value if type(value) != auto else self.make_default("LclTaxCtrySpcfc")

	@LclTaxCtrySpcfc.deleter
	def LclTaxCtrySpcfc(self):
		del self._LclTaxCtrySpcfc
		self._LclTaxCtrySpcfc = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if type(value) != auto else self.make_default("LclBrkrComssn")

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = None

	@property
	def StockXchgTax(self):
		return self._StockXchgTax

	@StockXchgTax.setter
	def StockXchgTax(self, value):
		self._StockXchgTax = value if type(value) != auto else self.make_default("StockXchgTax")

	@StockXchgTax.deleter
	def StockXchgTax(self):
		del self._StockXchgTax
		self._StockXchgTax = None

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if type(value) != auto else self.make_default("ChrgsFees")

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = None

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if type(value) != auto else self.make_default("LclTax")

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = None

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if type(value) != auto else self.make_default("TxTax")

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShppgAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMntrAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
	))

