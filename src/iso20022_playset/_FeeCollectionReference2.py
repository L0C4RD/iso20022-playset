# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FeeCollectionIdentification1
from . import Max35Text
from . import PartyType32Code

class FeeCollectionReference2(base_types._BaseFieldType):

	__slots__ = ["_AssgnrNtty", "_Id", "_OthrAssgnrNtty"]
	@property
	def AssgnrNtty(self):
		return self._AssgnrNtty

	@AssgnrNtty.setter
	def AssgnrNtty(self, value):
		self._AssgnrNtty = value if value is not None else base_types.UninitialisedField(self, 'AssgnrNtty', PartyType32Code, False)

	@AssgnrNtty.deleter
	def AssgnrNtty(self):
		del self._AssgnrNtty
		self._AssgnrNtty = base_types.UninitialisedField(self, 'AssgnrNtty', PartyType32Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', FeeCollectionIdentification1, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', FeeCollectionIdentification1, True)

	@property
	def OthrAssgnrNtty(self):
		return self._OthrAssgnrNtty

	@OthrAssgnrNtty.setter
	def OthrAssgnrNtty(self, value):
		self._OthrAssgnrNtty = value if value is not None else base_types.UninitialisedField(self, 'OthrAssgnrNtty', Max35Text, False)

	@OthrAssgnrNtty.deleter
	def OthrAssgnrNtty(self):
		del self._OthrAssgnrNtty
		self._OthrAssgnrNtty = base_types.UninitialisedField(self, 'OthrAssgnrNtty', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssgnrNtty', type=PartyType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=FeeCollectionIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrAssgnrNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))