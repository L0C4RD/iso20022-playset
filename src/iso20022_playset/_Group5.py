# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4AlphaNumericText
from . import Modification1Code
from . import PartyAndCertificate7

class Group5(base_types._BaseFieldType):

	__slots__ = ["_GrpId", "_ModCd", "_Pty"]
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
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyAndCertificate7, True)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyAndCertificate7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpId', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyAndCertificate7, min=1, max=None, mutex_group=None, array=True),
	))