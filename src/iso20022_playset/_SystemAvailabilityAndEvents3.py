# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import SystemClosure2
from . import SystemEvent3
from . import TimePeriod1

class SystemAvailabilityAndEvents3(base_types._BaseFieldType):

	__slots__ = ["_ClsrInf", "_Evt", "_SsnPrd", "_SysCcy"]
	@property
	def ClsrInf(self):
		return self._ClsrInf

	@ClsrInf.setter
	def ClsrInf(self, value):
		self._ClsrInf = value if value is not None else base_types.UninitialisedField(self, 'ClsrInf', SystemClosure2, True)

	@ClsrInf.deleter
	def ClsrInf(self):
		del self._ClsrInf
		self._ClsrInf = base_types.UninitialisedField(self, 'ClsrInf', SystemClosure2, True)

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if value is not None else base_types.UninitialisedField(self, 'Evt', SystemEvent3, True)

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = base_types.UninitialisedField(self, 'Evt', SystemEvent3, True)

	@property
	def SsnPrd(self):
		return self._SsnPrd

	@SsnPrd.setter
	def SsnPrd(self, value):
		self._SsnPrd = value if value is not None else base_types.UninitialisedField(self, 'SsnPrd', TimePeriod1, False)

	@SsnPrd.deleter
	def SsnPrd(self):
		del self._SsnPrd
		self._SsnPrd = base_types.UninitialisedField(self, 'SsnPrd', TimePeriod1, False)

	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if value is not None else base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, False)

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrInf', type=SystemClosure2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Evt', type=SystemEvent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SsnPrd', type=TimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))