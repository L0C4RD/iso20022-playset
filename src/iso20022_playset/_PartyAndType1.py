# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification43 import PartyIdentification43
from ._PartyType1Choice import PartyType1Choice

class PartyAndType1(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Tp"]
	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PartyType1Choice, min=1, max=1, mutex_group=None, array=False),
	))