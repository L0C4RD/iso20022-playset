# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SignatureEnvelope import SignatureEnvelope
from ._xs:IDREF import xs:IDREF

class QualifiedPartyAndXMLSignature1(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Sgntr"]
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
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != base_types.auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=SignatureEnvelope, min=1, max=1, mutex_group=None, array=False),
	))