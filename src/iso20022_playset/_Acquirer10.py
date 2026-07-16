# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification177
from . import Max256Text

class Acquirer10(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ParamsVrsn"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification177, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification177, False)

	@property
	def ParamsVrsn(self):
		return self._ParamsVrsn

	@ParamsVrsn.setter
	def ParamsVrsn(self, value):
		self._ParamsVrsn = value if value is not None else base_types.UninitialisedField(self, 'ParamsVrsn', Max256Text, False)

	@ParamsVrsn.deleter
	def ParamsVrsn(self):
		del self._ParamsVrsn
		self._ParamsVrsn = base_types.UninitialisedField(self, 'ParamsVrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=GenericIdentification177, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParamsVrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))