# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosedStatusReason1Choice
from . import ClosurePendingStatusReason1Choice
from . import DisabledStatusReason1Choice
from . import EnabledStatusReason1Choice
from . import OtherAccountStatus1
from . import PendingOpeningStatusReason1Choice
from . import PendingStatusReason1Choice
from . import ProformaStatusReason1Choice

class AccountStatus2(base_types._BaseFieldType):

	__slots__ = ["_Clsd", "_ClsrPdg", "_Dsbld", "_Nbld", "_Othr", "_Pdg", "_PdgOpng", "_Profrm"]
	@property
	def Clsd(self):
		return self._Clsd

	@Clsd.setter
	def Clsd(self, value):
		self._Clsd = value if value is not None else base_types.UninitialisedField(self, 'Clsd', ClosedStatusReason1Choice, False)

	@Clsd.deleter
	def Clsd(self):
		del self._Clsd
		self._Clsd = base_types.UninitialisedField(self, 'Clsd', ClosedStatusReason1Choice, False)

	@property
	def ClsrPdg(self):
		return self._ClsrPdg

	@ClsrPdg.setter
	def ClsrPdg(self, value):
		self._ClsrPdg = value if value is not None else base_types.UninitialisedField(self, 'ClsrPdg', ClosurePendingStatusReason1Choice, False)

	@ClsrPdg.deleter
	def ClsrPdg(self):
		del self._ClsrPdg
		self._ClsrPdg = base_types.UninitialisedField(self, 'ClsrPdg', ClosurePendingStatusReason1Choice, False)

	@property
	def Dsbld(self):
		return self._Dsbld

	@Dsbld.setter
	def Dsbld(self, value):
		self._Dsbld = value if value is not None else base_types.UninitialisedField(self, 'Dsbld', DisabledStatusReason1Choice, False)

	@Dsbld.deleter
	def Dsbld(self):
		del self._Dsbld
		self._Dsbld = base_types.UninitialisedField(self, 'Dsbld', DisabledStatusReason1Choice, False)

	@property
	def Nbld(self):
		return self._Nbld

	@Nbld.setter
	def Nbld(self, value):
		self._Nbld = value if value is not None else base_types.UninitialisedField(self, 'Nbld', EnabledStatusReason1Choice, False)

	@Nbld.deleter
	def Nbld(self):
		del self._Nbld
		self._Nbld = base_types.UninitialisedField(self, 'Nbld', EnabledStatusReason1Choice, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherAccountStatus1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherAccountStatus1, True)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatusReason1Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatusReason1Choice, False)

	@property
	def PdgOpng(self):
		return self._PdgOpng

	@PdgOpng.setter
	def PdgOpng(self, value):
		self._PdgOpng = value if value is not None else base_types.UninitialisedField(self, 'PdgOpng', PendingOpeningStatusReason1Choice, False)

	@PdgOpng.deleter
	def PdgOpng(self):
		del self._PdgOpng
		self._PdgOpng = base_types.UninitialisedField(self, 'PdgOpng', PendingOpeningStatusReason1Choice, False)

	@property
	def Profrm(self):
		return self._Profrm

	@Profrm.setter
	def Profrm(self, value):
		self._Profrm = value if value is not None else base_types.UninitialisedField(self, 'Profrm', ProformaStatusReason1Choice, False)

	@Profrm.deleter
	def Profrm(self):
		del self._Profrm
		self._Profrm = base_types.UninitialisedField(self, 'Profrm', ProformaStatusReason1Choice, False)

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