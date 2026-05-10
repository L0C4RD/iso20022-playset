from . import base_types
from ._ATMCassetteCounters6 import ATMCassetteCounters6
from ._ATMMediaType4Code import ATMMediaType4Code
from ._ATMCassetteStatus1Code import ATMCassetteStatus1Code
from ._ATMCassetteType1Code import ATMCassetteType1Code
from ._Max35Text import Max35Text
from ._ATMNoteType1Code import ATMNoteType1Code

class ATMCassette3(base_types._BaseFieldType):

	__slots__ = ["_SrlNb", "_SubTp", "_MdiaCntrs", "_Tp", "_PhysId", "_LogclId", "_MdiaTp", "_CssttSts"]
	@property
	def CssttSts(self):
		return self._CssttSts

	@CssttSts.setter
	def CssttSts(self, value):
		self._CssttSts = value if type(value) != base_types.auto else self.make_default("CssttSts")

	@CssttSts.deleter
	def CssttSts(self):
		del self._CssttSts
		self._CssttSts = None

	@property
	def LogclId(self):
		return self._LogclId

	@LogclId.setter
	def LogclId(self, value):
		self._LogclId = value if type(value) != base_types.auto else self.make_default("LogclId")

	@LogclId.deleter
	def LogclId(self):
		del self._LogclId
		self._LogclId = None

	@property
	def MdiaCntrs(self):
		return self._MdiaCntrs

	@MdiaCntrs.setter
	def MdiaCntrs(self, value):
		self._MdiaCntrs = value if type(value) != base_types.auto else self.make_default("MdiaCntrs")

	@MdiaCntrs.deleter
	def MdiaCntrs(self):
		del self._MdiaCntrs
		self._MdiaCntrs = None

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if type(value) != base_types.auto else self.make_default("MdiaTp")

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = None

	@property
	def PhysId(self):
		return self._PhysId

	@PhysId.setter
	def PhysId(self, value):
		self._PhysId = value if type(value) != base_types.auto else self.make_default("PhysId")

	@PhysId.deleter
	def PhysId(self):
		del self._PhysId
		self._PhysId = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != base_types.auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if type(value) != base_types.auto else self.make_default("SubTp")

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CssttSts', type=ATMCassetteStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LogclId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaCntrs', type=ATMCassetteCounters6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=ATMNoteType1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ATMCassetteType1Code, min=1, max=1, mutex_group=None, array=False),
	))

