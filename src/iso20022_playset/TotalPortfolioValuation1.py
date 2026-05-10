import base_types
import AmountAndDirection31
import InvestmentFund1
import AmountAndDirection30
import AmountAndRate2

class TotalPortfolioValuation1(base_types._BaseFieldType):

	__slots__ = ["_TtlPrtflVal", "_InvstmtFndDtls", "_RealsdGnOrLoss", "_PrvsTtlPrtflVal", "_IncmRcvd", "_ExpnssPd", "_TtlBookVal", "_TtlDsbrsmnts", "_TtlRcts", "_AcrdIncm", "_PrvsTtlBookVal", "_TtlPrtflValChng", "_UrlsdGnOrLoss", "_TtlBookValChng"]
	@property
	def TtlPrtflVal(self):
		return self._TtlPrtflVal

	@TtlPrtflVal.setter
	def TtlPrtflVal(self, value):
		self._TtlPrtflVal = value if type(value) != auto else self.make_default("TtlPrtflVal")

	@TtlPrtflVal.deleter
	def TtlPrtflVal(self):
		del self._TtlPrtflVal
		self._TtlPrtflVal = None

	@property
	def InvstmtFndDtls(self):
		return self._InvstmtFndDtls

	@InvstmtFndDtls.setter
	def InvstmtFndDtls(self, value):
		self._InvstmtFndDtls = value if type(value) != auto else self.make_default("InvstmtFndDtls")

	@InvstmtFndDtls.deleter
	def InvstmtFndDtls(self):
		del self._InvstmtFndDtls
		self._InvstmtFndDtls = None

	@property
	def RealsdGnOrLoss(self):
		return self._RealsdGnOrLoss

	@RealsdGnOrLoss.setter
	def RealsdGnOrLoss(self, value):
		self._RealsdGnOrLoss = value if type(value) != auto else self.make_default("RealsdGnOrLoss")

	@RealsdGnOrLoss.deleter
	def RealsdGnOrLoss(self):
		del self._RealsdGnOrLoss
		self._RealsdGnOrLoss = None

	@property
	def PrvsTtlPrtflVal(self):
		return self._PrvsTtlPrtflVal

	@PrvsTtlPrtflVal.setter
	def PrvsTtlPrtflVal(self, value):
		self._PrvsTtlPrtflVal = value if type(value) != auto else self.make_default("PrvsTtlPrtflVal")

	@PrvsTtlPrtflVal.deleter
	def PrvsTtlPrtflVal(self):
		del self._PrvsTtlPrtflVal
		self._PrvsTtlPrtflVal = None

	@property
	def IncmRcvd(self):
		return self._IncmRcvd

	@IncmRcvd.setter
	def IncmRcvd(self, value):
		self._IncmRcvd = value if type(value) != auto else self.make_default("IncmRcvd")

	@IncmRcvd.deleter
	def IncmRcvd(self):
		del self._IncmRcvd
		self._IncmRcvd = None

	@property
	def ExpnssPd(self):
		return self._ExpnssPd

	@ExpnssPd.setter
	def ExpnssPd(self, value):
		self._ExpnssPd = value if type(value) != auto else self.make_default("ExpnssPd")

	@ExpnssPd.deleter
	def ExpnssPd(self):
		del self._ExpnssPd
		self._ExpnssPd = None

	@property
	def TtlBookVal(self):
		return self._TtlBookVal

	@TtlBookVal.setter
	def TtlBookVal(self, value):
		self._TtlBookVal = value if type(value) != auto else self.make_default("TtlBookVal")

	@TtlBookVal.deleter
	def TtlBookVal(self):
		del self._TtlBookVal
		self._TtlBookVal = None

	@property
	def TtlDsbrsmnts(self):
		return self._TtlDsbrsmnts

	@TtlDsbrsmnts.setter
	def TtlDsbrsmnts(self, value):
		self._TtlDsbrsmnts = value if type(value) != auto else self.make_default("TtlDsbrsmnts")

	@TtlDsbrsmnts.deleter
	def TtlDsbrsmnts(self):
		del self._TtlDsbrsmnts
		self._TtlDsbrsmnts = None

	@property
	def TtlRcts(self):
		return self._TtlRcts

	@TtlRcts.setter
	def TtlRcts(self, value):
		self._TtlRcts = value if type(value) != auto else self.make_default("TtlRcts")

	@TtlRcts.deleter
	def TtlRcts(self):
		del self._TtlRcts
		self._TtlRcts = None

	@property
	def AcrdIncm(self):
		return self._AcrdIncm

	@AcrdIncm.setter
	def AcrdIncm(self, value):
		self._AcrdIncm = value if type(value) != auto else self.make_default("AcrdIncm")

	@AcrdIncm.deleter
	def AcrdIncm(self):
		del self._AcrdIncm
		self._AcrdIncm = None

	@property
	def PrvsTtlBookVal(self):
		return self._PrvsTtlBookVal

	@PrvsTtlBookVal.setter
	def PrvsTtlBookVal(self, value):
		self._PrvsTtlBookVal = value if type(value) != auto else self.make_default("PrvsTtlBookVal")

	@PrvsTtlBookVal.deleter
	def PrvsTtlBookVal(self):
		del self._PrvsTtlBookVal
		self._PrvsTtlBookVal = None

	@property
	def TtlPrtflValChng(self):
		return self._TtlPrtflValChng

	@TtlPrtflValChng.setter
	def TtlPrtflValChng(self, value):
		self._TtlPrtflValChng = value if type(value) != auto else self.make_default("TtlPrtflValChng")

	@TtlPrtflValChng.deleter
	def TtlPrtflValChng(self):
		del self._TtlPrtflValChng
		self._TtlPrtflValChng = None

	@property
	def UrlsdGnOrLoss(self):
		return self._UrlsdGnOrLoss

	@UrlsdGnOrLoss.setter
	def UrlsdGnOrLoss(self, value):
		self._UrlsdGnOrLoss = value if type(value) != auto else self.make_default("UrlsdGnOrLoss")

	@UrlsdGnOrLoss.deleter
	def UrlsdGnOrLoss(self):
		del self._UrlsdGnOrLoss
		self._UrlsdGnOrLoss = None

	@property
	def TtlBookValChng(self):
		return self._TtlBookValChng

	@TtlBookValChng.setter
	def TtlBookValChng(self, value):
		self._TtlBookValChng = value if type(value) != auto else self.make_default("TtlBookValChng")

	@TtlBookValChng.deleter
	def TtlBookValChng(self):
		del self._TtlBookValChng
		self._TtlBookValChng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlPrtflVal', type=AmountAndDirection30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndDtls', type=InvestmentFund1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RealsdGnOrLoss', type=AmountAndDirection31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlPrtflVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmRcvd', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExpnssPd', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookVal', type=AmountAndDirection30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDsbrsmnts', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRcts', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIncm', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlBookVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtflValChng', type=AmountAndRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrlsdGnOrLoss', type=AmountAndDirection31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookValChng', type=AmountAndRate2, min=0, max=1, mutex_group=None, array=False),
	))

