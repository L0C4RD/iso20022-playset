from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .NetworkParameters7 import NetworkParameters7
from .POICommunicationType2Code import POICommunicationType2Code
from .PartyType7Code import PartyType7Code
from .PhysicalInterfaceParameter1 import PhysicalInterfaceParameter1

class CommunicationCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_PhysIntrfc", "_Params", "_RmotPty", "_Actv", "_ComTp"]
	@property
	def PhysIntrfc(self):
		return self._PhysIntrfc

	@PhysIntrfc.setter
	def PhysIntrfc(self, value):
		self._PhysIntrfc = value if type(value) != base_types.auto else self.make_default("PhysIntrfc")

	@PhysIntrfc.deleter
	def PhysIntrfc(self):
		del self._PhysIntrfc
		self._PhysIntrfc = None

	@property
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if type(value) != base_types.auto else self.make_default("Params")

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = None

	@property
	def RmotPty(self):
		return self._RmotPty

	@RmotPty.setter
	def RmotPty(self, value):
		self._RmotPty = value if type(value) != base_types.auto else self.make_default("RmotPty")

	@RmotPty.deleter
	def RmotPty(self):
		del self._RmotPty
		self._RmotPty = None

	@property
	def Actv(self):
		return self._Actv

	@Actv.setter
	def Actv(self, value):
		self._Actv = value if type(value) != base_types.auto else self.make_default("Actv")

	@Actv.deleter
	def Actv(self):
		del self._Actv
		self._Actv = None

	@property
	def ComTp(self):
		return self._ComTp

	@ComTp.setter
	def ComTp(self, value):
		self._ComTp = value if type(value) != base_types.auto else self.make_default("ComTp")

	@ComTp.deleter
	def ComTp(self):
		del self._ComTp
		self._ComTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PhysIntrfc', type=PhysicalInterfaceParameter1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotPty', type=PartyType7Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Actv', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComTp', type=POICommunicationType2Code, min=1, max=1, mutex_group=None, array=False),
	))

