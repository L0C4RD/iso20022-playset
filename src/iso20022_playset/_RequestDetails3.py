# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class RequestDetails3(base_types._BaseFieldType):

	__slots__ = ["_Key", "_Tp"]
	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != base_types.auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Key', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))