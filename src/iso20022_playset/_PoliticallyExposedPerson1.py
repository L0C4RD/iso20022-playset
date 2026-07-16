# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PoliticalExposureType2Choice
from . import PoliticallyExposedPersonStatus1Choice

class PoliticallyExposedPerson1(base_types._BaseFieldType):

	__slots__ = ["_PltclyXpsdPrsnSts", "_PltclyXpsdPrsnTp"]
	@property
	def PltclyXpsdPrsnSts(self):
		return self._PltclyXpsdPrsnSts

	@PltclyXpsdPrsnSts.setter
	def PltclyXpsdPrsnSts(self, value):
		self._PltclyXpsdPrsnSts = value if value is not None else base_types.UninitialisedField(self, 'PltclyXpsdPrsnSts', PoliticallyExposedPersonStatus1Choice, False)

	@PltclyXpsdPrsnSts.deleter
	def PltclyXpsdPrsnSts(self):
		del self._PltclyXpsdPrsnSts
		self._PltclyXpsdPrsnSts = base_types.UninitialisedField(self, 'PltclyXpsdPrsnSts', PoliticallyExposedPersonStatus1Choice, False)

	@property
	def PltclyXpsdPrsnTp(self):
		return self._PltclyXpsdPrsnTp

	@PltclyXpsdPrsnTp.setter
	def PltclyXpsdPrsnTp(self, value):
		self._PltclyXpsdPrsnTp = value if value is not None else base_types.UninitialisedField(self, 'PltclyXpsdPrsnTp', PoliticalExposureType2Choice, False)

	@PltclyXpsdPrsnTp.deleter
	def PltclyXpsdPrsnTp(self):
		del self._PltclyXpsdPrsnTp
		self._PltclyXpsdPrsnTp = base_types.UninitialisedField(self, 'PltclyXpsdPrsnTp', PoliticalExposureType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PltclyXpsdPrsnSts', type=PoliticallyExposedPersonStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltclyXpsdPrsnTp', type=PoliticalExposureType2Choice, min=1, max=1, mutex_group=None, array=False),
	))