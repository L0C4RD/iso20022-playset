from . import base_types
from .ATMEnvironment9 import ATMEnvironment9
from .ATMStatus2 import ATMStatus2

class ATMDiagnosticRequest3(base_types._BaseFieldType):

	__slots__ = ["_ATMGblSts", "_Envt"]
	@property
	def ATMGblSts(self):
		return self._ATMGblSts

	@ATMGblSts.setter
	def ATMGblSts(self, value):
		self._ATMGblSts = value if type(value) != base_types.auto else self.make_default("ATMGblSts")

	@ATMGblSts.deleter
	def ATMGblSts(self):
		del self._ATMGblSts
		self._ATMGblSts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMGblSts', type=ATMStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment9, min=1, max=1, mutex_group=None, array=False),
	))

