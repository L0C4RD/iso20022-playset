from . import base_types
from .PartyIdentification43 import PartyIdentification43
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .Max2000Text import Max2000Text
from .Max35Text import Max35Text

class UndertakingConfirmation1(base_types._BaseFieldType):

	__slots__ = ["_Conf", "_Cnfrmr", "_Dt", "_RefNb"]
	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if type(value) != auto else self.make_default("Conf")

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = None

	@property
	def Cnfrmr(self):
		return self._Cnfrmr

	@Cnfrmr.setter
	def Cnfrmr(self, value):
		self._Cnfrmr = value if type(value) != auto else self.make_default("Cnfrmr")

	@Cnfrmr.deleter
	def Cnfrmr(self):
		del self._Cnfrmr
		self._Cnfrmr = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if type(value) != auto else self.make_default("RefNb")

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Conf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cnfrmr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

