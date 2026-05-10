from . import base_types
from .Max35Text import Max35Text
from .ATMConfigurationParameter1 import ATMConfigurationParameter1

class ATMEquipment1(base_types._BaseFieldType):

	__slots__ = ["_Manfctr", "_ApplNm", "_CfgtnParam", "_ApplVrsn", "_ApplPrvdr", "_SrlNb", "_ApprvlNb", "_Mdl"]
	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if type(value) != auto else self.make_default("Manfctr")

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = None

	@property
	def ApplNm(self):
		return self._ApplNm

	@ApplNm.setter
	def ApplNm(self, value):
		self._ApplNm = value if type(value) != auto else self.make_default("ApplNm")

	@ApplNm.deleter
	def ApplNm(self):
		del self._ApplNm
		self._ApplNm = None

	@property
	def CfgtnParam(self):
		return self._CfgtnParam

	@CfgtnParam.setter
	def CfgtnParam(self, value):
		self._CfgtnParam = value if type(value) != auto else self.make_default("CfgtnParam")

	@CfgtnParam.deleter
	def CfgtnParam(self):
		del self._CfgtnParam
		self._CfgtnParam = None

	@property
	def ApplVrsn(self):
		return self._ApplVrsn

	@ApplVrsn.setter
	def ApplVrsn(self, value):
		self._ApplVrsn = value if type(value) != auto else self.make_default("ApplVrsn")

	@ApplVrsn.deleter
	def ApplVrsn(self):
		del self._ApplVrsn
		self._ApplVrsn = None

	@property
	def ApplPrvdr(self):
		return self._ApplPrvdr

	@ApplPrvdr.setter
	def ApplPrvdr(self, value):
		self._ApplPrvdr = value if type(value) != auto else self.make_default("ApplPrvdr")

	@ApplPrvdr.deleter
	def ApplPrvdr(self):
		del self._ApplPrvdr
		self._ApplPrvdr = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def ApprvlNb(self):
		return self._ApprvlNb

	@ApprvlNb.setter
	def ApprvlNb(self, value):
		self._ApprvlNb = value if type(value) != auto else self.make_default("ApprvlNb")

	@ApprvlNb.deleter
	def ApprvlNb(self):
		del self._ApprvlNb
		self._ApprvlNb = None

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if type(value) != auto else self.make_default("Mdl")

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Manfctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CfgtnParam', type=ATMConfigurationParameter1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplPrvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

