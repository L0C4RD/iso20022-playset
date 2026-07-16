# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TransactionEnvironment3Code

class TerminalHosting1(base_types._BaseFieldType):

	__slots__ = ["_Ctgy", "_Id"]
	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', TransactionEnvironment3Code, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', TransactionEnvironment3Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctgy', type=TransactionEnvironment3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))