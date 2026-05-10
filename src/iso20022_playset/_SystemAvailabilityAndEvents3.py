from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._SystemClosure2 import SystemClosure2
from ._SystemEvent3 import SystemEvent3
from ._TimePeriod1 import TimePeriod1

class SystemAvailabilityAndEvents3(base_types._BaseFieldType):

	__slots__ = ["_ClsrInf", "_Evt", "_SsnPrd", "_SysCcy"]
	@property
	def ClsrInf(self):
		return self._ClsrInf

	@ClsrInf.setter
	def ClsrInf(self, value):
		self._ClsrInf = value if type(value) != base_types.auto else self.make_default("ClsrInf")

	@ClsrInf.deleter
	def ClsrInf(self):
		del self._ClsrInf
		self._ClsrInf = None

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if type(value) != base_types.auto else self.make_default("Evt")

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = None

	@property
	def SsnPrd(self):
		return self._SsnPrd

	@SsnPrd.setter
	def SsnPrd(self, value):
		self._SsnPrd = value if type(value) != base_types.auto else self.make_default("SsnPrd")

	@SsnPrd.deleter
	def SsnPrd(self):
		del self._SsnPrd
		self._SsnPrd = None

	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if type(value) != base_types.auto else self.make_default("SysCcy")

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrInf', type=SystemClosure2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Evt', type=SystemEvent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SsnPrd', type=TimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

