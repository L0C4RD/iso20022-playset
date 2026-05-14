# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ProprietaryReason4 import ProprietaryReason4

class Reason4(base_types._BaseFieldType):

	__slots__ = ["_Rsn"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=ProprietaryReason4, min=0, max=None, mutex_group=None, array=True),
	))