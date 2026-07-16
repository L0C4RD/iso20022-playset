# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max12Text
from . import UnderlyingProductIdentifier1Code

class ProductIdentifier3Choice(base_types._BaseFieldType):

	__slots__ = ["_UndrlygPdctIdr", "_UnqPdctIdr"]
	@property
	def UndrlygPdctIdr(self):
		return self._UndrlygPdctIdr

	@UndrlygPdctIdr.setter
	def UndrlygPdctIdr(self, value):
		self._UndrlygPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UndrlygPdctIdr', UnderlyingProductIdentifier1Code, False)

	@UndrlygPdctIdr.deleter
	def UndrlygPdctIdr(self):
		del self._UndrlygPdctIdr
		self._UndrlygPdctIdr = base_types.UninitialisedField(self, 'UndrlygPdctIdr', UnderlyingProductIdentifier1Code, False)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', Max12Text, False)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', Max12Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygPdctIdr', type=UnderlyingProductIdentifier1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=Max12Text, min=0, max=1, mutex_group=1, array=False),
	))