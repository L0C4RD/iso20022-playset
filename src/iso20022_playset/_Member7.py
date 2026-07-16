# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import CommunicationAddress10
from . import ContactIdentificationAndAddress2
from . import Max35Text
from . import MemberIdentification3Choice
from . import SystemMemberStatus1Choice
from . import SystemMemberType1Choice

class Member7(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_ComAdr", "_CtctRef", "_Nm", "_RtrAdr", "_Sts", "_Tp"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, True)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, True)

	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if value is not None else base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress10, False)

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = base_types.UninitialisedField(self, 'ComAdr', CommunicationAddress10, False)

	@property
	def CtctRef(self):
		return self._CtctRef

	@CtctRef.setter
	def CtctRef(self, value):
		self._CtctRef = value if value is not None else base_types.UninitialisedField(self, 'CtctRef', ContactIdentificationAndAddress2, True)

	@CtctRef.deleter
	def CtctRef(self):
		del self._CtctRef
		self._CtctRef = base_types.UninitialisedField(self, 'CtctRef', ContactIdentificationAndAddress2, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def RtrAdr(self):
		return self._RtrAdr

	@RtrAdr.setter
	def RtrAdr(self, value):
		self._RtrAdr = value if value is not None else base_types.UninitialisedField(self, 'RtrAdr', MemberIdentification3Choice, True)

	@RtrAdr.deleter
	def RtrAdr(self):
		del self._RtrAdr
		self._RtrAdr = base_types.UninitialisedField(self, 'RtrAdr', MemberIdentification3Choice, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', SystemMemberStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', SystemMemberStatus1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SystemMemberType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SystemMemberType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctRef', type=ContactIdentificationAndAddress2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrAdr', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=SystemMemberStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemMemberType1Choice, min=0, max=1, mutex_group=None, array=False),
	))