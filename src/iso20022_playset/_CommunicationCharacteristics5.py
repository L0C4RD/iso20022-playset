from . import base_types
from ._NetworkParameters7 import NetworkParameters7
from ._POICommunicationType2Code import POICommunicationType2Code
from ._PartyType7Code import PartyType7Code
from ._PhysicalInterfaceParameter1 import PhysicalInterfaceParameter1
from ._TrueFalseIndicator import TrueFalseIndicator

class CommunicationCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_Actv", "_ComTp", "_Params", "_PhysIntrfc", "_RmotPty"]
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
	def RmotPty(self):
		return self._RmotPty

	@RmotPty.setter
	def RmotPty(self, value):
		self._RmotPty = value if type(value) != base_types.auto else self.make_default("RmotPty")

	@RmotPty.deleter
	def RmotPty(self):
		del self._RmotPty
		self._RmotPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actv', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComTp', type=POICommunicationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysIntrfc', type=PhysicalInterfaceParameter1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotPty', type=PartyType7Code, min=1, max=None, mutex_group=None, array=True),
	))

