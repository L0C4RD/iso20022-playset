# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10KBinary
from . import Modification1Code
from . import PartyIdentification272

class PartyAndCertificate7(base_types._BaseFieldType):

	__slots__ = ["_Cert", "_ModCd", "_Pty"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if value is not None else base_types.UninitialisedField(self, 'Cert', Max10KBinary, False)

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = base_types.UninitialisedField(self, 'Cert', Max10KBinary, False)

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
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
	))