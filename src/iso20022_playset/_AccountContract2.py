from . import base_types
from ._ISODate import ISODate
from ._YesNoIndicator import YesNoIndicator

class AccountContract2(base_types._BaseFieldType):

	__slots__ = ["_TrgtClsgDt", "_TrgtGoLiveDt", "_UrgcyFlg"]
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
		base_types.FieldEntry(name='TrgtClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtGoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrgcyFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

