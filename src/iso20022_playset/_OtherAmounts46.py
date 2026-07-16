# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection44

class OtherAmounts46(base_types._BaseFieldType):

	__slots__ = ["_AcrdCptlstnAmt", "_AcrdIntrstAmt", "_BookVal", "_ChrgsFees", "_CollMntrAmt", "_CsmptnTax", "_CtryNtlFdrlTax", "_ExctgBrkrAmt", "_IsseDscntAllwnc", "_LclBrkrComssn", "_LclTax", "_LclTaxCtrySpcfc", "_Mrgn", "_NetGnLoss", "_NtwkFee", "_Othr", "_PmtLevyTax", "_RgltryAmt", "_RsrchFee", "_ShppgAmt", "_SpclCncssn", "_StmpDty", "_StockXchgTax", "_TradAmt", "_TrfTax", "_TxTax", "_ValAddedTax", "_WhldgTax"]
	@property
	def AcrdCptlstnAmt(self):
		return self._AcrdCptlstnAmt

	@AcrdCptlstnAmt.setter
	def AcrdCptlstnAmt(self, value):
		self._AcrdCptlstnAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection44, False)

	@AcrdCptlstnAmt.deleter
	def AcrdCptlstnAmt(self):
		del self._AcrdCptlstnAmt
		self._AcrdCptlstnAmt = base_types.UninitialisedField(self, 'AcrdCptlstnAmt', AmountAndDirection44, False)

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection44, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection44, False)

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', AmountAndDirection44, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', AmountAndDirection44, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection44, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', AmountAndDirection44, False)

	@property
	def CollMntrAmt(self):
		return self._CollMntrAmt

	@CollMntrAmt.setter
	def CollMntrAmt(self, value):
		self._CollMntrAmt = value if value is not None else base_types.UninitialisedField(self, 'CollMntrAmt', AmountAndDirection44, False)

	@CollMntrAmt.deleter
	def CollMntrAmt(self):
		del self._CollMntrAmt
		self._CollMntrAmt = base_types.UninitialisedField(self, 'CollMntrAmt', AmountAndDirection44, False)

	@property
	def CsmptnTax(self):
		return self._CsmptnTax

	@CsmptnTax.setter
	def CsmptnTax(self, value):
		self._CsmptnTax = value if value is not None else base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection44, False)

	@CsmptnTax.deleter
	def CsmptnTax(self):
		del self._CsmptnTax
		self._CsmptnTax = base_types.UninitialisedField(self, 'CsmptnTax', AmountAndDirection44, False)

	@property
	def CtryNtlFdrlTax(self):
		return self._CtryNtlFdrlTax

	@CtryNtlFdrlTax.setter
	def CtryNtlFdrlTax(self, value):
		self._CtryNtlFdrlTax = value if value is not None else base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection44, False)

	@CtryNtlFdrlTax.deleter
	def CtryNtlFdrlTax(self):
		del self._CtryNtlFdrlTax
		self._CtryNtlFdrlTax = base_types.UninitialisedField(self, 'CtryNtlFdrlTax', AmountAndDirection44, False)

	@property
	def ExctgBrkrAmt(self):
		return self._ExctgBrkrAmt

	@ExctgBrkrAmt.setter
	def ExctgBrkrAmt(self, value):
		self._ExctgBrkrAmt = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection44, False)

	@ExctgBrkrAmt.deleter
	def ExctgBrkrAmt(self):
		del self._ExctgBrkrAmt
		self._ExctgBrkrAmt = base_types.UninitialisedField(self, 'ExctgBrkrAmt', AmountAndDirection44, False)

	@property
	def IsseDscntAllwnc(self):
		return self._IsseDscntAllwnc

	@IsseDscntAllwnc.setter
	def IsseDscntAllwnc(self, value):
		self._IsseDscntAllwnc = value if value is not None else base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection44, False)

	@IsseDscntAllwnc.deleter
	def IsseDscntAllwnc(self):
		del self._IsseDscntAllwnc
		self._IsseDscntAllwnc = base_types.UninitialisedField(self, 'IsseDscntAllwnc', AmountAndDirection44, False)

	@property
	def LclBrkrComssn(self):
		return self._LclBrkrComssn

	@LclBrkrComssn.setter
	def LclBrkrComssn(self, value):
		self._LclBrkrComssn = value if value is not None else base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection44, False)

	@LclBrkrComssn.deleter
	def LclBrkrComssn(self):
		del self._LclBrkrComssn
		self._LclBrkrComssn = base_types.UninitialisedField(self, 'LclBrkrComssn', AmountAndDirection44, False)

	@property
	def LclTax(self):
		return self._LclTax

	@LclTax.setter
	def LclTax(self, value):
		self._LclTax = value if value is not None else base_types.UninitialisedField(self, 'LclTax', AmountAndDirection44, False)

	@LclTax.deleter
	def LclTax(self):
		del self._LclTax
		self._LclTax = base_types.UninitialisedField(self, 'LclTax', AmountAndDirection44, False)

	@property
	def LclTaxCtrySpcfc(self):
		return self._LclTaxCtrySpcfc

	@LclTaxCtrySpcfc.setter
	def LclTaxCtrySpcfc(self, value):
		self._LclTaxCtrySpcfc = value if value is not None else base_types.UninitialisedField(self, 'LclTaxCtrySpcfc', AmountAndDirection44, False)

	@LclTaxCtrySpcfc.deleter
	def LclTaxCtrySpcfc(self):
		del self._LclTaxCtrySpcfc
		self._LclTaxCtrySpcfc = base_types.UninitialisedField(self, 'LclTaxCtrySpcfc', AmountAndDirection44, False)

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if value is not None else base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection44, False)

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection44, False)

	@property
	def NetGnLoss(self):
		return self._NetGnLoss

	@NetGnLoss.setter
	def NetGnLoss(self, value):
		self._NetGnLoss = value if value is not None else base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection44, False)

	@NetGnLoss.deleter
	def NetGnLoss(self):
		del self._NetGnLoss
		self._NetGnLoss = base_types.UninitialisedField(self, 'NetGnLoss', AmountAndDirection44, False)

	@property
	def NtwkFee(self):
		return self._NtwkFee

	@NtwkFee.setter
	def NtwkFee(self, value):
		self._NtwkFee = value if value is not None else base_types.UninitialisedField(self, 'NtwkFee', AmountAndDirection44, False)

	@NtwkFee.deleter
	def NtwkFee(self):
		del self._NtwkFee
		self._NtwkFee = base_types.UninitialisedField(self, 'NtwkFee', AmountAndDirection44, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', AmountAndDirection44, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', AmountAndDirection44, False)

	@property
	def PmtLevyTax(self):
		return self._PmtLevyTax

	@PmtLevyTax.setter
	def PmtLevyTax(self, value):
		self._PmtLevyTax = value if value is not None else base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection44, False)

	@PmtLevyTax.deleter
	def PmtLevyTax(self):
		del self._PmtLevyTax
		self._PmtLevyTax = base_types.UninitialisedField(self, 'PmtLevyTax', AmountAndDirection44, False)

	@property
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if value is not None else base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection44, False)

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = base_types.UninitialisedField(self, 'RgltryAmt', AmountAndDirection44, False)

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
		self._ShppgAmt = value if value is not None else base_types.UninitialisedField(self, 'ShppgAmt', AmountAndDirection44, False)

	@ShppgAmt.deleter
	def ShppgAmt(self):
		del self._ShppgAmt
		self._ShppgAmt = base_types.UninitialisedField(self, 'ShppgAmt', AmountAndDirection44, False)

	@property
	def SpclCncssn(self):
		return self._SpclCncssn

	@SpclCncssn.setter
	def SpclCncssn(self, value):
		self._SpclCncssn = value if value is not None else base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection44, False)

	@SpclCncssn.deleter
	def SpclCncssn(self):
		del self._SpclCncssn
		self._SpclCncssn = base_types.UninitialisedField(self, 'SpclCncssn', AmountAndDirection44, False)

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if value is not None else base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection44, False)

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = base_types.UninitialisedField(self, 'StmpDty', AmountAndDirection44, False)

	@property
	def StockXchgTax(self):
		return self._StockXchgTax

	@StockXchgTax.setter
	def StockXchgTax(self, value):
		self._StockXchgTax = value if value is not None else base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection44, False)

	@StockXchgTax.deleter
	def StockXchgTax(self):
		del self._StockXchgTax
		self._StockXchgTax = base_types.UninitialisedField(self, 'StockXchgTax', AmountAndDirection44, False)

	@property
	def TradAmt(self):
		return self._TradAmt

	@TradAmt.setter
	def TradAmt(self, value):
		self._TradAmt = value if value is not None else base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection44, False)

	@TradAmt.deleter
	def TradAmt(self):
		del self._TradAmt
		self._TradAmt = base_types.UninitialisedField(self, 'TradAmt', AmountAndDirection44, False)

	@property
	def TrfTax(self):
		return self._TrfTax

	@TrfTax.setter
	def TrfTax(self, value):
		self._TrfTax = value if value is not None else base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection44, False)

	@TrfTax.deleter
	def TrfTax(self):
		del self._TrfTax
		self._TrfTax = base_types.UninitialisedField(self, 'TrfTax', AmountAndDirection44, False)

	@property
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if value is not None else base_types.UninitialisedField(self, 'TxTax', AmountAndDirection44, False)

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = base_types.UninitialisedField(self, 'TxTax', AmountAndDirection44, False)

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection44, False)

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = base_types.UninitialisedField(self, 'ValAddedTax', AmountAndDirection44, False)

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection44, False)

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = base_types.UninitialisedField(self, 'WhldgTax', AmountAndDirection44, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMntrAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkrAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDscntAllwnc', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclBrkrComssn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTaxCtrySpcfc', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetGnLoss', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrchFee', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclCncssn', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
	))