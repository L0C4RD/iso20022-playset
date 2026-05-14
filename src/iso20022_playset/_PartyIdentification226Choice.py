# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification222 import PartyIdentification222
from ._PartyIdentification224 import PartyIdentification224

class PartyIdentification226Choice(base_types._BaseFieldType):

	__slots__ = ["_LglPrsn", "_NtrlPrsn"]
	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if type(value) != base_types.auto else self.make_default("LglPrsn")

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = None

	@property
	def NtrlPrsn(self):
		return self._NtrlPrsn

	@NtrlPrsn.setter
	def NtrlPrsn(self, value):
		self._NtrlPrsn = value if type(value) != base_types.auto else self.make_default("NtrlPrsn")

	@NtrlPrsn.deleter
	def NtrlPrsn(self):
		del self._NtrlPrsn
		self._NtrlPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification224, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlPrsn', type=PartyIdentification222, min=0, max=1, mutex_group=1, array=False),
	))