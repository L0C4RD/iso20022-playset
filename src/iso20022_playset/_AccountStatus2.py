from . import base_types
from ._ClosedStatusReason1Choice import ClosedStatusReason1Choice
from ._ClosurePendingStatusReason1Choice import ClosurePendingStatusReason1Choice
from ._DisabledStatusReason1Choice import DisabledStatusReason1Choice
from ._EnabledStatusReason1Choice import EnabledStatusReason1Choice
from ._OtherAccountStatus1 import OtherAccountStatus1
from ._PendingOpeningStatusReason1Choice import PendingOpeningStatusReason1Choice
from ._PendingStatusReason1Choice import PendingStatusReason1Choice
from ._ProformaStatusReason1Choice import ProformaStatusReason1Choice

class AccountStatus2(base_types._BaseFieldType):

	__slots__ = ["_Clsd", "_ClsrPdg", "_Dsbld", "_Nbld", "_Othr", "_Pdg", "_PdgOpng", "_Profrm"]
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
	def Dsbld(self):
		return self._Dsbld

	@Dsbld.setter
	def Dsbld(self, value):
		self._Dsbld = value if type(value) != base_types.auto else self.make_default("Dsbld")

	@Dsbld.deleter
	def Dsbld(self):
		del self._Dsbld
		self._Dsbld = None

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
	def Profrm(self):
		return self._Profrm

	@Profrm.setter
	def Profrm(self, value):
		self._Profrm = value if type(value) != base_types.auto else self.make_default("Profrm")

	@Profrm.deleter
	def Profrm(self):
		del self._Profrm
		self._Profrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clsd', type=ClosedStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrPdg', type=ClosurePendingStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsbld', type=DisabledStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nbld', type=EnabledStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherAccountStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pdg', type=PendingStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgOpng', type=PendingOpeningStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Profrm', type=ProformaStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))

