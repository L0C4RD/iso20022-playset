# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODate
from . import MarketSpecificAttribute1
from . import SystemPartyIdentification8
from . import SystemPartyType1Choice
from . import SystemRestriction1
from . import SystemSecuritiesAccountType1Choice
from . import TrueFalseIndicator

class SystemSecuritiesAccount6(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_ClsgDt", "_EndInvstrFlg", "_HldInd", "_MktSpcfcAttr", "_NegPos", "_OpngDt", "_PricgSchme", "_PtyTp", "_Rstrctn", "_Tp"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

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
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if value is not None else base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, True)

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = base_types.UninitialisedField(self, 'MktSpcfcAttr', MarketSpecificAttribute1, True)

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
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', ISODate, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', ISODate, False)

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

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if value is not None else base_types.UninitialisedField(self, 'PtyTp', SystemPartyType1Choice, False)

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = base_types.UninitialisedField(self, 'PtyTp', SystemPartyType1Choice, False)

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if value is not None else base_types.UninitialisedField(self, 'Rstrctn', SystemRestriction1, True)

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = base_types.UninitialisedField(self, 'Rstrctn', SystemRestriction1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SystemSecuritiesAccountType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SystemSecuritiesAccountType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NegPos', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=SystemRestriction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SystemSecuritiesAccountType1Choice, min=0, max=1, mutex_group=None, array=False),
	))