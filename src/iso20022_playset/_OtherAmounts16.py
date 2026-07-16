# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection29
from . import YesNoIndicator

class OtherAmounts16(base_types._BaseFieldType):

	__slots__ = ["_AcrdCptlstnAmt", "_BookVal", "_BrrwgFee", "_BrrwgIntrstAmt", "_ChrgsFees", "_ClrBrkrComssn", "_ConvtdAmt", "_CsmptnTax", "_CtryNtlFdrlTax", "_DiffInPric", "_ExctgBrkrAmt", "_IsseDscntAllwnc", "_LclBrkrComssn", "_LclTax", "_LclTaxCtrySpcfc1", "_LclTaxCtrySpcfc2", "_LclTaxCtrySpcfc3", "_LclTaxCtrySpcfc4", "_MktMmbFeeAmt", "_Mrgn", "_MtchgConfFee", "_NetGnLoss", "_NetMktVal", "_OddLotFee", "_OrgnlCcyAmt", "_Othr", "_PmtLevyTax", "_RgltryAmt", "_RmngBookVal", "_RmngFaceVal", "_RmnrtnAmt", "_RmnrtnAmtReq", "_ShrdBrkrgAmt", "_SpclCncssn", "_StmpDty", "_StockXchgTax", "_TrfTax", "_TxTax", "_ValAddedTax", "_WhldgTax"]
	@property
	def AcrdCptlstnAmt(self):
		return self._AcrdCptlstnAmt

	@AcrdCptlstnAmt.setter
	def AcrdCptlstnAmt(self, value):
		self._AcrdCptlstnAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection29, False)

	@AcrdCptlstnAmt.deleter
	def AcrdCptlstnAmt(self):
		del self._AcrdCptlstnAmt
		self._AcrdCptlstnAmt = base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection29, False)

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', AmountAndDirection29, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', AmountAndDirection29, False)

	@property
	def BrrwgFee(self):
		return self._BrrwgFee

	@BrrwgFee.setter
	def BrrwgFee(self, value):
		self._BrrwgFee = value if value is not None else base_types.UninitialisedField(self, 'BrrwgFee', AmountAndDirection29, False)

	@BrrwgFee.deleter
	def BrrwgFee(self):
		del self._BrrwgFee
		self._BrrwgFee = base_types.UninitialisedField(self, 'BrrwgFee', AmountAndDirection29, False)

	@property
	def BrrwgIntrstAmt(self):
		return self._BrrwgIntrstAmt

	@BrrwgIntrstAmt.setter
	def BrrwgIntrstAmt(self, value):
		self._BrrwgIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'BrrwgIntrstAmt', AmountAndDirection29, False)

	@BrrwgIntrstAmt.deleter
	def BrrwgIntrstAmt(self):
		del self._BrrwgIntrstAmt
		self._BrrwgIntrstAmt = base_types.UninitialisedField(self, 'BrrwgIntrstAmt', AmountAndDirection29, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection29, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection29, False)

	@property
	def ClrBrkrComssn(self):
		return self._ClrBrkrComssn

	@ClrBrkrComssn.setter
	def ClrBrkrComssn(self, value):
		self._ClrBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'ClrBrkrComssn', AmountAndDirection29, False)

	@ClrBrkrComssn.deleter
	def ClrBrkrComssn(self):
		del self._ClrBrkrComssn
		self._ClrBrkrComssn = base_types.UninitialisedField(self, 'ClrBrkrComssn', AmountAndDirection29, False)

	@property
	def ConvtdAmt(self):
		return self._ConvtdAmt

	@ConvtdAmt.setter
	def ConvtdAmt(self, value):
		self._ConvtdAmt = value if value is not None else base_types.UninitialisedField(self, 'ConvtdAmt', AmountAndDirection29, False)

	@ConvtdAmt.deleter
	def ConvtdAmt(self):
		del self._ConvtdAmt
		self._ConvtdAmt = base_types.UninitialisedField(self, 'ConvtdAmt', AmountAndDirection29, False)

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if value is not None else base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection29, False)

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection29, False)

	@property
	def CtryNtlFdrlTax(self):
		return self._CtryNtlFdrlTax

	@CtryNtlFdrlTax.setter
	def CtryNtlFdrlTax(self, value):
		self._CtryNtlFdrlTax = value if value is not None else base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection29, False)

	@CtryNtlFdrlTax.deleter
	def CtryNtlFdrlTax(self):
		del self._CtryNtlFdrlTax
		self._CtryNtlFdrlTax = base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection29, False)

	@property
	def DiffInPric(self):
		return self._DiffInPric

	@DiffInPric.setter
	def DiffInPric(self, value):
		self._DiffInPric = value if value is not None else base_types.UninitialisedField(self, 'DiffInPric', AmountAndDirection29, False)

	@DiffInPric.deleter
	def DiffInPric(self):
		del self._DiffInPric
		self._DiffInPric = base_types.UninitialisedField(self, 'DiffInPric', AmountAndDirection29, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection29, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection29, False)

	@property
	def IsseDscntAllwnc(self):
		return self._IsseDscntAllwnc

	@IsseDscntAllwnc.setter
	def IsseDscntAllwnc(self, value):
		self._IsseDscntAllwnc = value if value is not None else base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection29, False)

	@IsseDscntAllwnc.deleter
	def IsseDscntAllwnc(self):
		del self._IsseDscntAllwnc
		self._IsseDscntAllwnc = base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection29, False)

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection29, False)

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection29, False)

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if value is not None else base_types.UninitialisedField(self, 'LclTax', AmountAndDirection29, False)

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = base_types.UninitialisedField(self, 'LclTax', AmountAndDirection29, False)

	@property
	def LclTaxCtrySpcfc1(self):
		return self._LclTaxCtrySpcfc1

	@LclTaxCtrySpcfc1.setter
	def LclTaxCtrySpcfc1(self, value):
		self._LclTaxCtrySpcfc1 = value if value is not None else base_types.UninitialisedField(self, 'LclTaxCtrySpcfc1', AmountAndDirection29, False)

	@LclTaxCtrySpcfc1.deleter
	def LclTaxCtrySpcfc1(self):
		del self._LclTaxCtrySpcfc1
		self._LclTaxCtrySpcfc1 = base_types.UninitialisedField(self, 'LclTaxCtrySpcfc1', AmountAndDirection29, False)

	@property
	def LclTaxCtrySpcfc2(self):
		return self._LclTaxCtrySpcfc2

	@LclTaxCtrySpcfc2.setter
	def LclTaxCtrySpcfc2(self, value):
		self._LclTaxCtrySpcfc2 = value if value is not None else base_types.UninitialisedField(self, 'LclTaxCtrySpcfc2', AmountAndDirection29, False)

	@LclTaxCtrySpcfc2.deleter
	def LclTaxCtrySpcfc2(self):
		del self._LclTaxCtrySpcfc2
		self._LclTaxCtrySpcfc2 = base_types.UninitialisedField(self, 'LclTaxCtrySpcfc2', AmountAndDirection29, False)

	@property
	def LclTaxCtrySpcfc3(self):
		return self._LclTaxCtrySpcfc3

	@LclTaxCtrySpcfc3.setter
	def LclTaxCtrySpcfc3(self, value):
		self._LclTaxCtrySpcfc3 = value if value is not None else base_types.UninitialisedField(self, 'LclTaxCtrySpcfc3', AmountAndDirection29, False)

	@LclTaxCtrySpcfc3.deleter
	def LclTaxCtrySpcfc3(self):
		del self._LclTaxCtrySpcfc3
		self._LclTaxCtrySpcfc3 = base_types.UninitialisedField(self, 'LclTaxCtrySpcfc3', AmountAndDirection29, False)

	@property
	def LclTaxCtrySpcfc4(self):
		return self._LclTaxCtrySpcfc4

	@LclTaxCtrySpcfc4.setter
	def LclTaxCtrySpcfc4(self, value):
		self._LclTaxCtrySpcfc4 = value if value is not None else base_types.UninitialisedField(self, 'LclTaxCtrySpcfc4', AmountAndDirection29, False)

	@LclTaxCtrySpcfc4.deleter
	def LclTaxCtrySpcfc4(self):
		del self._LclTaxCtrySpcfc4
		self._LclTaxCtrySpcfc4 = base_types.UninitialisedField(self, 'LclTaxCtrySpcfc4', AmountAndDirection29, False)

	@property
	def MktMmbFeeAmt(self):
		return self._MktMmbFeeAmt

	@MktMmbFeeAmt.setter
	def MktMmbFeeAmt(self, value):
		self._MktMmbFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'MktMmbFeeAmt', AmountAndDirection29, False)

	@MktMmbFeeAmt.deleter
	def MktMmbFeeAmt(self):
		del self._MktMmbFeeAmt
		self._MktMmbFeeAmt = base_types.UninitialisedField(self, 'MktMmbFeeAmt', AmountAndDirection29, False)

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if value is not None else base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection29, False)

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection29, False)

	@property
	def MtchgConfFee(self):
		return self._MtchgConfFee

	@MtchgConfFee.setter
	def MtchgConfFee(self, value):
		self._MtchgConfFee = value if value is not None else base_types.UninitialisedField(self, 'MtchgConfFee', AmountAndDirection29, False)

	@MtchgConfFee.deleter
	def MtchgConfFee(self):
		del self._MtchgConfFee
		self._MtchgConfFee = base_types.UninitialisedField(self, 'MtchgConfFee', AmountAndDirection29, False)

	@property
	def NetGnLoss(self):
		return self._NetGnLoss

	@NetGnLoss.setter
	def NetGnLoss(self, value):
		self._NetGnLoss = value if value is not None else base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection29, False)

	@NetGnLoss.deleter
	def NetGnLoss(self):
		del self._NetGnLoss
		self._NetGnLoss = base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection29, False)

	@property
	def NetMktVal(self):
		return self._NetMktVal

	@NetMktVal.setter
	def NetMktVal(self, value):
		self._NetMktVal = value if value is not None else base_types.UninitialisedField(self, 'NetMktVal', AmountAndDirection29, False)

	@NetMktVal.deleter
	def NetMktVal(self):
		del self._NetMktVal
		self._NetMktVal = base_types.UninitialisedField(self, 'NetMktVal', AmountAndDirection29, False)

	@property
	def OddLotFee(self):
		return self._OddLotFee

	@OddLotFee.setter
	def OddLotFee(self, value):
		self._OddLotFee = value if value is not None else base_types.UninitialisedField(self, 'OddLotFee', YesNoIndicator, False)

	@OddLotFee.deleter
	def OddLotFee(self):
		del self._OddLotFee
		self._OddLotFee = base_types.UninitialisedField(self, 'OddLotFee', YesNoIndicator, False)

	@property
	def OrgnlCcyAmt(self):
		return self._OrgnlCcyAmt

	@OrgnlCcyAmt.setter
	def OrgnlCcyAmt(self, value):
		self._OrgnlCcyAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCcyAmt', AmountAndDirection29, False)

	@OrgnlCcyAmt.deleter
	def OrgnlCcyAmt(self):
		del self._OrgnlCcyAmt
		self._OrgnlCcyAmt = base_types.UninitialisedField(self, 'OrgnlCcyAmt', AmountAndDirection29, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AmountAndDirection29, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AmountAndDirection29, False)

	@property
	def PmtLevyTax(self):
		return self._PmtLevyTax

	@PmtLevyTax.setter
	def PmtLevyTax(self, value):
		self._PmtLevyTax = value if value is not None else base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection29, False)

	@PmtLevyTax.deleter
	def PmtLevyTax(self):
		del self._PmtLevyTax
		self._PmtLevyTax = base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection29, False)

	@property
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if value is not None else base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection29, False)

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection29, False)

	@property
	def RmngBookVal(self):
		return self._RmngBookVal

	@RmngBookVal.setter
	def RmngBookVal(self, value):
		self._RmngBookVal = value if value is not None else base_types.UninitialisedField(self, 'RmngBookVal', AmountAndDirection29, False)

	@RmngBookVal.deleter
	def RmngBookVal(self):
		del self._RmngBookVal
		self._RmngBookVal = base_types.UninitialisedField(self, 'RmngBookVal', AmountAndDirection29, False)

	@property
	def RmngFaceVal(self):
		return self._RmngFaceVal

	@RmngFaceVal.setter
	def RmngFaceVal(self, value):
		self._RmngFaceVal = value if value is not None else base_types.UninitialisedField(self, 'RmngFaceVal', AmountAndDirection29, False)

	@RmngFaceVal.deleter
	def RmngFaceVal(self):
		del self._RmngFaceVal
		self._RmngFaceVal = base_types.UninitialisedField(self, 'RmngFaceVal', AmountAndDirection29, False)

	@property
	def RmnrtnAmt(self):
		return self._RmnrtnAmt

	@RmnrtnAmt.setter
	def RmnrtnAmt(self, value):
		self._RmnrtnAmt = value if value is not None else base_types.UninitialisedField(self, 'RmnrtnAmt', AmountAndDirection29, False)

	@RmnrtnAmt.deleter
	def RmnrtnAmt(self):
		del self._RmnrtnAmt
		self._RmnrtnAmt = base_types.UninitialisedField(self, 'RmnrtnAmt', AmountAndDirection29, False)

	@property
	def RmnrtnAmtReq(self):
		return self._RmnrtnAmtReq

	@RmnrtnAmtReq.setter
	def RmnrtnAmtReq(self, value):
		self._RmnrtnAmtReq = value if value is not None else base_types.UninitialisedField(self, 'RmnrtnAmtReq', YesNoIndicator, False)

	@RmnrtnAmtReq.deleter
	def RmnrtnAmtReq(self):
		del self._RmnrtnAmtReq
		self._RmnrtnAmtReq = base_types.UninitialisedField(self, 'RmnrtnAmtReq', YesNoIndicator, False)

	@property
	def ShrdBrkrgAmt(self):
		return self._ShrdBrkrgAmt

	@ShrdBrkrgAmt.setter
	def ShrdBrkrgAmt(self, value):
		self._ShrdBrkrgAmt = value if value is not None else base_types.UninitialisedField(self, 'ShrdBrkrgAmt', AmountAndDirection29, False)

	@ShrdBrkrgAmt.deleter
	def ShrdBrkrgAmt(self):
		del self._ShrdBrkrgAmt
		self._ShrdBrkrgAmt = base_types.UninitialisedField(self, 'ShrdBrkrgAmt', AmountAndDirection29, False)

	@property
	def SpclCncssn(self):
		return self._SpclCncssn

	@SpclCncssn.setter
	def SpclCncssn(self, value):
		self._SpclCncssn = value if value is not None else base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection29, False)

	@SpclCncssn.deleter
	def SpclCncssn(self):
		del self._SpclCncssn
		self._SpclCncssn = base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection29, False)

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if value is not None else base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection29, False)

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection29, False)

	@property
	def StockXchgTax(self):
		return self._StockXchgTax

	@StockXchgTax.setter
	def StockXchgTax(self, value):
		self._StockXchgTax = value if value is not None else base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection29, False)

	@StockXchgTax.deleter
	def StockXchgTax(self):
		del self._StockXchgTax
		self._StockXchgTax = base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection29, False)

	@property
	def TrfTax(self):
		return self._TrfTax

	@TrfTax.setter
	def TrfTax(self, value):
		self._TrfTax = value if value is not None else base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection29, False)

	@TrfTax.deleter
	def TrfTax(self):
		del self._TrfTax
		self._TrfTax = base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection29, False)

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if value is not None else base_types.UninitialisedField(self, 'TxTax', AmountAndDirection29, False)

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = base_types.UninitialisedField(self, 'TxTax', AmountAndDirection29, False)

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection29, False)

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection29, False)

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection29, False)

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection29, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgFee', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwgIntrstAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBrkrComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtdAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DiffInPric', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc1', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc2', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc3', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc4', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktMmbFeeAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgConfFee', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetMktVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OddLotFee', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngBookVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngFaceVal', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmnrtnAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmnrtnAmtReq', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrdBrkrgAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
	))