from . import base_types
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator

class SystemSecuritiesAccount5(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_EndInvstrFlg", "_HldInd", "_NegPos", "_PricgSchme"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if type(value) != base_types.auto else self.make_default("EndInvstrFlg")

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = None

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if type(value) != base_types.auto else self.make_default("HldInd")

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = None

	@property
	def NegPos(self):
		return self._NegPos

	@NegPos.setter
	def NegPos(self, value):
		self._NegPos = value if type(value) != base_types.auto else self.make_default("NegPos")

	@NegPos.deleter
	def NegPos(self):
		del self._NegPos
		self._NegPos = None

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if type(value) != base_types.auto else self.make_default("PricgSchme")

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NegPos', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

