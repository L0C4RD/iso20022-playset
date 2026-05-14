# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMEnvironment9 import ATMEnvironment9

class HostToATMAcknowledgement1(base_types._BaseFieldType):

	__slots__ = ["_Envt"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=ATMEnvironment9, min=1, max=1, mutex_group=None, array=False),
	))