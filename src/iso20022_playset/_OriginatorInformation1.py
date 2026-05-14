# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max5000Binary import Max5000Binary

class OriginatorInformation1(base_types._BaseFieldType):

	__slots__ = ["_Cert"]
	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != base_types.auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cert', type=Max5000Binary, min=0, max=None, mutex_group=None, array=True),
	))