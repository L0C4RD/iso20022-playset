from . import base_types
from .MemberIdentification3Choice import MemberIdentification3Choice
from .SystemMemberStatus1Choice import SystemMemberStatus1Choice
from .SystemMemberType1Choice import SystemMemberType1Choice

class MemberSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_Tp", "_Id"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=SystemMemberStatus1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SystemMemberType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
	))

