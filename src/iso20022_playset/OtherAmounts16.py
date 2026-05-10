from . import base_types
from .YesNoIndicator import YesNoIndicator
from .AmountAndDirection29 import AmountAndDirection29

class OtherAmounts16(base_types._BaseFieldType):

	__slots__ = ["_LclTaxCtrySpcfc3", "_NetMktVal", "_RgltryAmt", "_LclTaxCtrySpcfc4", "_LclTaxCtrySpcfc2", "_SpclCncssn", "_RmngFaceVal", "_TxTax", "_MktMmbFeeAmt", "_TrfTax", "_Othr", "_StmpDty", "_PmtLevyTax", "_StockXchgTax", "_OddLotFee", "_RmnrtnAmtReq", "_ExctgBrkrAmt", "_RmngBookVal", "_DiffInPric", "_RmnrtnAmt", "_IsseDscntAllwnc", "_LclBrkrComssn", "_LclTaxCtrySpcfc1", "_ClrBrkrComssn", "_ConvtdAmt", "_ChrgsFees", "_ValAddedTax", "_Mrgn", "_BrrwgFee", "_CsmptnTax", "_BookVal", "_MtchgConfFee", "_LclTax", "_AcrdCptlstnAmt", "_WhldgTax", "_ShrdBrkrgAmt", "_OrgnlCcyAmt", "_NetGnLoss", "_CtryNtlFdrlTax", "_BrrwgIntrstAmt"]
	@property
	def LclTaxCtrySpcfc3(self):
		return self._LclTaxCtrySpcfc3

	@LclTaxCtrySpcfc3.setter
	def LclTaxCtrySpcfc3(self, value):
		self._LclTaxCtrySpcfc3 = value if type(value) != base_types.auto else self.make_default("LclTaxCtrySpcfc3")

	@LclTaxCtrySpcfc3.deleter
	def LclTaxCtrySpcfc3(self):
		del self._LclTaxCtrySpcfc3
		self._LclTaxCtrySpcfc3 = None

	@property
	def NetMktVal(self):
		return self._NetMktVal

	@NetMktVal.setter
	def NetMktVal(self, value):
		self._NetMktVal = value if type(value) != base_types.auto else self.make_default("NetMktVal")

	@NetMktVal.deleter
	def NetMktVal(self):
		del self._NetMktVal
		self._NetMktVal = None

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
	def LclTaxCtrySpcfc4(self):
		return self._LclTaxCtrySpcfc4

	@LclTaxCtrySpcfc4.setter
	def LclTaxCtrySpcfc4(self, value):
		self._LclTaxCtrySpcfc4 = value if type(value) != base_types.auto else self.make_default("LclTaxCtrySpcfc4")

	@LclTaxCtrySpcfc4.deleter
	def LclTaxCtrySpcfc4(self):
		del self._LclTaxCtrySpcfc4
		self._LclTaxCtrySpcfc4 = None

	@property
	def LclTaxCtrySpcfc2(self):
		return self._LclTaxCtrySpcfc2

	@LclTaxCtrySpcfc2.setter
	def LclTaxCtrySpcfc2(self, value):
		self._LclTaxCtrySpcfc2 = value if type(value) != base_types.auto else self.make_default("LclTaxCtrySpcfc2")

	@LclTaxCtrySpcfc2.deleter
	def LclTaxCtrySpcfc2(self):
		del self._LclTaxCtrySpcfc2
		self._LclTaxCtrySpcfc2 = None

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
	def RmngFaceVal(self):
		return self._RmngFaceVal

	@RmngFaceVal.setter
	def RmngFaceVal(self, value):
		self._RmngFaceVal = value if type(value) != base_types.auto else self.make_default("RmngFaceVal")

	@RmngFaceVal.deleter
	def RmngFaceVal(self):
		del self._RmngFaceVal
		self._RmngFaceVal = None

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
	def MktMmbFeeAmt(self):
		return self._MktMmbFeeAmt

	@MktMmbFeeAmt.setter
	def MktMmbFeeAmt(self, value):
		self._MktMmbFeeAmt = value if type(value) != base_types.auto else self.make_default("MktMmbFeeAmt")

	@MktMmbFeeAmt.deleter
	def MktMmbFeeAmt(self):
		del self._MktMmbFeeAmt
		self._MktMmbFeeAmt = None

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
	def OddLotFee(self):
		return self._OddLotFee

	@OddLotFee.setter
	def OddLotFee(self, value):
		self._OddLotFee = value if type(value) != base_types.auto else self.make_default("OddLotFee")

	@OddLotFee.deleter
	def OddLotFee(self):
		del self._OddLotFee
		self._OddLotFee = None

	@property
	def RmnrtnAmtReq(self):
		return self._RmnrtnAmtReq

	@RmnrtnAmtReq.setter
	def RmnrtnAmtReq(self, value):
		self._RmnrtnAmtReq = value if type(value) != base_types.auto else self.make_default("RmnrtnAmtReq")

	@RmnrtnAmtReq.deleter
	def RmnrtnAmtReq(self):
		del self._RmnrtnAmtReq
		self._RmnrtnAmtReq = None

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
	def RmngBookVal(self):
		return self._RmngBookVal

	@RmngBookVal.setter
	def RmngBookVal(self, value):
		self._RmngBookVal = value if type(value) != base_types.auto else self.make_default("RmngBookVal")

	@RmngBookVal.deleter
	def RmngBookVal(self):
		del self._RmngBookVal
		self._RmngBookVal = None

	@property
	def DiffInPric(self):
		return self._DiffInPric

	@DiffInPric.setter
	def DiffInPric(self, value):
		self._DiffInPric = value if type(value) != base_types.auto else self.make_default("DiffInPric")

	@DiffInPric.deleter
	def DiffInPric(self):
		del self._DiffInPric
		self._DiffInPric = None

	@property
	def RmnrtnAmt(self):
		return self._RmnrtnAmt

	@RmnrtnAmt.setter
	def RmnrtnAmt(self, value):
		self._RmnrtnAmt = value if type(value) != base_types.auto else self.make_default("RmnrtnAmt")

	@RmnrtnAmt.deleter
	def RmnrtnAmt(self):
		del self._RmnrtnAmt
		self._RmnrtnAmt = None

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
	def LclTaxCtrySpcfc1(self):
		return self._LclTaxCtrySpcfc1

	@LclTaxCtrySpcfc1.setter
	def LclTaxCtrySpcfc1(self, value):
		self._LclTaxCtrySpcfc1 = value if type(value) != base_types.auto else self.make_default("LclTaxCtrySpcfc1")

	@LclTaxCtrySpcfc1.deleter
	def LclTaxCtrySpcfc1(self):
		del self._LclTaxCtrySpcfc1
		self._LclTaxCtrySpcfc1 = None

	@property
	def ClrBrkrComssn(self):
		return self._ClrBrkrComssn

	@ClrBrkrComssn.setter
	def ClrBrkrComssn(self, value):
		self._ClrBrkrComssn = value if type(value) != base_types.auto else self.make_default("ClrBrkrComssn")

	@ClrBrkrComssn.deleter
	def ClrBrkrComssn(self):
		del self._ClrBrkrComssn
		self._ClrBrkrComssn = None

	@property
	def ConvtdAmt(self):
		return self._ConvtdAmt

	@ConvtdAmt.setter
	def ConvtdAmt(self, value):
		self._ConvtdAmt = value if type(value) != base_types.auto else self.make_default("ConvtdAmt")

	@ConvtdAmt.deleter
	def ConvtdAmt(self):
		del self._ConvtdAmt
		self._ConvtdAmt = None

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
	def BrrwgFee(self):
		return self._BrrwgFee

	@BrrwgFee.setter
	def BrrwgFee(self, value):
		self._BrrwgFee = value if type(value) != base_types.auto else self.make_default("BrrwgFee")

	@BrrwgFee.deleter
	def BrrwgFee(self):
		del self._BrrwgFee
		self._BrrwgFee = None

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
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if type(value) != base_types.auto else self.make_default("BookVal")

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = None

	@property
	def MtchgConfFee(self):
		return self._MtchgConfFee

	@MtchgConfFee.setter
	def MtchgConfFee(self, value):
		self._MtchgConfFee = value if type(value) != base_types.auto else self.make_default("MtchgConfFee")

	@MtchgConfFee.deleter
	def MtchgConfFee(self):
		del self._MtchgConfFee
		self._MtchgConfFee = None

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
	def ShrdBrkrgAmt(self):
		return self._ShrdBrkrgAmt

	@ShrdBrkrgAmt.setter
	def ShrdBrkrgAmt(self, value):
		self._ShrdBrkrgAmt = value if type(value) != base_types.auto else self.make_default("ShrdBrkrgAmt")

	@ShrdBrkrgAmt.deleter
	def ShrdBrkrgAmt(self):
		del self._ShrdBrkrgAmt
		self._ShrdBrkrgAmt = None

	@property
	def OrgnlCcyAmt(self):
		return self._OrgnlCcyAmt

	@OrgnlCcyAmt.setter
	def OrgnlCcyAmt(self, value):
		self._OrgnlCcyAmt = value if type(value) != base_types.auto else self.make_default("OrgnlCcyAmt")

	@OrgnlCcyAmt.deleter
	def OrgnlCcyAmt(self):
		del self._OrgnlCcyAmt
		self._OrgnlCcyAmt = None

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
	def BrrwgIntrstAmt(self):
		return self._BrrwgIntrstAmt

	@BrrwgIntrstAmt.setter
	def BrrwgIntrstAmt(self, value):
		self._BrrwgIntrstAmt = value if type(value) != base_types.auto else self.make_default("BrrwgIntrstAmt")

	@BrrwgIntrstAmt.deleter
	def BrrwgIntrstAmt(self):
		del self._BrrwgIntrstAmt
		self._BrrwgIntrstAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LclTaxCtrySpcfc3', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetMktVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc4', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc2', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngFaceVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktMmbFeeAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OddLotFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmnrtnAmtReq', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngBookVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DiffInPric', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmnrtnAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc1', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkrComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtdAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgFee', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgConfFee', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrdBrkrgAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgIntrstAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
	))

