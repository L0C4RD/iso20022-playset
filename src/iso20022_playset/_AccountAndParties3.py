# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorityRequestType1
from . import CashAccount43
from . import InvestigatedParties1Choice

class AccountAndParties3(base_types._BaseFieldType):

	__slots__ = ["_AuthrtyReqTp", "_Id", "_InvstgtdPties"]
	@property
	def AuthrtyReqTp(self):
		return self._AuthrtyReqTp

	@AuthrtyReqTp.setter
	def AuthrtyReqTp(self, value):
		self._AuthrtyReqTp = value if value is not None else base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, True)

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', CashAccount43, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', CashAccount43, False)

	@property
	def InvstgtdPties(self):
		return self._InvstgtdPties

	@InvstgtdPties.setter
	def InvstgtdPties(self, value):
		self._InvstgtdPties = value if value is not None else base_types.UninitialisedField(self, 'InvstgtdPties', InvestigatedParties1Choice, False)

	@InvstgtdPties.deleter
	def InvstgtdPties(self):
		del self._InvstgtdPties
		self._InvstgtdPties = base_types.UninitialisedField(self, 'InvstgtdPties', InvestigatedParties1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtdPties', type=InvestigatedParties1Choice, min=1, max=1, mutex_group=None, array=False),
	))