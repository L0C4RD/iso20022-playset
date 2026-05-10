from . import base_types
from .MarginReportData9 import MarginReportData9

class TradeReport34Choice(base_types._BaseFieldType):

	__slots__ = ["_Err", "_MrgnUpd", "_New", "_Crrctn"]
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
	def MrgnUpd(self):
		return self._MrgnUpd

	@MrgnUpd.setter
	def MrgnUpd(self, value):
		self._MrgnUpd = value if type(value) != base_types.auto else self.make_default("MrgnUpd")

	@MrgnUpd.deleter
	def MrgnUpd(self):
		del self._MrgnUpd
		self._MrgnUpd = None

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
		base_types.FieldEntry(name='Err', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnUpd', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
	))

