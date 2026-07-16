# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number

class Count1(base_types._BaseFieldType):

	__slots__ = ["_Nb"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Number, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))