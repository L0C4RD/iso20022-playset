from . import base_types
from ._Max35Text import Max35Text
from ._ATMEnvironment7 import ATMEnvironment7
from ._ATMVersionReport1 import ATMVersionReport1

class ATMConfigurationReportComponent1(base_types._BaseFieldType):

	__slots__ = ["_NonActvVrsn", "_Envt", "_ActvVrsn"]
	@property
	def ActvVrsn(self):
		return self._ActvVrsn

	@ActvVrsn.setter
	def ActvVrsn(self, value):
		self._ActvVrsn = value if type(value) != base_types.auto else self.make_default("ActvVrsn")

	@ActvVrsn.deleter
	def ActvVrsn(self):
		del self._ActvVrsn
		self._ActvVrsn = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def NonActvVrsn(self):
		return self._NonActvVrsn

	@NonActvVrsn.setter
	def NonActvVrsn(self, value):
		self._NonActvVrsn = value if type(value) != base_types.auto else self.make_default("NonActvVrsn")

	@NonActvVrsn.deleter
	def NonActvVrsn(self):
		del self._NonActvVrsn
		self._NonActvVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonActvVrsn', type=ATMVersionReport1, min=0, max=None, mutex_group=None, array=True),
	))

