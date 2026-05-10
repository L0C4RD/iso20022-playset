from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ReportingAssetBreakdown2 import ReportingAssetBreakdown2

class AvailableFinancialResourcesAmount2(base_types._BaseFieldType):

	__slots__ = ["_CCPSkinInTheGame", "_OthrDfltFndCntrbtn", "_UfnddThrdPtyCmmtmnt", "_UfnddMmbCmmtmnt", "_TtlInitlMrgn", "_TtlPrfnddDfltFnd"]
	@property
	def CCPSkinInTheGame(self):
		return self._CCPSkinInTheGame

	@CCPSkinInTheGame.setter
	def CCPSkinInTheGame(self, value):
		self._CCPSkinInTheGame = value if type(value) != base_types.auto else self.make_default("CCPSkinInTheGame")

	@CCPSkinInTheGame.deleter
	def CCPSkinInTheGame(self):
		del self._CCPSkinInTheGame
		self._CCPSkinInTheGame = None

	@property
	def OthrDfltFndCntrbtn(self):
		return self._OthrDfltFndCntrbtn

	@OthrDfltFndCntrbtn.setter
	def OthrDfltFndCntrbtn(self, value):
		self._OthrDfltFndCntrbtn = value if type(value) != base_types.auto else self.make_default("OthrDfltFndCntrbtn")

	@OthrDfltFndCntrbtn.deleter
	def OthrDfltFndCntrbtn(self):
		del self._OthrDfltFndCntrbtn
		self._OthrDfltFndCntrbtn = None

	@property
	def UfnddThrdPtyCmmtmnt(self):
		return self._UfnddThrdPtyCmmtmnt

	@UfnddThrdPtyCmmtmnt.setter
	def UfnddThrdPtyCmmtmnt(self, value):
		self._UfnddThrdPtyCmmtmnt = value if type(value) != base_types.auto else self.make_default("UfnddThrdPtyCmmtmnt")

	@UfnddThrdPtyCmmtmnt.deleter
	def UfnddThrdPtyCmmtmnt(self):
		del self._UfnddThrdPtyCmmtmnt
		self._UfnddThrdPtyCmmtmnt = None

	@property
	def UfnddMmbCmmtmnt(self):
		return self._UfnddMmbCmmtmnt

	@UfnddMmbCmmtmnt.setter
	def UfnddMmbCmmtmnt(self, value):
		self._UfnddMmbCmmtmnt = value if type(value) != base_types.auto else self.make_default("UfnddMmbCmmtmnt")

	@UfnddMmbCmmtmnt.deleter
	def UfnddMmbCmmtmnt(self):
		del self._UfnddMmbCmmtmnt
		self._UfnddMmbCmmtmnt = None

	@property
	def TtlInitlMrgn(self):
		return self._TtlInitlMrgn

	@TtlInitlMrgn.setter
	def TtlInitlMrgn(self, value):
		self._TtlInitlMrgn = value if type(value) != base_types.auto else self.make_default("TtlInitlMrgn")

	@TtlInitlMrgn.deleter
	def TtlInitlMrgn(self):
		del self._TtlInitlMrgn
		self._TtlInitlMrgn = None

	@property
	def TtlPrfnddDfltFnd(self):
		return self._TtlPrfnddDfltFnd

	@TtlPrfnddDfltFnd.setter
	def TtlPrfnddDfltFnd(self, value):
		self._TtlPrfnddDfltFnd = value if type(value) != base_types.auto else self.make_default("TtlPrfnddDfltFnd")

	@TtlPrfnddDfltFnd.deleter
	def TtlPrfnddDfltFnd(self):
		del self._TtlPrfnddDfltFnd
		self._TtlPrfnddDfltFnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCPSkinInTheGame', type=ReportingAssetBreakdown2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDfltFndCntrbtn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfnddThrdPtyCmmtmnt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfnddMmbCmmtmnt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInitlMrgn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrfnddDfltFnd', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

