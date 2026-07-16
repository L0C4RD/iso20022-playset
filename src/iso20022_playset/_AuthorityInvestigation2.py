# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorityRequestType1
from . import InvestigatedParties1Choice
from . import Max500Text

class AuthorityInvestigation2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlInvstgtdPties", "_InvstgtdRoles", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@property
	def AddtlInvstgtdPties(self):
		return self._AddtlInvstgtdPties

	@AddtlInvstgtdPties.setter
	def AddtlInvstgtdPties(self, value):
		self._AddtlInvstgtdPties = value if value is not None else base_types.UninitialisedField(self, 'AddtlInvstgtdPties', InvestigatedParties1Choice, False)

	@AddtlInvstgtdPties.deleter
	def AddtlInvstgtdPties(self):
		del self._AddtlInvstgtdPties
		self._AddtlInvstgtdPties = base_types.UninitialisedField(self, 'AddtlInvstgtdPties', InvestigatedParties1Choice, False)

	@property
	def InvstgtdRoles(self):
		return self._InvstgtdRoles

	@InvstgtdRoles.setter
	def InvstgtdRoles(self, value):
		self._InvstgtdRoles = value if value is not None else base_types.UninitialisedField(self, 'InvstgtdRoles', InvestigatedParties1Choice, False)

	@InvstgtdRoles.deleter
	def InvstgtdRoles(self):
		del self._InvstgtdRoles
		self._InvstgtdRoles = base_types.UninitialisedField(self, 'InvstgtdRoles', InvestigatedParties1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AuthorityRequestType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AuthorityRequestType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInvstgtdPties', type=InvestigatedParties1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtdRoles', type=InvestigatedParties1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AuthorityRequestType1, min=1, max=1, mutex_group=None, array=False),
	))