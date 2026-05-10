from . import base_types
from .DateFormat43Choice import DateFormat43Choice

class CorporateActionDate88(base_types._BaseFieldType):

	__slots__ = ["_TradgDt", "_CoverXprtnDdln"]
	@property
	def TradgDt(self):
		return self._TradgDt

	@TradgDt.setter
	def TradgDt(self, value):
		self._TradgDt = value if type(value) != base_types.auto else self.make_default("TradgDt")

	@TradgDt.deleter
	def TradgDt(self):
		del self._TradgDt
		self._TradgDt = None

	@property
	def CoverXprtnDdln(self):
		return self._CoverXprtnDdln

	@CoverXprtnDdln.setter
	def CoverXprtnDdln(self, value):
		self._CoverXprtnDdln = value if type(value) != base_types.auto else self.make_default("CoverXprtnDdln")

	@CoverXprtnDdln.deleter
	def CoverXprtnDdln(self):
		del self._CoverXprtnDdln
		self._CoverXprtnDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverXprtnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
	))

