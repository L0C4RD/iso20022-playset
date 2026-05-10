from . import base_types
from .AmountAndDirection44 import AmountAndDirection44

class OtherAmounts45(base_types._BaseFieldType):

	__slots__ = ["_TradAmt", "_NtwkFee", "_TrfTax", "_LclTax", "_TxTax", "_RsrchFee", "_CtryNtlFdrlTax", "_RgltryAmt", "_ChrgsFees", "_Othr", "_StmpDty", "_Mrgn", "_LclTaxCtrySpcfc", "_ExctgBrkrAmt", "_CsmptnTax", "_ValAddedTax", "_StockXchgTax", "_ShppgAmt", "_SpclCncssn", "_AcrdCptlstnAmt", "_WhldgTax", "_LclBrkrComssn", "_NetGnLoss", "_AcrdIntrstAmt", "_PmtLevyTax", "_IsseDscntAllwnc"]
	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if type(value) != base_types.auto else self.make_default("TradAmt")

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = None

	@property
	def NtwkFee(self):
		return self._NtwkFee

	@NtwkFee.setter
	def NtwkFee(self, value):
		self._NtwkFee = value if type(value) != base_types.auto else self.make_default("NtwkFee")

	@NtwkFee.deleter
	def NtwkFee(self):
		del self._NtwkFee
		self._NtwkFee = None

	@property
	def TrfTax(self):
		return self._TrfTax

	@TrfTax.setter
	def TrfTax(self, value):
		self._TrfTax = value if type(value) != base_types.auto else self.make_default("TrfTax")

	@TrfTax.deleter
	def TrfTax(self):
		del self._TrfTax
		self._TrfTax = None

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if type(value) != base_types.auto else self.make_default("LclTax")

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = None

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
	def RsrchFee(self):
		return self._RsrchFee

	@RsrchFee.setter
	def RsrchFee(self, value):
		self._RsrchFee = value if type(value) != base_types.auto else self.make_default("RsrchFee")

	@RsrchFee.deleter
	def RsrchFee(self):
		del self._RsrchFee
		self._RsrchFee = None

	@property
	def CtryNtlFdrlTax(self):
		return self._CtryNtlFdrlTax

	@CtryNtlFdrlTax.setter
	def CtryNtlFdrlTax(self, value):
		self._CtryNtlFdrlTax = value if type(value) != base_types.auto else self.make_default("CtryNtlFdrlTax")

	@CtryNtlFdrlTax.deleter
	def CtryNtlFdrlTax(self):
		del self._CtryNtlFdrlTax
		self._CtryNtlFdrlTax = None

	@property
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if type(value) != base_types.auto else self.make_default("RgltryAmt")

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = None

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if type(value) != base_types.auto else self.make_default("ChrgsFees")

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if type(value) != base_types.auto else self.make_default("StmpDty")

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = None

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if type(value) != base_types.auto else self.make_default("Mrgn")

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = None

	@property
	def LclTaxCtrySpcfc(self):
		return self._LclTaxCtrySpcfc

	@LclTaxCtrySpcfc.setter
	def LclTaxCtrySpcfc(self, value):
		self._LclTaxCtrySpcfc = value if type(value) != base_types.auto else self.make_default("LclTaxCtrySpcfc")

	@LclTaxCtrySpcfc.deleter
	def LclTaxCtrySpcfc(self):
		del self._LclTaxCtrySpcfc
		self._LclTaxCtrySpcfc = None

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
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if type(value) != base_types.auto else self.make_default("CsmptnTax")

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = None

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if type(value) != base_types.auto else self.make_default("ValAddedTax")

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = None

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
	def ShppgAmt(self):
		return self._ShppgAmt

	@ShppgAmt.setter
	def ShppgAmt(self, value):
		self._ShppgAmt = value if type(value) != base_types.auto else self.make_default("ShppgAmt")

	@ShppgAmt.deleter
	def ShppgAmt(self):
		del self._ShppgAmt
		self._ShppgAmt = None

	@property
	def SpclCncssn(self):
		return self._SpclCncssn

	@SpclCncssn.setter
	def SpclCncssn(self, value):
		self._SpclCncssn = value if type(value) != base_types.auto else self.make_default("SpclCncssn")

	@SpclCncssn.deleter
	def SpclCncssn(self):
		del self._SpclCncssn
		self._SpclCncssn = None

	@property
	def AcrdCptlstnAmt(self):
		return self._AcrdCptlstnAmt

	@AcrdCptlstnAmt.setter
	def AcrdCptlstnAmt(self, value):
		self._AcrdCptlstnAmt = value if type(value) != base_types.auto else self.make_default("AcrdCptlstnAmt")

	@AcrdCptlstnAmt.deleter
	def AcrdCptlstnAmt(self):
		del self._AcrdCptlstnAmt
		self._AcrdCptlstnAmt = None

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if type(value) != base_types.auto else self.make_default("WhldgTax")

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = None

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if type(value) != base_types.auto else self.make_default("LclBrkrComssn")

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = None

	@property
	def NetGnLoss(self):
		return self._NetGnLoss

	@NetGnLoss.setter
	def NetGnLoss(self, value):
		self._NetGnLoss = value if type(value) != base_types.auto else self.make_default("NetGnLoss")

	@NetGnLoss.deleter
	def NetGnLoss(self):
		del self._NetGnLoss
		self._NetGnLoss = None

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
	def PmtLevyTax(self):
		return self._PmtLevyTax

	@PmtLevyTax.setter
	def PmtLevyTax(self, value):
		self._PmtLevyTax = value if type(value) != base_types.auto else self.make_default("PmtLevyTax")

	@PmtLevyTax.deleter
	def PmtLevyTax(self):
		del self._PmtLevyTax
		self._PmtLevyTax = None

	@property
	def IsseDscntAllwnc(self):
		return self._IsseDscntAllwnc

	@IsseDscntAllwnc.setter
	def IsseDscntAllwnc(self, value):
		self._IsseDscntAllwnc = value if type(value) != base_types.auto else self.make_default("IsseDscntAllwnc")

	@IsseDscntAllwnc.deleter
	def IsseDscntAllwnc(self):
		del self._IsseDscntAllwnc
		self._IsseDscntAllwnc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
	))

