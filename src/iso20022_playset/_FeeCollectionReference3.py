# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICAPartyType1Code
from . import Max70Text

class FeeCollectionReference3(base_types._BaseFieldType):

	__slots__ = ["_AssgnrNtty", "_Id"]
	@property
	def AssgnrNtty(self):
		return self._AssgnrNtty

	@AssgnrNtty.setter
	def AssgnrNtty(self, value):
		self._AssgnrNtty = value if value is not None else base_types.UninitialisedField(self, 'AssgnrNtty', ATICAPartyType1Code, False)

	@AssgnrNtty.deleter
	def AssgnrNtty(self):
		del self._AssgnrNtty
		self._AssgnrNtty = base_types.UninitialisedField(self, 'AssgnrNtty', ATICAPartyType1Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnrNtty', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
	))