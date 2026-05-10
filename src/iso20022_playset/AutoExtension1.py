from . import base_types
from .NonExtension1 import NonExtension1
from .AutoExtend1Choice import AutoExtend1Choice
from .ISODate import ISODate

class AutoExtension1(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_FnlXpryDt", "_NonXtnsnNtfctn"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def FnlXpryDt(self):
		return self._FnlXpryDt

	@FnlXpryDt.setter
	def FnlXpryDt(self, value):
		self._FnlXpryDt = value if type(value) != base_types.auto else self.make_default("FnlXpryDt")

	@FnlXpryDt.deleter
	def FnlXpryDt(self):
		del self._FnlXpryDt
		self._FnlXpryDt = None

	@property
	def NonXtnsnNtfctn(self):
		return self._NonXtnsnNtfctn

	@NonXtnsnNtfctn.setter
	def NonXtnsnNtfctn(self, value):
		self._NonXtnsnNtfctn = value if type(value) != base_types.auto else self.make_default("NonXtnsnNtfctn")

	@NonXtnsnNtfctn.deleter
	def NonXtnsnNtfctn(self):
		del self._NonXtnsnNtfctn
		self._NonXtnsnNtfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=AutoExtend1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlXpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonXtnsnNtfctn', type=NonExtension1, min=0, max=None, mutex_group=None, array=True),
	))

