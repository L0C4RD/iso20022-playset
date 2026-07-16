# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification201
from . import PartyIdentification202

class PartyIdentification205Choice(base_types._BaseFieldType):

	__slots__ = ["_LglPrsn", "_NtrlPrsn"]
	@property
	def LglPrsn(self):
		return self._LglPrsn

	@LglPrsn.setter
	def LglPrsn(self, value):
		self._LglPrsn = value if value is not None else base_types.UninitialisedField(self, 'LglPrsn', PartyIdentification201, False)

	@LglPrsn.deleter
	def LglPrsn(self):
		del self._LglPrsn
		self._LglPrsn = base_types.UninitialisedField(self, 'LglPrsn', PartyIdentification201, False)

	@property
	def NtrlPrsn(self):
		return self._NtrlPrsn

	@NtrlPrsn.setter
	def NtrlPrsn(self, value):
		self._NtrlPrsn = value if value is not None else base_types.UninitialisedField(self, 'NtrlPrsn', PartyIdentification202, False)

	@NtrlPrsn.deleter
	def NtrlPrsn(self):
		del self._NtrlPrsn
		self._NtrlPrsn = base_types.UninitialisedField(self, 'NtrlPrsn', PartyIdentification202, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglPrsn', type=PartyIdentification201, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlPrsn', type=PartyIdentification202, min=0, max=1, mutex_group=1, array=False),
	))