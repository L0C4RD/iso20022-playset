# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MemberIdentification3Choice
from . import SystemMemberStatus1Choice
from . import SystemMemberType1Choice

class MemberSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Sts", "_Tp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', MemberIdentification3Choice, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', MemberIdentification3Choice, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', SystemMemberStatus1Choice, True)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', SystemMemberStatus1Choice, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SystemMemberType1Choice, True)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SystemMemberType1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=SystemMemberStatus1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SystemMemberType1Choice, min=0, max=None, mutex_group=None, array=True),
	))