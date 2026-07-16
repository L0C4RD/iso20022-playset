# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import NameAndLocation1
from . import SectorAndLocation1

class CounterpartyIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_NmAndLctn", "_SctrAndLctn"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if value is not None else base_types.UninitialisedField(self, 'NmAndLctn', NameAndLocation1, False)

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = base_types.UninitialisedField(self, 'NmAndLctn', NameAndLocation1, False)

	@property
	def SctrAndLctn(self):
		return self._SctrAndLctn

	@SctrAndLctn.setter
	def SctrAndLctn(self, value):
		self._SctrAndLctn = value if value is not None else base_types.UninitialisedField(self, 'SctrAndLctn', SectorAndLocation1, False)

	@SctrAndLctn.deleter
	def SctrAndLctn(self):
		del self._SctrAndLctn
		self._SctrAndLctn = base_types.UninitialisedField(self, 'SctrAndLctn', SectorAndLocation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=NameAndLocation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctrAndLctn', type=SectorAndLocation1, min=0, max=1, mutex_group=1, array=False),
	))