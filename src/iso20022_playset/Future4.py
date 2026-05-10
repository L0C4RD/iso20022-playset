import base_types
import UnitOfMeasure7Choice
import BaseOneRate
import TimeUnit3Choice
import Price8
import ISODateTime
import UnderlyingAttributes4
import ActiveCurrencyAndAmount

class Future4(base_types._BaseFieldType):

	__slots__ = ["_MinSz", "_AddtlUndrlygAttrbts", "_ExrcPric", "_TmUnit", "_FutrDt", "_CtrctSz", "_UnitOfMeasr"]
	@property
	def MinSz(self):
		return self._MinSz

	@MinSz.setter
	def MinSz(self, value):
		self._MinSz = value if type(value) != auto else self.make_default("MinSz")

	@MinSz.deleter
	def MinSz(self):
		del self._MinSz
		self._MinSz = None

	@property
	def AddtlUndrlygAttrbts(self):
		return self._AddtlUndrlygAttrbts

	@AddtlUndrlygAttrbts.setter
	def AddtlUndrlygAttrbts(self, value):
		self._AddtlUndrlygAttrbts = value if type(value) != auto else self.make_default("AddtlUndrlygAttrbts")

	@AddtlUndrlygAttrbts.deleter
	def AddtlUndrlygAttrbts(self):
		del self._AddtlUndrlygAttrbts
		self._AddtlUndrlygAttrbts = None

	@property
	def ExrcPric(self):
		return self._ExrcPric

	@ExrcPric.setter
	def ExrcPric(self, value):
		self._ExrcPric = value if type(value) != auto else self.make_default("ExrcPric")

	@ExrcPric.deleter
	def ExrcPric(self):
		del self._ExrcPric
		self._ExrcPric = None

	@property
	def TmUnit(self):
		return self._TmUnit

	@TmUnit.setter
	def TmUnit(self, value):
		self._TmUnit = value if type(value) != auto else self.make_default("TmUnit")

	@TmUnit.deleter
	def TmUnit(self):
		del self._TmUnit
		self._TmUnit = None

	@property
	def FutrDt(self):
		return self._FutrDt

	@FutrDt.setter
	def FutrDt(self, value):
		self._FutrDt = value if type(value) != auto else self.make_default("FutrDt")

	@FutrDt.deleter
	def FutrDt(self):
		del self._FutrDt
		self._FutrDt = None

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if type(value) != auto else self.make_default("CtrctSz")

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinSz', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlUndrlygAttrbts', type=UnderlyingAttributes4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExrcPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmUnit', type=TimeUnit3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FutrDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure7Choice, min=0, max=1, mutex_group=None, array=False),
	))

