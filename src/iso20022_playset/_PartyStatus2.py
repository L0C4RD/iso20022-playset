from . import base_types
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._StatusReasonInformation10 import StatusReasonInformation10
from ._Status6Code import Status6Code

class PartyStatus2(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_SysPtyId", "_StsRsn"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def SysPtyId(self):
		return self._SysPtyId

	@SysPtyId.setter
	def SysPtyId(self, value):
		self._SysPtyId = value if type(value) != base_types.auto else self.make_default("SysPtyId")

	@SysPtyId.deleter
	def SysPtyId(self):
		del self._SysPtyId
		self._SysPtyId = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=Status6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysPtyId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation10, min=0, max=None, mutex_group=None, array=True),
	))

