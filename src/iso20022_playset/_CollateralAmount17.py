from . import base_types
from .AmountAndDirection53 import AmountAndDirection53
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .CollateralTransactionAmountBreakdown2 import CollateralTransactionAmountBreakdown2

class CollateralAmount17(base_types._BaseFieldType):

	__slots__ = ["_TtlPdgCollIn", "_TxAmtBrkdwn", "_TtlValOfOwnColl", "_TtlAcrdIntrst", "_TtlCollReqrd", "_TtlOfPrncpls", "_Mrgn", "_TermntnTxAmt", "_TtlPdgCollOut", "_TtlValOfReusdColl", "_TxAmt", "_ValOfCollHeld", "_TtlXpsr", "_TtlCshFaild"]
	@property
	def TtlPdgCollIn(self):
		return self._TtlPdgCollIn

	@TtlPdgCollIn.setter
	def TtlPdgCollIn(self, value):
		self._TtlPdgCollIn = value if type(value) != base_types.auto else self.make_default("TtlPdgCollIn")

	@TtlPdgCollIn.deleter
	def TtlPdgCollIn(self):
		del self._TtlPdgCollIn
		self._TtlPdgCollIn = None

	@property
	def TxAmtBrkdwn(self):
		return self._TxAmtBrkdwn

	@TxAmtBrkdwn.setter
	def TxAmtBrkdwn(self, value):
		self._TxAmtBrkdwn = value if type(value) != base_types.auto else self.make_default("TxAmtBrkdwn")

	@TxAmtBrkdwn.deleter
	def TxAmtBrkdwn(self):
		del self._TxAmtBrkdwn
		self._TxAmtBrkdwn = None

	@property
	def TtlValOfOwnColl(self):
		return self._TtlValOfOwnColl

	@TtlValOfOwnColl.setter
	def TtlValOfOwnColl(self, value):
		self._TtlValOfOwnColl = value if type(value) != base_types.auto else self.make_default("TtlValOfOwnColl")

	@TtlValOfOwnColl.deleter
	def TtlValOfOwnColl(self):
		del self._TtlValOfOwnColl
		self._TtlValOfOwnColl = None

	@property
	def TtlAcrdIntrst(self):
		return self._TtlAcrdIntrst

	@TtlAcrdIntrst.setter
	def TtlAcrdIntrst(self, value):
		self._TtlAcrdIntrst = value if type(value) != base_types.auto else self.make_default("TtlAcrdIntrst")

	@TtlAcrdIntrst.deleter
	def TtlAcrdIntrst(self):
		del self._TtlAcrdIntrst
		self._TtlAcrdIntrst = None

	@property
	def TtlCollReqrd(self):
		return self._TtlCollReqrd

	@TtlCollReqrd.setter
	def TtlCollReqrd(self, value):
		self._TtlCollReqrd = value if type(value) != base_types.auto else self.make_default("TtlCollReqrd")

	@TtlCollReqrd.deleter
	def TtlCollReqrd(self):
		del self._TtlCollReqrd
		self._TtlCollReqrd = None

	@property
	def TtlOfPrncpls(self):
		return self._TtlOfPrncpls

	@TtlOfPrncpls.setter
	def TtlOfPrncpls(self, value):
		self._TtlOfPrncpls = value if type(value) != base_types.auto else self.make_default("TtlOfPrncpls")

	@TtlOfPrncpls.deleter
	def TtlOfPrncpls(self):
		del self._TtlOfPrncpls
		self._TtlOfPrncpls = None

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
	def TermntnTxAmt(self):
		return self._TermntnTxAmt

	@TermntnTxAmt.setter
	def TermntnTxAmt(self, value):
		self._TermntnTxAmt = value if type(value) != base_types.auto else self.make_default("TermntnTxAmt")

	@TermntnTxAmt.deleter
	def TermntnTxAmt(self):
		del self._TermntnTxAmt
		self._TermntnTxAmt = None

	@property
	def TtlPdgCollOut(self):
		return self._TtlPdgCollOut

	@TtlPdgCollOut.setter
	def TtlPdgCollOut(self, value):
		self._TtlPdgCollOut = value if type(value) != base_types.auto else self.make_default("TtlPdgCollOut")

	@TtlPdgCollOut.deleter
	def TtlPdgCollOut(self):
		del self._TtlPdgCollOut
		self._TtlPdgCollOut = None

	@property
	def TtlValOfReusdColl(self):
		return self._TtlValOfReusdColl

	@TtlValOfReusdColl.setter
	def TtlValOfReusdColl(self, value):
		self._TtlValOfReusdColl = value if type(value) != base_types.auto else self.make_default("TtlValOfReusdColl")

	@TtlValOfReusdColl.deleter
	def TtlValOfReusdColl(self):
		del self._TtlValOfReusdColl
		self._TtlValOfReusdColl = None

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if type(value) != base_types.auto else self.make_default("TxAmt")

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = None

	@property
	def ValOfCollHeld(self):
		return self._ValOfCollHeld

	@ValOfCollHeld.setter
	def ValOfCollHeld(self, value):
		self._ValOfCollHeld = value if type(value) != base_types.auto else self.make_default("ValOfCollHeld")

	@ValOfCollHeld.deleter
	def ValOfCollHeld(self):
		del self._ValOfCollHeld
		self._ValOfCollHeld = None

	@property
	def TtlXpsr(self):
		return self._TtlXpsr

	@TtlXpsr.setter
	def TtlXpsr(self, value):
		self._TtlXpsr = value if type(value) != base_types.auto else self.make_default("TtlXpsr")

	@TtlXpsr.deleter
	def TtlXpsr(self):
		del self._TtlXpsr
		self._TtlXpsr = None

	@property
	def TtlCshFaild(self):
		return self._TtlCshFaild

	@TtlCshFaild.setter
	def TtlCshFaild(self, value):
		self._TtlCshFaild = value if type(value) != base_types.auto else self.make_default("TtlCshFaild")

	@TtlCshFaild.deleter
	def TtlCshFaild(self):
		del self._TtlCshFaild
		self._TtlCshFaild = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlPdgCollIn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmtBrkdwn', type=CollateralTransactionAmountBreakdown2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlValOfOwnColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAcrdIntrst', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCollReqrd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOfPrncpls', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnTxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgCollOut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfReusdColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValOfCollHeld', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlXpsr', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshFaild', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

