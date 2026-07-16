# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max5000Binary

class PublicRSAKey1(base_types._BaseFieldType):

	__slots__ = ["_Expnt", "_Mdlus"]
	@property
	def Expnt(self):
		return self._Expnt

	@Expnt.setter
	def Expnt(self, value):
		self._Expnt = value if value is not None else base_types.UninitialisedField(self, 'Expnt', Max5000Binary, False)

	@Expnt.deleter
	def Expnt(self):
		del self._Expnt
		self._Expnt = base_types.UninitialisedField(self, 'Expnt', Max5000Binary, False)

	@property
	def Mdlus(self):
		return self._Mdlus

	@Mdlus.setter
	def Mdlus(self, value):
		self._Mdlus = value if value is not None else base_types.UninitialisedField(self, 'Mdlus', Max5000Binary, False)

	@Mdlus.deleter
	def Mdlus(self):
		del self._Mdlus
		self._Mdlus = base_types.UninitialisedField(self, 'Mdlus', Max5000Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Expnt', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdlus', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
	))