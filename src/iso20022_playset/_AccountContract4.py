from . import base_types
from ._ISODate import ISODate
from ._YesNoIndicator import YesNoIndicator

class AccountContract4(base_types._BaseFieldType):

	__slots__ = ["_RmvlInd", "_TrgtClsgDt", "_UrgcyFlg"]
	@property
	def RmvlInd(self):
		return self._RmvlInd

	@RmvlInd.setter
	def RmvlInd(self, value):
		self._RmvlInd = value if type(value) != base_types.auto else self.make_default("RmvlInd")

	@RmvlInd.deleter
	def RmvlInd(self):
		del self._RmvlInd
		self._RmvlInd = None

	@property
	def TrgtClsgDt(self):
		return self._TrgtClsgDt

	@TrgtClsgDt.setter
	def TrgtClsgDt(self, value):
		self._TrgtClsgDt = value if type(value) != base_types.auto else self.make_default("TrgtClsgDt")

	@TrgtClsgDt.deleter
	def TrgtClsgDt(self):
		del self._TrgtClsgDt
		self._TrgtClsgDt = None

	@property
	def UrgcyFlg(self):
		return self._UrgcyFlg

	@UrgcyFlg.setter
	def UrgcyFlg(self, value):
		self._UrgcyFlg = value if type(value) != base_types.auto else self.make_default("UrgcyFlg")

	@UrgcyFlg.deleter
	def UrgcyFlg(self):
		del self._UrgcyFlg
		self._UrgcyFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmvlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrgcyFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

