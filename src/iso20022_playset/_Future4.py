# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BaseOneRate
from . import ISODateTime
from . import Price8
from . import TimeUnit3Choice
from . import UnderlyingAttributes4
from . import UnitOfMeasure7Choice

class Future4(base_types._BaseFieldType):

	__slots__ = ["_AddtlUndrlygAttrbts", "_CtrctSz", "_ExrcPric", "_FutrDt", "_MinSz", "_TmUnit", "_UnitOfMeasr"]
	@property
	def AddtlUndrlygAttrbts(self):
		return self._AddtlUndrlygAttrbts

	@AddtlUndrlygAttrbts.setter
	def AddtlUndrlygAttrbts(self, value):
		self._AddtlUndrlygAttrbts = value if value is not None else base_types.UninitialisedField(self, 'AddtlUndrlygAttrbts', UnderlyingAttributes4, True)

	@AddtlUndrlygAttrbts.deleter
	def AddtlUndrlygAttrbts(self):
		del self._AddtlUndrlygAttrbts
		self._AddtlUndrlygAttrbts = base_types.UninitialisedField(self, 'AddtlUndrlygAttrbts', UnderlyingAttributes4, True)

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', BaseOneRate, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', BaseOneRate, False)

	@property
	def ExrcPric(self):
		return self._ExrcPric

	@ExrcPric.setter
	def ExrcPric(self, value):
		self._ExrcPric = value if value is not None else base_types.UninitialisedField(self, 'ExrcPric', Price8, False)

	@ExrcPric.deleter
	def ExrcPric(self):
		del self._ExrcPric
		self._ExrcPric = base_types.UninitialisedField(self, 'ExrcPric', Price8, False)

	@property
	def FutrDt(self):
		return self._FutrDt

	@FutrDt.setter
	def FutrDt(self, value):
		self._FutrDt = value if value is not None else base_types.UninitialisedField(self, 'FutrDt', ISODateTime, False)

	@FutrDt.deleter
	def FutrDt(self):
		del self._FutrDt
		self._FutrDt = base_types.UninitialisedField(self, 'FutrDt', ISODateTime, False)

	@property
	def MinSz(self):
		return self._MinSz

	@MinSz.setter
	def MinSz(self, value):
		self._MinSz = value if value is not None else base_types.UninitialisedField(self, 'MinSz', ActiveCurrencyAndAmount, False)

	@MinSz.deleter
	def MinSz(self):
		del self._MinSz
		self._MinSz = base_types.UninitialisedField(self, 'MinSz', ActiveCurrencyAndAmount, False)

	@property
	def TmUnit(self):
		return self._TmUnit

	@TmUnit.setter
	def TmUnit(self, value):
		self._TmUnit = value if value is not None else base_types.UninitialisedField(self, 'TmUnit', TimeUnit3Choice, False)

	@TmUnit.deleter
	def TmUnit(self):
		del self._TmUnit
		self._TmUnit = base_types.UninitialisedField(self, 'TmUnit', TimeUnit3Choice, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure7Choice, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure7Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlUndrlygAttrbts', type=UnderlyingAttributes4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctSz', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FutrDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSz', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmUnit', type=TimeUnit3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure7Choice, min=0, max=1, mutex_group=None, array=False),
	))