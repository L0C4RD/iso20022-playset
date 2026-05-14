# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._Max70Text import Max70Text

class FeeCollectionReference3(base_types._BaseFieldType):

	__slots__ = ["_AssgnrNtty", "_Id"]
	@property
	def AssgnrNtty(self):
		return self._AssgnrNtty

	@AssgnrNtty.setter
	def AssgnrNtty(self, value):
		self._AssgnrNtty = value if type(value) != base_types.auto else self.make_default("AssgnrNtty")

	@AssgnrNtty.deleter
	def AssgnrNtty(self):
		del self._AssgnrNtty
		self._AssgnrNtty = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnrNtty', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
	))