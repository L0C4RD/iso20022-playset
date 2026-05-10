import base_types
import PoliticalExposureType2Choice
import PoliticallyExposedPersonStatus1Choice

class PoliticallyExposedPerson1(base_types._BaseFieldType):

	__slots__ = ["_PltclyXpsdPrsnSts", "_PltclyXpsdPrsnTp"]
	@property
	def PltclyXpsdPrsnSts(self):
		return self._PltclyXpsdPrsnSts

	@PltclyXpsdPrsnSts.setter
	def PltclyXpsdPrsnSts(self, value):
		self._PltclyXpsdPrsnSts = value if type(value) != auto else self.make_default("PltclyXpsdPrsnSts")

	@PltclyXpsdPrsnSts.deleter
	def PltclyXpsdPrsnSts(self):
		del self._PltclyXpsdPrsnSts
		self._PltclyXpsdPrsnSts = None

	@property
	def PltclyXpsdPrsnTp(self):
		return self._PltclyXpsdPrsnTp

	@PltclyXpsdPrsnTp.setter
	def PltclyXpsdPrsnTp(self, value):
		self._PltclyXpsdPrsnTp = value if type(value) != auto else self.make_default("PltclyXpsdPrsnTp")

	@PltclyXpsdPrsnTp.deleter
	def PltclyXpsdPrsnTp(self):
		del self._PltclyXpsdPrsnTp
		self._PltclyXpsdPrsnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PltclyXpsdPrsnSts', type=PoliticallyExposedPersonStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PltclyXpsdPrsnTp', type=PoliticalExposureType2Choice, min=1, max=1, mutex_group=None, array=False),
	))

