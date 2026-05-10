from . import base_types
from .OtherAccountStatus1 import OtherAccountStatus1
from .ProformaStatusReason1Choice import ProformaStatusReason1Choice
from .EnabledStatusReason1Choice import EnabledStatusReason1Choice
from .PendingOpeningStatusReason1Choice import PendingOpeningStatusReason1Choice
from .ClosurePendingStatusReason1Choice import ClosurePendingStatusReason1Choice
from .DisabledStatusReason1Choice import DisabledStatusReason1Choice
from .PendingStatusReason1Choice import PendingStatusReason1Choice
from .ClosedStatusReason1Choice import ClosedStatusReason1Choice

class AccountStatus2(base_types._BaseFieldType):

	__slots__ = ["_Clsd", "_ClsrPdg", "_Othr", "_PdgOpng", "_Nbld", "_Profrm", "_Pdg", "_Dsbld"]
	@property
	def Clsd(self):
		return self._Clsd

	@Clsd.setter
	def Clsd(self, value):
		self._Clsd = value if type(value) != base_types.auto else self.make_default("Clsd")

	@Clsd.deleter
	def Clsd(self):
		del self._Clsd
		self._Clsd = None

	@property
	def ClsrPdg(self):
		return self._ClsrPdg

	@ClsrPdg.setter
	def ClsrPdg(self, value):
		self._ClsrPdg = value if type(value) != base_types.auto else self.make_default("ClsrPdg")

	@ClsrPdg.deleter
	def ClsrPdg(self):
		del self._ClsrPdg
		self._ClsrPdg = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def PdgOpng(self):
		return self._PdgOpng

	@PdgOpng.setter
	def PdgOpng(self, value):
		self._PdgOpng = value if type(value) != base_types.auto else self.make_default("PdgOpng")

	@PdgOpng.deleter
	def PdgOpng(self):
		del self._PdgOpng
		self._PdgOpng = None

	@property
	def Nbld(self):
		return self._Nbld

	@Nbld.setter
	def Nbld(self, value):
		self._Nbld = value if type(value) != base_types.auto else self.make_default("Nbld")

	@Nbld.deleter
	def Nbld(self):
		del self._Nbld
		self._Nbld = None

	@property
	def Profrm(self):
		return self._Profrm

	@Profrm.setter
	def Profrm(self, value):
		self._Profrm = value if type(value) != base_types.auto else self.make_default("Profrm")

	@Profrm.deleter
	def Profrm(self):
		del self._Profrm
		self._Profrm = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Dsbld(self):
		return self._Dsbld

	@Dsbld.setter
	def Dsbld(self, value):
		self._Dsbld = value if type(value) != base_types.auto else self.make_default("Dsbld")

	@Dsbld.deleter
	def Dsbld(self):
		del self._Dsbld
		self._Dsbld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clsd', type=ClosedStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrPdg', type=ClosurePendingStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherAccountStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgOpng', type=PendingOpeningStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nbld', type=EnabledStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Profrm', type=ProformaStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsbld', type=DisabledStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))

