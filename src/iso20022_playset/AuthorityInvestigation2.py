from . import base_types
import AuthorityRequestType1
import Max500Text
import InvestigatedParties1Choice

class AuthorityInvestigation2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInvstgtdPties", "_Tp", "_AddtlInf", "_InvstgtdRoles"]
	@property
	def AddtlInvstgtdPties(self):
		return self._AddtlInvstgtdPties

	@AddtlInvstgtdPties.setter
	def AddtlInvstgtdPties(self, value):
		self._AddtlInvstgtdPties = value if type(value) != auto else self.make_default("AddtlInvstgtdPties")

	@AddtlInvstgtdPties.deleter
	def AddtlInvstgtdPties(self):
		del self._AddtlInvstgtdPties
		self._AddtlInvstgtdPties = None

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
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def InvstgtdRoles(self):
		return self._InvstgtdRoles

	@InvstgtdRoles.setter
	def InvstgtdRoles(self, value):
		self._InvstgtdRoles = value if type(value) != auto else self.make_default("InvstgtdRoles")

	@InvstgtdRoles.deleter
	def InvstgtdRoles(self):
		del self._InvstgtdRoles
		self._InvstgtdRoles = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInvstgtdPties', type=InvestigatedParties1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AuthorityRequestType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtdRoles', type=InvestigatedParties1Choice, min=1, max=1, mutex_group=None, array=False),
	))

