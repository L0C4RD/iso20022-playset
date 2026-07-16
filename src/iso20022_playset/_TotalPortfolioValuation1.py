# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection30
from . import AmountAndDirection31
from . import AmountAndRate2
from . import InvestmentFund1

class TotalPortfolioValuation1(base_types._BaseFieldType):

	__slots__ = ["_AcrdIncm", "_ExpnssPd", "_IncmRcvd", "_InvstmtFndDtls", "_PrvsTtlBookVal", "_PrvsTtlPrtflVal", "_RealsdGnOrLoss", "_TtlBookVal", "_TtlBookValChng", "_TtlDsbrsmnts", "_TtlPrtflVal", "_TtlPrtflValChng", "_TtlRcts", "_UrlsdGnOrLoss"]
	@property
	def AcrdIncm(self):
		return self._AcrdIncm

	@AcrdIncm.setter
	def AcrdIncm(self, value):
		self._AcrdIncm = value if value is not None else base_types.UninitialisedField(self, 'AcrdIncm', AmountAndDirection30, False)

	@AcrdIncm.deleter
	def AcrdIncm(self):
		del self._AcrdIncm
		self._AcrdIncm = base_types.UninitialisedField(self, 'AcrdIncm', AmountAndDirection30, False)

	@property
	def ExpnssPd(self):
		return self._ExpnssPd

	@ExpnssPd.setter
	def ExpnssPd(self, value):
		self._ExpnssPd = value if value is not None else base_types.UninitialisedField(self, 'ExpnssPd', AmountAndDirection30, False)

	@ExpnssPd.deleter
	def ExpnssPd(self):
		del self._ExpnssPd
		self._ExpnssPd = base_types.UninitialisedField(self, 'ExpnssPd', AmountAndDirection30, False)

	@property
	def IncmRcvd(self):
		return self._IncmRcvd

	@IncmRcvd.setter
	def IncmRcvd(self, value):
		self._IncmRcvd = value if value is not None else base_types.UninitialisedField(self, 'IncmRcvd', AmountAndDirection30, False)

	@IncmRcvd.deleter
	def IncmRcvd(self):
		del self._IncmRcvd
		self._IncmRcvd = base_types.UninitialisedField(self, 'IncmRcvd', AmountAndDirection30, False)

	@property
	def InvstmtFndDtls(self):
		return self._InvstmtFndDtls

	@InvstmtFndDtls.setter
	def InvstmtFndDtls(self, value):
		self._InvstmtFndDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndDtls', InvestmentFund1, True)

	@InvstmtFndDtls.deleter
	def InvstmtFndDtls(self):
		del self._InvstmtFndDtls
		self._InvstmtFndDtls = base_types.UninitialisedField(self, 'InvstmtFndDtls', InvestmentFund1, True)

	@property
	def PrvsTtlBookVal(self):
		return self._PrvsTtlBookVal

	@PrvsTtlBookVal.setter
	def PrvsTtlBookVal(self, value):
		self._PrvsTtlBookVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlBookVal', AmountAndDirection30, False)

	@PrvsTtlBookVal.deleter
	def PrvsTtlBookVal(self):
		del self._PrvsTtlBookVal
		self._PrvsTtlBookVal = base_types.UninitialisedField(self, 'PrvsTtlBookVal', AmountAndDirection30, False)

	@property
	def PrvsTtlPrtflVal(self):
		return self._PrvsTtlPrtflVal

	@PrvsTtlPrtflVal.setter
	def PrvsTtlPrtflVal(self, value):
		self._PrvsTtlPrtflVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlPrtflVal', AmountAndDirection30, False)

	@PrvsTtlPrtflVal.deleter
	def PrvsTtlPrtflVal(self):
		del self._PrvsTtlPrtflVal
		self._PrvsTtlPrtflVal = base_types.UninitialisedField(self, 'PrvsTtlPrtflVal', AmountAndDirection30, False)

	@property
	def RealsdGnOrLoss(self):
		return self._RealsdGnOrLoss

	@RealsdGnOrLoss.setter
	def RealsdGnOrLoss(self, value):
		self._RealsdGnOrLoss = value if value is not None else base_types.UninitialisedField(self, 'RealsdGnOrLoss', AmountAndDirection31, False)

	@RealsdGnOrLoss.deleter
	def RealsdGnOrLoss(self):
		del self._RealsdGnOrLoss
		self._RealsdGnOrLoss = base_types.UninitialisedField(self, 'RealsdGnOrLoss', AmountAndDirection31, False)

	@property
	def TtlBookVal(self):
		return self._TtlBookVal

	@TtlBookVal.setter
	def TtlBookVal(self, value):
		self._TtlBookVal = value if value is not None else base_types.UninitialisedField(self, 'TtlBookVal', AmountAndDirection30, False)

	@TtlBookVal.deleter
	def TtlBookVal(self):
		del self._TtlBookVal
		self._TtlBookVal = base_types.UninitialisedField(self, 'TtlBookVal', AmountAndDirection30, False)

	@property
	def TtlBookValChng(self):
		return self._TtlBookValChng

	@TtlBookValChng.setter
	def TtlBookValChng(self, value):
		self._TtlBookValChng = value if value is not None else base_types.UninitialisedField(self, 'TtlBookValChng', AmountAndRate2, False)

	@TtlBookValChng.deleter
	def TtlBookValChng(self):
		del self._TtlBookValChng
		self._TtlBookValChng = base_types.UninitialisedField(self, 'TtlBookValChng', AmountAndRate2, False)

	@property
	def TtlDsbrsmnts(self):
		return self._TtlDsbrsmnts

	@TtlDsbrsmnts.setter
	def TtlDsbrsmnts(self, value):
		self._TtlDsbrsmnts = value if value is not None else base_types.UninitialisedField(self, 'TtlDsbrsmnts', AmountAndDirection30, False)

	@TtlDsbrsmnts.deleter
	def TtlDsbrsmnts(self):
		del self._TtlDsbrsmnts
		self._TtlDsbrsmnts = base_types.UninitialisedField(self, 'TtlDsbrsmnts', AmountAndDirection30, False)

	@property
	def TtlPrtflVal(self):
		return self._TtlPrtflVal

	@TtlPrtflVal.setter
	def TtlPrtflVal(self, value):
		self._TtlPrtflVal = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtflVal', AmountAndDirection30, False)

	@TtlPrtflVal.deleter
	def TtlPrtflVal(self):
		del self._TtlPrtflVal
		self._TtlPrtflVal = base_types.UninitialisedField(self, 'TtlPrtflVal', AmountAndDirection30, False)

	@property
	def TtlPrtflValChng(self):
		return self._TtlPrtflValChng

	@TtlPrtflValChng.setter
	def TtlPrtflValChng(self, value):
		self._TtlPrtflValChng = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtflValChng', AmountAndRate2, False)

	@TtlPrtflValChng.deleter
	def TtlPrtflValChng(self):
		del self._TtlPrtflValChng
		self._TtlPrtflValChng = base_types.UninitialisedField(self, 'TtlPrtflValChng', AmountAndRate2, False)

	@property
	def TtlRcts(self):
		return self._TtlRcts

	@TtlRcts.setter
	def TtlRcts(self, value):
		self._TtlRcts = value if value is not None else base_types.UninitialisedField(self, 'TtlRcts', AmountAndDirection30, False)

	@TtlRcts.deleter
	def TtlRcts(self):
		del self._TtlRcts
		self._TtlRcts = base_types.UninitialisedField(self, 'TtlRcts', AmountAndDirection30, False)

	@property
	def UrlsdGnOrLoss(self):
		return self._UrlsdGnOrLoss

	@UrlsdGnOrLoss.setter
	def UrlsdGnOrLoss(self, value):
		self._UrlsdGnOrLoss = value if value is not None else base_types.UninitialisedField(self, 'UrlsdGnOrLoss', AmountAndDirection31, False)

	@UrlsdGnOrLoss.deleter
	def UrlsdGnOrLoss(self):
		del self._UrlsdGnOrLoss
		self._UrlsdGnOrLoss = base_types.UninitialisedField(self, 'UrlsdGnOrLoss', AmountAndDirection31, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIncm', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExpnssPd', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmRcvd', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtFndDtls', type=InvestmentFund1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsTtlBookVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlPrtflVal', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RealsdGnOrLoss', type=AmountAndDirection31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookVal', type=AmountAndDirection30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBookValChng', type=AmountAndRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDsbrsmnts', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtflVal', type=AmountAndDirection30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtflValChng', type=AmountAndRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRcts', type=AmountAndDirection30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrlsdGnOrLoss', type=AmountAndDirection31, min=0, max=1, mutex_group=None, array=False),
	))