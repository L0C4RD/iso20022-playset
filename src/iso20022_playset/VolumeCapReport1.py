from . import base_types
from .MICIdentifier import MICIdentifier
from .Period4Choice import Period4Choice
from .VolumeCapReport2 import VolumeCapReport2

class VolumeCapReport1(base_types._BaseFieldType):

	__slots__ = ["_TradgVn", "_InstrmRpt", "_RptgPrd"]
	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != base_types.auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def InstrmRpt(self):
		return self._InstrmRpt

	@InstrmRpt.setter
	def InstrmRpt(self, value):
		self._InstrmRpt = value if type(value) != base_types.auto else self.make_default("InstrmRpt")

	@InstrmRpt.deleter
	def InstrmRpt(self):
		del self._InstrmRpt
		self._InstrmRpt = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmRpt', type=VolumeCapReport2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))

