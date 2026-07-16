# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection44
from . import AmountAndDirection58

class OtherAmounts42(base_types._BaseFieldType):

	__slots__ = ["_AcrdCptlstnAmt", "_AcrdIntrstAmt", "_BookVal", "_ChrgsFees", "_CsmptnTax", "_CtryNtlFdrlTax", "_ExctgBrkrAmt", "_IsseDscntAllwnc", "_LclBrkrComssn", "_LclTax", "_Mrgn", "_NetGnLoss", "_Othr", "_PmtLevyTax", "_RgltryAmt", "_RsrchFee", "_ShppgAmt", "_SpclCncssn", "_StmpDty", "_StockXchgTax", "_TradAmt", "_TrfTax", "_TxTax", "_ValAddedTax", "_WhldgTax"]
	@property
	def AcrdCptlstnAmt(self):
		return self._AcrdCptlstnAmt

	@AcrdCptlstnAmt.setter
	def AcrdCptlstnAmt(self, value):
		self._AcrdCptlstnAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection58, False)

	@AcrdCptlstnAmt.deleter
	def AcrdCptlstnAmt(self):
		del self._AcrdCptlstnAmt
		self._AcrdCptlstnAmt = base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection58, False)

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection58, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection58, False)

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', AmountAndDirection58, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', AmountAndDirection58, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection58, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection58, False)

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if value is not None else base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection58, False)

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection58, False)

	@property
	def CtryNtlFdrlTax(self):
		return self._CtryNtlFdrlTax

	@CtryNtlFdrlTax.setter
	def CtryNtlFdrlTax(self, value):
		self._CtryNtlFdrlTax = value if value is not None else base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection58, False)

	@CtryNtlFdrlTax.deleter
	def CtryNtlFdrlTax(self):
		del self._CtryNtlFdrlTax
		self._CtryNtlFdrlTax = base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection58, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection58, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection58, False)

	@property
	def IsseDscntAllwnc(self):
		return self._IsseDscntAllwnc

	@IsseDscntAllwnc.setter
	def IsseDscntAllwnc(self, value):
		self._IsseDscntAllwnc = value if value is not None else base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection58, False)

	@IsseDscntAllwnc.deleter
	def IsseDscntAllwnc(self):
		del self._IsseDscntAllwnc
		self._IsseDscntAllwnc = base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection58, False)

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection58, False)

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection58, False)

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if value is not None else base_types.UninitialisedField(self, 'LclTax', AmountAndDirection58, False)

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = base_types.UninitialisedField(self, 'LclTax', AmountAndDirection58, False)

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if value is not None else base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection58, False)

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection58, False)

	@property
	def NetGnLoss(self):
		return self._NetGnLoss

	@NetGnLoss.setter
	def NetGnLoss(self, value):
		self._NetGnLoss = value if value is not None else base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection58, False)

	@NetGnLoss.deleter
	def NetGnLoss(self):
		del self._NetGnLoss
		self._NetGnLoss = base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection58, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AmountAndDirection58, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AmountAndDirection58, False)

	@property
	def PmtLevyTax(self):
		return self._PmtLevyTax

	@PmtLevyTax.setter
	def PmtLevyTax(self, value):
		self._PmtLevyTax = value if value is not None else base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection58, False)

	@PmtLevyTax.deleter
	def PmtLevyTax(self):
		del self._PmtLevyTax
		self._PmtLevyTax = base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection58, False)

	@property
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if value is not None else base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection58, False)

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection58, False)

	@property
	def RsrchFee(self):
		return self._RsrchFee

	@RsrchFee.setter
	def RsrchFee(self, value):
		self._RsrchFee = value if value is not None else base_types.UninitialisedField(self, 'RsrchFee', AmountAndDirection44, False)

	@RsrchFee.deleter
	def RsrchFee(self):
		del self._RsrchFee
		self._RsrchFee = base_types.UninitialisedField(self, 'RsrchFee', AmountAndDirection44, False)

	@property
	def ShppgAmt(self):
		return self._ShppgAmt

	@ShppgAmt.setter
	def ShppgAmt(self, value):
		self._ShppgAmt = value if value is not None else base_types.UninitialisedField(self, 'ShppgAmt', AmountAndDirection58, False)

	@ShppgAmt.deleter
	def ShppgAmt(self):
		del self._ShppgAmt
		self._ShppgAmt = base_types.UninitialisedField(self, 'ShppgAmt', AmountAndDirection58, False)

	@property
	def SpclCncssn(self):
		return self._SpclCncssn

	@SpclCncssn.setter
	def SpclCncssn(self, value):
		self._SpclCncssn = value if value is not None else base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection58, False)

	@SpclCncssn.deleter
	def SpclCncssn(self):
		del self._SpclCncssn
		self._SpclCncssn = base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection58, False)

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if value is not None else base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection58, False)

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection58, False)

	@property
	def StockXchgTax(self):
		return self._StockXchgTax

	@StockXchgTax.setter
	def StockXchgTax(self, value):
		self._StockXchgTax = value if value is not None else base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection58, False)

	@StockXchgTax.deleter
	def StockXchgTax(self):
		del self._StockXchgTax
		self._StockXchgTax = base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection58, False)

	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if value is not None else base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection58, False)

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection58, False)

	@property
	def TrfTax(self):
		return self._TrfTax

	@TrfTax.setter
	def TrfTax(self, value):
		self._TrfTax = value if value is not None else base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection58, False)

	@TrfTax.deleter
	def TrfTax(self):
		del self._TrfTax
		self._TrfTax = base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection58, False)

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if value is not None else base_types.UninitialisedField(self, 'TxTax', AmountAndDirection58, False)

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = base_types.UninitialisedField(self, 'TxTax', AmountAndDirection58, False)

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection58, False)

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection58, False)

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection58, False)

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection58, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection58, min=0, max=1, mutex_group=None, array=False),
	))