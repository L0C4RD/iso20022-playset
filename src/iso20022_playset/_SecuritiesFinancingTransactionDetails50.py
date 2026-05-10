from . import base_types
from ._TerminationDate7Choice import TerminationDate7Choice
from ._LegalFramework4Choice import LegalFramework4Choice
from ._YesNoIndicator import YesNoIndicator
from ._RestrictedFINXMax52Text import RestrictedFINXMax52Text
from ._RateName2 import RateName2
from ._Rate2 import Rate2
from ._AmountAndDirection59 import AmountAndDirection59
from ._Exact3NumericText import Exact3NumericText
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text
from ._RestrictedFINXMax140Text import RestrictedFINXMax140Text
from ._RateType67Choice import RateType67Choice

class SecuritiesFinancingTransactionDetails50(base_types._BaseFieldType):

	__slots__ = ["_LglFrmwk", "_AcrdIntrstAmt", "_IntrstPmt", "_SctiesFincgTradId", "_RateTp", "_TxCallDely", "_ScndLegNrrtv", "_TermntnTxAmt", "_ClsgLegId", "_VarblRateSpprt", "_RpRate", "_MtrtyDtMod", "_TermntnDt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if type(value) != base_types.auto else self.make_default("ClsgLegId")

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = None

	@property
	def IntrstPmt(self):
		return self._IntrstPmt

	@IntrstPmt.setter
	def IntrstPmt(self, value):
		self._IntrstPmt = value if type(value) != base_types.auto else self.make_default("IntrstPmt")

	@IntrstPmt.deleter
	def IntrstPmt(self):
		del self._IntrstPmt
		self._IntrstPmt = None

	@property
	def LglFrmwk(self):
		return self._LglFrmwk

	@LglFrmwk.setter
	def LglFrmwk(self, value):
		self._LglFrmwk = value if type(value) != base_types.auto else self.make_default("LglFrmwk")

	@LglFrmwk.deleter
	def LglFrmwk(self):
		del self._LglFrmwk
		self._LglFrmwk = None

	@property
	def MtrtyDtMod(self):
		return self._MtrtyDtMod

	@MtrtyDtMod.setter
	def MtrtyDtMod(self, value):
		self._MtrtyDtMod = value if type(value) != base_types.auto else self.make_default("MtrtyDtMod")

	@MtrtyDtMod.deleter
	def MtrtyDtMod(self):
		del self._MtrtyDtMod
		self._MtrtyDtMod = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def RpRate(self):
		return self._RpRate

	@RpRate.setter
	def RpRate(self, value):
		self._RpRate = value if type(value) != base_types.auto else self.make_default("RpRate")

	@RpRate.deleter
	def RpRate(self):
		del self._RpRate
		self._RpRate = None

	@property
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if type(value) != base_types.auto else self.make_default("ScndLegNrrtv")

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = None

	@property
	def SctiesFincgTradId(self):
		return self._SctiesFincgTradId

	@SctiesFincgTradId.setter
	def SctiesFincgTradId(self, value):
		self._SctiesFincgTradId = value if type(value) != base_types.auto else self.make_default("SctiesFincgTradId")

	@SctiesFincgTradId.deleter
	def SctiesFincgTradId(self):
		del self._SctiesFincgTradId
		self._SctiesFincgTradId = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

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
	def TxCallDely(self):
		return self._TxCallDely

	@TxCallDely.setter
	def TxCallDely(self, value):
		self._TxCallDely = value if type(value) != base_types.auto else self.make_default("TxCallDely")

	@TxCallDely.deleter
	def TxCallDely(self):
		del self._TxCallDely
		self._TxCallDely = None

	@property
	def VarblRateSpprt(self):
		return self._VarblRateSpprt

	@VarblRateSpprt.setter
	def VarblRateSpprt(self, value):
		self._VarblRateSpprt = value if type(value) != base_types.auto else self.make_default("VarblRateSpprt")

	@VarblRateSpprt.deleter
	def VarblRateSpprt(self):
		del self._VarblRateSpprt
		self._VarblRateSpprt = None

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

