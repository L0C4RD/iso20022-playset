# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODate
from . import TrueFalseIndicator

class SystemSecuritiesAccount5(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_EndInvstrFlg", "_HldInd", "_NegPos", "_PricgSchme"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@property
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if value is not None else base_types.UninitialisedField(self, 'EndInvstrFlg', Exact4AlphaNumericText, False)

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = base_types.UninitialisedField(self, 'EndInvstrFlg', Exact4AlphaNumericText, False)

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if value is not None else base_types.UninitialisedField(self, 'HldInd', TrueFalseIndicator, False)

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = base_types.UninitialisedField(self, 'HldInd', TrueFalseIndicator, False)

	@property
	def NegPos(self):
		return self._NegPos

	@NegPos.setter
	def NegPos(self, value):
		self._NegPos = value if value is not None else base_types.UninitialisedField(self, 'NegPos', TrueFalseIndicator, False)

	@NegPos.deleter
	def NegPos(self):
		del self._NegPos
		self._NegPos = base_types.UninitialisedField(self, 'NegPos', TrueFalseIndicator, False)

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if value is not None else base_types.UninitialisedField(self, 'PricgSchme', Exact4AlphaNumericText, False)

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = base_types.UninitialisedField(self, 'PricgSchme', Exact4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NegPos', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))