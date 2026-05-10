from . import base_types
import AmountAndDirection44

class OtherAmounts29(base_types._BaseFieldType):

	__slots__ = ["_ValAddedTax", "_PmtLevyTax", "_ChrgsFees", "_WhldgTax", "_Othr", "_ShppgAmt", "_StmpDty", "_TxTax", "_AcrdCptlstnAmt", "_TrfTax", "_CtryNtlFdrlTax", "_StockXchgTax", "_CsmptnTax", "_AcrdIntrstAmt", "_LclTax", "_RgltryAmt"]
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
	def TxTax(self):
		return self._TxTax

	@TxTax.setter
	def TxTax(self, value):
		self._TxTax = value if type(value) != auto else self.make_default("TxTax")

	@TxTax.deleter
	def TxTax(self):
		del self._TxTax
		self._TxTax = None

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
	def RgltryAmt(self):
		return self._RgltryAmt

	@RgltryAmt.setter
	def RgltryAmt(self, value):
		self._RgltryAmt = value if type(value) != auto else self.make_default("RgltryAmt")

	@RgltryAmt.deleter
	def RgltryAmt(self):
		del self._RgltryAmt
		self._RgltryAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValAddedTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtLevyTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdCptlstnAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryNtlFdrlTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchgTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CsmptnTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTax', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryAmt', type=AmountAndDirection44, min=0, max=1, mutex_group=None, array=False),
	))

