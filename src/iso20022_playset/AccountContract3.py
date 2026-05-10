from . import base_types
from .YesNoIndicator import YesNoIndicator
from .ISODate import ISODate

class AccountContract3(base_types._BaseFieldType):

	__slots__ = ["_UrgcyFlg", "_TrgtGoLiveDt", "_RmvlInd", "_ClsgDt", "_TrgtClsgDt", "_GoLiveDt"]
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

	@property
	def TrgtGoLiveDt(self):
		return self._TrgtGoLiveDt

	@TrgtGoLiveDt.setter
	def TrgtGoLiveDt(self, value):
		self._TrgtGoLiveDt = value if type(value) != base_types.auto else self.make_default("TrgtGoLiveDt")

	@TrgtGoLiveDt.deleter
	def TrgtGoLiveDt(self):
		del self._TrgtGoLiveDt
		self._TrgtGoLiveDt = None

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
	def GoLiveDt(self):
		return self._GoLiveDt

	@GoLiveDt.setter
	def GoLiveDt(self, value):
		self._GoLiveDt = value if type(value) != base_types.auto else self.make_default("GoLiveDt")

	@GoLiveDt.deleter
	def GoLiveDt(self):
		del self._GoLiveDt
		self._GoLiveDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UrgcyFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtGoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

