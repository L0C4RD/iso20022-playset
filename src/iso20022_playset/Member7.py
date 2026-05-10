from . import base_types
from .Max35Text import Max35Text
from .ContactIdentificationAndAddress2 import ContactIdentificationAndAddress2
from .SystemMemberType1Choice import SystemMemberType1Choice
from .MemberIdentification3Choice import MemberIdentification3Choice
from .SystemMemberStatus1Choice import SystemMemberStatus1Choice
from .CommunicationAddress10 import CommunicationAddress10
from .CashAccount40 import CashAccount40

class Member7(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_CtctRef", "_Tp", "_Acct", "_Nm", "_RtrAdr", "_ComAdr"]
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
	def CtctRef(self):
		return self._CtctRef

	@CtctRef.setter
	def CtctRef(self, value):
		self._CtctRef = value if type(value) != auto else self.make_default("CtctRef")

	@CtctRef.deleter
	def CtctRef(self):
		del self._CtctRef
		self._CtctRef = None

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
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def RtrAdr(self):
		return self._RtrAdr

	@RtrAdr.setter
	def RtrAdr(self, value):
		self._RtrAdr = value if type(value) != auto else self.make_default("RtrAdr")

	@RtrAdr.deleter
	def RtrAdr(self):
		del self._RtrAdr
		self._RtrAdr = None

	@property
	def ComAdr(self):
		return self._ComAdr

	@ComAdr.setter
	def ComAdr(self, value):
		self._ComAdr = value if type(value) != auto else self.make_default("ComAdr")

	@ComAdr.deleter
	def ComAdr(self):
		del self._ComAdr
		self._ComAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=SystemMemberStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctRef', type=ContactIdentificationAndAddress2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=SystemMemberType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrAdr', type=MemberIdentification3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComAdr', type=CommunicationAddress10, min=0, max=1, mutex_group=None, array=False),
	))

