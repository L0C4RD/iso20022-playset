# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification10 import AccountIdentification10
from ._AccountIdentification69 import AccountIdentification69

class AccountIdentification73Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctsList", "_ForAllAccts"]
	@property
	def AcctsList(self):
		return self._AcctsList

	@AcctsList.setter
	def AcctsList(self, value):
		self._AcctsList = value if type(value) != base_types.auto else self.make_default("AcctsList")

	@AcctsList.deleter
	def AcctsList(self):
		del self._AcctsList
		self._AcctsList = None

	@property
	def ForAllAccts(self):
		return self._ForAllAccts

	@ForAllAccts.setter
	def ForAllAccts(self, value):
		self._ForAllAccts = value if type(value) != base_types.auto else self.make_default("ForAllAccts")

	@ForAllAccts.deleter
	def ForAllAccts(self):
		del self._ForAllAccts
		self._ForAllAccts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctsList', type=AccountIdentification69, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ForAllAccts', type=AccountIdentification10, min=0, max=1, mutex_group=1, array=False),
	))