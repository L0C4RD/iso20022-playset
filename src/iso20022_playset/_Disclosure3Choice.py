# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NoReasonCode import NoReasonCode
from ._SafekeepingAccount17 import SafekeepingAccount17

class Disclosure3Choice(base_types._BaseFieldType):

	__slots__ = ["_NoDsclsr", "_SfkpgAcctAndHldgs"]
	@property
	def NoDsclsr(self):
		return self._NoDsclsr

	@NoDsclsr.setter
	def NoDsclsr(self, value):
		self._NoDsclsr = value if type(value) != base_types.auto else self.make_default("NoDsclsr")

	@NoDsclsr.deleter
	def NoDsclsr(self):
		del self._NoDsclsr
		self._NoDsclsr = None

	@property
	def SfkpgAcctAndHldgs(self):
		return self._SfkpgAcctAndHldgs

	@SfkpgAcctAndHldgs.setter
	def SfkpgAcctAndHldgs(self, value):
		self._SfkpgAcctAndHldgs = value if type(value) != base_types.auto else self.make_default("SfkpgAcctAndHldgs")

	@SfkpgAcctAndHldgs.deleter
	def SfkpgAcctAndHldgs(self):
		del self._SfkpgAcctAndHldgs
		self._SfkpgAcctAndHldgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoDsclsr', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SfkpgAcctAndHldgs', type=SafekeepingAccount17, min=1, max=None, mutex_group=1, array=True),
	))