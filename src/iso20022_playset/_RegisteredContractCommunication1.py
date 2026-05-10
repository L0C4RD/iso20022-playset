from . import base_types
from ._ISODate import ISODate
from ._CommunicationMethod4Code import CommunicationMethod4Code

class RegisteredContractCommunication1(base_types._BaseFieldType):

	__slots__ = ["_Mtd", "_Dt"]
	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != base_types.auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtd', type=CommunicationMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

