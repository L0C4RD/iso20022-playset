from . import base_types
from ._DateFormat41Choice import DateFormat41Choice
from ._DateFormat49Choice import DateFormat49Choice
from ._DateFormat64Choice import DateFormat64Choice

class CorporateActionDate97(base_types._BaseFieldType):

	__slots__ = ["_EarlstPmtDt", "_FXRateFxgDt", "_PmtDt", "_ValDt"]
	@property
	def EarlstPmtDt(self):
		return self._EarlstPmtDt

	@EarlstPmtDt.setter
	def EarlstPmtDt(self, value):
		self._EarlstPmtDt = value if type(value) != base_types.auto else self.make_default("EarlstPmtDt")

	@EarlstPmtDt.deleter
	def EarlstPmtDt(self):
		del self._EarlstPmtDt
		self._EarlstPmtDt = None

	@property
	def FXRateFxgDt(self):
		return self._FXRateFxgDt

	@FXRateFxgDt.setter
	def FXRateFxgDt(self, value):
		self._FXRateFxgDt = value if type(value) != base_types.auto else self.make_default("FXRateFxgDt")

	@FXRateFxgDt.deleter
	def FXRateFxgDt(self):
		del self._FXRateFxgDt
		self._FXRateFxgDt = None

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRateFxgDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateFormat64Choice, min=0, max=1, mutex_group=None, array=False),
	))

