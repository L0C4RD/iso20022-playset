# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorityInvestigation2
from . import PartyIdentification272

class CustomerIdentification2(base_types._BaseFieldType):

	__slots__ = ["_AuthrtyReq", "_Pty"]
	@property
	def AuthrtyReq(self):
		return self._AuthrtyReq

	@AuthrtyReq.setter
	def AuthrtyReq(self, value):
		self._AuthrtyReq = value if value is not None else base_types.UninitialisedField(self, 'AuthrtyReq', AuthorityInvestigation2, True)

	@AuthrtyReq.deleter
	def AuthrtyReq(self):
		del self._AuthrtyReq
		self._AuthrtyReq = base_types.UninitialisedField(self, 'AuthrtyReq', AuthorityInvestigation2, True)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrtyReq', type=AuthorityInvestigation2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
	))