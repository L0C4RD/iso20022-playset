# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection59
from . import Exact3NumericText
from . import LegalFramework4Choice
from . import Rate2
from . import RateName2
from . import RateType67Choice
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax16Text
from . import RestrictedFINXMax52Text
from . import TerminationDate7Choice
from . import YesNoIndicator

class SecuritiesFinancingTransactionDetails50(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_ClsgLegId", "_IntrstPmt", "_LglFrmwk", "_MtrtyDtMod", "_RateTp", "_RpRate", "_ScndLegNrrtv", "_SctiesFincgTradId", "_TermntnDt", "_TermntnTxAmt", "_TxCallDely", "_VarblRateSpprt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection59, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection59, False)

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if value is not None else base_types.UninitialisedField(self, 'ClsgLegId', RestrictedFINXMax16Text, False)

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = base_types.UninitialisedField(self, 'ClsgLegId', RestrictedFINXMax16Text, False)

	@property
	def IntrstPmt(self):
		return self._IntrstPmt

	@IntrstPmt.setter
	def IntrstPmt(self, value):
		self._IntrstPmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmt', YesNoIndicator, False)

	@IntrstPmt.deleter
	def IntrstPmt(self):
		del self._IntrstPmt
		self._IntrstPmt = base_types.UninitialisedField(self, 'IntrstPmt', YesNoIndicator, False)

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if value is not None else base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework4Choice, False)

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = base_types.UninitialisedField(self, 'LglFrmwk', LegalFramework4Choice, False)

	@property
	def MtrtyDtMod(self):
		return self._MtrtyDtMod

	@MtrtyDtMod.setter
	def MtrtyDtMod(self, value):
		self._MtrtyDtMod = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDtMod', YesNoIndicator, False)

	@MtrtyDtMod.deleter
	def MtrtyDtMod(self):
		del self._MtrtyDtMod
		self._MtrtyDtMod = base_types.UninitialisedField(self, 'MtrtyDtMod', YesNoIndicator, False)

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if value is not None else base_types.UninitialisedField(self, 'RateTp', RateType67Choice, False)

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = base_types.UninitialisedField(self, 'RateTp', RateType67Choice, False)

	@property
	def RpRate(self):
		return self._RpRate

	@RpRate.setter
	def RpRate(self, value):
		self._RpRate = value if value is not None else base_types.UninitialisedField(self, 'RpRate', Rate2, False)

	@RpRate.deleter
	def RpRate(self):
		del self._RpRate
		self._RpRate = base_types.UninitialisedField(self, 'RpRate', Rate2, False)

	@property
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if value is not None else base_types.UninitialisedField(self, 'ScndLegNrrtv', RestrictedFINXMax140Text, False)

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = base_types.UninitialisedField(self, 'ScndLegNrrtv', RestrictedFINXMax140Text, False)

	@property
	def SctiesFincgTradId(self):
		return self._SctiesFincgTradId

	@SctiesFincgTradId.setter
	def SctiesFincgTradId(self, value):
		self._SctiesFincgTradId = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTradId', RestrictedFINXMax52Text, False)

	@SctiesFincgTradId.deleter
	def SctiesFincgTradId(self):
		del self._SctiesFincgTradId
		self._SctiesFincgTradId = base_types.UninitialisedField(self, 'SctiesFincgTradId', RestrictedFINXMax52Text, False)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', TerminationDate7Choice, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', TerminationDate7Choice, False)

	@property
	def TermntnTxAmt(self):
		return self._TermntnTxAmt

	@TermntnTxAmt.setter
	def TermntnTxAmt(self, value):
		self._TermntnTxAmt = value if value is not None else base_types.UninitialisedField(self, 'TermntnTxAmt', AmountAndDirection59, False)

	@TermntnTxAmt.deleter
	def TermntnTxAmt(self):
		del self._TermntnTxAmt
		self._TermntnTxAmt = base_types.UninitialisedField(self, 'TermntnTxAmt', AmountAndDirection59, False)

	@property
	def TxCallDely(self):
		return self._TxCallDely

	@TxCallDely.setter
	def TxCallDely(self, value):
		self._TxCallDely = value if value is not None else base_types.UninitialisedField(self, 'TxCallDely', Exact3NumericText, False)

	@TxCallDely.deleter
	def TxCallDely(self):
		del self._TxCallDely
		self._TxCallDely = base_types.UninitialisedField(self, 'TxCallDely', Exact3NumericText, False)

	@property
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if value is not None else base_types.UninitialisedField(self, 'VarblRateSpprt', RateName2, False)

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = base_types.UninitialisedField(self, 'VarblRateSpprt', RateName2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgLegId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglFrmwk', type=LegalFramework4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDtMod', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType67Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpRate', type=Rate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLegNrrtv', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTradId', type=RestrictedFINXMax52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=TerminationDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnTxAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCallDely', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateSpprt', type=RateName2, min=0, max=1, mutex_group=None, array=False),
	))