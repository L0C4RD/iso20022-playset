# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4AlphaNumericText
from . import PartyAndCertificate6

class Group6(base_types._BaseFieldType):

	__slots__ = ["_GrpId", "_Pty"]
	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if value is not None else base_types.UninitialisedField(self, 'GrpId', Max4AlphaNumericText, False)

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = base_types.UninitialisedField(self, 'GrpId', Max4AlphaNumericText, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyAndCertificate6, True)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyAndCertificate6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpId', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyAndCertificate6, min=1, max=None, mutex_group=None, array=True),
	))