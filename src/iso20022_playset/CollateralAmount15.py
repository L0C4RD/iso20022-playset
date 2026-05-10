import base_types
import ActiveOrHistoricCurrencyAndAmount
import AmountAndDirection53

class CollateralAmount15(base_types._BaseFieldType):

	__slots__ = ["_TtlCshFaild", "_TtlValOfOwnColl", "_TtlCollReqrd", "_TtlFeesComssns", "_Mrgn", "_TtlAcrdIntrst", "_TtlOfPrncpls", "_TtlXpsr", "_TtlValOfReusdColl", "_ValOfCollHeld", "_TtlPdgCollIn", "_TtlPdgCollOut"]
	@property
	def TtlCshFaild(self):
		return self._TtlCshFaild

	@TtlCshFaild.setter
	def TtlCshFaild(self, value):
		self._TtlCshFaild = value if type(value) != auto else self.make_default("TtlCshFaild")

	@TtlCshFaild.deleter
	def TtlCshFaild(self):
		del self._TtlCshFaild
		self._TtlCshFaild = None

	@property
	def TtlValOfOwnColl(self):
		return self._TtlValOfOwnColl

	@TtlValOfOwnColl.setter
	def TtlValOfOwnColl(self, value):
		self._TtlValOfOwnColl = value if type(value) != auto else self.make_default("TtlValOfOwnColl")

	@TtlValOfOwnColl.deleter
	def TtlValOfOwnColl(self):
		del self._TtlValOfOwnColl
		self._TtlValOfOwnColl = None

	@property
	def TtlCollReqrd(self):
		return self._TtlCollReqrd

	@TtlCollReqrd.setter
	def TtlCollReqrd(self, value):
		self._TtlCollReqrd = value if type(value) != auto else self.make_default("TtlCollReqrd")

	@TtlCollReqrd.deleter
	def TtlCollReqrd(self):
		del self._TtlCollReqrd
		self._TtlCollReqrd = None

	@property
	def TtlFeesComssns(self):
		return self._TtlFeesComssns

	@TtlFeesComssns.setter
	def TtlFeesComssns(self, value):
		self._TtlFeesComssns = value if type(value) != auto else self.make_default("TtlFeesComssns")

	@TtlFeesComssns.deleter
	def TtlFeesComssns(self):
		del self._TtlFeesComssns
		self._TtlFeesComssns = None

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
	def TtlAcrdIntrst(self):
		return self._TtlAcrdIntrst

	@TtlAcrdIntrst.setter
	def TtlAcrdIntrst(self, value):
		self._TtlAcrdIntrst = value if type(value) != auto else self.make_default("TtlAcrdIntrst")

	@TtlAcrdIntrst.deleter
	def TtlAcrdIntrst(self):
		del self._TtlAcrdIntrst
		self._TtlAcrdIntrst = None

	@property
	def TtlOfPrncpls(self):
		return self._TtlOfPrncpls

	@TtlOfPrncpls.setter
	def TtlOfPrncpls(self, value):
		self._TtlOfPrncpls = value if type(value) != auto else self.make_default("TtlOfPrncpls")

	@TtlOfPrncpls.deleter
	def TtlOfPrncpls(self):
		del self._TtlOfPrncpls
		self._TtlOfPrncpls = None

	@property
	def TtlXpsr(self):
		return self._TtlXpsr

	@TtlXpsr.setter
	def TtlXpsr(self, value):
		self._TtlXpsr = value if type(value) != auto else self.make_default("TtlXpsr")

	@TtlXpsr.deleter
	def TtlXpsr(self):
		del self._TtlXpsr
		self._TtlXpsr = None

	@property
	def TtlValOfReusdColl(self):
		return self._TtlValOfReusdColl

	@TtlValOfReusdColl.setter
	def TtlValOfReusdColl(self, value):
		self._TtlValOfReusdColl = value if type(value) != auto else self.make_default("TtlValOfReusdColl")

	@TtlValOfReusdColl.deleter
	def TtlValOfReusdColl(self):
		del self._TtlValOfReusdColl
		self._TtlValOfReusdColl = None

	@property
	def ValOfCollHeld(self):
		return self._ValOfCollHeld

	@ValOfCollHeld.setter
	def ValOfCollHeld(self, value):
		self._ValOfCollHeld = value if type(value) != auto else self.make_default("ValOfCollHeld")

	@ValOfCollHeld.deleter
	def ValOfCollHeld(self):
		del self._ValOfCollHeld
		self._ValOfCollHeld = None

	@property
	def TtlPdgCollIn(self):
		return self._TtlPdgCollIn

	@TtlPdgCollIn.setter
	def TtlPdgCollIn(self, value):
		self._TtlPdgCollIn = value if type(value) != auto else self.make_default("TtlPdgCollIn")

	@TtlPdgCollIn.deleter
	def TtlPdgCollIn(self):
		del self._TtlPdgCollIn
		self._TtlPdgCollIn = None

	@property
	def TtlPdgCollOut(self):
		return self._TtlPdgCollOut

	@TtlPdgCollOut.setter
	def TtlPdgCollOut(self, value):
		self._TtlPdgCollOut = value if type(value) != auto else self.make_default("TtlPdgCollOut")

	@TtlPdgCollOut.deleter
	def TtlPdgCollOut(self):
		del self._TtlPdgCollOut
		self._TtlPdgCollOut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCshFaild', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfOwnColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCollReqrd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFeesComssns', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAcrdIntrst', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOfPrncpls', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlXpsr', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfReusdColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValOfCollHeld', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgCollIn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgCollOut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

