from . import base_types
import Max35Text

class ATMEquipment2(base_types._BaseFieldType):

	__slots__ = ["_SrlNb", "_FrmwrVrsn", "_FrmwrId", "_FrmwrPrvdr", "_Vrsn", "_Mdl", "_Manfctr"]
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
	def FrmwrVrsn(self):
		return self._FrmwrVrsn

	@FrmwrVrsn.setter
	def FrmwrVrsn(self, value):
		self._FrmwrVrsn = value if type(value) != auto else self.make_default("FrmwrVrsn")

	@FrmwrVrsn.deleter
	def FrmwrVrsn(self):
		del self._FrmwrVrsn
		self._FrmwrVrsn = None

	@property
	def FrmwrId(self):
		return self._FrmwrId

	@FrmwrId.setter
	def FrmwrId(self, value):
		self._FrmwrId = value if type(value) != auto else self.make_default("FrmwrId")

	@FrmwrId.deleter
	def FrmwrId(self):
		del self._FrmwrId
		self._FrmwrId = None

	@property
	def FrmwrPrvdr(self):
		return self._FrmwrPrvdr

	@FrmwrPrvdr.setter
	def FrmwrPrvdr(self, value):
		self._FrmwrPrvdr = value if type(value) != auto else self.make_default("FrmwrPrvdr")

	@FrmwrPrvdr.deleter
	def FrmwrPrvdr(self):
		del self._FrmwrPrvdr
		self._FrmwrPrvdr = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmwrVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmwrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmwrPrvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Manfctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

