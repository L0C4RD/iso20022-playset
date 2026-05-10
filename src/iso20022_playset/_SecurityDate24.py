from . import base_types
from ._DateFormat41Choice import DateFormat41Choice

class SecurityDate24(base_types._BaseFieldType):

	__slots__ = ["_EarlstPmtDt", "_LastTradgDt", "_AvlblDt", "_PmtDt", "_DvddRnkgDt", "_PrpssDt"]
	@property
	def AvlblDt(self):
		return self._AvlblDt

	@AvlblDt.setter
	def AvlblDt(self, value):
		self._AvlblDt = value if type(value) != base_types.auto else self.make_default("AvlblDt")

	@AvlblDt.deleter
	def AvlblDt(self):
		del self._AvlblDt
		self._AvlblDt = None

	@property
	def DvddRnkgDt(self):
		return self._DvddRnkgDt

	@DvddRnkgDt.setter
	def DvddRnkgDt(self, value):
		self._DvddRnkgDt = value if type(value) != base_types.auto else self.make_default("DvddRnkgDt")

	@DvddRnkgDt.deleter
	def DvddRnkgDt(self):
		del self._DvddRnkgDt
		self._DvddRnkgDt = None

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
	def LastTradgDt(self):
		return self._LastTradgDt

	@LastTradgDt.setter
	def LastTradgDt(self, value):
		self._LastTradgDt = value if type(value) != base_types.auto else self.make_default("LastTradgDt")

	@LastTradgDt.deleter
	def LastTradgDt(self):
		del self._LastTradgDt
		self._LastTradgDt = None

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
	def PrpssDt(self):
		return self._PrpssDt

	@PrpssDt.setter
	def PrpssDt(self, value):
		self._PrpssDt = value if type(value) != base_types.auto else self.make_default("PrpssDt")

	@PrpssDt.deleter
	def PrpssDt(self):
		del self._PrpssDt
		self._PrpssDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlblDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddRnkgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstPmtDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTradgDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrpssDt', type=DateFormat41Choice, min=0, max=1, mutex_group=None, array=False),
	))

