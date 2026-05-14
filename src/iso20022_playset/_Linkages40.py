# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._References47Choice import References47Choice

class Linkages40(base_types._BaseFieldType):

	__slots__ = ["_Ref"]
	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ref', type=References47Choice, min=1, max=1, mutex_group=None, array=False),
	))