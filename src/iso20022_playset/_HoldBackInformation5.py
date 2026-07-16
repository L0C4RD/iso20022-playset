# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GateHoldBack1Code
from . import ISODate
from . import Max350Text
from . import RedemptionCompletion1Code
from . import SecurityIdentification46Choice
from . import YesNoIndicator

class HoldBackInformation5(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_FinInstrmId", "_FinInstrmNm", "_FnlConf", "_RedCmpltn", "_Tp", "_XpctdRlsDt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification46Choice, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification46Choice, False)

	@property
	def FinInstrmNm(self):
		return self._FinInstrmNm

	@FinInstrmNm.setter
	def FinInstrmNm(self, value):
		self._FinInstrmNm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmNm', Max350Text, False)

	@FinInstrmNm.deleter
	def FinInstrmNm(self):
		del self._FinInstrmNm
		self._FinInstrmNm = base_types.UninitialisedField(self, 'FinInstrmNm', Max350Text, False)

	@property
	def FnlConf(self):
		return self._FnlConf

	@FnlConf.setter
	def FnlConf(self, value):
		self._FnlConf = value if value is not None else base_types.UninitialisedField(self, 'FnlConf', YesNoIndicator, False)

	@FnlConf.deleter
	def FnlConf(self):
		del self._FnlConf
		self._FnlConf = base_types.UninitialisedField(self, 'FnlConf', YesNoIndicator, False)

	@property
	def RedCmpltn(self):
		return self._RedCmpltn

	@RedCmpltn.setter
	def RedCmpltn(self, value):
		self._RedCmpltn = value if value is not None else base_types.UninitialisedField(self, 'RedCmpltn', RedemptionCompletion1Code, False)

	@RedCmpltn.deleter
	def RedCmpltn(self):
		del self._RedCmpltn
		self._RedCmpltn = base_types.UninitialisedField(self, 'RedCmpltn', RedemptionCompletion1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', GateHoldBack1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', GateHoldBack1Code, False)

	@property
	def XpctdRlsDt(self):
		return self._XpctdRlsDt

	@XpctdRlsDt.setter
	def XpctdRlsDt(self, value):
		self._XpctdRlsDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdRlsDt', ISODate, False)

	@XpctdRlsDt.deleter
	def XpctdRlsDt(self):
		del self._XpctdRlsDt
		self._XpctdRlsDt = base_types.UninitialisedField(self, 'XpctdRlsDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification46Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlConf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedCmpltn', type=RedemptionCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GateHoldBack1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdRlsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))