# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AmountAndDirection53

class CollateralAmount15(base_types._BaseFieldType):

	__slots__ = ["_Mrgn", "_TtlAcrdIntrst", "_TtlCollReqrd", "_TtlCshFaild", "_TtlFeesComssns", "_TtlOfPrncpls", "_TtlPdgCollIn", "_TtlPdgCollOut", "_TtlValOfOwnColl", "_TtlValOfReusdColl", "_TtlXpsr", "_ValOfCollHeld"]
	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if value is not None else base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection53, False)

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = base_types.UninitialisedField(self, 'Mrgn', AmountAndDirection53, False)

	@property
	def TtlAcrdIntrst(self):
		return self._TtlAcrdIntrst

	@TtlAcrdIntrst.setter
	def TtlAcrdIntrst(self, value):
		self._TtlAcrdIntrst = value if value is not None else base_types.UninitialisedField(self, 'TtlAcrdIntrst', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlAcrdIntrst.deleter
	def TtlAcrdIntrst(self):
		del self._TtlAcrdIntrst
		self._TtlAcrdIntrst = base_types.UninitialisedField(self, 'TtlAcrdIntrst', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlCollReqrd(self):
		return self._TtlCollReqrd

	@TtlCollReqrd.setter
	def TtlCollReqrd(self, value):
		self._TtlCollReqrd = value if value is not None else base_types.UninitialisedField(self, 'TtlCollReqrd', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlCollReqrd.deleter
	def TtlCollReqrd(self):
		del self._TtlCollReqrd
		self._TtlCollReqrd = base_types.UninitialisedField(self, 'TtlCollReqrd', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlCshFaild(self):
		return self._TtlCshFaild

	@TtlCshFaild.setter
	def TtlCshFaild(self, value):
		self._TtlCshFaild = value if value is not None else base_types.UninitialisedField(self, 'TtlCshFaild', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlCshFaild.deleter
	def TtlCshFaild(self):
		del self._TtlCshFaild
		self._TtlCshFaild = base_types.UninitialisedField(self, 'TtlCshFaild', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlFeesComssns(self):
		return self._TtlFeesComssns

	@TtlFeesComssns.setter
	def TtlFeesComssns(self, value):
		self._TtlFeesComssns = value if value is not None else base_types.UninitialisedField(self, 'TtlFeesComssns', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlFeesComssns.deleter
	def TtlFeesComssns(self):
		del self._TtlFeesComssns
		self._TtlFeesComssns = base_types.UninitialisedField(self, 'TtlFeesComssns', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlOfPrncpls(self):
		return self._TtlOfPrncpls

	@TtlOfPrncpls.setter
	def TtlOfPrncpls(self, value):
		self._TtlOfPrncpls = value if value is not None else base_types.UninitialisedField(self, 'TtlOfPrncpls', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlOfPrncpls.deleter
	def TtlOfPrncpls(self):
		del self._TtlOfPrncpls
		self._TtlOfPrncpls = base_types.UninitialisedField(self, 'TtlOfPrncpls', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlPdgCollIn(self):
		return self._TtlPdgCollIn

	@TtlPdgCollIn.setter
	def TtlPdgCollIn(self, value):
		self._TtlPdgCollIn = value if value is not None else base_types.UninitialisedField(self, 'TtlPdgCollIn', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlPdgCollIn.deleter
	def TtlPdgCollIn(self):
		del self._TtlPdgCollIn
		self._TtlPdgCollIn = base_types.UninitialisedField(self, 'TtlPdgCollIn', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlPdgCollOut(self):
		return self._TtlPdgCollOut

	@TtlPdgCollOut.setter
	def TtlPdgCollOut(self, value):
		self._TtlPdgCollOut = value if value is not None else base_types.UninitialisedField(self, 'TtlPdgCollOut', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlPdgCollOut.deleter
	def TtlPdgCollOut(self):
		del self._TtlPdgCollOut
		self._TtlPdgCollOut = base_types.UninitialisedField(self, 'TtlPdgCollOut', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlValOfOwnColl(self):
		return self._TtlValOfOwnColl

	@TtlValOfOwnColl.setter
	def TtlValOfOwnColl(self, value):
		self._TtlValOfOwnColl = value if value is not None else base_types.UninitialisedField(self, 'TtlValOfOwnColl', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlValOfOwnColl.deleter
	def TtlValOfOwnColl(self):
		del self._TtlValOfOwnColl
		self._TtlValOfOwnColl = base_types.UninitialisedField(self, 'TtlValOfOwnColl', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlValOfReusdColl(self):
		return self._TtlValOfReusdColl

	@TtlValOfReusdColl.setter
	def TtlValOfReusdColl(self, value):
		self._TtlValOfReusdColl = value if value is not None else base_types.UninitialisedField(self, 'TtlValOfReusdColl', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlValOfReusdColl.deleter
	def TtlValOfReusdColl(self):
		del self._TtlValOfReusdColl
		self._TtlValOfReusdColl = base_types.UninitialisedField(self, 'TtlValOfReusdColl', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlXpsr(self):
		return self._TtlXpsr

	@TtlXpsr.setter
	def TtlXpsr(self, value):
		self._TtlXpsr = value if value is not None else base_types.UninitialisedField(self, 'TtlXpsr', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlXpsr.deleter
	def TtlXpsr(self):
		del self._TtlXpsr
		self._TtlXpsr = base_types.UninitialisedField(self, 'TtlXpsr', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def ValOfCollHeld(self):
		return self._ValOfCollHeld

	@ValOfCollHeld.setter
	def ValOfCollHeld(self, value):
		self._ValOfCollHeld = value if value is not None else base_types.UninitialisedField(self, 'ValOfCollHeld', ActiveOrHistoricCurrencyAndAmount, False)

	@ValOfCollHeld.deleter
	def ValOfCollHeld(self):
		del self._ValOfCollHeld
		self._ValOfCollHeld = base_types.UninitialisedField(self, 'ValOfCollHeld', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mrgn', type=AmountAndDirection53, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAcrdIntrst', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCollReqrd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshFaild', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFeesComssns', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOfPrncpls', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgCollIn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgCollOut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfOwnColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfReusdColl', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlXpsr', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValOfCollHeld', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))