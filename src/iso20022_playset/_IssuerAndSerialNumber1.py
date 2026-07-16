# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificateIssuer1
from . import Max35Binary

class IssuerAndSerialNumber1(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_SrlNb"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', CertificateIssuer1, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', CertificateIssuer1, False)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max35Binary, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max35Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=CertificateIssuer1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Binary, min=1, max=1, mutex_group=None, array=False),
	))