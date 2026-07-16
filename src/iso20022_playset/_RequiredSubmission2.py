# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1

class RequiredSubmission2(base_types._BaseFieldType):

	__slots__ = ["_Submitr"]
	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if value is not None else base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = base_types.UninitialisedField(self, 'Submitr', BICIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))