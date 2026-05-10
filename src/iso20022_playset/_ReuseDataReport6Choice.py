from . import base_types
from .ReuseDataReportNew6 import ReuseDataReportNew6
from .ReuseDataReportCorrection14 import ReuseDataReportCorrection14
from .ReuseDataReportError5 import ReuseDataReportError5

class ReuseDataReport6Choice(base_types._BaseFieldType):

	__slots__ = ["_CollReuseUpd", "_Err", "_New", "_Crrctn"]
	@property
	def CollReuseUpd(self):
		return self._CollReuseUpd

	@CollReuseUpd.setter
	def CollReuseUpd(self, value):
		self._CollReuseUpd = value if type(value) != base_types.auto else self.make_default("CollReuseUpd")

	@CollReuseUpd.deleter
	def CollReuseUpd(self):
		del self._CollReuseUpd
		self._CollReuseUpd = None

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != base_types.auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != base_types.auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if type(value) != base_types.auto else self.make_default("Crrctn")

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollReuseUpd', type=ReuseDataReportCorrection14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=ReuseDataReportError5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=ReuseDataReportNew6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=ReuseDataReportCorrection14, min=0, max=1, mutex_group=1, array=False),
	))

