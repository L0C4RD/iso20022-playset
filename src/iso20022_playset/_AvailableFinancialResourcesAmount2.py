# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ReportingAssetBreakdown2

class AvailableFinancialResourcesAmount2(base_types._BaseFieldType):

	__slots__ = ["_CCPSkinInTheGame", "_OthrDfltFndCntrbtn", "_TtlInitlMrgn", "_TtlPrfnddDfltFnd", "_UfnddMmbCmmtmnt", "_UfnddThrdPtyCmmtmnt"]
	@property
	def CCPSkinInTheGame(self):
		return self._CCPSkinInTheGame

	@CCPSkinInTheGame.setter
	def CCPSkinInTheGame(self, value):
		self._CCPSkinInTheGame = value if value is not None else base_types.UninitialisedField(self, 'CCPSkinInTheGame', ReportingAssetBreakdown2, True)

	@CCPSkinInTheGame.deleter
	def CCPSkinInTheGame(self):
		del self._CCPSkinInTheGame
		self._CCPSkinInTheGame = base_types.UninitialisedField(self, 'CCPSkinInTheGame', ReportingAssetBreakdown2, True)

	@property
	def OthrDfltFndCntrbtn(self):
		return self._OthrDfltFndCntrbtn

	@OthrDfltFndCntrbtn.setter
	def OthrDfltFndCntrbtn(self, value):
		self._OthrDfltFndCntrbtn = value if value is not None else base_types.UninitialisedField(self, 'OthrDfltFndCntrbtn', ActiveCurrencyAndAmount, False)

	@OthrDfltFndCntrbtn.deleter
	def OthrDfltFndCntrbtn(self):
		del self._OthrDfltFndCntrbtn
		self._OthrDfltFndCntrbtn = base_types.UninitialisedField(self, 'OthrDfltFndCntrbtn', ActiveCurrencyAndAmount, False)

	@property
	def TtlInitlMrgn(self):
		return self._TtlInitlMrgn

	@TtlInitlMrgn.setter
	def TtlInitlMrgn(self, value):
		self._TtlInitlMrgn = value if value is not None else base_types.UninitialisedField(self, 'TtlInitlMrgn', ActiveCurrencyAndAmount, False)

	@TtlInitlMrgn.deleter
	def TtlInitlMrgn(self):
		del self._TtlInitlMrgn
		self._TtlInitlMrgn = base_types.UninitialisedField(self, 'TtlInitlMrgn', ActiveCurrencyAndAmount, False)

	@property
	def TtlPrfnddDfltFnd(self):
		return self._TtlPrfnddDfltFnd

	@TtlPrfnddDfltFnd.setter
	def TtlPrfnddDfltFnd(self, value):
		self._TtlPrfnddDfltFnd = value if value is not None else base_types.UninitialisedField(self, 'TtlPrfnddDfltFnd', ActiveCurrencyAndAmount, False)

	@TtlPrfnddDfltFnd.deleter
	def TtlPrfnddDfltFnd(self):
		del self._TtlPrfnddDfltFnd
		self._TtlPrfnddDfltFnd = base_types.UninitialisedField(self, 'TtlPrfnddDfltFnd', ActiveCurrencyAndAmount, False)

	@property
	def UfnddMmbCmmtmnt(self):
		return self._UfnddMmbCmmtmnt

	@UfnddMmbCmmtmnt.setter
	def UfnddMmbCmmtmnt(self, value):
		self._UfnddMmbCmmtmnt = value if value is not None else base_types.UninitialisedField(self, 'UfnddMmbCmmtmnt', ActiveCurrencyAndAmount, False)

	@UfnddMmbCmmtmnt.deleter
	def UfnddMmbCmmtmnt(self):
		del self._UfnddMmbCmmtmnt
		self._UfnddMmbCmmtmnt = base_types.UninitialisedField(self, 'UfnddMmbCmmtmnt', ActiveCurrencyAndAmount, False)

	@property
	def UfnddThrdPtyCmmtmnt(self):
		return self._UfnddThrdPtyCmmtmnt

	@UfnddThrdPtyCmmtmnt.setter
	def UfnddThrdPtyCmmtmnt(self, value):
		self._UfnddThrdPtyCmmtmnt = value if value is not None else base_types.UninitialisedField(self, 'UfnddThrdPtyCmmtmnt', ActiveCurrencyAndAmount, False)

	@UfnddThrdPtyCmmtmnt.deleter
	def UfnddThrdPtyCmmtmnt(self):
		del self._UfnddThrdPtyCmmtmnt
		self._UfnddThrdPtyCmmtmnt = base_types.UninitialisedField(self, 'UfnddThrdPtyCmmtmnt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCPSkinInTheGame', type=ReportingAssetBreakdown2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDfltFndCntrbtn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInitlMrgn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrfnddDfltFnd', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfnddMmbCmmtmnt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UfnddThrdPtyCmmtmnt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))