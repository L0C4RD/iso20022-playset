from . import base_types
import ISODate
import SystemRestriction1
import SystemSecuritiesAccountType1Choice
import MarketSpecificAttribute1
import TrueFalseIndicator
import Exact4AlphaNumericText
import SystemPartyType1Choice
import SystemPartyIdentification8

class SystemSecuritiesAccount6(base_types._BaseFieldType):

	__slots__ = ["_NegPos", "_Tp", "_OpngDt", "_HldInd", "_MktSpcfcAttr", "_EndInvstrFlg", "_Rstrctn", "_PtyTp", "_PricgSchme", "_ClsgDt", "_AcctOwnr"]
	@property
	def NegPos(self):
		return self._NegPos

	@NegPos.setter
	def NegPos(self, value):
		self._NegPos = value if type(value) != auto else self.make_default("NegPos")

	@NegPos.deleter
	def NegPos(self):
		del self._NegPos
		self._NegPos = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if type(value) != auto else self.make_default("HldInd")

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = None

	@property
	def MktSpcfcAttr(self):
		return self._MktSpcfcAttr

	@MktSpcfcAttr.setter
	def MktSpcfcAttr(self, value):
		self._MktSpcfcAttr = value if type(value) != auto else self.make_default("MktSpcfcAttr")

	@MktSpcfcAttr.deleter
	def MktSpcfcAttr(self):
		del self._MktSpcfcAttr
		self._MktSpcfcAttr = None

	@property
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if type(value) != auto else self.make_default("EndInvstrFlg")

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = None

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if type(value) != auto else self.make_default("Rstrctn")

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = None

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if type(value) != auto else self.make_default("PtyTp")

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = None

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if type(value) != auto else self.make_default("PricgSchme")

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NegPos', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemSecuritiesAccountType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktSpcfcAttr', type=MarketSpecificAttribute1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=SystemRestriction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyTp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

