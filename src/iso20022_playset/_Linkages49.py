# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import References58Choice

class Linkages49(base_types._BaseFieldType):

	__slots__ = ["_Ref"]
	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References58Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References58Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ref', type=References58Choice, min=1, max=1, mutex_group=None, array=False),
	))